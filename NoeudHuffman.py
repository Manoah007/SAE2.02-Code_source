from NoeudBinaire import NoeudBinaire

class NoeudHuffman(NoeudBinaire):
    """
    Arbre de Huffman : arbre binaire où chaque nœud
    a pour valeur un tuple (chaine, poids).
    - chaine : str = les caractères du sous-arbre
    - poids  : int = somme des effectifs des caractères
    """
 
    # ---------------#
    #  Constructeur  #                                                      #
    # ---------------#
 
    def __init__(self, chaine, poids, gauche=None, droit=None):
        # On appelle le constructeur de NoeudBinaire en passant
        # un tuple (chaine, poids) comme valeur du nœud
        super().__init__((chaine, poids), gauche, droit)
 
    # ---------#
    #  Getters #
    # ---------#
 
    def get_chaine(self):
        """Retourne la chaine de caractères du nœud (1er élément du tuple)."""
        return self._valeur[0]
 
    def get_poids(self):
        """Retourne le poids du nœud (2ème élément du tuple)."""
        return self._valeur[1]
 
 #-- Pas de Setter car on ne modifie pas les informations d'un neoud après sa création --#


    # ---------------------------------------------------#
    #    Méthodes statiques : construction de l'arbre    #
    # ---------------------------------------------------#
 
    @staticmethod
    def effectifs(texte):
        """
        Construit la liste L des couples (caractère, effectif)
        triée par effectif décroissant.
        """
        eff = {}
        for c in texte:
            eff[c] = eff.get(c, 0) + 1
        return sorted(eff.items(), key=lambda x: x[1], reverse=True)
 

    @staticmethod
    def construire(texte):
        """
        Construit et renvoie la racine de l'arbre de Huffman associé à texte.
        Suit les étapes 2 à 6 de l'algorithme du cahier des charges.
 
        Retourne None si le texte est vide.
        """
        if not texte:
            return None
 
        # Chaque couple (caractère, effectif) forme une feuille
        liste = [NoeudHuffman(c, e) for c, e in NoeudHuffman.effectifs(texte)]
 
        # Un seul caractère unique → arbre = une seule feuille
        if len(liste) == 1:
            return liste[0]
 
        # On répète jusqu'à obtenir un seul arbre (la racine)
        while len(liste) > 1:
 
            # On trie par effectif croissant pour accéder aux deux plus petits
            liste.sort(key=lambda n: n.get_poids())
 
            # On prend les deux nœuds de poids minimal
            g = liste.pop(0)
            d = liste.pop(0)
 
            # On forme le nouveau nœud parent :
            # - sa chaine est la concaténation des chaines de ses deux fils
            # - son poids est la somme des poids de ses deux fils
            parent = NoeudHuffman(
                g.get_chaine() + d.get_chaine(),
                g.get_poids() + d.get_poids(),
                g,
                d
            )
 
            # On ajoute le nœud parent à la liste et on recommence
            liste.append(parent)
 
        # On retourne le dernier nœud restant : la racine de l'arbre
        return liste[0]
 

    @staticmethod
    def encoder(racine):
        """
        Méthode statique utilitaire appelée depuis main.py.
        Retourne le dictionnaire {caractère: code_huffman} en appelant
        get_encodages() sur la racine.
        """
        if racine is None:
            return {}
        return racine.get_encodages()
 


    # ---------------------------------------------#
    #  Méthodes d'instance : encodage et décodage  #
    # ---------------------------------------------#
 
    def get_encodages(self, encodages=None, prefixe=""):
        """
        Parcourt l'arbre récursivement et construit un dictionnaire
        {caractère: code_huffman}.
        Branche gauche -> '0', branche droite -> '1'.
        """
        # Initialisation du dictionnaire au premier appel
        if encodages is None:
            encodages = {}
 
        if self.est_feuille():
            # Cas particulier : arbre avec un seul caractère unique → code = "0"
            encodages[self.get_chaine()] = prefixe if prefixe else "0"
        else:
            if self.admet_gauche():
                self._gauche.get_encodages(encodages, prefixe + "0")
            if self.admet_droit():
                self._droit.get_encodages(encodages, prefixe + "1")
 
        return encodages
 

    def compresser(self, texte):
        """
        Compresse le texte en utilisant les encodages de l'arbre.
        Renvoie la chaine compressée composée de '0' et de '1'.
        """
        encodages = self.get_encodages()
        res = ""
        for c in texte:
            res += encodages[c]
        return res
 


    def decompresser(self, texte_compresse):
        """
        Décompresse une chaine de '0' et '1' en utilisant l'arbre.
        Branche gauche -> '0', branche droite -> '1'.
 
        Si la racine est une feuille (un seul caractère unique),
        on retourne ce caractère répété autant de fois qu'il y a de bits.
        """

        # Cas particulier : arbre = une seule feuille
        if self.est_feuille():
            return self.get_chaine() * self.get_poids()
 
        decode = ""
        noeud_actuel = self
 
        for bit in texte_compresse:
            if bit == "0":
                noeud_actuel = noeud_actuel.get_gauche()
            else:
                noeud_actuel = noeud_actuel.get_droit()
 
            if noeud_actuel is None:
                break
 
            if noeud_actuel.est_feuille():
                decode += noeud_actuel.get_chaine()
                noeud_actuel = self
 
        return decode