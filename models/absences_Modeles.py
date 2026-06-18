from database.DB import ManagerBase

class Absence_model(ManagerBase):
    def __init__(self):
        super().__init__()
        
    def creer_table_absences(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS absences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                status INTEGER DEFAULT 0, -- 0 = Non justifié, 1 = Justifié
                FOREIGN KEY (student_id) REFERENCES students(id)
            );
        """)
        self.connecte.commit()

    def ajouter_absence(self, student_id, date, status=0):
        self.cusor.execute("""
            INSERT INTO absences (student_id, date, status) 
            VALUES (?, ?, ?);
        """, (student_id, date, status))
        self.connecte.commit()
        
        return True

    def supprimer_absence(self, id_absence):
        self.cusor.execute("DELETE FROM absences WHERE id = ?", (id_absence,))
        self.connecte.commit()
        

    def justifier_absence(self, id_absence):
        self.cusor.execute("""
            UPDATE absences 
            SET status = 1
            WHERE id = ?
        """, (id_absence,))
        self.connecte.commit()
        print(" L'absence a été marquée comme justifiée !")

    def nombre_absences_etudiant(self, student_id):
        self.cusor.execute("SELECT COUNT(*) FROM absences WHERE student_id = ?", (student_id,))
        resultat = self.cusor.fetchone()
        return resultat[0] if resultat else 0

    def supprimer_toutes_les_absences(self):
        self.cusor.execute("DELETE FROM absences")
        self.cusor.execute("DELETE FROM sqlite_sequence WHERE name='absences'")
        self.connecte.commit()
       

    def liste_toutes_absences(self):
        self.cusor.execute("SELECT * FROM absences")
        return self.cusor.fetchall()

    def supprimer_table_absences_definitivement(self):
        self.cusor.execute("DROP TABLE IF EXISTS absences")
        self.cusor.execute("DELETE FROM sqlite_sequence WHERE name='absences'")
        self.connecte.commit()
        print(" La table 'absences' a été définitivement supprimée !")

    def close(self):
        self.connecte.close()