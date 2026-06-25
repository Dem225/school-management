from services.service_students import GestionStudents
from confige.Menu_choix_students import MENU_CONSULTATION_ETUDIANT

def Gere_choix_student(etudiant_id):  
    regularisation = GestionStudents(etudiant_id) 
    
    while True:
        print(MENU_CONSULTATION_ETUDIANT)
        choix = input("Entrez votre choix : ")
        
        if choix == '1':
            regularisation.Liste_Moyenne_Etudiant()
        elif choix == '2':
            regularisation.Rechercher_Note()
        elif choix == '3':
            regularisation.Liste_Absences_Etudiant()
        elif choix == '4':
            regularisation.Afficher_Toutes_Absences_Etudiant()
        elif choix == '5':
            regularisation.Listes_Tout_Note_Etudant()
        elif choix == '6':
            print("Fermeture de l'espace consultation étudiant. Au revoir !")
            break
        else:
            print("Option invalide ! Veuillez choisir un nombre entre 1 et 6.")