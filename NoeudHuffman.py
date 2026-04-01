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
        pass

    def set_gauche(self, nouveau_gauche):
        pass

    def set_droit(self, nouveau_droit):
        pass

    #Méthodes
    #Membre A
    def est_vide(self):
        pass
        
    def est_feuille(self):
        pass
         
        
    def admet_gauche(self):
        pass

    def admet_droit(self):      
        pass
    
    def hauteur(self):
        pass
    
    def ajouter_element(self, element):
        pass
    
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
    