from models.absences_Modeles import Absence_model
from models.notes_Modeles import Notes_model

class GestionStudents:
    def __init__(self):
        self.module_Absence=Absence_model()
        self.module_Notes =Notes_model()

    def Liste_Moyenne_Etudiant(self):
        print("\n")
        student_id=input("entrez l'id de l'étudant :" )
        resultat= self.module_Notes.rechercher_moyenne(student_id)
        return resultat 
    

    def Liste_Notes_Etudiant(self):
        print("\n    ")
        id_note = input("entrez l'id de la note à rechercher : ")
        ressultat  = self.module_Notes.rechercher_note(id_note)
        return ressultat
    

    def Liste_Absences_Etudiant(self):
        print("\n")
        student_id=input("entrez id  de l'étudiant pour avoir les heures absences : ")
        self.module_Absence.nombre_absences_etudiant(student_id)
    
    
    def Afficher_Toutes_Absences_Etudiant(self):
        print("\n")
         
        resultat=self.module_Absence.liste_toutes_absences()
        for i in resultat:
            print(i)