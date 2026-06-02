import sqlite3
import string

conex = sqlite3.connect("Ecole.db")
cursor = conex.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ÉTUDIANTS(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        prénom TEXT NOT NULL,
        âge INTEGER NOT NULL,
        classe TEXT NOT NULL,
        matricule TEXT NOT NULL
    )
""")
conex.commit()

def chec_names(name):
    if not name:
        raise ValueError("Le prénom et le nom de famille ne peuvent pas être vides.")
    special_characters = string.punctuation + string.digits
    for character in name:
        if character in special_characters:
            raise ValueError(f"Nom ou prénom invalide : {name}")

def Ajouter_Etudiant():
    nom = input("Entrez votre nom : ").strip().upper()       
    prenom = input("Entrez votre prénom : ").strip().title() 
    chec_names(nom)
    chec_names(prenom)
    age = int(input("Entrez votre âge : "))
    classe = input("Entrez votre classe : ").strip().upper()
    matricule = input("Veuillez entrer le matricule : ").strip()
    
    cursor.execute("""
        INSERT INTO ÉTUDIANTS (nom, prénom, âge, classe, matricule)
        VALUES (?, ?, ?, ?, ?)
    """, (nom, prenom, age, classe, matricule))
   
    conex.commit()
    print(f"Succès : L'étudiant {prenom} {nom} a bien été ajouté.")

def Modifier_Etudiant():
    print(" MISE A JOUR DES INFORMATION DE LA BASE DE NONNE ")
    matricule_cible = input("Entrez le matricule de l'étudiant à modifier : ").strip()
    
    nouveau_nom = input("Nouveau nom : ").strip().upper()
    nouveau_prenom = input("Nouveau prénom : ").strip().title()
    nouveau_age = int(input("Nouvel âge : "))
    nouvelle_classe = input("Nouvelle classe : ").strip().upper()
    
    cursor.execute("""
        UPDATE ÉTUDIANTS 
        SET nom = ?, prénom = ?, âge = ?, classe = ?
        WHERE matricule = ?
    """, (nouveau_nom, nouveau_prenom, nouveau_age, nouvelle_classe, matricule_cible))
    
    conex.commit()
    print("L'étudiant a été modifié.")

def Supprimer_Etudiant():
   
    id_cible = int(input("Entrez l'ID de l'étudiant à supprimer : "))
    
    cursor.execute("DELETE FROM ÉTUDIANTS WHERE id = ?", (id_cible,))
    
    conex.commit()
    
    print("L'étudiant a été supprimé avec succès.")

def Rechercher_Etudiant():
    
   
    cursor.execute("SELECT * FROM ÉTUDIANTS ")
    for i in cursor.fetchall():
        print(i)

Ajouter_Etudiant()

cursor.close()
conex.close()