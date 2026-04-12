from NoeudBinaire import NoeudBinaire

class NoeudHuffman(NoeudBinaire):
    """
    Arbre de Huffman : arbre binaire ou chaque nœud
    a pour valeur un tuple (chaine, poids).
    - chaine : str = les caractères du sous-arbre
    - poids  : int = somme des effectifs des caractères
    
    Les setters ne sont pas redéfinis ici car :
    - on ne modifie jamais un nœud existant dans l'algorithme de Huffman
    - on crée toujours de nouveaux nœuds parents lors des fusions
    - les setters de NoeudBinaire sont déjà hérités si besoin
    """

    # Constructeur                                                   
    def __init__(self, chaine, poids, gauche=None, droit=None):
        # On appelle le constructeur de NoeudBinaire en passant un tuple (chaine, poids) comme valeur du nœud
        super().__init__((chaine, poids), gauche, droit)

    # Getters                                                              
    def get_chaine(self):
        # Retourne la chaine de caractères du nœud (1er élément du tuple)
        return self._valeur[0]

    def get_poids(self):
        # Retourne le poids du nœud, la somme des effectifs des caractères présents dans ce sous-arbre (2ème élément du tuple)
        return self._valeur[1]
    
    
    # Méthodes                                                             
    @staticmethod
    def effectifs(texte):
        """
        Etape 1 de l'algorithme de Huffman :
        Construit la liste L des couples (caractère, effectif)
        triée par effectif décroissant.
        """
        eff = {}
        for c in texte:
            # On compte le nombre d'occurrences de chaque caractère
            eff[c] = eff.get(c, 0) + 1
        # On trie par effectif décroissant
        return sorted(eff.items(), key=lambda x: x[1], reverse=True)

    @staticmethod
    def construire(texte):
        """
        Construit et renvoie la racine de l'arbre de Huffman associé à texte.
        Suit les étapes 2 à 6 de l'algorithme du cahier des charges.
        """
        if not texte:
            return None

        # Etape 2 : chaque couple (caractère, effectif) forme une feuille
        liste = [NoeudHuffman(c, e) for c, e in NoeudHuffman.effectifs(texte)]

        # Etape 6 : on répète jusqu'à obtenir un seul arbre (la racine)
        while len(liste) > 1:

            # Etape 3 : on trie par effectif croissant pour accéder aux deux plus petits
            liste.sort(key=lambda n: n.get_poids())

            # Etape 4 : on prend les deux nœuds de poids minimal
            g = liste.pop(0)
            d = liste.pop(0)

            # On forme le nouveau nœud parent :
            # - sa chaine est la concatenation des chaines de ses deux fils
            # - son poids est la somme des poids de ses deux fils
            parent = NoeudHuffman(
                g.get_chaine() + d.get_chaine(),
                g.get_poids() + d.get_poids(),
                g,
                d
            )

            # Etape 5 : on ajoute le nouveau nœud parent à la liste
            # et on recommence jusqu'à n'avoir plus qu'un seul nœud
            liste.append(parent)

        # On retourne le dernier nœud restant : la racine de l'arbre
        return liste[0]
    

    # Affichage    
    def __str__(self, niveau=0):
        """Affichage hiérarchique de l'arbre avec indentation."""
        # On affiche le nœud actuel avec une indentation proportionnelle à son niveau
        res = "    " * niveau + f"|--> {self._valeur}\n"

        # On affiche récursivement le sous-arbre gauche puis le sous-arbre droit
        if self.admet_gauche():
            res += self._gauche.__str__(niveau + 1)
        if self.admet_droit():
            res += self._droit.__str__(niveau + 1)

        return res
    
    def get_encodages(self, encodages={}, prefixe=""):
        """
        Parcourt l'arbre et construit un dictionnaire {caractère: code_huffman}.
        Branche gauche -> '0', branche droite -> '1'.
        """
        # Si c'est une feuille on enregistre le code du caractère
        if self.est_feuille():
            encodages[self.get_chaine()] = prefixe if prefixe else "0"
        else:
            # On descend à gauche en ajoutant '0' au préfixe
            if self.admet_gauche():
                self._gauche.get_encodages(encodages, prefixe + "0")
            # On descend à droite en ajoutant '1' au préfixe
            if self.admet_droit():
                self._droit.get_encodages(encodages, prefixe + "1")

        return encodages

    def compresser(self, texte):
        """
        Compresse le texte en utilisant les encodages de l'arbre.
        Renvoie la chaine compressée composée de '0' et de '1'.
        """
        # On récupère les encodages
        encodages = self.get_encodages()
        
        # On remplace chaque caractère par son code Huffman
        res = ""
        for c in texte:
            res += encodages[c]
        
        return res
    
    def decompresser(self, texte_compresse):
        """
        Décompresse une chaine de '0' et '1' en utilisant l'arbre.
        Branche gauche -> '0', branche droite -> '1'.
        """
        decode = ""
        noeud_actuel = self

        for bit in texte_compresse:
            # On descend dans l'arbre selon le bit
            if bit == "0":
                noeud_actuel = noeud_actuel.get_gauche()
            else:
                noeud_actuel = noeud_actuel.get_droit()

            # Si on arrive sur une feuille on a trouvé un caractère
            if noeud_actuel.est_feuille():
                decode += noeud_actuel.get_chaine()
                # On repart de la racine
                noeud_actuel = self

        return decode

