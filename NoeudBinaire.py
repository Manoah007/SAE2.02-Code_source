class NoeudBinaire:

    def __init__(self, valeur, gauche=None, droit=None): #constructeur
        self._valeur = valeur # le '_' signifie que l'attributs est privé
        self._gauche = gauche
        self._droit = droit

    #Getters 
    def get_valeur(self):
        return self._valeur
    
    def get_gauche(self):
        return self._gauche
    
    def get_droit(self):
        return self._droit

    #Setters
    def set_valeur(self,nouvelle_valeur):
        if nouvelle_valeur != "":
            self._valeur = nouvelle_valeur
        else:
            print("Erreur : la valeur ne peut pas être vide.")

    def set_gauche(self, nouveau_gauche):
            self._gauche = nouveau_gauche

    def set_droit(self, nouveau_droit):
            self._droit = nouveau_droit

    #Méthodes
    #Membre A
    def est_vide(self):
        """Un nœud est vide s'il ne contient rien du tout. 
        Donc sa valeur, son fils gauche et son fils droit doivent tous 
        être égaux à None."""
        return self._valeur is None and self._gauche is None and self._droit is None

        
    def est_feuille(self):
        """Dans un arbre, une feuille est le bout d'une branche. C'est
          donc un nœud qui n'a pas de fils gauche ET pas de fils droit."""
        return self._gauche is None and self._droit is None
         
        
    def admet_gauche(self):
        """Un nœud "admet" un fils gauche si son attribut self._gauche 
        contient bien quelque chose (c'est-à-dire s'il n'est pas égal 
        à None"""
        return self._gauche is not None

    def admet_droit(self):
        """Un nœud "admet" un fils droit si son attribut self._droit
        contient bien quelque chose (c'est-à-dire s'il n'est pas égal 
        à None"""        
        return self._droit is not None
    
    def hauteur(self):
        """
        Calcule la hauteur du nœud de manière récursive.
        La hauteur est définie comme la longueur du chemin le plus long 
        entre ce nœud et une feuille. Un nœud feuille a une hauteur de 0.
        
        Retourne :
            int : La hauteur de l'arbre à partir de ce nœud.
        """
        if self.est_feuille():
            return 0
        h_gauche = 0
        h_droit = 0

        if self.admet_gauche():
            h_gauche = 1 + self._gauche.hauteur()

        if self.admet_droit():
            h_droit = 1 + self._droit.hauteur()

        return max(h_gauche, h_droit)

    
    def ajouter_element(self, element):
        """
        Insère un nouvel élément dans l'arbre en respectant la structure 
        d'un Arbre Binaire de Recherche (ABR) :
        - Si l'élément est inférieur à la valeur du nœud, on va à gauche.
        - Si l'élément est supérieur, on va à droite.
        
        Args:
            element : La valeur à insérer dans l'arbre.
        """
        
        if element < self._valeur:
            if self._gauche is None:
                self._gauche = NoeudBinaire(element)
            else : 
                self._gauche.ajouter_element(element)
        elif element > self._valeur:
            if self._droit is None:
                self._droit = NoeudBinaire(element)
            else : 
                self._droit.ajouter_element(element)
        else:
            print("L'élément existe déjà")

     #Membre B
    def parcours_prefixe(self):
        pass


    def parcours_infixe(self):
        pass

    
    def parcours_suffixe(self):
        pass


    def parcours_largeur(self):
        pass

   
    def __str__(self):
        pass
            

#main
if __name__ == "__main__":

    #Test de la méthode est_vide
    print("\n--- Test de la méthode est_vide() ---")
    noeud_plein = NoeudBinaire("A")
    noeud_vide = NoeudBinaire(None)

    print(noeud_plein.est_vide())
    print(noeud_vide.est_vide())

    #Test de la méthode est_feuille
    print("\n--- Test de la méthode est_feuille() ---")
    noeud_enfant = NoeudBinaire("Enfant")
    noeud_parent = NoeudBinaire("Parent", gauche = noeud_enfant)

    print(noeud_enfant.est_feuille())
    print(noeud_parent.est_feuille())

    #Test de la méthode admet_gauche()
    print("\n--- Test de la méthode admet_gauche() ---")
    noeud_enfant = NoeudBinaire("Enfant",)
    noeud_parent1 = NoeudBinaire("Parent1", gauche = noeud_enfant)
    noeud_parent2 = NoeudBinaire("Parent2", droit = noeud_enfant)

    print(noeud_parent1.admet_gauche())
    print(noeud_parent2.admet_gauche())

    #Test de la méthode admet_droit()
    print("\n--- Test de la méthode admet_droit() ---")
    noeud_enfant = NoeudBinaire("Enfant",)
    noeud_parent1 = NoeudBinaire("Parent1", gauche = noeud_enfant)
    noeud_parent2 = NoeudBinaire("Parent2", droit = noeud_enfant)

    print(noeud_parent1.admet_droit())
    print(noeud_parent2.admet_droit())

    #Test de la méthode ajouter_element()
    print("\n--- Test de la méthode ajouter_element() ---")
    racine = NoeudBinaire(10)

    racine.ajouter_element(5)
    racine.ajouter_element(15)
    racine.ajouter_element(3)
    racine.ajouter_element(7)

    print("Valeur de la racine (Attendu : 10) ->", racine.get_valeur())

    noeud_gauche = racine.get_gauche()
    print("Fils gauche de 10 (Attendu : 5) ->", noeud_gauche.get_valeur())
    print("Fils gauche de 5 (Attendu : 3) ->", noeud_gauche.get_gauche().get_valeur())
    print("Fils droit de 5 (Attendu : 7) ->", noeud_gauche.get_droit().get_valeur())
    
    noeud_droit = racine.get_droit()
    print("Fils droit de 10 (Attendu : 15) ->", noeud_droit.get_valeur())
    
    print("\nTest de l'ajout d'un doublon (On ajoute 15 à nouveau) :")
    racine.ajouter_element(15)

    # Test de la méthode hauteur()
    print("\n--- Test de la méthode hauteur() ---")

    print("Hauteur de la racine 10 (Attendu : 2) ->", racine.hauteur())
    
    noeud_cinq = racine.get_gauche()
    print("Hauteur du nœud 5 (Attendu : 1) ->", noeud_cinq.hauteur())
    
    noeud_quinze = racine.get_droit()
    print("Hauteur du nœud 15 (Attendu : 0) ->", noeud_quinze.hauteur())
    
    print("\nOn ajoute le chiffre 1 tout en bas à gauche...")
    racine.ajouter_element(1) 

    print("Nouvelle hauteur de la racine 10 (Attendu : 3) ->", racine.hauteur())
