from database.DB import ManagerBase

class Notes_model(ManagerBase):
    def __init__(self):
        super().__init__()
      
    def believe_table_notes(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS grades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                subject_id INTEGER NOT NULL,
                note REAL NOT NULL CHECK(note >= 0 AND note <= 20),
                FOREIGN KEY (student_id) REFERENCES students(id),
                FOREIGN KEY (subject_id) REFERENCES subjects(id)
            );
        """)
        self.connecte.commit()

    def ajouter_note(self, student_id, subject_id, note):
        if not (0 <= note <= 20):
            print("Erreur : La note doit être comprise entre 0 et 20.")
            return False 
            
        self.cusor.execute("""
            INSERT INTO grades (student_id, subject_id, note) 
            VALUES (?, ?, ?);
        """, (student_id, subject_id, note))
        self.connecte.commit()
       
        return True

    def supprimer_note(self, id_note):
        self.cusor.execute("DELETE FROM grades WHERE id = ?", (id_note,))
        self.connecte.commit()
       

    def modifier_note_valeur(self, id_note, nouvelle_note):
        if not (0 <= nouvelle_note <= 20):
            print("Erreur : La note doit être comprise entre 0 et 20.")
            return False 

        self.cusor.execute("""
            UPDATE grades 
            SET note = ?
            WHERE id = ?
        """, (nouvelle_note, id_note))
        self.connecte.commit()
        print(" Note mise à jour avec succès !")
        return True

    def calculer_moyenne_etudiant(self, student_id):
        self.cursor.execute("SELECT AVG(note) FROM grades WHERE student_id = ?", (student_id,))
        return self.cursor.fetchone()[0] or 0.0

    def supprimer_toutes_les_notes(self):
        self.cusor.execute("DELETE FROM grades")
        self.cusor.execute("DELETE FROM sqlite_sequence WHERE name='grades'")
        self.connecte.commit()
        print(" Toutes les notes ont été supprimées.")

    def rechercher_moyenne(self,student_id):
        self.cusor.execute("SELECT AVG(note) FROM grades WHERE student_id = ?",(student_id))
        return self.cusor.fetchall()[0] or 0.0

    def rechercher_note(self, id_note):
        self.cusor.execute("SELECT * FROM grades WHERE id = ?", (id_note,))
        return self.cusor.fetchone()

    def liste_tout_note(self):
        self.cusor.execute("SELECT * FROM grades")
        return self.cusor.fetchall()

    def supprimer_table_notes_definitivement(self):
        self.cusor.execute("DROP TABLE IF EXISTS grades")
        self.cusor.execute("DELETE FROM sqlite_sequence WHERE name='grades'")
        self.connecte.commit()
        print(" La table 'grades' a été définitivement supprimée !")

    def close(self):
        self.connecte.close()