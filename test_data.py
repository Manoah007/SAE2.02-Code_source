import unittest

from data import (
    nettoyer_texte,
    taille_ascii,
    ascii_vers_base2,
    texte_vers_base2,
    taille_compressee
)


class TestData(unittest.TestCase):

    # nettoyer_texte
    def test_nettoyer_texte_accents(self):
        self.assertEqual(nettoyer_texte("éàç"), "eac")
        self.assertEqual(nettoyer_texte("français"), "francais")
        self.assertEqual(nettoyer_texte("École"), "Ecole")

    def test_nettoyer_texte_deja_ascii(self):
        self.assertEqual(nettoyer_texte("abc123"), "abc123")


    # taille_ascii
    def test_taille_ascii_simple(self):
        self.assertEqual(taille_ascii("abc"), 24)

    def test_taille_ascii_vide(self):
        self.assertEqual(taille_ascii(""), 0)


    # ascii_vers_base2
    def test_ascii_vers_base2_a(self):
        self.assertEqual(ascii_vers_base2('a'), "01100001")

    def test_ascii_vers_base2_A(self):
        self.assertEqual(ascii_vers_base2('A'), "01000001")

    def test_ascii_vers_base2_zero(self):
        self.assertEqual(ascii_vers_base2('0'), "00110000")


    # texte_vers_base2
    def test_texte_vers_base2_simple(self):
        self.assertEqual(
            texte_vers_base2("ab"),
            "0110000101100010"
        )

    def test_texte_vers_base2_un_caractere(self):
        self.assertEqual(texte_vers_base2("a"), "01100001")

    def test_texte_vers_base2_vide(self):
        self.assertEqual(texte_vers_base2(""), "")


    # taille_compressee
    def test_taille_compressee_simple(self):
        self.assertEqual(taille_compressee("0101"), 4)

    def test_taille_compressee_vide(self):
        self.assertEqual(taille_compressee(""), 0)


if __name__ == "__main__":
    unittest.main()