from services.services_auth import CONNEXION_User
from confige.Menu import MENU_PRINCIPALE, MENU_PROFESSEUR, MENU_ETUDIANT,MENU_CONNECTION,MENU_PRINCIPALE_ADMINE
from confige.Menu_choix_admin import MENU_GESTION_DES_UTILISATEURS,MENU_GESTION_DES_PROFESSEURS,MENU_GESTION_DES_ETUDIANTS

from services.service_user import GestionAdmin

def gerer_choix_admin():
   
    gestion = GestionAdmin()
    
    while True:
        print(MENU_PRINCIPALE_ADMINE)
        choix = input("Entrez votre choix : ")
        print(MENU_GESTION_DES_UTILISATEURS)
        if choix == '1':
            Choix_Menu_UTILISATEURS=input("Entrez votre choix ?:")
            if Choix_Menu_UTILISATEURS=='1':
                gestion.ajouter_utilisateur()
            elif Choix_Menu_UTILISATEURS=='2':
                gestion.supprimer_utilisateur()
            elif Choix_Menu_UTILISATEURS=='3':
                gestion.modifier_utilisateur()
        elif choix == '2':
           
            gestion.ajouter_professeur()
            
        elif choix == '3':
            print("Déconnexion réussie. Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def main():
   
    role = CONNEXION_User()

   
    if role == 'admin':
        gerer_choix_admin()
        
    elif role == 'professeur':
        print(MENU_PROFESSEUR)
       
      
    elif role == 'étudiant':
        print(MENU_ETUDIANT)
       
if __name__ == "__main__":
    main()