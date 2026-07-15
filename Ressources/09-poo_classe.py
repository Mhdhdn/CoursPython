#on utilise les majuscules au lieu de separer par _
#une classe est un moule
from animal import Mammal

class TrainElectrique:
    pass

class Chaise:   
    nb_pieds: int
    materiau : str
    couleur : str

    def __init__(self, nb_pieds: int, materiau: str, couleur: str):
        self.nb_pieds = nb_pieds
        self.materiau = materiau
        self.couleur = couleur
        

chaise_a = Chaise(4, "bois", "rouge")
chaise_b = Chaise(5, "plastique", "bleu")

print(type(chaise_a.couleur))
print(chaise_a.couleur, chaise_b.nb_pieds)

chat_1 = Mammal(4, "Sushi", "Felis Felidae", "orange")
#print(chat_1)

chat_2 = Mammal(4, "Zouzou", "Felus Felidae", "grise")
#print(chat_2)

print(Mammal)