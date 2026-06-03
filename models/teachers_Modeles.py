from database.DB import ManagerBase


class ProfesseurModel(ManagerBase):
    def __init__(self):
        super().__init__()

    def creer_table_Professuer(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom text NOT null,
                matiere TEXT NOT NULL
            );
        """)
        self.connecte.commit()

    def Ajouter(self, nom, matiere):

        self.cusor.execute(
            """
                INSERT INTO teachers (nom, matiere)
                VALUES (?, ?)
            """,
            (nom, matiere),
        )

        self.connecte.commit()

    def supprimer(self, id_teacher):

        self.cusor.execute("DELETE FROM teachers  WHERE id = ? ", (id_teacher,))
        self.connecte.commit()

    def Modifier(self, matiere):
        self.cusor.execute("UPDATE teachers SET matiere = ? WHERE id=? ", (matiere))
        self.connecte.commit()
    
    def Rechercher(self,id_teacher):
      self.cusor.execute("SELECT * FROM WHERE id= ?",(id_teacher))
      self.cusor.fetchall()
      self.connecte.commit()

      
    def close(self):
        self.connecte.close()
