#on utilise les majuscules au lieu de separer par _
#une classe est un moule
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