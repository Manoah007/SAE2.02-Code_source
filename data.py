import os
import sys
from unidecode import unidecode


def nettoyer_texte(texte):
    """Nettoie le texte en supprimant les accents et diacritiques."""
    return unidecode(texte)


def taille_ascii(texte):
    """Retourne la taille du texte encodé en ASCII (en bits) : 8 bits par caractère."""
    return len(texte) * 8


def taille_compressee(texte_compresse):
    """Retourne la taille en bits d'un texte déjà compressé (chaine de '0' et '1')."""
    return len(texte_compresse)

##===  ENCODAGE ASCII (vérification) ===#
# def ascii_vers_base2(c):
#     """
#     Reçoit un caractère c et retourne sa représentation binaire
#     sur 8 bits sous forme de chaine de caractères composée de '0' et '1'.
#     Exemple : ascii_vers_base2('a') -> '01100001'
#     """
#     valeur = ord(c)
#     resultat = ""
#     for i in range(7, -1, -1):
#         bit = (valeur >> i) & 1
#         resultat += str(bit)
#     return resultat
 
 
# def texte_vers_base2(texte):
#     """
#     Retourne la représentation binaire complète d'un texte ASCII
#     sous forme de chaine de '0' et '1'.
#     Exemple : texte_vers_base2("ab") -> '0110000101100010'
#     """
#     resultat = ""
#     for c in texte:
#         resultat += ascii_vers_base2(c)
#     return resultat