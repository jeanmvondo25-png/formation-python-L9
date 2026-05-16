def main():
    # Création d'un dictionnaire structuré
    # Clé : Pseudo de l'ingénieur | Valeur : Un autre dictionnaire (Données)
    equipe_L9 = {
        "jmvondo": {"nom": "Jean", "niveau": "Junior", "langage": "Python"},
        "alinux": {"nom": "Alice", "niveau": "Senior", "langage": "Rust"},
    }

    # 1. Accès classique (Dangereux si la clé n'existe pas)
    print(f"Ingénieur trouvé : {equipe_L9['jmvondo']['nom']}")

    # 2. Accès sécurisé avec .get() (Le standard Google)
    # Si la clé n'existe pas, il renvoie "Non trouvé" au lieu de crasher
    pseudo_inconnu = "root_x"
    infos = equipe_L9.get(pseudo_inconnu, "❌ Utilisateur inexistant dans la base.")
    print(f"Recherche de {pseudo_inconnu} : {infos}")

    # 3. Ajouter un nouvel élément
    equipe_L9["skywalker"] = {"nom": "Luke", "niveau": "Expert", "langage": "Go"}
    
    print(f"\nNombre total d'ingénieurs : {len(equipe_L9)}")
    # --- SOLUTION DU DÉFI ---
    print("\n--- LISTE DES NOMS DE L'ÉQUIPE ---")
    for pseudo, details in equipe_L9.items():
        # 'details' est lui-même un dictionnaire, on accède donc à la clé 'nom'
        nom_ingenieur = details.get("nom")
        print(f"Ingénieur : {nom_ingenieur} (ID: {pseudo})")

if __name__ == "__main__":
    main()
        

