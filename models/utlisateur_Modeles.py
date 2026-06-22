from database.DB import ManagerBase
import sqlite3
class Utilisateur(ManagerBase):
    def __init__(self):
        super().__init__()
    
    def creer_table_utilisateur(self):
        self.cusor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                role text NOT NULL CHECK(role IN ('admin', 'professeur', 'étudiant')),
                user_name TEXT UNIQUE,
                password TEXT
                
            );
        """)
        self.connecte.commit()
        


    def ajouter_utilisateur(self, nom, role, user_name, password):
        try:
            self.cusor.execute("""
                INSERT INTO users (nom, role, user_name, password)
                VALUES (?, ?, ?, ?)
            """, (nom, role, user_name, password))
            self.connecte.commit()
                  
        except sqlite3.IntegrityError as e:
            error_msg = str(e).lower()
            if "check" in error_msg:
                return {"succes": False, "message": "Rôle invalide ! Les rôles autorisés sont : admin, professeur, étudiant."}
            elif "unique" in error_msg:
                return {"succes": False, "message": f"Le pseudo '{user_name}' est déjà utilisé."}
            else:
                return {"succes": False, "message": f"Erreur de base de données : {e}"}
            
    def supprimer_utilisateur(self, id_user):
        self.cusor.execute("DELETE FROM users WHERE id = ?", (id_user,))
        self.cusor.execute("DELETE FROM sqlite_sequence WHERE nom='users'")
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
        


      
    def verifier_identifiants(self, user_name, password):
        self.cusor.execute("SELECT * FROM users WHERE user_name = ? AND password = ?", (user_name, password))
        return self.cusor.fetchone() 

   

    def supprimer_tous_le_contenue_utilisateur(self):
        self.cusor.execute("DELETE FROM users")
        self.cusor.execute("DELETE FROM sqlite_sequence WHERE nom='users'")
        self.connecte.commit()
        
    def rechercher_utilisateur(self,id_user):
        self.cusor.execute("SELECT * FROM users  WHERE id= ?",(id_user))
        return self.cusor.fetchall()
    
    def liste_tout_utilisateur(self):
        self.cusor.execute("SELECT * FROM users ")
        return self.cusor.fetchall()
    


    def supprimer_table_utilisateurs(self):
        try:
            self.cusor.execute("DROP TABLE IF EXISTS users")
            self.connecte.commit() 
        except Exception as e:
            print(f"Une erreur est survenue lors de la suppression : {e}")
        
      
    def close(self):
        self.connecte.close()