import unittest
from NoeudHuffman import NoeudHuffman


class TestNoeudHuffman(unittest.TestCase):

    def setUp(self):
        """Initialisation de quelques structures de test avant chaque test"""
        # Feuilles simples
        self.feuille_a = NoeudHuffman("a", 5)
        self.feuille_b = NoeudHuffman("b", 3)
        self.feuille_c = NoeudHuffman("c", 1)

        # Nœud parent construit manuellement
        self.parent = NoeudHuffman(
            self.feuille_b.get_chaine() + self.feuille_c.get_chaine(),
            self.feuille_b.get_poids() + self.feuille_c.get_poids(),
            self.feuille_b,
            self.feuille_c
        )

        # Arbre complet construit via construire()
        self.racine = NoeudHuffman.construire("abracadabra")

    def test_valeur_stockee_comme_tuple(self):
        self.assertEqual(self.feuille_a._valeur, ("a", 5), "ERREUR: la valeur interne devrait être un tuple (chaine, poids)")

    def test_feuille_sans_enfants(self):
        self.assertFalse(self.feuille_a.admet_gauche(), "ERREUR: une feuille ne devrait pas avoir de fils gauche")
        self.assertFalse(self.feuille_a.admet_droit(), "ERREUR: une feuille ne devrait pas avoir de fils droit")

    def test_parent_avec_enfants(self):
        self.assertTrue(self.parent.admet_gauche(), "ERREUR: le parent devrait avoir un fils gauche")
        self.assertTrue(self.parent.admet_droit(), "ERREUR: le parent devrait avoir un fils droit")

    # Tests de la méthode effectifs
    def test_effectifs_texte_vide(self):
        self.assertEqual(NoeudHuffman.effectifs(""), [], "ERREUR: effectifs d'un texte vide devrait être []")

    def test_effectifs_un_caractere(self):
        self.assertEqual(NoeudHuffman.effectifs("a"), [("a", 1)], "ERREUR: effectifs de 'a' devrait être [('a', 1)]")

    def test_effectifs_caractere_repete(self):
        self.assertEqual(NoeudHuffman.effectifs("aaa"), [("a", 3)], "ERREUR: effectifs de 'aaa' devrait être [('a', 3)]")

    def test_effectifs_tri_decroissant(self):
        res = NoeudHuffman.effectifs("aaabbc")
        poids = [e for _, e in res]
        self.assertEqual(poids, sorted(poids, reverse=True), "ERREUR: effectifs devrait être trié par ordre décroissant")

    def test_effectifs_premier_plus_frequent(self):
        res = NoeudHuffman.effectifs("aaabbc")
        self.assertEqual(res[0], ("a", 3), "ERREUR: le premier élément devrait être le plus fréquent ('a', 3)")

    def test_effectifs_tous_caracteres_presents(self):
        res = NoeudHuffman.effectifs("abc")
        caracteres = [c for c, _ in res]
        self.assertIn("a", caracteres, "ERREUR: 'a' devrait apparaître dans les effectifs")
        self.assertIn("b", caracteres, "ERREUR: 'b' devrait apparaître dans les effectifs")
        self.assertIn("c", caracteres, "ERREUR: 'c' devrait apparaître dans les effectifs")

    # Tests de la méthode construire
    def test_construire_texte_vide(self):
        self.assertIsNone(NoeudHuffman.construire(""), "ERREUR: construire('') devrait retourner None")

    def test_construire_un_caractere(self):
        racine = NoeudHuffman.construire("a")
        self.assertEqual(racine.get_chaine(), "a", "ERREUR: chaine de la racine devrait être 'a'")
        self.assertEqual(racine.get_poids(), 1, "ERREUR: poids de la racine devrait être 1")

    def test_construire_poids_racine_egal_longueur_texte(self):
        texte = "abracadabra"
        self.assertEqual(self.racine.get_poids(), len(texte), "ERREUR: le poids de la racine devrait être égal à la longueur du texte")

    def test_construire_chaine_racine_contient_tous_les_caracteres(self):
        for c in set("abracadabra"):
            self.assertIn(c, self.racine.get_chaine(), f"ERREUR: '{c}' devrait apparaître dans la chaine de la racine")

    def test_construire_feuille_sans_enfants(self):
        racine = NoeudHuffman.construire("a")
        self.assertFalse(racine.admet_gauche(), "ERREUR: une feuille ne devrait pas avoir de fils gauche")
        self.assertFalse(racine.admet_droit(), "ERREUR: une feuille ne devrait pas avoir de fils droit")

    def test_construire_plusieurs_caracteres_a_des_enfants(self):
        racine = NoeudHuffman.construire("ab")
        self.assertTrue(racine.admet_gauche() or racine.admet_droit(), "ERREUR: la racine devrait avoir au moins un enfant")

    # Tests de la méthode __str__
    def test_str_contient_chaine_et_poids(self):
        affichage = str(self.feuille_a)
        self.assertIn("a", affichage, "ERREUR: __str__ devrait contenir la chaine du nœud")
        self.assertIn("5", affichage, "ERREUR: __str__ devrait contenir le poids du nœud")

    def test_str_feuille_une_seule_ligne(self):
        self.assertEqual(str(self.feuille_a).count("\n"), 1, "ERREUR: l'affichage d'une feuille devrait tenir sur une seule ligne")

    def test_str_enfants_indentes(self):
        affichage = str(self.parent)
        lignes = affichage.splitlines()
        self.assertTrue(lignes[0].startswith("|->"), "ERREUR: la racine (niveau 0) ne devrait pas être indentée")
        for ligne in lignes[1:]:
            self.assertTrue(ligne.startswith("    "), "ERREUR: les enfants devraient être indentés d'un niveau")

if __name__ == '__main__':
    unittest.main()