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
    special_characters = string.punctuation
    for character in name:
        if character in special_characters:
            raise ValueError(f"Nom ou prénom invalide : {name}")

def Ajouter_Etudiant():
    
    
    nom = input("Entrez votre nom : ").strip().upper()
    prenom = input("Entrez votre prénom : ").strip().title() 
    chec_names(nom)
    chec_names(prenom)
    
    while True:
        try:
            age = int(input("Entrez votre âge : "))
        except ValueError:
            print("entrez un nombree entier")
        break
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

def Unique_Recherche_Etudiant():
    unique_recherche = int(input("ENTREZ L'ETUDIANTS QUE VOUS RECHERCHE A PARTIE DE L'ID :" ))
    cursor.execute("SELECT * FROM ÉTUDIANTS  WHERE id=? ", (unique_recherche, ))
    for i in cursor.fetchall():
        print(f"Voici  les donné de l'étudiant que vous avez recherche\n {i}")

def listes_Etudiant():
    while True:
        print("\n--- MENU ---")
        print("1. VOULEZ-VOUS LISTÉS TOUT LES ÈTUDIANT .")
        print("2.VOULEZ-VOUS QUITTÉ ?.")
        
        Choix = input("FAITE VOTRE CHOIX :")
        
        if Choix == "1": 
            cursor.execute("SELECT * FROM ÉTUDIANTS ")
            resultsats = cursor.fetchall()
            print(f"VOICI LA LISTE DE TOUS LES ÉTUDIANTS QUI EXISTENT DANS LA DB : ")
            for resultat in resultsats:
                print(resultat)
            break
        elif Choix == "2":
            print("MERCI BEAUCOUP POUR LA VISTE ")
            break
        else:
            print("Option invalide. Choisissez 1 ou 2.")
        
Ajouter_Etudiant()

cursor.close()
conex.close()