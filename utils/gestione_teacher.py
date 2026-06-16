from confige.Menu import MENU_PROFESSEUR
from services.service_teachers import GestionTeacher
from confige.Menu_choix_teacher import MENU_GESTION_DES_NOTES , MENU_GESTION_DES_ABSENCES


def Gere_choix_teacher():


    classification=GestionTeacher()

    

    while True:
        print(MENU_PROFESSEUR)
        Choix = input("Entrez votre Choix : ")
        
        # ==========================================
        # SOU-MENU : GESTION DES NOTES
        # ==========================================
        if Choix == '1':
            while True: 
                print(MENU_GESTION_DES_NOTES)
                choix_menu_notes = input("Entrez votre choix : ")
                
                if choix_menu_notes == '1':
                    classification.Ajouter_Notes_Etudiant()
                elif choix_menu_notes == '2':
                    classification.Supprimer_Notes_Etudiant()
                elif choix_menu_notes == '3':
                    classification.Modifier_Note_Etudiant()
                elif choix_menu_notes == '4':
                    classification.Afficher_Moyenne_Etudiant()
                elif choix_menu_notes == '5':
                    classification.Recherche_Notes_Etudiant()
                elif choix_menu_notes == '6':
                    classification.Listes_Notes_Etudiant()
                elif choix_menu_notes == '9':  
                    print(" Retour au menu Professeur...")
                    break  
                else:
                    print(" Choix invalide dans le sous-menu notes.")

        # ==========================================
        # SOUS-MENU : GESTION DES ABSENCES
        # ==========================================
        elif Choix == "2":
            while True:  
                print(MENU_GESTION_DES_ABSENCES)  
                choix_menu_absences = input("Entrez votre choix : ") 
                
                if choix_menu_absences == '1':
                    classification.Ajouter_Absence_Etudiant()
                elif choix_menu_absences == '2':
                    classification.Supprimer_Absence_Etudiant()
                elif choix_menu_absences == '3':
                    classification.Justifier_Absence_Etudiant()
                elif choix_menu_absences == '4':
                    classification.Mombre_Absences_Etudiant()
                elif choix_menu_absences == '5':
                    classification.Liste_Toutes_Absences_Etudiant()
                elif choix_menu_absences == '6':
                    classification.Rechercher_Moyenne_Etudiant()
                elif choix_menu_absences == '9':  
                    print(" Retour au menu Professeur...")
                    break  
                else:
                    print(" Choix invalide dans le sous-menu absences.")

        # ==========================================
        # DECONNEXION DU MENU PROFESSEUR
        # ==========================================
        elif Choix == "3":
            print(" Merci, à bientôt !")
            break  
        
        else:
            print(" Choix invalide. Veuillez réessayer.")