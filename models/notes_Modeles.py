from database.DB import ManagerBase

class Notes_model(ManagerBase):
    def __init__(self):
        super().__init__()
        
    def creer_table_Notes(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS grades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                subject_id INTEGER NOT NULL,
                note REAL NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students(id),
                FOREIGN KEY (subject_id) REFERENCES subjects(id)
            );
        """)
        self.connecte.commit()

    def ajouter_note(self, student_id, subject_id, note):
        # 1. Validation de la note entre 0 et 20
        if not (0 <= note <= 20):
            print("Erreur : La note doit être comprise entre 0 et 20.")
            return False # On arrête la fonction ici si la note est fausse
            
        # 2. Insertion dans la base de données SQLite
        self.cusor.execute("""
            INSERT INTO grades (student_id, subject_id, note) 
            VALUES (?, ?, ?);
        """, (student_id, subject_id, note))
        
        # 3. Sauvegarde
        self.connecte.commit()
        print(f"Note de {note}/20 ajoutée avec succès pour l'étudiant ID {student_id} !")
        return True