victoires = 0
NDPJ = 0
from termcolor import *

TDV = 0

def replay():
    TDV = int(victoires / NDPJ)
    print(TDV)
    trejouer = colored("Voulez vous rejouer ? Y/n ", "blue")
    rejouer = input(trejouer)
    if rejouer == "Y":
        jeux()
    if rejouer == "n":
        cprint("Aurevoir" , "blue" , attrs=["bold" , "italic"])



def jeux():

    
 import random

 tChoixJ = colored("Pierre,Feuille ou Ciseaux? " , "cyan", attrs=["bold"]) 

 ChoixJ = input(tChoixJ)

 propositions = ["Pierre","Feuille","Ciseaux"]

 ChoixR = random.choice(propositions)

    #cas d'égalites (ROUGE)

    
    
 if ChoixJ == "Pierre" and ChoixR == "Pierre":
        cprint("Toi: Pierre \nPC: Pierre  \nIl y'a égalité ! -_-" , "red" , attrs=["italic"])
        NDPJ += 1

        replay()



 if ChoixJ == "Feuille" and ChoixR == "Feuille":
        cprint("Toi: Feuille \nPC: Feuille \nIl y'a égalité ! -_-" , "red" , attrs=["italic"])
        NDPJ += 1
        replay()


 if ChoixJ == "Ciseaux" and ChoixR == "Ciseaux":
        cprint("Toi : Ciseaux \nPC : Ciseaux \nIl y'a égalité ! -_-" , "red" , attrs=["italic"])
        NDPJ += 1
        replay()

    #cas gagnant (jaune_clair)


 if ChoixJ == "Pierre" and ChoixR == "Ciseaux":
            cprint("Toi : Pierre \nPC : Ciseaux \nVous avez gagné! :)" , "light_yellow" , attrs=["bold"])
            victoires +1
            NDPJ += 1
            replay()

 if ChoixJ == "Feuille" and ChoixR == "Pierre":
            cprint("Toi : Feuille \nPC : Pierre \nVous avez gagné! :)" , "light_yellow" , attrs=["bold"])
            victoires +1
            NDPJ += 1
            replay()


 if ChoixJ == "Ciseaux" and ChoixR == "Feuille":
            cprint("Toi : Ciseaux \nPC : Feuille \nVous avez gagné! :)" , "light_yellow" , attrs=["bold"])
            victoires +1
            NDPJ += 1
            replay()


    #cas perdant (bleu foncé)

 if ChoixJ == "Pierre" and ChoixR == "Feuille":
            cprint("Toi : Pierre  \nPC : Feuille \nVous avez perdu ! :(" , "blue", attrs=["bold"])
            NDPJ += 1
            replay()

 if ChoixJ == "Feuille" and ChoixR == "Ciseaux":
            cprint("Toi : Feuille \nPC : Ciseaux \nVous avez perdu ! :(" , "blue" , attrs=["bold"])
            NDPJ += 1
            replay()

 if ChoixJ == "Ciseaux" and ChoixR ==  "Pierre":
            cprint("Toi : Ciseaux \nPC : Pierre \nVous avez perdu ! :(" , "blue" , attrs=["bold"])
            NDPJ += 1
            replay()

jeux()
