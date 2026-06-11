from database.DB import ManagerBase

class Absences_model(ManagerBase):
    def __init__(self):
        super().__init__()
        
    def creer_table_absences(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS absences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students(id)
            );
        """)
        self.connecte.commit()

    
    def ajouter_absence(self, student_id, date, status="Non justifiée"):
       
        statuts_autorises = ["Justifiée", "Non justifiée"]
        if status not in statuts_autorises:
            print(" Erreur : Le statut doit être 'Justifiée' ou 'Non justifiée'.")
            return False 
            
       
        self.cusor.execute("""
            INSERT INTO absences (student_id, date, status) 
            VALUES (?, ?, ?);
        """, (student_id, date, status))
        
        self.connecte.commit()
        print(f" Absence enregistrée le {date} pour l'étudiant ID {student_id} ({status}) !")
        return True