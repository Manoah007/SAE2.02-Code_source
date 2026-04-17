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