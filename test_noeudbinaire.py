import unittest
from NoeudBinaire import NoeudBinaire 

class TestNoeudBinaire(unittest.TestCase):

    def setUp(self):
        """Initialisation de quelques structures de test avant chaque test"""
        # Un nœud seul (feuille)
        self.feuille = NoeudBinaire('O')
        self.vide = NoeudBinaire(None)
        self.racine = NoeudBinaire('A')
        self.racine.set_gauche(NoeudBinaire('B'))
        self.racine.set_droit(NoeudBinaire('C'))
        self.racine.get_droit().set_droit(NoeudBinaire('D'))

    # Tests de la méthode est_vide
    def test_est_vide(self):
        self.assertTrue(self.vide.est_vide(), "ERREUR: noeud vide non detecté")
        self.assertFalse(self.feuille.est_vide(), "ERREUR: feuille vide non detecté")

    # Tests de la méthode est_feuille
    def test_est_feuille(self):
        self.assertTrue(self.feuille.est_feuille(), "ERREUR: feuille non reconnue")
        self.assertFalse(self.racine.est_feuille(), "ERREUR: noeud interne vu comme feuille")
        self.assertFalse(self.racine.est_feuille(), "ERREUR: racine a des enfants")
        self.assertFalse(self.vide.est_feuille(), "ERREUR: noeud vide ne devrait pas être une feuille")

    def test_admet_gauche_droit(self):
        # La racine a les deux
        self.assertTrue(self.racine.admet_gauche())
        self.assertTrue(self.racine.admet_droit())

        # Le nœud 'C' n'a qu'un fils droit ('D')
        noeud_c = self.racine.get_droit()
        self.assertFalse(noeud_c.admet_gauche(), "ERREUR: 'C' n'a pas de fils gauche")
        self.assertTrue(noeud_c.admet_droit(), "ERREUR: 'C' doit avoir un fils droit ('D')")

    # Tests de la méthode hauteur
    def test_hauteur(self):
        self.assertEqual(self.feuille.hauteur(), 0, "ERREUR: hauteur d'une feuille devrait être 0")
        self.assertEqual(self.racine.hauteur(), 2, "ERREUR: hauteur devrait être 2")

        # Arbre penché uniquement à gauche
        arbre_gauche = NoeudBinaire('M')
        arbre_gauche.set_gauche(NoeudBinaire('A'))
        arbre_gauche.get_gauche().set_gauche(NoeudBinaire('Z'))
        self.assertEqual(arbre_gauche.hauteur(), 2, "ERREUR: hauteur d'un arbre gauche de 3 niveaux devrait être 2")

    # Tests de la méthode ajouter_element
    def test_ajouter_element(self):
        arbre_test = NoeudBinaire('M')
        # 'A' est avant 'M', donc va à gauche
        arbre_test.ajouter_element('A')
        # 'Z' est après 'M', donc va à droite
        arbre_test.ajouter_element('Z')
        
        self.assertEqual(arbre_test.get_gauche().get_valeur(), 'A', "ERREUR: 'A' devrait être à gauche de 'M'")
        self.assertEqual(arbre_test.get_droit().get_valeur(), 'Z', "ERREUR: 'Z' devrait être à droite de 'M'")

    def test_ajouter_element_recursif(self):
        arbre_test = NoeudBinaire('M')
        arbre_test.ajouter_element('A')
        # 'B' est après 'A' mais avant 'M', donc va à droite de 'A'
        arbre_test.ajouter_element('B')

        self.assertEqual(arbre_test.get_gauche().get_droit().get_valeur(), 'B', "ERREUR: 'B' devrait être à droite de 'A'")

    def test_ajouter_element_doublon(self):
        arbre_test = NoeudBinaire('M')
        arbre_test.ajouter_element('A')
        # Insérer un doublon ne doit pas modifier l'arbre
        arbre_test.ajouter_element('A')

        self.assertIsNone(arbre_test.get_gauche().get_gauche(), "ERREUR: un doublon ne devrait pas être inséré à gauche")
        self.assertIsNone(arbre_test.get_gauche().get_droit(), "ERREUR: un doublon ne devrait pas être inséré à droite")

if __name__ == '__main__':
    unittest.main()