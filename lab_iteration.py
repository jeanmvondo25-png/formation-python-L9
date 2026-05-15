def filtrer_notes():
    notes = [14.5, 8.0, 12.0, 9.5, 17.0, 10.0, 5.5, 19.0]
    
    # List comprehension avec une condition (IF) à la fin
    notes_valides = [n for n in notes if n >= 10.0]
    
    print("--- RÉSULTAT DU FILTRAGE ---")
    print(f"Toutes les notes : {notes}")
    print(f"Notes supérieures ou égales à 10 : {notes_valides}")

if __name__ == "__main__":
    filtrer_notes()
