def main():
    # Deux chaînes de caractères identiques
    texte1 = "Google"
    texte2 = "Google"
    
    # Deux listes ayant le même contenu
    liste1 = [1, 2, 3]
    liste2 = [1, 2, 3]
    
    print("--- CAS DES STRING (IMMUTABLES) ---")
    print(f"Adresse de texte1 : {id(texte1)}")
    print(f"Adresse de texte2 : {id(texte2)}")
    print(f"Est-ce le même objet ? {texte1 is texte2}")
    
    print("\n--- CAS DES LISTES (MUTABLES) ---")
    print(f"Adresse de liste1 : {id(liste1)}")
    print(f"Adresse de liste2 : {id(liste2)}")
    print(f"Est-ce le même objet ? {liste1 is liste2}")

if __name__ == "__main__":
    main()

