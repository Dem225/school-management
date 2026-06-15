from database.DB import ManagerBase

class Utilisateur(ManagerBase):
    def __init__(self):
        super().__init__()
    
    def creer_table_utilisateur(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                role TEXT NOT NULL CHECK(role IN ('admin', 'professeur', 'étudiant')),
                password TEXT
            );
        """)
        self.connecte.commit()
        
    def ajouter_utilisateur(self, nom, role, password):
        self.cusor.execute("""
            INSERT INTO users (name, role, password)
            VALUES (?, ?, ?)
        """, (nom, role, password))
        self.connecte.commit()
        
    def supprimer_utilisateur(self, id_user):
        self.cusor.execute("DELETE FROM users WHERE id = ?", (id_user,))
        self.cusor.execute("DELETE FROM sqlite_sequence WHERE name='users'")
        self.connecte.commit()
    
    def modifier_utilisateur_nom(self, id_user, nom):
        self.cusor.execute("""
            UPDATE users 
            SET nom = ?
            WHERE id = ?
        """, (nom, id_user))
        self.connecte.commit()
    

    def modifier_utilisateur_role(self, id_user,role ):
        self.cusor.execute("""
            UPDATE users 
            SET  role = ?  
            WHERE id = ?
        """, ( role, id_user))
        self.connecte.commit()
        

    def modifier_utilisateur_password(self, id_user, password):
        self.cusor.execute("""
            UPDATE users 
            SET  password= ?
            WHERE id = ?
        """, ( password, id_user))
        self.connecte.commit()
        



    def verifier_identifiants(self, nom, password):
        self.cusor.execute("""
            SELECT * FROM users WHERE name = ? AND password = ?
        """, (nom, password))

        return self.cusor.fetchone()

    def supprimer_tous_les_utilisateurs(self):
        self.cusor.execute("DELETE FROM users")
        self.cusor.execute("DELETE FROM sqlite_sequence WHERE name='users'")
        self.connecte.commit()
        
    def rechercher_utilisateur(self,id_user):
        self.cusor.execute("SELECT * FROM users  WHERE id= ?",(id_user))
        return self.cusor.fetchall()
    
    def liste_tout_utilisateur(self):
        self.cusor.execute("SELECT * FROM users ")
        return self.cusor.fetchall()
       
    def close(self):
        self.connecte.close()