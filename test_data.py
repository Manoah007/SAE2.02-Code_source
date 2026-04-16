import unittest
from data import nettoyer_texte, taille_ascii, ascii_vers_base2, texte_vers_base2, compresser, decompresser
# On importe une version simplifiée de Noeud pour le test de décompression
# Si ton fichier s'appelle différemment, adapte l'import
from NoeudHuffman import NoeudHuffman 

class TestData(unittest.TestCase):

    def test_nettoyer_texte(self):
        """Vérifie que les accents sont bien supprimés."""
        entree = "Héloïse à l'école"
        attendu = "Heloise a l'ecole"
        self.assertEqual(nettoyer_texte(entree), attendu)

    def test_taille_ascii(self):
        """Vérifie le calcul de la taille (nb_caracteres * 8)."""
        self.assertEqual(taille_ascii("abc"), 24)
        self.assertEqual(taille_ascii(""), 0)

    def test_ascii_vers_base2(self):
        """Vérifie la conversion d'un caractère en binaire sur 8 bits."""
        # 'a' vaut 97 en ASCII, soit 01100001
        self.assertEqual(ascii_vers_base2('a'), '01100001')
        # 'A' vaut 65 en ASCII, soit 01000001
        self.assertEqual(ascii_vers_base2('A'), '01000001')

    def test_texte_vers_base2(self):
        """Vérifie la conversion d'une chaîne complète."""
        self.assertEqual(texte_vers_base2('a'), '01100001')
        self.assertEqual(texte_vers_base2('ab'), '0110000101100010')

    def test_compresser(self):
        """Vérifie la compression avec un dictionnaire de codes donné."""
        codes = {'a': '0', 'b': '10', 'c': '11'}
        self.assertEqual(compresser("abc", codes), "01011")

    def test_decompresser(self):
        """Vérifie la décompression à l'aide d'un arbre de Huffman miniature."""
        # Construction manuelle d'un petit arbre :
        #      racine
        #     /      \
        #  'a'(0)     node
        #            /    \
        #         'b'(10) 'c'(11)
        feuille_a = NoeudHuffman('a', 1)
        feuille_b = NoeudHuffman('b', 1)
        feuille_c = NoeudHuffman('c', 1)
        
        noeud_bc = NoeudHuffman(None, 2, feuille_b, feuille_c)
        racine = NoeudHuffman(None, 3, feuille_a, noeud_bc)

        self.assertEqual(decompresser("01011", racine), "abc")

if __name__ == '__main__':
    unittest.main()