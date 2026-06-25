from models.absences_Modeles import Absence_model
from models.notes_Modeles import Notes_model
import logging
class GestionStudents:
    def __init__(self, etudiant_id): 
        self.module_Absence = Absence_model()
        self.module_Notes = Notes_model()
        self.etudiant_id = etudiant_id  

    def Liste_Moyenne_Etudiant(self):
        print("\n")
        resultat = self.module_Notes.rechercher_moyenne(self.etudiant_id)  
        if resultat and resultat[0]:
            print(f" Votre moyenne générale : {resultat[0]:.2f}/20")
        else:
            print("Aucune note trouvée.")
        logging.info(f"RECHERCHE DE MOYENNE POUR L'ÉTUDIANT ID ({self.etudiant_id})")

    def Rechercher_Note(self):
        print("\n")
        resultats = self.module_Notes.liste_tout_note_etudiant(self.etudiant_id)  
        if resultats:
            print("=" * 50)
            print("        VOS NOTES")
            print("=" * 50)
            for ligne in resultats:
                print(f" {ligne[0]} ➔ Note : {ligne[1]}/20")
            print("=" * 50)
        else:
            print("Aucune note trouvée pour votre compte.")
        logging.info(f"CONSULTATION DES NOTES PAR ÉTUDIANT ID:{self.etudiant_id}")

    def Listes_Tout_Note_Etudant(self):
        print("\n")
        resultat = self.module_Notes.liste_tout_note_etudiant(self.etudiant_id)  
        if not resultat:
            print("Aucune note trouvée.")
        else:
            for ligne in resultat:
                print(f" {ligne[0]} ➔ Note : {ligne[1]}/20")
        print("\n")
        logging.info(f"LECTURE DE TOUTES LES NOTES POUR L'ÉTUDIANT ID ({self.etudiant_id})")

    def Liste_Absences_Etudiant(self):
        print("\n")
        total_absences = self.module_Absence.nombre_absences_etudiant(self.etudiant_id)  
        print(f" Vous avez été absent {total_absences} fois.")
        logging.info(f"RECHERCHE D'ABSENCES POUR L'ÉTUDIANT ID ({self.etudiant_id})")
        return total_absences

    def Afficher_Toutes_Absences_Etudiant(self):
        print("\n LISTE COMPLÈTE DES ABSENCES ")
        resultat = self.module_Absence.liste_toutes_absences()
        if not resultat:
            print("Aucune absence enregistrée.")
        else:
            for i in resultat:
                print(i)
        logging.info(f"LECTURE DE TOUTES LES ABSENCES EFFECTUÉE")