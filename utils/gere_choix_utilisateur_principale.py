from confige.Menu import  MENU_PRINCIPALE_ADMINE
from confige.Menu_choix_admin import MENU_GESTION_DES_UTILISATEURS,MENU_GESTION_DES_PROFESSEURS,MENU_GESTION_DES_ETUDIANTS,MENU_MODIFICATION_DES_ETUDIANTS,MENU_GESTION_MODIFICATION_DES_UTILISATEURS
from services.service_user import GestionAdmin

def gerer_choix_admin():
   
    gestion = GestionAdmin()
    
    while True:
        print(MENU_PRINCIPALE_ADMINE)
        choix = input("Entrez votre choix : ")
        
        if choix == '1':
            while True:  
                print(MENU_GESTION_DES_UTILISATEURS)
                Choix_Menu_UTILISATEURS = input("Entrez votre choix : ")
                
                if Choix_Menu_UTILISATEURS == '1':
                    gestion.ajouter_utilisateur()
                elif Choix_Menu_UTILISATEURS == '2':
                    gestion.supprimer_utilisateur()
                elif Choix_Menu_UTILISATEURS == '3':
                    while True:  
                        print(MENU_GESTION_MODIFICATION_DES_UTILISATEURS)
                        choix_modification_utilisateur = input("entrez votre choix :")
                        if choix_modification_utilisateur == '1':
                            gestion.modifiers_utilisateur_nom()
                        elif choix_modification_utilisateur == '2':
                            gestion.modifiers_utilisateur_role()
                        elif choix_modification_utilisateur == '3':
                            gestion.modifiers_utilisateur_password()
                        elif choix_modification_utilisateur == '4':  
                            break
                elif Choix_Menu_UTILISATEURS == '4':
                    gestion.listes_touts_utilisateurs()
                elif Choix_Menu_UTILISATEURS == '5':  
                    break
                    
        elif choix == '2':
            while True:  
                print(MENU_GESTION_DES_PROFESSEURS)
                Choix_Menu_PROFESSEURS = input("Entrez votre choix :")
                
                if Choix_Menu_PROFESSEURS == '1':
                    gestion.ajouter_professeur()
                elif Choix_Menu_PROFESSEURS=='2':
                    gestion.consigne_matiere_professeur()
                elif Choix_Menu_PROFESSEURS == '3':
                    gestion.supprimer_professeur()
                elif Choix_Menu_PROFESSEURS == '4':
                    gestion.modifier_professeur()
                elif Choix_Menu_PROFESSEURS == '5':
                    gestion.rechercher_professeur()
                elif Choix_Menu_PROFESSEURS == '6':
                    gestion.listes_touts_prof()
                elif Choix_Menu_PROFESSEURS=='8':
                    gestion.supprimer_contenue_matiere()
                elif Choix_Menu_PROFESSEURS == '7':  
                    break
                    
        elif choix == '3':
            while True:  
                print(MENU_GESTION_DES_ETUDIANTS)
                Choix_menu_ETUDIANTS = input("entrez votre choix :")
                
                if Choix_menu_ETUDIANTS == '1':
                    gestion.ajouter_etudiant()
                elif Choix_menu_ETUDIANTS == '2':
                    gestion.supprimer_etudiant()
                elif Choix_menu_ETUDIANTS == '3':
                    gestion.rechercher_etudiants()
                elif Choix_menu_ETUDIANTS == '4':
                    gestion.listes_touts_etudiants()
                elif Choix_menu_ETUDIANTS == '5':
                    while True:  
                        print(MENU_MODIFICATION_DES_ETUDIANTS)
                        choix_modificatio_etudiants = input("entrez votre choix : ")
                        if choix_modificatio_etudiants == '1':
                            gestion.modifier_non()
                        elif choix_modificatio_etudiants == '2':
                            gestion.modifier_prenom()
                        elif choix_modificatio_etudiants == '3':
                            gestion.modifier_age()
                        elif choix_modificatio_etudiants == '4':
                            gestion.modifier_classe()
                        elif choix_modificatio_etudiants == '5':
                            gestion.modifier_matricule()
                        elif choix_modificatio_etudiants == '6': 
                            break
                elif Choix_menu_ETUDIANTS == '6':  
                    break
                    
        elif choix == '4':
            print("Déconnexion réussie. Au revoir ! ")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")