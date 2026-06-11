from database.DB import ManagerBase

class Sujet_matiere(ManagerBase):
    def __init__(self):
        super().__init__()
    
    def creer_table_matiere(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS subjects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,                                  
                teacher_id INTEGER,
                FOREIGN KEY (teacher_id) REFERENCES teachers(id)
                ON DELETE SET NULL
            );
        """)
        self.connecte.commit()

   
    def ajouter_matiere(self, nom, teacher_id=None):
      
        if not nom or nom.strip() == "":
            print(" Erreur : Le nom de la matière ne peut pas être vide.")
            return False
            
       
        self.cusor.execute("""
            INSERT INTO subjects (nom, teacher_id) 
            VALUES (?, ?);
        """, (nom, teacher_id))
        
        
        self.connecte.commit()
        print(f" Matière '{nom}' ajoutée avec succès !")
        return True