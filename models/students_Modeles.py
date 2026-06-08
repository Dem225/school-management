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

    def Ajouter(self, nom, prenom, age, classe, matricule):
        
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

    def Rechercher_etudiant(self, id_students):

        self.cusor.execute("SELECT * FROM students WHERE id=? ", (id_students, ))
        return self.cusor.fetchall()
        

        
    def Lister_etudiant(self):
        self.cusor.execute("SELECT * FROM students")
        return self.cusor.fetchall()

        

    def close(self):
        self.connecte.close()
