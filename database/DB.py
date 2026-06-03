import sqlite3

class ManagerBase:
    def __init__(self):
        self.connecte = sqlite3.connect("MANAGER.db")
        self.cusor=self.connecte.cursor()
        
        
        