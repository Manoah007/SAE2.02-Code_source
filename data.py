import os
import sys
from unidecode import unidecode

def nettoyer_texte(texte):
    return unidecode(texte)

def compter_caracteres(texte):
    compteur = {}
    for c in texte:
        if c in compteur:
            compteur[c] += 1
        else:
            compteur[c] = 1
    # Trier par effectif décroissant
    liste_triee = sorted(compteur.items(), key=lambda x: x[1], reverse=True)
    return liste_triee

def taille_ascii(texte):
    return len(texte) * 8