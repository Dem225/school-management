import sys
from models.utlisateur_Modeles import Utilisateur
from confige.Menu import  MENU_PRINCIPALE, MENU_CONNECTION
import logging

def CONNEXION_User():
    etudiant_id = None
    id_user = None
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
                
    
                
                if COMPTE:
                    result = verification.get_student_id_from_user_id(COMPTE[0])
                    Role_utilisateur = COMPTE[2]   
                    if Role_utilisateur == 'étudiant':
                        if result is None:
                            print("Aucun profil étudiant associé à ce compte.")
                            continue
                        etudiant_id = result[0]
                    elif Role_utilisateur=='admin':
                        id_user          =verification.get_user_id_from_user_id(COMPTE[0])
                    user_name        = COMPTE[3]   
                    verification.close()
                    print(f"\nConnexion réussie ! Bienvenue, {user_name} ({Role_utilisateur})\n")
                    logging.info(f"Mr ou Md :({user_name}) pour role ({Role_utilisateur}) c'est connecter")
                    
                    return Role_utilisateur, etudiant_id,id_user
                else:
                    print("\n Nom d'utilisateur ou mot de passe incorrect.")
                    logging.warning(f"ÉCHEC DE CONNEXION VEUILLE VOUS RECONNECTER ! ")
                    print("Veuillez réessayer de vous connecter.\n")
                   
        elif Choix_connect == '2':
            print("\nMerci, à bientôt !")
            logging.info("Application fermée par l'utilisateur.")
            sys.exit()
            
        else:
            print("\nOption invalide ! Veuillez choisir 1 ou 2.\n")