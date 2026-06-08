import sys
from models.utlisateur_Modeles import Utilisateur
from confige.Menu import MENU_PRINCIPALE_ADMINE, MENU_PROFESSEUR, MENU_ETUDIANT, MENU_PRINCIPALE ,MENU_CONNECTION


def CONNEXION_User():
    
    print(MENU_PRINCIPALE)
    Choix_connect=input("entrez votre choix : ")
    if Choix_connect=='1':
        print(MENU_CONNECTION)
        name = input("Entrez votre nom d'utilisateur : ")
        password = input("Entrez votre mot de passe : ")

        verification = Utilisateur()
        verification.creer_table_utilisateur()
        COMPTE = verification.verifier_identifiants(name, password)
        verification.close()

        if COMPTE:
            Nom_utilisateur, Role_utilisateur = COMPTE[1], COMPTE[2]
            print(f"Connexion réussie ! Bienvenue, {Nom_utilisateur} ({Role_utilisateur})")
            
            return Role_utilisateur
        else:
            print("Échec de la connexion. Nom d'utilisateur ou mot de passe incorrect.")
            sys.exit()

    elif Choix_connect=='2':
        print("Merci a bientot !! ")
        return