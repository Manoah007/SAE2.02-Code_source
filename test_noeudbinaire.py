import unittest
from unittest.mock import patch
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

    # Tests de la méthode admet_gauche / admet_droit
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

    # Tests de la méthode parcours_prefixe (racine -> gauche -> droite)
    def test_parcours_prefixe(self):
        # Arbre : A, gauche=B, droit=C, C.droit=D  → attendu : A B C D
        with patch('builtins.print') as mock_print:
            self.racine.parcours_prefixe()
            valeurs = [appel.args[0] for appel in mock_print.call_args_list]
        self.assertEqual(valeurs, ['A', 'B', 'C', 'D'], "ERREUR: ordre prefixe incorrect")

    def test_parcours_prefixe_feuille(self):
        # Une feuille seule doit juste afficher sa valeur
        with patch('builtins.print') as mock_print:
            self.feuille.parcours_prefixe()
            valeurs = [appel.args[0] for appel in mock_print.call_args_list]
        self.assertEqual(valeurs, ['O'], "ERREUR: prefixe d'une feuille devrait afficher uniquement sa valeur")

    # Tests de la méthode parcours_infixe (gauche -> racine -> droite)
    def test_parcours_infixe(self):
        # Arbre : A, gauche=B, droit=C, C.droit=D  → attendu : B A C D
        with patch('builtins.print') as mock_print:
            self.racine.parcours_infixe()
            valeurs = [appel.args[0] for appel in mock_print.call_args_list]
        self.assertEqual(valeurs, ['B', 'A', 'C', 'D'], "ERREUR: ordre infixe incorrect")

    def test_parcours_infixe_feuille(self):
        with patch('builtins.print') as mock_print:
            self.feuille.parcours_infixe()
            valeurs = [appel.args[0] for appel in mock_print.call_args_list]
        self.assertEqual(valeurs, ['O'], "ERREUR: infixe d'une feuille devrait afficher uniquement sa valeur")

    # Tests de la méthode parcours_suffixe (gauche -> droite -> racine)
    def test_parcours_suffixe(self):
        # Arbre : A, gauche=B, droit=C, C.droit=D  → attendu : B D C A
        with patch('builtins.print') as mock_print:
            self.racine.parcours_suffixe()
            valeurs = [appel.args[0] for appel in mock_print.call_args_list]
        self.assertEqual(valeurs, ['B', 'D', 'C', 'A'], "ERREUR: ordre suffixe incorrect")

    def test_parcours_suffixe_feuille(self):
        with patch('builtins.print') as mock_print:
            self.feuille.parcours_suffixe()
            valeurs = [appel.args[0] for appel in mock_print.call_args_list]
        self.assertEqual(valeurs, ['O'], "ERREUR: suffixe d'une feuille devrait afficher uniquement sa valeur")

    # Tests de la méthode parcours_largeur
    def test_parcours_largeur_etage_0(self):
        # L'étage 0 contient toujours la racine, donc 1 nœud
        self.assertEqual(self.racine.parcours_largeur(0), 1, "ERREUR: l'étage 0 devrait contenir 1 nœud (la racine)")

    def test_parcours_largeur_etage_1(self):
        # L'étage 1 contient B et C, donc 2 nœuds
        self.assertEqual(self.racine.parcours_largeur(1), 2, "ERREUR: l'étage 1 devrait contenir 2 nœuds")

    def test_parcours_largeur_etage_2(self):
        # L'étage 2 contient uniquement D, donc 1 nœud
        self.assertEqual(self.racine.parcours_largeur(2), 1, "ERREUR: l'étage 2 devrait contenir 1 nœud")

    def test_parcours_largeur_etage_inexistant(self):
        # Un étage au-delà de la hauteur de l'arbre doit retourner 0
        self.assertEqual(self.racine.parcours_largeur(5), 0, "ERREUR: un étage inexistant devrait retourner 0")

    # Tests de la méthode largeur_max
    def test_largeur_max(self):
        # L'étage 1 a 2 nœuds (B et C), c'est le plus large
        self.assertEqual(self.racine.largeur_max(), 2, "ERREUR: largeur max devrait être 2")

    def test_largeur_max_feuille(self):
        # Une feuille seule a une largeur max de 1
        self.assertEqual(self.feuille.largeur_max(), 1, "ERREUR: largeur max d'une feuille devrait être 1")

    # Tests de la méthode __str__ (via constructeur)
    def test_str_feuille(self):
        # Une feuille doit contenir sa valeur précédée de "-> "
        self.assertIn('-> O', str(self.feuille), "ERREUR: __str__ d'une feuille devrait contenir '-> O'")

    def test_str_contient_toutes_valeurs(self):
        # __str__ de la racine doit mentionner tous les nœuds de l'arbre
        resultat = str(self.racine)
        for lettre in ['A', 'B', 'C', 'D']:
            self.assertIn(lettre, resultat, f"ERREUR: __str__ devrait contenir '{lettre}'")

    def test_str_indentation(self):
        # Les nœuds fils doivent être plus indentés que la racine
        resultat = str(self.racine)
        lignes = resultat.splitlines()
        ligne_racine = next(l for l in lignes if '-> A' in l)
        ligne_fils = next(l for l in lignes if '-> B' in l)
        self.assertGreater(len(ligne_fils) - len(ligne_fils.lstrip()),
                           len(ligne_racine) - len(ligne_racine.lstrip()),
                           "ERREUR: un fils devrait être plus indenté que la racine")

if __name__ == '__main__':
    unittest.main()