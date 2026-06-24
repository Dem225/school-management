import sys
from models.utlisateur_Modeles import Utilisateur
from confige.Menu import  MENU_PRINCIPALE, MENU_CONNECTION
import logging

def CONNEXION_User():
    while True:
        print(MENU_PRINCIPALE)
        Choix_connect = input(" Entrez le numéro de votre option : ")
        
        if Choix_connect == '1':
            
            while True:
                print(MENU_CONNECTION)
                
                user_name = input("Entrez voutre user_name (pseudo): ")
                password = input("Entrez votre mot de passe : ")

                verification = Utilisateur()
                verification.creer_table_utilisateur()
                COMPTE = verification.verifier_identifiants(user_name, password)
                verification.close()
    
                
                if COMPTE:
                    user_name, Role_utilisateur = COMPTE[3], COMPTE[2]
                    print(f"\nConnexion réussie ! Bienvenue, {user_name} ({Role_utilisateur})\n")
                    logging.info(f"Mr ou Md :({user_name} )pour role ({Role_utilisateur}) c'est connecter ")
                    return Role_utilisateur  
                else:
                    print("\n Nom d'utilisateur ou mot de passe incorrect.")
                    logging.warning(f"ÉCHEC DE CONNEXION VEUILLE VOUS RECONNECTER ! ")
                    print("Veuillez réessayer de vous connecter.\n")
                   
        elif Choix_connect == '2':
            print("\nMerci, à bientôt ! ")
            logging.info(f"Mr ou Md {user_name}  pour role {Role_utilisateur} c'est déconnecter  ")
            sys.exit()  
            
        else:
            print("\nOption invalide ! Veuillez choisir 1 ou 2.\n")