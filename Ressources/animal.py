class Mammal: 
    nb_pattes: int
    nom : str
    race : str
    couleur : str

    def __init__(self, nb_pattes: int, nom: str, race : str, couleur: str):
        self.couleur = couleur
        self.nb_pattes = nb_pattes
        self.race = race
        self.nom = nom

    def __str__(self):
        return f"Le mammifère de race '{self.race}' s'appelle '{self.nom}', il est de couleur '{self.couleur}', il a '{self.nb_pattes}' pattes"