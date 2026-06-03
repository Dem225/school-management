from database.DB import ManagerBase

class Utilisateur(ManagerBase):
    def __init__(self):
        super().__init__()
    
    def creer_table_utilisateur(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                role TEXT NOT NULL CHECK(role IN ('admin', 'professeur', 'étudiant'))
            );
        """)
        self.connecte.commit()
        
    def ajouter_utilisateur(self, nom, role):
            
        self.cusor.execute("""
                INSERT INTO users (name, role)
                VALUES (?, ?)
            """, (nom, role))
            
        self.connecte.commit()
        
    def supprimer_utilisateur(self,id_user):
        
        self.cusor.execute("DELETE FROM users WHERE id = ? ", (id_user,))
        self.connecte.commit()
    

    def Modifier(self,name,role):
    
        self.cusor.execute("UPDATE users SET name= ?  role:?  WHERE id=?",(name,role))



    def close(self):
        self.connecte.close()
    
