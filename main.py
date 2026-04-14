import sys
import os
from data import nettoyer_texte, compter_caracteres, taille_ascii

input_dir = sys.argv[1]

#Pour le moment ce main est temporaire en attendant vos fichiers
for f in os.listdir(input_dir):
    if f.endswith('.txt'):
        f_path = os.path.join(input_dir, f)
        with open(f_path, 'r', encoding='utf-8') as fichier:
            texte_brut = fichier.read()
        
        texte = nettoyer_texte(texte_brut)
        liste = compter_caracteres(texte)
        taille_initiale = taille_ascii(texte)
        
        print(f"Fichier {f_path} chargé.")
        print(f"Taille initiale : {taille_initiale} bits")
        print(f"Liste des caractères : {liste[:5]}...")  # Affiche les 5 premiers