#STRUCTURES CONDITIONNELLES 

age = int(input("Quel âge avez vous ?"))
majeur= age >= 18
mineur = age <= 18

if majeur: 
    print("vous êtes majeur")
else:
    print("vous êtes mineur")

majeur_france = age >= 18
majeur_USA = age >= 21

if majeur_USA : 
    print("You are an Adult in the US OF A")
elif majeur_france : 
    print("Vosu êtes majeur en france")
else:
    print("Vosu êtes mineurs")

statut = ""

#if age >= 18:
    #statut = "ADULTE"
#else: 
    #statut = "ENFANT"

 #en une ligne : 

statut = "ADULT USA" if age >= 21 else "ADULTFRANCE" if age >=18  else "ENFANT"

print (statut)  
  


choix_user = input("Choisissez une option du menu\n  " \
"1 - Coca - Cola\n  " \
"2 - Sprite\n  " \
"3 - Ice Tea\n  " \
"4 - Volvic\n  " \
"5 - Orangina\n")

match choix_user:
    case "1":
        print("enjoy your coke")               #MATCH ET CASE PERMETTENT DE NE PAS A AVOIR A REECRIR LE NOM DE LA VARIABLE
    case "2":
        print("enjoy your sprite")
    case "3":
        print("enjoy your Ice Tea")
    case "4":
        print("enjoy your Volvic")
    case "5":
        print("enjoy your Orangina")

##STRUCTURES ITERATIVES

age = 0 #age = int(input("Quel âge avez vous ?"))


while age<18:
    print ("je suis mineur")
    age = age + 1
else :("je ne boucle pas :(")
print("je suis majeur")

entre_user = ""

while entre_user != "STOP":
    entre_user = input(" ENTREZ STOP POUR STOPPER LA BOUCLE  ")


while True : #while true veut dire que la boucle se lance en permanance tant qu'on  a pas entré la condition
    if input("TAPEZ STOP POUR ARRETER LA BOUCLE\0") == "STOP":
        break

#BOUCLE AVEC X ITERATIONS

for i in range(5):
    print(i + ": Je me répète...")

