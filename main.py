from models.students_Modeles import studentsModel

def main():
    print("--- Test de la base de données ---")
    user_manager = studentsModel()
    user_manager.Ajouter("nom", "prenom", 13, "classe", "matricule")
    print(user_manager.Lister_etudiant())
    user_manager.close()
if __name__ == "__main__":
    main()
    
























        