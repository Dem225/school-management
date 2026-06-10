
from confige.Menu import  MENU_PRINCIPALE_ADMINE
from confige.Menu_choix_admin import MENU_GESTION_DES_UTILISATEURS,MENU_GESTION_DES_PROFESSEURS,MENU_GESTION_DES_ETUDIANTS
from services.service_user import GestionAdmin

def gerer_choix_admin():
   
    gestion = GestionAdmin()
    
    while True:
        print(MENU_PRINCIPALE_ADMINE)
        choix = input("Entrez votre choix : ")
        
        if choix == '1':
            print(MENU_GESTION_DES_UTILISATEURS)
            Choix_Menu_UTILISATEURS=input("Entrez votre choix :")
            if Choix_Menu_UTILISATEURS=='1':
                gestion.ajouter_utilisateur()
            elif Choix_Menu_UTILISATEURS=='2':
                gestion.supprimer_utilisateur()
            elif Choix_Menu_UTILISATEURS=='3':
                gestion.modifier_utilisateur()
            elif Choix_Menu_UTILISATEURS=='4':
                gestion.listes_touts_utilisateurs()
        elif choix == '2':
            print(MENU_GESTION_DES_PROFESSEURS)
            Choix_Menu_PROFESSEURS=input("Entrez votre choix :")
            if Choix_Menu_PROFESSEURS=='1':
                gestion.ajouter_professeur()
            elif Choix_Menu_PROFESSEURS=='2':
                gestion.supprimer_professeur()
            elif Choix_Menu_PROFESSEURS=='3':
                gestion.modifier_professeur()
            elif Choix_Menu_PROFESSEURS=='4':
                gestion.rechercher_professeur()
            elif Choix_Menu_PROFESSEURS=='5':
                gestion.listes_touts_prof()
        elif choix=='3':
            print(MENU_GESTION_DES_ETUDIANTS)
            Choix_menu_ETUDIANTS=input("entrez votre choix :")
            if Choix_menu_ETUDIANTS=='1':
              gestion.ajouter_etudiant()
            elif Choix_menu_ETUDIANTS=='2':
                gestion.supprimer_etudiant()
            elif Choix_menu_ETUDIANTS=='3':
                gestion.rechercher_etudiants()
            elif Choix_menu_ETUDIANTS=='4':
                gestion.listes_touts_etudiants()
        elif choix == '4':
            print("Déconnexion réussie. Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
