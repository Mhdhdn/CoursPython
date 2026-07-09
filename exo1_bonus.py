from datetime import date

nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prénom : ")
date_jour = date.today()

date_naissance = input("Entrez votre date de naissance au format DD/MM/YYYY : ")
day , month , year = date_naissance.split ('/')
birthday = date(int(year), int(month), int(day))

age = date_jour.year - birthday.year

if date_jour.month < birthday.month :
    age -= 1
elif date_jour.month == birthday.month and date_jour.day < birthday.day : 
    age -= 1
print("Vous avez ",age," ans")