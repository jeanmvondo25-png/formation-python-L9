def nettoyer_donnees(entrees: list) -> list[float]:
    notes_propres = []
    
    for item in entrees:
        try:
            # On tente de transformer l'élément en nombre décimal
            valeur = float(item)
            notes_propres.append(valeur)
        except ValueError:
            # Si ça échoue (ex: item est "Absent"), on ignore et on continue
            print(f"⚠️ Donnée invalide ignorée : {item}")
        except Exception as e:
            # Pour toute autre erreur inconnue
            print(f"🔥 Erreur inattendue : {e}")
            
    return notes_propres

def main():
    # Liste "sale" avec des erreurs volontaires
    donnees_utilisateurs = [15.5, "12",[], "Absent", 8.0, "Pas de note", 19]
    
    print("Début du nettoyage...")
    resultat = nettoyer_donnees(donnees_utilisateurs)
    
    print(f"\nNotes récupérées : {resultat}")
    print(f"Moyenne : {sum(resultat) / len(resultat)}")

if __name__ == "__main__":
    main()
