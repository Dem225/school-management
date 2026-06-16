from database.DB import ManagerBase

class Sujet_matiere(ManagerBase):
    def __init__(self):
        super().__init__()
    
    def creer_table_matiere(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS subjects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                matiere TEXT NOT NULL,                                  
                teacher_id INTEGER,
                FOREIGN KEY (teacher_id) REFERENCES teachers(id)
                ON DELETE SET NULL
            );
        """)
        self.connecte.commit()
        
    def ajouter_matiere(self, matiere, teacher_id=None):
        if not matiere or matiere.strip() == "":
            print(" Erreur : Le non de la matière ne peut pas être vide.")
            return False
            
        self.cusor.execute("""
            INSERT INTO subjects (nom, teacher_id) 
            VALUES (?, ?);
        """, (matiere, teacher_id))
        self.connecte.commit()
        print(f" Matière '{matiere}' ajoutée avec succès !")
        return True
        
    def supprimer_matiere(self, id_matiere):
        self.cusor.execute("DELETE FROM subjects WHERE id = ?", (id_matiere,))
        self.cusor.execute("DELETE FROM sqlite_sequence WHERE name='subjects'")
        self.connecte.commit()
        print(" Matière supprimée avec succès !")
    
    def modifier_matiere_nom(self, id_matiere, matiere):
        self.cusor.execute("""
            UPDATE subjects 
            SET nom = ?
            WHERE id = ?
        """, (matiere, id_matiere))
        self.connecte.commit()
        print(" Nom de la matière mis à jour !")

    def affecter_professeur(self, id_matiere, teacher_id):
        self.cusor.execute("""
            UPDATE subjects 
            SET teacher_id = ?  
            WHERE id = ?
        """, (teacher_id, id_matiere))
        self.connecte.commit()
        print(" Professeur affecté à la matière avec succès !")

    def supprimer_tous_les_matieres(self):
        self.cusor.execute("DELETE FROM subjects")
        self.cusor.execute("DELETE FROM sqlite_sequence WHERE name='subjects'")
        self.connecte.commit()
        print(" Toutes les matières ont été supprimées.")
        
    def rechercher_matiere(self, id_matiere):
        self.cusor.execute("SELECT * FROM subjects WHERE id = ?", (id_matiere,))
        return self.cusor.fetchone()
    
    def liste_tout_matiere(self):
        self.cusor.execute("SELECT * FROM subjects")
        return self.cusor.fetchall()
    

    def supprimer_table_matiere_definitively(self):
        self.cusor.execute("DROP TABLE IF EXISTS subjects")
        self.cusor.execute("DELETE FROM sqlite_sequence WHERE name='subjects'")
        self.connecte.commit()
        print(" La table 'subjects' a été définitivement supprimée de la base de données !")
        return True
       
   

    def close(self):
        self.connecte.close()