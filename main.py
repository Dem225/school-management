from models.notes_Modeles import Notes_model


def main():

    recepteur = Notes_model()
    recepteur.creer_table_Notes()
    
    print("Fait avec succès !")
   
if __name__ == "__main__":
    main()