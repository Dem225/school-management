import sys
from models.utlisateur_Modeles import Utilisateur
from confige.Menu import MENU_PRINCIPALE_ADMINE, MENU_PROFESSEUR, MENU_ETUDIANT, MENU_PRINCIPALE, MENU_CONNECTION

def CONNEXION_User():
    while True:
        print(MENU_PRINCIPALE)
        Choix_connect = input(" Entrez le numéro de votre option : ")
        
        if Choix_connect == '1':
            print(MENU_CONNECTION)
            name = input("Entrez votre nom d'utilisateur : ")
            password = input("Entrez votre mot de passe : ")

            verification = Utilisateur()
            verification.creer_table_utilisateur()
            COMPTE = verification.verifier_identifiants(name, password)
            verification.close()

            if COMPTE:
                Nom_utilisateur, Role_utilisateur = COMPTE[1], COMPTE[2]
                print(f"\n Connexion réussie ! Bienvenue, {Nom_utilisateur} ({Role_utilisateur})\n")
                return Role_utilisateur  
            else:
                print("\n Échec de la connexion. Nom d'utilisateur ou mot de passe incorrect.")
                print("Veuillez réessayer.\n")
                

        elif Choix_connect == '2':
            print("\nMerci, à bientôt ! ")
            sys.exit()  
            
        else:
            print("\n Option invalide ! Veuillez choisir 1 ou 2.\n")