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