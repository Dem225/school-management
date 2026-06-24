from models.utlisateur_Modeles import Utilisateur
from models.teachers_Modeles import ProfesseurModel
from models.students_Modeles import studentsModel
from models.matiere_Modeles import Sujet_matiere
from utils.util_Matricule import genere_matricule
import logging
class GestionAdmin:
    def __init__(self):
        self.modele_user = Utilisateur()
        self.modele_prof_matiere=Sujet_matiere()
        self.modele_prof = ProfesseurModel()
        self.modele_etudiant = studentsModel()

    # ==========================================
    # GESTION DES UTILISATEURS
    # ==========================================
    def ajouter_utilisateur(self):
        print("\n--- Création d'un nouvel utilisateur ---")
        
        nom = input("Entrez votre nom : ").strip()
        role = input("Entrez votre rôle (admin/professeur/étudiant) : ").strip()
        password = input("Entrez votre mot de passe : ").strip()
        user_name = input("Entrez votre user_name (pseudo) : ").strip()

       
        if not nom or not role or not user_name or not password:
            print("\nErreur : Tous les champs doivent être remplis.")
            logging.warning("Tentative d'ajout avec des champs vides.")
            return

        if len(password) <= 4:
            print("\nErreur : Le mot de passe doit comporter au moins 4 caractères.")
            logging.warning(f"Mot de passe trop court pour l'utilisateur {user_name}.")
            return
        MOTS_DE_PASSE_INTERDITS = ['1234', '1111', '0000', 'admin', 'password']
        
        if password in MOTS_DE_PASSE_INTERDITS:
            print("Désolé, ce mot de passe est trop facile ! Veuillez en utiliser un plus complexe.")
            logging.warning("L'utilisateur a tenté d'utiliser un mot de passe trop facile (blacklisté).")
            return
            
        
        resultat = self.modele_user.ajouter_utilisateur(nom, role, user_name, password)
     
        if resultat["succes"]:
            print(f"\nSuccès : Utilisateur {user_name} ajouté.")
            logging.info(f"Utilisateur ajouté avec succès : {user_name}")
        else:
            print(f"\nErreur : {resultat['message']}")
            logging.error(f"Échec ajout utilisateur {user_name} : {resultat['message']}")

             
    def supprimer_utilisateur(self):
        print("\n    ")
        id_user = input("Entrez ID de utlisateur que vous voulez surpprimer : ").strip()
        self.modele_user.supprimer_utilisateur(id_user)
        print("Utilisateur suppressé avec succès.")
        logging.warning(f"ALETE UN UTILISATEUR ÉTÉ SUPPRIMERER DE LA BASE DE BONNÉ A L'ID ({id_user})")

    def rechercher_utilisateur(self):
        id_user = input("Entrez votre id_user : ").strip()
        resultat=self.modele_user.rechercher_utilisateur(id_user)
        print(f" \n Recherch Result:" ,resultat)
        logging.info(f"UNE RECHERCHE A ÉTÉ ÈFFECTUER PAR LA ID  {id_user}")
        return resultat
    
    def listes_touts_utilisateurs(self):
        print("\n ")
        resultat=self.modele_user.liste_tout_utilisateur()
        for i in resultat:
            print(i)

    def modifiers_utilisateur_nom(self):
        print("\n   ")
        id_students=input("Entrez id_students : ").strip()
        nom=input("Entrez le nouveux nom : ").strip()
        self.modele_user.modifier_utilisateur_nom(nom,id_students)
        print(f" \n le nom a été modifier pour : {nom}")
        logging.info(f"UNE MODIFICATION SUR  LE NOM D'UN UTLISATEUR A L'ID :( {id_students} )")

    def modifiers_utilisateur_role(self):
        print("\n   ")
        id_students=input("Entrez id_students : ").strip()
        role=input("Entrez le nouveux role : ").strip()
        self.modele_user.modifier_utilisateur_role(role,id_students)
        print(f" \n le nom a été modifier pour : {role}")
        logging.info(f"UNE MODIFICATION SUR  LE ROLE D'UN UTILISATEUR A  L'ID  : ({id_students} )")
    def modifiers_utilisateur_password(self):
        print("\n   ")
        id_students=input("Entrez id_students : ").strip()
        password=input("Entrez le nouveux password : ").strip()
        self.modele_user.modifier_utilisateur_password(password,id_students)
        print(f" \n le nom a été modifier pour : {password}")
        logging.info(f"UNE MODIFICATION SUR  LE MOT DE PASSE  D'UN UTILISATEUR A  L'ID  : ({id_students} )")
    
    # ==========================================
    # GESTION DES PROFESSEURS
    # ==========================================
    def ajouter_professeur(self):
        print("\n    ")
        nom = input("Entrez votre nom : ").strip()
        subject_id = input("Entrez l'ID de la matière enseignée : ").strip()
        self.modele_prof.Ajouter(nom, subject_id)
        print("PROFESSEURS ajoutez  avec succès.")
        logging.info(f" UN PROFESSEURS A ÉTÉ AJOUTEZ A LA BASE DE DONNÉ de non : {nom} ET DE ID MATIERE  : {subject_id}")

    def supprimer_professeur(self):
        print("\n    ")
        id_teacher = input("Entrez votre id_teacher : ").strip()
        self.modele_prof.supprimer(id_teacher)
        print("professeur supprimer avec succès.")
        logging.warning(f"ALETE UN PROFESSEURS ÉTÉ SUPPRIMER DE LA BASE DE DONNÉ A L'ID ({id_teacher})")
        
    def modifier_professeur(self):
        print("\n    ")
        id_teacher = input("Entrez votre id_teacher : ").strip()
        subject_id = input("Entrez votre matiere : ").strip()
        self.modele_prof.Modifier(subject_id, id_teacher)
        print("Utilisateur modifié avec succès.")
        logging.info(f"UNE MODIFICATION D'UNE  MATIERER A ID ({subject_id})  SUR LE PROFESSEURS  A L ID ({id_teacher}) ")
        
    def consigne_matiere_professeur(self):
        print("profsseur list available ")
        self.listes_touts_prof()
        print("\n    ")
        teacher_id=input("Entrez ID du professuere : ").strip()
        matiere=input("Entrez le nom de la Matiere :").strip()
        self.modele_prof_matiere.ajouter_matiere(matiere,teacher_id)
        print(f" Matière '{matiere}' ajoutée avec succès !")
        logging.info(f"UNE MATIERE :({matiere}) A ÉTÉ CONSIGNE AUX PROFESSEURS A ID ({teacher_id})")
        
    def supprimer_contenue_matiere(self):
        print("\n    ")
        choix=input("Entrez ('oui'/ 'non') : ").strip()
        if choix=='oui':
            self.modele_prof_matiere.supprimer_tous_les_matieres()
            print("c'est ok ")
        else:
            print("annuele")

    def rechercher_professeur(self):
        print("\n    ")
        id_teacher = input("Entrez votre id_teacher : ").strip()
        resultat = self.modele_prof.Rechercher(id_teacher)
        print("\nRésultat de la recherche :", resultat)
        logging.info(f"UNE RECHERCHE PAR ID ({id_teacher}) A ÉTÉ  EFFECTUER ")
        return resultat
        

    def listes_touts_prof(self):
        print("\n ")
        resultats=self.modele_prof.Liste_tout_professeur()
        for i in resultats:
            print("ID :",i[0],"nom :",i[1],"matiere_id:",i[2])
        logging.info(f"UNE RECHERCHE A ÉTÉ EFFECTUER")
        
    # ==========================================
    # GESTION DES ÉTUDIANTS
    # ==========================================
    def ajouter_etudiant(self):
        print("\n    ")
        nom = input("Entrez votre nom : ").strip()
        prenom = input("Entrez votre prenom : ").strip()
        age = input("Entrez votre age : ").strip()
        classe = input("Entrez votre classe : ").strip()
        matricule = genere_matricule()
        self.modele_etudiant.ajouter(nom, prenom, age, classe, matricule)
        print("Utilisateur modifié avec succès.")
        logging.info(f"UN ÉTUDIANTS A ÉTÉ AJOUTEZ A LA BASE DE DONNÉ DE NOM  :( {nom}) ,DE MATRICULE : ({matricule}) ET DE CLASSE ({classe})")
    def supprimer_etudiant(self):
        print("\n    ")
        id_students = input("Entrez votre id_students : ")
        self.modele_etudiant.supprimer_etudiant(id_students)
        print("Utilisateur modifié avec succès.")
        logging.warning (f"UN ÉTUDIANTS A  L'ID ({id_students}) ÉTÉ SUPPRIMER  DE LA BASSE DE DONNÉ ")
        
    def rechercher_etudiants(self):
        print("\n    ")
        id_students = input("Entrez votre id_students : ")
        resultat=self.modele_etudiant.rechercher_etudiant(id_students)
        print("Utilisateur modifié avec succès.",resultat)
        return resultat
    
    def listes_touts_etudiants(self):
        print("\n ")
        resultats=self.modele_etudiant.Lister_etudiant()
        for i in resultats:
            print(i)
    
    def modifier_non(self):
        print("\n   ")
        id_students=input("Entrez id_students : ")
        non=input("Entrez le nouveux Nom : ")
        self.modele_etudiant.Modifier_etudiant_Non(non,id_students)
        print(f" \n le nom a été modifier pour : {non}")
        logging.info(f"UNE MODIFICATION SUR LE NOM A L'ID ({id_students}) ")
    


    def modifier_prenom(self):
        print("\n   ")
        id_students=input("Entrez id_students : ")
        prenom=input("Entrez le nouveux prenom : ")
        self.modele_etudiant.Modifier_etudiant_prenom(prenom,id_students)
        print(f"\n le nom a été modifier pour : {prenom}")
        logging.info(f"UNE MODIFICATION SUR LE PRENOM  A L'ID ({id_students}) ")

    def modifier_age(self):
        print("\n   ")
        id_students=input("Entrez id_students : ")
        age=input("Entrez le nouveux age : ")
       
        self.modele_etudiant.Modifier_etudiant_age(age,id_students)
        print(f" \n le nom a été modifier pour : {age}")
        logging.info(f"UNE MODIFICATION SUR LE AGE  A L'ID ({id_students}) ")
    

    def modifier_classe(self):
        print("\n   ")
        id_students=input("Entrez id_students : ")
        classe=input("Entrez le nouveux classe : ")
        self.modele_etudiant.Modifier_etudiant_classe(classe,id_students)
        print(f" \n le nom a été modifier pour : {classe}")
        logging.info(f"UNE MODIFICATION SUR LE CLASSE  A L'ID ({id_students}) ")
        
    def modifier_matricule(self):
        print("\n   ")
        id_students=input("Entrez id_students : ")
        matricule=input("Entrez le nouveux matricule : ")
        self.modele_etudiant.Modifier_etudiant_Non(matricule,id_students)
        print(f" \n le nom a été modifier pour : {matricule}")
        logging.info(f"UNE MODIFICATION SUR LE MATRICULE  A L'ID ({id_students}) ")



