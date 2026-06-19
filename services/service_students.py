from models.absences_Modeles import Absence_model
from models.notes_Modeles import Notes_model
import logging

class GestionStudents:
    def __init__(self):
        self.module_Absence = Absence_model()
        self.module_Notes = Notes_model()

    def Liste_Moyenne_Etudiant(self):
        print("\n")
        student_id = input("Entrez l'id de l'étudiant : ")
        resultat = self.module_Notes.rechercher_moyenne(student_id)
      
        print(f" Moyenne générale de l'étudiant ID {student_id} : {resultat:.2f}/20")
        logging.info(f"UNE RECHERCHE DE MOYENNE A ÉTÉ EFFECTUER POUR L'ÉTUDIANT A L'ID ({student_id})")
        return resultat 

    def Rechercher_Note(self):
        print("\n")
        id_note = input("Entrez l'id de la note à rechercher : ")
        resultat = self.module_Notes.rechercher_note(id_note)
        
        if resultat:
           print(f"ID Note: {resultat[0]} | Étudiant A ID: {resultat[1]} | Matière: {resultat[2]} | Note: {resultat[3]}/20")
        else:
            print(" Aucune note trouvée avec cet identifiant.")
        logging.info(f"UNE RECHERCHE DE NOTE A ÉTÉ EFFECTUER PAR LA ID ({id_note})")
        return resultat
   
    def Listes_Tout_Note_Etudant(self):
        print("\n  ")
        student_id = int(input("Entrez l'id student : "))
        resultat = self.module_Notes.liste_tout_note_etudiant(student_id)
        
        if not resultat:
            print("Aucune note trouvée pour cet étudiant.")
        else:
            for ligne in resultat:
                nom_matiere = ligne[0]
                note_valeur = ligne[1]
                print(f" {nom_matiere} ➔ Note : {note_valeur}/20")
        print("\n")
        logging.info(f"UNE LECTURE DE TOUTES LES NOTES A ÉTÉ EFFECTUER POUR L'ÉTUDIANT A L'ID ({student_id})")
    
    def Liste_Absences_Etudiant(self):
        print("\n")
        student_id = input("Entrez l'id de l'étudiant pour avoir le nombre d'absences : ")
        
        total_absences = self.module_Absence.nombre_absences_etudiant(student_id)
        
        print(f" L'étudiant ID {student_id} a été absent {total_absences} fois.")
        logging.info(f"UNE RECHERCHE DE NOMBRE D'ABSENCES A ÉTÉ EFFECTUER POUR L'ÉTUDIANT A L'ID ({student_id})")
        return total_absences
    
    def Afficher_Toutes_Absences_Etudiant(self):
        print("\n LISTE COMPLÈTE DES ABSENCES ")
        resultat = self.module_Absence.liste_toutes_absences()
        
        if not resultat:
            print("Aucune absence enregistrée.")
        else:
            for i in resultat:
                print(i)
        logging.info(f"UNE LECTURE DE TOUTES LES ABSENCES A ÉTÉ EFFECTUER")