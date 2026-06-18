from models.absences_Modeles import Absence_model
from models.notes_Modeles import Notes_model

class GestionStudents:
    def __init__(self):
        self.module_Absence = Absence_model()
        self.module_Notes = Notes_model()

    def Liste_Moyenne_Etudiant(self):
        print("\n")
        student_id = input("Entrez l'id de l'étudiant : ")
        resultat = self.module_Notes.rechercher_moyenne(student_id)
      
        print(f" Moyenne générale de l'étudiant ID {student_id} : {resultat:.2f}/20")
        return resultat 

    def Liste_Notes_Etudiant(self):
        print("\n")
        id_note = input("Entrez l'id de la note à rechercher : ")
        resultat = self.module_Notes.rechercher_note(id_note)
        
        if resultat:
           print(f"ID Note: {resultat[0]} | Étudiant A ID: {resultat[1]} | Matière: {resultat[2]} | Note: {resultat[3]}/20")
        else:
            print(" Aucune note trouvée avec cet identifiant.")
        return resultat

    def Liste_Absences_Etudiant(self):
        print("\n")
        student_id = input("Entrez l'id de l'étudiant pour avoir le nombre d'absences : ")
        
        total_absences = self.module_Absence.nombre_absences_etudiant(student_id)
        
        print(f" L'étudiant ID {student_id} a été absent {total_absences} fois.")
        return total_absences
    
    def Afficher_Toutes_Absences_Etudiant(self):
        print("\n LISTE COMPLÈTE DES ABSENCES ")
        resultat = self.module_Absence.liste_toutes_absences()
        
        if not resultat:
            print("Aucune absence enregistrée.")
        else:
            for i in resultat:
                print(i)