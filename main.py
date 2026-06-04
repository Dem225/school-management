from models.utlisateur_Modeles import Utilisateur

def main():
    print("--- Nettoyage de la Base de Données ---")
    user_manager = Utilisateur()
    user_manager.close()
    print("bien enregister")
if __name__ == "__main__":
    main()
