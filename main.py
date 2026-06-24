from services.services_auth import CONNEXION_User
from utils.gere_choix_utilisateur_principale import gerer_choix_admin
from utils.gestione_teacher import Gere_choix_teacher
from utils.gestione_students import Gere_choix_student
from utils.logger import logging

def main():
    role = CONNEXION_User()
    if role == 'admin':
        gerer_choix_admin()
        
    elif role == 'professeur':
        Gere_choix_teacher()
       

    elif role == 'étudiant':
        Gere_choix_student()
       
if __name__ == '__main__':
    logging.info("Démarrage de l'application...")
    main()

   