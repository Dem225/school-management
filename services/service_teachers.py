from models.notes_Modeles import Notes_model
from models.absences_Modeles import Absence_model


class GestionTeacher :
    def __int__(self):
        self.Model_Notes = Notes_model ()
        self.Model_Absences=Absence_model()


    #  ==========================================
    #  GESTION DES NOTES DES ÈTUDIANTS
    # ==========================================

    def Ajouter_Notes_Etudiant(self):
        print("\n    ")
        
        student_id=input("entrez id de l'étudiant : ")
        subject_id=input("entrez id Matiere : ")
        note =input("entrez la note commpris en 0 et 20 :")
        self.Model_Notes.ajouter_note(student_id,subject_id,note)
        print(f"Note de {note}/20 ajoutée avec succès pour l'étudiant ID {student_id} !")
        

    def Supprimer_Notes_Etudiant(self):
        print("\n    ")
        id_note=input("entrez l'id de la note :")
        self.Model_Notes.supprimer_note(id_note)
        print(" Note supprimée avec succès !")


    def Modifier_Note_Etudiant(self):
        print("\n    ")
        id_note=input("entrez l'id de la note : ")
        nouvelle_note=input("entrez la nouvelle note ")
        self.Model_Notes.modifier_note_valeur(id_note,nouvelle_note)

    def Afficher_Moyenne_Etudiant(self):
        print("\n    ")
        student_id = input("entrez l'id de l'étudiant : ")
        moyenne = self.Model_Notes.calculer_moyenne_etudiant(student_id)
        print(f"La moyenne de l'étudiant ID {student_id} est de : {moyenne}/20")

        
    def Supprimer_Toutes_Les_Notes_Menu(self):
        reponse = input("Voulez-vous vraiment supprimer toutes les notes ? (oui/non) : ")
        if reponse.lower() == "oui":
            self.Model_Notes.supprimer_toutes_les_notes()
        else:
            print("Suppression annulée.")
            
    def Recherche_Notes_Etudiant(self):
        print("\n    ")
        id_note = input("entrez l'id de la note à rechercher : ")
        note = self.Model_Notes.rechercher_note(id_note)
        return note
    

    def Listes_Notes_Etudiant(self):
        print("\n    ")
        resultat= self.Model_Notes.liste_tout_note()
        for i in resultat:
            print(i)
            
    def Supprimer_Table_Note(self):
        reponse=input("Voulez-vous vraiment supprimer toutes les notes ? (oui/non) :")
        if reponse.lower()=="oui":
            self.Model_Notes.supprimer_table_notes_definitivement()
        else:
            print("Suppression annulée.")


    #  ==========================================
    #  GESTION DES ABSENCE DES ÈTUDIANTS
    # ==========================================


    def Ajouter_Absence_Etudiant(self):
        print("\n    ")
        student_id = input("entrez l'id de l'étudiant : ")
        date = input("entrez la date de l'absence (JJ/MM/AAAA) : ")
        justifie = input("L'absence est-elle justifiée ? (1 pour oui, 0 pour non) : ")
        
        self.Model_Absences.ajouter_absence_(student_id, date, justifie)
        
    def Supprimer_Absence_Etudiant(self):
        print("\n    ")
        
        id_absence = input("entrez l'id de l'absence à supprimer : ")
        
        self.Model_Absences.supprimer_absence(id_absence)
        print(" Absence supprimée avec succès !")

    def Justifier_Absence_Etudiant(self):
        print("\n    ")
        id_absence=input("entrez l'id de l'absence non justifier ou justifier : ")
        
        self.Model_Absences.justifier_absence(id_absence)
        
    def Mombre_Absences_Etudiant(self):
        print("\n")
        student_id=input("entrez id  de l'étudiant pour avoir les heures absences : ")
        resultat=self.Model_Absences.nombre_absences_etudiant(student_id)
        return resultat
        
    def Supprimer_Toutes_Les_Absences_Etudiant(self):
        print("\n")
        resultat=input("Voulez-vous supprimer toutes les Absences ? (oui / non) :")
        if resultat.lower()=='oui':
            self.Model_Absences.supprimer_toutes_les_absences()
            
        else:
            print("Toutes les absences ont été supprimées.")

    
    def Liste_Toutes_Absences_Etudiant(self):
        print("\n")
         
        resultat=self.Model_Absences.liste_toutes_absences()
        for i in resultat:
            print(i)

    def Supprimer_Table_Absences_Definitivement_Etudiant(self):
        print("\n")
        resultat=input("Voulez-vous supprimer toutes la Table ? (oui / non) :")
        
        if resultat.lower()=='oui':
            self.Model_Absences.supprimer_table_absences_definitivement()
        
        else:
            print("Suppression annulée")


    def Rechercher_Moyenne_Etudiant(self):
        print("\n")
        student_id=input("entrez l'id de l'étudant :" )
        resultat= self.Model_Notes.rechercher_moyenne(student_id)
        return resultat 