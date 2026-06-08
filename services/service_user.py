from models.utlisateur_Modeles import Utilisateur
from models.teachers_Modeles import ProfesseurModel
from models.students_Modeles import studentsModel

class GestionAdmin:
    def __init__(self):
        self.modele_user = Utilisateur()
        self.modele_prof = ProfesseurModel()
        self.modele_etudiant = studentsModel()

    # ==========================================
    # GESTION DES UTILISATEURS
    # ==========================================
    def ajouter_utilisateur(self):
        nom = input("entrez votre nom : ")
        role = input("entrez votre role : ")
        password = input("entrez votre mot de passe : ")
        self.modele_user.ajouter_utilisateur(nom, role, password)

    def supprimer_utilisateur(self):
        id_user = input("entrez ID de utlisateur que vous voulez surpprimer : ")
        self.modele_user.supprimer_utilisateur(id_user)

    def modifier_utilisateur(self):
        id_user = input("entrez votre id_user : ")
        name = input("entrez votre name : ")
        role = input("entrez votre role : ")
        self.modele_user.modifier_utilisateur(id_user, name, role)

    # ==========================================
    # GESTION DES PROFESSEURS
    # ==========================================
    def ajouter_professeur(self):
        id_user = input("entrez votre id_user : ")
        matiere = input("entrez votre matiere : ")
        self.modele_prof.Ajouter(id_user, matiere)

    def supprimer_professeur(self):
        id_teacher = input("entrez votre id_teacher : ")
        self.modele_prof.supprimer(id_teacher)

    def modifier_professeur(self):
        id_teacher = input("entrez votre id_teacher : ")
        matiere = input("entrez votre matiere : ")
        self.modele_prof.modifier(matiere, id_teacher)

    def rechercher_professeur(self):
        id_teacher = input("entrez votre id_teacher : ")
        self.modele_prof.rechercher(id_teacher)

    # ==========================================
    # GESTION DES ÉTUDIANTS
    # ==========================================
    def ajouter_etudiant(self):
        nom = input("entrez votre nom : ")
        prenom = input("entrez votre prenom : ")
        age = input("entrez votre age : ")
        classe = input("entrez votre classe : ")
        matricule = input("entrez votre matricule : ")
        self.modele_etudiant.Ajouter(nom, prenom, age, classe, matricule)

    def supprimer_etudiant(self):
        id_students = input("entrez votre id_students : ")
        self.modele_etudiant.supprimer_etudiant(id_students)
    
    def rechercher_etudiant(self):
        id_students = input("entrez votre id_students : ")
        self.modele_etudiant.Rechercher_etudiant(id_students)