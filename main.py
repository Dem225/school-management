from models.utlisateur_Modeles import Utilisateur
import sys  

def MENU_principale():
    print(" \n Bienvenue dans le système de gestion de utilisateurs  principale (ADMIS) !")
    print("1. Gérer les utilisateurs")
    print("2. Gérer les Professeurs")
    print("3. DECONNEXION")

def MENU_PROFESSEUR():
    print(" \n Bienvenue dans le système de gestion des utilisateurs  professeur !")
    print("1. Saisir les notes des étudiants")
    print("2. Gérer les  absences des étudiants")
    print("3. DECONNEXION")

def MENU_ETUDIANT():
    print(" \n Bienvenue dans le système de gestion des utilisateurs  étudiant !")
    print("1. Consulter les notes")
    print("2. Consulter les absences")
    print("3. DECONNEXION")


def CONNEXION():
    print("=*==*=*=*=*=*=*=*===*=*=*=*=*=*=**=")
    print("BIENVENUE DANS LE SYSTÈME DE GESTION DES UTILISATEURS (SGU) !")
    print("=*==*=*=*=*=*=*=*===*=*=*=*=*=*=**=")

    name = input("Entrez votre nom d'utilisateur : ")
    password = input("Entrez votre mot de passe : ")
    return name, password 

name, password = CONNEXION()

verification = Utilisateur()

verification.creer_table_utilisateur()

COMPTE=verification.verifier_identifiants(name, password)
verification.close()

if COMPTE:
    Nom_utilisateur, Role_utilisateur = COMPTE[1], COMPTE[2]
    print(f"Connexion réussie ! Bienvenue, {Nom_utilisateur} ({Role_utilisateur})")
    if Role_utilisateur == 'admin':
        MENU_principale()

    elif Role_utilisateur == 'professeur':
        MENU_PROFESSEUR()
    elif Role_utilisateur == 'étudiant':
        MENU_ETUDIANT()
    else:
        print("Rôle inconnu. Veuillez contacter l'administrateur.")
else:
    print("Échec de la connexion. Nom d'utilisateur ou mot de passe incorrect.")
    sys.exit()


def main():
    while True:
        choix = input("Entrez votre choix : ")
        if choix == '1':
            print("Gérer les utilisateurs")
        elif choix == '2':
            print("Gérer les Professeurs")
        elif choix == '3':
            print("Déconnexion réussie. Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
        raise KeyboardInterrupt("VOUS N'AVEZ QUITTEZ LE SYSTEME PAS LA MANIERE FORCER .")
if __name__ == "__main__":
    main()