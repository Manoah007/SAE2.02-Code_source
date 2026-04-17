import sys
import os
from data import *
from NoeudHuffman import NoeudHuffman

# Récupération du dossier en paramètre
if len(sys.argv) < 2:
    print("Usage : python3 main.py <dossier_input>")
    sys.exit(1)

# On assigne à la variable le nom du dossier passé en paramètre (ex: "input/")
input_dir = sys.argv[1]


for f in os.listdir(input_dir):

    if f.endswith('.txt'):

        # On récupère le chemin du fichier à partir du dossier input
        f_path = os.path.join(input_dir, f)


        ##--- Lecture du fichier ---##
        with open(f_path, 'r', encoding='utf-8') as fichier:
            texte_brut = fichier.read()

        print(f"\nFichier {f_path} chargé.")


        ##--- Nettoyage ASCII ---##
        # Nettoyage du texte - caractères ASCII (valeurs 0 à 127)
        texte = nettoyer_texte(texte_brut)
        print("Encodage du texte en ASCII OK.")


        ## --- Construction de l'arbre + compression --- #
        print("Construction de l'arbre de Huffman. Compression du texte.")

        racine = NoeudHuffman.construire(texte)
        codes = NoeudHuffman.encoder(racine)
        texte_compresse = racine.compresser(texte)

        print("Construction de l'arbre OK.         Compression OK.")


        ##--- Tailles ---##
        taille_init = taille_ascii(texte)
        taille_comp = taille_compressee(texte_compresse)

        print(f"Taille initiale   :  {taille_init} bits")
        print(f"Taille compressée :  {taille_comp} bits")


        ##--- Vérification décompression (Validation) ---##
        texte_decode = racine.decompresser(texte_compresse)
        if texte_decode == texte:
            print("Vérification décompression : OK")
        else:
            print("Vérification décompression : ERREUR")
        
        print("\n" + "-"*50 + "\n")