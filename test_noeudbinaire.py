import unittest
from NoeudBinaire import NoeudBinaire 

class TestNoeudBinaire(unittest.TestCase):

    def setUp(self):
        """Initialisation de quelques structures de test avant chaque test"""
        # Un nœud seul (feuille)
        self.feuille = NoeudBinaire(10)
        self.vide = NoeudBinaire(None)
        self.racine = NoeudBinaire(10)
        self.racine.set_gauche(NoeudBinaire(5))
        self.racine.set_droit(NoeudBinaire(15))
        self.racine.get_droit().set_droit(NoeudBinaire(20))

    # Tests de la méthode est_vide
    def test_est_vide(self):
        self.assertTrue(self.vide.est_vide(), "ERREUR: noeud vide non detecté")
        self.assertFalse(self.feuille.est_vide(), "ERREUR: feuille vide non detecté")

    # Tests de la méthode est_feuille
    def test_est_feuille(self):
        self.assertTrue(self.feuille.est_feuille(), "ERREUR: feuille non reconnue")
        self.assertFalse(self.racine.est_feuille(), "ERREUR: noeud interne vu comme feuille")

    # Tests des méthodes admet_gauche et admet_droit
    def test_admet_gauche(self):
        self.assertTrue(self.racine.admet_gauche(), "ERREUR: fils gauche manquant")
        self.assertFalse(self.feuille.admet_gauche(), "ERREUR: faux fils gauche detecte")

    def test_admet_droit(self):
        self.assertTrue(self.racine.admet_droit(), "ERREUR: fils droit manquant")
        self.assertFalse(self.feuille.admet_droit(), "ERREUR: faux fils droit detecte")

    # Tests de la méthode hauteur
    def test_hauteur(self):
        self.assertEqual(self.feuille.hauteur(), 0)
        self.assertEqual(self.racine.hauteur(), 2)
        n_unique = NoeudBinaire(1)
        n_unique.set_gauche(NoeudBinaire(0))
        self.assertEqual(n_unique.hauteur(), 1)

    # Tests de la méthode ajouter_element
    def test_ajouter_element(self):
        abr = NoeudBinaire(10)
        
        # Test ajout à gauche
        abr.ajouter_element(5)
        self.assertIsNotNone(abr.get_gauche())
        self.assertEqual(abr.get_gauche().get_valeur(), 5)
        
        # Test ajout à droite
        abr.ajouter_element(15)
        self.assertIsNotNone(abr.get_droit())
        self.assertEqual(abr.get_droit().get_valeur(), 15)
        
        # Test récursivité (doit descendre à gauche de 5)
        abr.ajouter_element(2)
        self.assertEqual(abr.get_gauche().get_gauche().get_valeur(), 2)
        
        # Test élément déjà existant (ne doit rien changer à la structure)
        abr.ajouter_element(10) 

    # Test du constructeur (cas limites)
    def test_init(self):
        n = NoeudBinaire(42)
        self.assertEqual(n.get_valeur(), 42)
        self.assertIsNone(n.get_gauche())
        self.assertIsNone(n.get_droit())

if __name__ == '__main__':
    unittest.main()