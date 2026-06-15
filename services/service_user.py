from models.utlisateur_Modeles import Utilisateur
from models.teachers_Modeles import ProfesseurModel
from models.students_Modeles import studentsModel
from utils.util_Matricule import genere_matricule
class GestionAdmin:
    def __init__(self):
        self.modele_user = Utilisateur()
        self.modele_prof = ProfesseurModel()
        self.modele_etudiant = studentsModel()

    # ==========================================
    # GESTION DES UTILISATEURS
    # ==========================================
    def ajouter_utilisateur(self):
        print("\n    ")
        nom = input("entrez votre nom : ")
        role = input("entrez votre role : ")
        password = input("entrez votre mot de passe : ")
        self.modele_user.ajouter_utilisateur(nom, role, password)
        print("Utilisateur ajouté avec succès.")

    def supprimer_utilisateur(self):
        print("\n    ")
        id_user = input("entrez ID de utlisateur que vous voulez surpprimer : ")
        self.modele_user.supprimer_utilisateur(id_user)
        print("Utilisateur supprimé avec succès.")

    def rechercher_utilisateur(self):
        id_user = input("entrez votre id_user : ")
        resultat=self.modele_user.rechercher_utilisateur(id_user)
        print("\ nRecherch Result:", resultat)
        
        return resultat
    
    def listes_touts_utilisateurs(self):
        print("\n ")
        resultat=self.modele_user.liste_tout_utilisateur()
        for i in resultat:
            print(i)
    
    def modifiers_utilisateur_nom(self):
        print("\n   ")
        id_students=input("entrez id_students : ")
        nom=input("entrez le nouveux nom : ")
        self.modele_user.modifier_utilisateur_nom(nom,id_students)
        print(f" \n le nom a été modifier pour : {nom}")
    

    def modifiers_utilisateur_role(self):
        print("\n   ")
        id_students=input("entrez id_students : ")
        role=input("entrez le nouveux role : ")
        self.modele_user.modifier_utilisateur_role(role,id_students)
        print(f" \n le nom a été modifier pour : {role}")
        
    def modifiers_utilisateur_password(self):
        print("\n   ")
        id_students=input("entrez id_students : ")
        password=input("entrez le nouveux password : ")
        self.modele_user.modifier_utilisateur_password(password,id_students)
        print(f" \n le nom a été modifier pour : {password}")
        
    
    # ==========================================
    # GESTION DES PROFESSEURS
    # ==========================================
    def ajouter_professeur(self):
        print("\n    ")
        non = input("entrez votre non : ")
        matiere = input("entrez votre matiere : ")
        self.modele_prof.Ajouter(non, matiere)
        print("Utilisateur modifié avec succès.")

    def supprimer_professeur(self):
        print("\n    ")
        id_teacher = input("entrez votre id_teacher : ")
        self.modele_prof.supprimer(id_teacher)
        print("Utilisateur modifié avec succès.")
        
    def modifier_professeur(self):
        print("\n    ")
        id_teacher = input("entrez votre id_teacher : ")
        matiere = input("entrez votre matiere : ")
        self.modele_prof.Modifier(matiere, id_teacher)
        print("Utilisateur modifié avec succès.")
            
    def rechercher_professeur(self):
        print("\n    ")
        id_teacher = input("entrez votre id_teacher : ")
        resultat = self.modele_prof.Rechercher(id_teacher)
        print("\nRésultat de la recherche :", resultat)
        return resultat

    def listes_touts_prof(self):
        print("\n ")
        resultats=self.modele_prof.Liste_tout_professeur()
        for i in resultats:
            print(i)

    # ==========================================
    # GESTION DES ÉTUDIANTS
    # ==========================================
    def ajouter_etudiant(self):
        print("\n    ")
        nom = input("entrez votre nom : ")
        prenom = input("entrez votre prenom : ")
        age = input("entrez votre age : ")
        classe = input("entrez votre classe : ")
        matricule = genere_matricule()
        self.modele_etudiant.ajouter(nom, prenom, age, classe, matricule)
        print("Utilisateur modifié avec succès.")

    def supprimer_etudiant(self):
        print("\n    ")
        id_students = input("entrez votre id_students : ")
        self.modele_etudiant.supprimer_etudiant(id_students)
        print("Utilisateur modifié avec succès.")
    
    def rechercher_etudiants(self):
        print("\n    ")
        id_students = input("entrez votre id_students : ")
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
        id_students=input("entrez id_students : ")
        non=input("entrez le nouveux Nom : ")
        self.modele_etudiant.Modifier_etudiant_Non(non,id_students)
        print(f" \n le nom a été modifier pour : {non}")
    

    def modifier_prenom(self):
        print("\n   ")
        id_students=input("entrez id_students : ")
        prenom=input("entrez le nouveux prenom : ")
        self.modele_etudiant.Modifier_etudiant_prenom(prenom,id_students)
        print(f"\n le nom a été modifier pour : {prenom}")

    def modifier_age(self):
        print("\n   ")
        id_students=input("entrez id_students : ")
        age=input("entrez le nouveux age : ")
       
        self.modele_etudiant.Modifier_etudiant_age(age,id_students)
        print(f" \n le nom a été modifier pour : {age}")
    

    def modifier_classe(self):
        print("\n   ")
        id_students=input("entrez id_students : ")
        classe=input("entrez le nouveux classe : ")
        self.modele_etudiant.Modifier_etudiant_classe(classe,id_students)
        print(f" \n le nom a été modifier pour : {classe}")
        
    def modifier_matricule(self):
        print("\n   ")
        id_students=input("entrez id_students : ")
        matricule=input("entrez le nouveux matricule : ")
        self.modele_etudiant.Modifier_etudiant_Non(matricule,id_students)
        print(f" \n le nom a été modifier pour : {matricule}")



