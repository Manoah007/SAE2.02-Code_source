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
        return self._valeur is not None and self._gauche is None and self._droit is None
         
        
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


#====================#
#  Membre B - WESLEY #
#====================#

    def parcours_prefixe(self):
        """
        Cette méthode va parcourir un arbre binaire
        dans l'ordre suivant : racine -> gauche -> droite.
        """
        
        if self is not None: #Condition d'arrêt de la récursion

            # On affiche la valeur de la racine 
            print(self._valeur)

            # On regarde si une branche gauche existe 
            if  self._gauche:
                # On se déplace vers la racine au bout de la racine de gauche
                self._gauche.parcours_prefixe()

            # On regarde si une branche droite existe
            if self._droit:
                # On se déplace vers la racine au bout de la racine de droite
                self._droit.parcours_prefixe()


    def parcours_infixe(self):
        """ 
        Cette méthode va parcourir un arbre binaire
        dans l'ordre suivant : gauche -> racine -> droite.
        """

        if self is not None:

            if  self._gauche:
                self._gauche.parcours_infixe()

            print(self._valeur) # On recitue la valeur d'un noeud après être passé par sa branche gauche
            
            if self._droit:
                self._droit.parcours_infixe()

    
    def parcours_suffixe(self):
        """
        Cette méthode va parcourir un arbre binaire
        dans l'ordre suivant : gauche -> droite -> racine.
        """
        if self is not None:

            if  self._gauche:
                self._gauche.parcours_suffixe()
            
            if self._droit:
                self._droit.parcours_suffixe()

            print(self._valeur)


    def parcours_largeur(self, etage_demander, niveau_actuel=0):
        """
        On cherche la largeur spécifique d'un étage donnée
        On envoie compte le nombre de noeud présent à un étage
        grâce à un compteur et une récursion qui parcours l'arbre
        de manière similaire au méthode précedente
        """
        
        # Ajoute 1 uniquement si on est au niveau demandé
        if niveau_actuel == etage_demander:
            return 1
        
        total_enfants = 0

        # On demande au fils gauche (s'il existe) de chercher au niveau suivant
        if self._gauche is not None:
            total_enfants += self._gauche.parcours_largeur(etage_demander, niveau_actuel + 1)

        # On demande au fils droit (s'il existe) de faire de même
        if self._droit is not None:
            total_enfants += self._droit.parcours_largeur(etage_demander, niveau_actuel + 1)
            
        # On renvoie la somme accumulée
        return total_enfants


    def largeur_max(self):
        """
        Cherche la largeur maximale de l'arbre 
        puis la retourne. 
        """
        
        ascenceur = 0
        largeur_max = 0 # personne à l'étage 0 (la racine)
        largeur_actuelle = 7 # initialisation à une valeur arbitraire pour entrer dans la boucle

        # Tant que l'on est pas arrivé à un étage sans personne
        # On continue de monter dans l'arbre
        while largeur_actuelle != 0: 
            largeur_actuelle = self.parcours_largeur(ascenceur) # personne a l'étage suivant
            
            if largeur_max < largeur_actuelle:
                largeur_max = largeur_actuelle
            ascenceur += 1


        return largeur_max


    def __str__(self):
        return self.constructeur()

    def constructeur(self, niveau=0):
        """
        Affiche l'arbre de manière hiérarchique dans le terminal.
        Le paramètre 'niveau' gère l'espacement (l'indentation).
        """

        affichage = ""
        
        # On parcourt d'abord le fils DROIT (il sera en haut à droite)
        if self._droit is not None:
            affichage += self._droit.constructeur(niveau + 1)

        # On affiche le nœud actuel avec une indentation proportionnelle au niveau
        affichage += "    " * niveau + "-> " + str(self._valeur) + "\n"

        # On parcourt le fils GAUCHE (il sera en bas à droite)
        if self._gauche is not None:
            affichage += self._gauche.constructeur(niveau + 1)
                
        return affichage

#main
if __name__ == "__main__":
    """
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
    """

    ##===== Test de la méthode __str__() et de la méthode constructeur() =====##
    arbre = NoeudBinaire(10)
    arbre.ajouter_element(5)
    arbre.ajouter_element(15)
    arbre.ajouter_element(3)
    arbre.ajouter_element(7)

    # Visualisation pour vérifier la structure
    print("--- Structure de l'arbre ---")
    print(arbre)

    ##===== Test de la méthode parcours_largeur() =====##
    print("--- Test de parcours_largeur ---")
    l0 = arbre.parcours_largeur(0)
    l1 = arbre.parcours_largeur(1)
    l2 = arbre.parcours_largeur(2)
    l3 = arbre.parcours_largeur(3)

    print(f"Étage 0 (doit être 1) : {l0}")
    print(f"Étage 1 (doit être 2) : {l1}")
    print(f"Étage 2 (doit être 2) : {l2}")
    print(f"Étage 3 (doit être 0) : {l3}")

    ##===== Test de la méthode largeur_max() =====##
    print("\n--- Test de largeur_max ---")
    record = arbre.largeur_max()
    print(f"La largeur maximale trouvée est : {record}")

    # Petit test de validation
    if record == 2:
        print("✅ Succès : La largeur max est correcte !")
    else:
        print("❌ Erreur : On attendait 2.")