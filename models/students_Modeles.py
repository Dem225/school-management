from database.DB import ManagerBase


class studentsModel(ManagerBase):
    def __init__(self):
        super().__init__()

    def creer_table_students(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prenom text NOT NULL,
                age INTEGER NOT NULL,
                classe TEXT NOT NULL,
                matricule TEXT NOT NULL

            );
        """)
        self.connecte.commit()

    def ajouter(self, nom, prenom, age, classe, matricule):
        
        self.cusor.execute(
            """
                INSERT INTO students (nom, prenom,age,classe,matricule)
                VALUES (?, ?,?, ?,?)
            """,
            (nom, prenom, age, classe, matricule),
        )

        self.connecte.commit()

    def supprimer_etudiant(self, id_students):

        self.cusor.execute("DELETE FROM students  WHERE id = ? ", (id_students,  ))
        self.connecte.commit()

    def rechercher_etudiant(self, id_students):

        self.cusor.execute("SELECT * FROM students WHERE id=? ", (id_students, ))
        return self.cusor.fetchall()
        
    def Modifier_etudiant_Non(self,id_students,nom,):
        
        self.cusor.execute("UPDATE students SET nom=? WHERE id=?", (nom, id_students))
        self.connecte.commit()

        

    def Modifier_etudiant_prenom(self,id_students,prenom,):
        
        self.cusor.execute("UPDATE students SET prenom=? WHERE id=?", (id_students,prenom))
        self.connecte.commit()

        
    def Modifier_etudiant_age(self,id_students,age):
        
        self.cusor.execute("UPDATE students SET age=? WHERE id=?",(id_students,age))
        self.connecte.commit()



        
    def Modifier_etudiant_classe(self,id_students,classe):
        self.cusor.execute("UPDATE students SET classe=? WHERE id=?", (id_students,classe))
        self.connecte.commit()


        
    def Modifier_etudiant_matricule(self,id_students,matricule):
    
        self.cusor.execute("UPDATE students SET matricule=? WHERE id=?" ,(id_students,matricule))
        self.connecte.commit()
        
    def Lister_etudiant(self):
        self.cusor.execute("SELECT * FROM students")
        return self.cusor.fetchall()

        

    def close(self):
        self.connecte.close()
