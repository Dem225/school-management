import random
lists="1 2 3 4 5 6 7 8 9".split()
lists_lette=" A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
def genere_matricule(n=12):
    recepteur =""
    for _ in range(n-1):
        recepteur +=random.choice(lists)
    recepteur+=random.choice(lists_lette)
    return recepteur
