import os
import sys
from unidecode import unidecode


def nettoyer_texte(texte):
    """Convertit le texte en ASCII en supprimant les accents et diacritiques."""
    return unidecode(texte)


def taille_ascii(texte):
    """Retourne la taille du texte encodé en ASCII (en bits) : 8 bits par caractère."""
    return len(texte) * 8


def ascii_vers_base2(c):
    """
    Reçoit un caractère c et retourne sa représentation binaire
    sur 8 bits sous forme de chaine de caractères composée de '0' et '1'.
    Exemple : ascii_vers_base2('a') -> '01100001'
    """
    valeur = ord(c)
    resultat = ""
    for i in range(7, -1, -1):
        bit = (valeur >> i) & 1
        resultat += str(bit)
    return resultat


def texte_vers_base2(texte):
    """
    Retourne la représentation binaire complète d'un texte ASCII
    sous forme de chaine de '0' et '1'.
    """
    resultat = ""
    for c in texte:
        resultat += ascii_vers_base2(c)
    return resultat


def compresser(texte, codes_huffman):
    """
    Compresse le texte en remplaçant chaque caractère par son code Huffman.
    
    Paramètres :
        texte         : chaine de caractères à compresser
        codes_huffman : dictionnaire {caractère: code_binaire}
    
    Retourne la chaine compressée (composée de '0' et '1').
    """
    resultat = ""
    for c in texte:
        resultat += codes_huffman[c]
    return resultat


def decompresser(texte_compresse, racine_huffman):
    """
    Décompresse une chaine binaire en utilisant l'arbre de Huffman.
    
    Paramètres :
        texte_compresse : chaine de '0' et '1'
        racine_huffman  : racine de l'arbre de Huffman (NoeudHuffman)
    
    Retourne la chaine de caractères décompressée.
    """
    chaine_decodee = ""
    noeud_courant = racine_huffman

    for bit in texte_compresse:
        if bit == '0':
            noeud_courant = noeud_courant.get_gauche()
        else:
            noeud_courant = noeud_courant.get_droit()

        if noeud_courant.est_feuille():
            chaine_decodee += noeud_courant.get_chaine()
            noeud_courant = racine_huffman

    return chaine_decodee


def taille_compressee(texte_compresse):
    """Retourne la taille en bits d'un texte déjà compressé (chaine de '0' et '1')."""
    return len(texte_compresse)