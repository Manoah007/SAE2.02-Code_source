import sys
import os
from data import nettoyer_texte, taille_ascii, taille_compressee
from NoeudHuffman import NoeudHuffman

# Récupération du dossier en paramètre
if len(sys.argv) < 2:
    print("Usage : python3 main.py <dossier_input>")
    sys.exit(1)

input_dir = sys.argv[1]

for f in os.listdir(input_dir):
    if f.endswith('.txt'):
        f_path = os.path.join(input_dir, f)

        # --- Lecture du fichier ---
        with open(f_path, 'r', encoding='utf-8') as fichier:
            texte_brut = fichier.read()

        print(f"Fichier {f_path} chargé.")

        # --- Nettoyage ASCII ---
        texte = nettoyer_texte(texte_brut)
        print("Encodage du texte en ASCII OK.")

        # --- Construction de l'arbre + compression ---
        print("Construction de l'arbre de Huffman. Compression du texte.")

        racine = NoeudHuffman.construire(texte)
        codes = NoeudHuffman.encoder(racine)
        texte_compresse = racine.compresser(texte)

        print("Construction de l'arbre OK.        Compression OK.")

        # --- Tailles ---
        taille_init = taille_ascii(texte)
        taille_comp = taille_compressee(texte_compresse)

        print(f"Taille initiale :   {taille_init} bits")
        print(f"Taille compressée : {taille_comp} bits")

        # --- Vérification décompression (optionnel, pour valider) ---
        # texte_decode = decompresser(texte_compresse, racine)
        # if texte_decode == texte:
        #     print("Vérification décompression : OK")
        # else:
        #     print("Vérification décompression : ERREUR")

        print()