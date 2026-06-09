from database.DB import ManagerBase



class Notation (ManagerBase):
    def __init__(self):
        super().__init__()
    def creer_table_Note_etudiant(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS teachers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom text NOT null,
                matiere TEXT NOT NULL
            );
        """)
        self.connecte.commit()