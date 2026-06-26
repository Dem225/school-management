from database.DB import ManagerBase


class ProfesseurModel(ManagerBase):
    def __init__(self):
        super().__init__()

    def creer_table_Professeur(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                subject_id INTEGER NOT null,
                id_user INTEGER,
                FOREIGN KEY (subject_id) REFERENCES subjects(id), 
                FOREIGN KEY (id_user) REFERENCES users(id)
            );
        """)
        self.connecte.commit()

    def Ajouter(self, nom, subject_id, id_user):
        self.cusor.execute("""
            INSERT INTO teachers (nom, subject_id, id_user) 
            VALUES (?, ?, ?);
        """, (nom, subject_id, id_user))
        
        self.connecte.commit()

    def supprimer(self, id_teacher):

        self.cusor.execute("DELETE FROM teachers  WHERE id = ? ", (id_teacher, ))
        self.connecte.commit()

    def Modifier(self, subject_id,id_teacher):
        self.cusor.execute("UPDATE teachers SET subject_id = ? WHERE id=? ", (subject_id ,id_teacher))
        self.connecte.commit()
    
    def Rechercher(self,id_teacher):
      self.cusor.execute("SELECT * FROM teachers  WHERE id= ?",(id_teacher ,))
      return self.cusor.fetchall()

    def Liste_tout_professeur(self):
        self.cusor.execute("SELECT * FROM teachers ")
        return self.cusor.fetchall()
    
    def supprimer_table_professeur_definitively(self):
        self.cusor.execute("DROP TABLE IF EXISTS teachers;")
        self.connecte.commit()
        
    
    def Renommer_columns(self):
        self.cusor.execute("ALTER TABLE teachers RENAME COLUMN matiere TO subject_name;")
    


    
    def close(self):
        self.connecte.close()
