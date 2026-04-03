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


    # Affichage    
    def __str__(self, niveau=0):
        """Affichage hiérarchique de l'arbre avec indentation."""
        # On affiche le nœud actuel avec une indentation proportionnelle à son niveau
        res = "    " * niveau + f"|-> {self._valeur}\n"

        # On affiche récursivement le sous-arbre gauche puis le sous-arbre droit
        if self.admet_gauche():
            res += self._gauche.__str__(niveau + 1)
        if self.admet_droit():
            res += self._droit.__str__(niveau + 1)

        return res
