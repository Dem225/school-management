from services.services_auth import CONNEXION_User
from confige.Menu import  MENU_PROFESSEUR, MENU_ETUDIANT
from utils.gere_choix_utilisateur_principale import gerer_choix_admin
from utils.gestione_teacher import Gere_choix_teacher

def main():
    role = CONNEXION_User()
    if role == 'admin':
        gerer_choix_admin()
        
    elif role == 'professeur':
        Gere_choix_teacher()
       

    elif role == 'étudiant':
        print(MENU_ETUDIANT)
       
if __name__ == '__main__':
    
    main()















