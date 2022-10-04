from ast import If
from unicodedata import name
from random import shuffle
from ast import While



# # place cinema les conditions EXERCICE REUSSIR
mon_age= int(input("Entrer votre age!!!"))
if mon_age < 18:
    print("Payer 7£!!!")
    demande = input("Souhaitez vous du pop corn???")
    if demande == 'oui':
        payer = 7 + 5
    else:
        print("Vous aurez juste a payer le prix du cinema!!!")
        payer = 7
elif 18 <= mon_age < 80:
    print("Payer 12£")        
    demande = input("Souhaitez vous du pop corn???")
    if demande == 'oui':
        payer = 12 + 5
    else:
        print("Vous aurez juste a payer le prix du cinema!!!")
        payer = 12
else:
    print("Desoler vous etre pas autoriser a suivre le cinema!!!")  
    payer = 0      

print("Le prix total a payer est donc {} ".format(payer))


# Generateur de phrase les listes EXERCICE REUSSIR shuffle melanger une liste

chaine = input("Entrer une chaine de cette forme (mot1/mot2/mot3/mot4):").split("/")
print(chaine)
shuffle(chaine)
print(chaine)
if len(chaine) < 10:
    print(chaine[1],chaine[2],chaine[len(chaine) - 1])
elif len(chaine) >= 10: 
  print(chaine[0],chaine[1])
  
  
  # JEU DU JUSTE PRIX, les boucles EXERCICE NON REUSSIR
# nombre = 50 
# for nbre in range(1, 1001):
#     input("Entrer le prix!!!")
#     while nbre < nombre:
#         print("c'est moins")
#         continue
#     while nbre > nombre:
#         print("c'est plus!!")
#         continue
#     while nbre == nombre:
#        print("c'est gagner!!")
#        break


    


# fonction pour calculer le nombre de voyelle dans un mot EXERCICE NON REUSSIR
voyelle = ["a", "e", "i", "o", "u", "y"]
mot ="malaury"
lettre_voyelle = mot.lower()
def get_vowels_numbers(lettre_voyelle):
    compteur = 0
    for lettre in lettre_voyelle:
        if lettre in voyelle:
            compteur += 1
            return compteur
    
get_vowels_numbers() 
   
