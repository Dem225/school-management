from models.notes_Modeles import Notes_model
from models.absences_Modeles import Absence_model
import logging


class GestionTeacher :
    def __init__(self):
        self.Model_Notes =Notes_model()
        self.Model_Absences=Absence_model()
      
    #  ==========================================
    #  GESTION DES NOTES DES ÈTUDIANTS
    # ==========================================

    def Ajouter_Notes_Etudiant(self):
        print("\n    ")
        
        student_id=int(input("entrez id de l'étudiant : "))
        subject_id=int(input("entrez id Matiere : "))
        note =float(input("entrez la note commpris en 0 et 20 :"))
        self.Model_Notes.ajouter_note(student_id,subject_id,note)
        print(f"Note de {note}/20 ajoutée avec succès pour l'étudiant ID {student_id} !")
        logging.info(f"UNE NOTE DE ({note}) A ÉTÉ AJOUTEZ POUR L'ÉTUDIANT A L'ID ({student_id}) ET ID MATIERE : ({subject_id})")
        

    def Supprimer_Notes_Etudiant(self):
        print("\n    ")
        id_note=input("entrez l'id de la note :")
        self.Model_Notes.supprimer_note(id_note)
        print(" Note supprimée avec succès !")
        logging.warning(f"ALERTE UNE NOTE A ÉTÉ SUPPRIMER DE LA BASE DE DONNÉ A L'ID ({id_note})")


    def Modifier_Note_Etudiant(self):
        print("\n    ")
        id_note=input("entrez l'id de la note : ")
        nouvelle_note=input("entrez la nouvelle note ")
        self.Model_Notes.modifier_note_valeur(id_note,nouvelle_note)
        logging.info(f"UNE MODIFICATION SUR LA NOTE A L'ID ({id_note}) AVEC LA NOUVELLE NOTE : ({nouvelle_note})")

    def Afficher_Moyenne_Etudiant(self):
        print("\n    ")
        student_id = input("entrez l'id de l'étudiant : ")
        moyenne = self.Model_Notes.calculer_moyenne_etudiant(student_id)
        print(f"La moyenne de l'étudiant ID {student_id} est de : {moyenne}/20")
        logging.info(f"UN CALCUL DE MOYENNE A ÉTÉ EFFECTUER POUR L'ÉTUDIANT A L'ID ({student_id})")

        
    def Supprimer_Toutes_Les_Notes_Menu(self):
        reponse = input("Voulez-vous vraiment supprimer toutes les notes ? (oui/non) : ")
        if reponse.lower() == "oui":
            self.Model_Notes.supprimer_toutes_les_notes()
            logging.warning(f"ALERTE TOUTES LES NOTES ONT ÉTÉ SUPPRIMER DE LA BASE DE DONNÉ")
        else:
            print("Suppression annulée.")
            
    def Recherche_Notes_Etudiant(self):
        print("\n    ")
        id_note = input("entrez l'id de la note à rechercher : ")
        note = self.Model_Notes.rechercher_note(id_note)
        logging.info(f"UNE RECHERCHE DE NOTE A ÉTÉ EFFECTUER PAR LA ID ({id_note})")
        return note
    

    def Listes_Notes_Etudiant(self):
        print("\n    ")
        resultat= self.Model_Notes.liste_tout_note()
        for i in resultat:
            print(i)
        logging.info(f"UNE LECTURE DE TOUTES LES NOTES A ÉTÉ EFFECTUER")
            
    def Supprimer_Table_Note(self):
        reponse=input("Voulez-vous vraiment supprimer toutes les notes ? (oui/non) :")
        if reponse.lower()=="oui":
            self.Model_Notes.supprimer_table_notes_definitivement()
            logging.warning(f"ALERTE LA TABLE DES NOTES A ÉTÉ DÉFINITIVEMENT SUPPRIMER")
        else:
            print("Suppression annulée.")
            
    def afficher_meilleurs_etudiants(self):
        try:
            nb = int(input("Combien d'étudiants souhaitez-vous afficher ? "))
            resultats = self.Model_Notes.identifier_meilleurs_etudiants(nb)
            
            print(f"\n Top {nb} des meilleurs étudiants")
            if resultats:
                for i, (nom, moyenne) in enumerate(resultats, 1):
                    print(f"{i}. {nom} : {moyenne:.2f}/20")
            else:
                print("Aucune donnée disponible pour le moment.")
            
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier valide.")

    #  ==========================================
    #  GESTION DES ABSENCE DES ÈTUDIANTS
    # ==========================================


    def Ajouter_Absence_Etudiant(self):
        print("\n    ")
        student_id = input("entrez l'id de l'étudiant : ")
        date = input("entrez la date de l'absence (JJ/MM/AAAA) : ")
        status = input("L'absence est-elle justifiée ? (1 pour oui, 0 pour non) : ")
        
        self.Model_Absences.ajouter_absence(student_id, date, status)
        print(f" Absence enregistrée pour l'étudiant ID {student_id} à la date du {date} !")
        logging.info(f"UNE ABSENCE A ÉTÉ AJOUTEZ POUR L'ÉTUDIANT A L'ID ({student_id}) A LA DATE DU ({date}) AVEC LE STATUT ({status})")
        
    def Supprimer_Absence_Etudiant(self):
        print("\n    ")
        
        id_absence = input("entrez l'id de l'absence à supprimer : ")
        
        self.Model_Absences.supprimer_absence(id_absence)
        print(" Absence supprimée avec succès !")
        logging.warning(f"ALERTE UNE ABSENCE A ÉTÉ SUPPRIMER DE LA BASE DE DONNÉ A L'ID ({id_absence})")

    def Justifier_Absence_Etudiant(self):
        print("\n    ")
        id_absence=input("entrez l'id de l'absence non justifier ou justifier : ")
        
        self.Model_Absences.justifier_absence(id_absence)
        logging.info(f"UNE MODIFICATION SUR L'ABSENCE A L'ID ({id_absence})")
        
    def Mombre_Absences_Etudiant(self):
        print("\n")
        student_id=input("entrez id  de l'étudiant pour avoir les heures absences : ")
        resultat=self.Model_Absences.nombre_absences_etudiant(student_id)
        logging.info(f"UNE RECHERCHE DE NOMBRE D'ABSENCES A ÉTÉ EFFECTUER POUR L'ÉTUDIANT A L'ID ({student_id})")
        return resultat
        
    def Supprimer_Toutes_Les_Absences_Etudiant(self):
        print("\n")
        resultat=input("Voulez-vous supprimer toutes les Absences ? (oui / non) :")
        if resultat.lower()=='oui':
            self.Model_Absences.supprimer_toutes_les_absences()
            logging.warning(f"ALERTE TOUTES LES ABSENCES ONT ÉTÉ SUPPRIMER DE LA BASE DE DONNÉ")
            
        else:
            print("Toutes les absences ont été supprimées.")

    
    def Liste_Toutes_Absences_Etudiant(self):
        print("\n")
         
        resultat=self.Model_Absences.liste_toutes_absences()
        for i in resultat:
            print(i)
        logging.info(f"UNE LECTURE DE TOUTES LES ABSENCES A ÉTÉ EFFECTUER")

    def Supprimer_Table_Absences_Definitivement_Etudiant(self):
        print("\n")
        resultat=input("Voulez-vous supprimer toutes la Table ? (oui / non) :")
        
        if resultat.lower()=='oui':
            self.Model_Absences.supprimer_table_absences_definitivement()
            logging.warning(f"ALERTE LA TABLE DES ABSENCES A ÉTÉ DÉFINITIVEMENT SUPPRIMER")
        
        else:
            print("Suppression annulée")


    def Rechercher_Moyenne_Etudiant(self):
        print("\n")
        student_id=input("entrez l'id de l'étudant :" )
        resultat= self.Model_Notes.rechercher_moyenne(student_id)
        logging.info(f"UNE RECHERCHE DE MOYENNE A ÉTÉ EFFECTUER POUR L'ÉTUDIANT A L'ID ({student_id})")
        return resultat