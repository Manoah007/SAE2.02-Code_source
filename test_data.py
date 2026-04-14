from data import nettoyer_texte, compter_caracteres, taille_ascii

# Test nettoyage
assert nettoyer_texte("Élève") == "Eleve"
assert nettoyer_texte("café") == "cafe"
print("Tests nettoyage OK")

# Test comptage
liste = compter_caracteres("bonjour")
assert liste[0][0] == 'o'  # 'o' apparait 2 fois, donc en premier
assert liste[0][1] == 2
print("Tests comptage OK")

# Test taille
assert taille_ascii("abc") == 24  # 3 caractères x 8 bits
print("Tests taille OK")