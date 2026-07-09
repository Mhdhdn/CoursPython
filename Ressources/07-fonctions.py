##FONCTIONS

def dire_bonjour():                         #on defini la fonction
    print("hello world")

dire_bonjour()

ensemble_a = [1, 6, 7, 89]
def faire_lasomme(ensemble):
    somme = 0
    for n in ensemble:
        somme += n

    return somme 
    print (f"la somme de l'ensemble {ensemble} est {somme}")

faire_lasomme(ensemble_a)