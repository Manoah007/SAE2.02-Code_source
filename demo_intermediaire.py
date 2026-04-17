from NoeudBinaire import NoeudBinaire
from NoeudHuffman import NoeudHuffman

def demonstration_abr_lettres():
    print("--- PARTIE 1 : Arbre Binaire de Recherche (ABR) ---")
    
    # On commence avec une lettre "centrale" (M) pour avoir un arbre équilibré
    racine = NoeudBinaire("M")
    
    # Insertion de lettres dans le désordre
    # 'F' ira à gauche de 'M', 'S' à droite, etc.
    lettres = ["F", "S", "B", "I", "P", "X"]
    for l in lettres:
        racine.ajouter_element(l)
    
    print("\nStructure de l'arbre binaire (Visualisation hiérarchique) :")
    # Utilise ta méthode __str__ qui appelle constructeur()
    print(racine)
    
    print(f"Hauteur de l'arbre : {racine.hauteur()}") #
    print(f"Largeur maximale : {racine.largeur_max()}") #
    
    print("\n--- Vérification des parcours ---")
    print("Préfixe (Racine -> G -> D) :", end=" ")
    racine.parcours_prefixe() #
    
    print("\nInfixe (Alphabet trié : B F I M P S X) :", end=" ")
    racine.parcours_infixe() #
    
    print("\nSuffixe (G -> D -> Racine) :", end=" ")
    racine.parcours_suffixe() #
    print("\n" + "="*50 + "\n")



def demonstration_huffman():
    print("--- PARTIE 2 : Algorithme de Huffman ---")
    # On utilise une chaîne de caractères pour générer l'arbre
    phrase = "L'algorithme, c'est trop cool !"
    print(f"Texte à compresser : '{phrase}'")
    
    # Calcul des fréquences (Etape 1)
    frequences = NoeudHuffman.effectifs(phrase)
    print(f"Effectifs calculés : {frequences}")
    
    # Construction de l'arbre de Huffman
    arbre = NoeudHuffman.construire(phrase)
    
    print("\nArbre de Huffman généré :")
    # Utilise ta méthode __str__ spécifique à Huffman
    print(arbre)
    
    # Le poids total doit être égal au nombre de lettres (6 pour 'banane')
    print(f"Poids total (somme des fréquences) : {arbre.get_poids()}")



if __name__ == "__main__":
    demonstration_abr_lettres()
    demonstration_huffman()