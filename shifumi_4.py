from termcolor import *
import random

victoires = 0
parties_jouees = 0
taux_victoires = 0.0

def replay():
    global victoires, parties_jouees, taux_victoires
    cprint("victoires: " + str(victoires) , "yellow" , attrs=["italic" , "bold"])
    cprint("total: " + str(parties_jouees) , "green" , attrs=["bold"])
    taux_victoires = (victoires / parties_jouees) * 100
    cprint("Taux de réussite: " + str(taux_victoires) , "blue" , attrs=["bold" , "italic"])
    texte_rejouer = colored("Voulez vous rejouer ? Y/n ", "blue")
    rejouer = input(texte_rejouer)
    if rejouer == "Y":
        jeux()
    if rejouer == "n":
        cprint("Aurevoir" , "blue" , attrs=["bold" , "italic"])



def jeux():
 global victoires, parties_jouees

    
 tChoixJ = colored("Pierre,Feuille ou Ciseaux? " , "cyan", attrs=["bold"]) 

 ChoixJ = input(tChoixJ)

 propositions = ["Pierre","Feuille","Ciseaux"]

 ChoixR = random.choice(propositions)

    #cas d'égalites (ROUGE)

    
 if ChoixJ == "Pierre" and ChoixR == "Pierre" or ChoixR == "Feuille" and ChoixJ == "Feuille" or ChoixJ == "Ciseaux" and ChoixR == "Ciseaux":
        cprint(f"Toi: {ChoixJ} \nPC: {ChoixR}   \nIl y'a égalité ! -_-" , "red" , attrs=["italic"])
        parties_jouees += 1
        replay()

    #cas perdant (BLEU)
 
 if ChoixJ == "Pierre" and ChoixR == "Feuille" or ChoixJ == "Feuille" and ChoixR == "Ciseaux" or ChoixJ == "Ciseaux" and ChoixR == "Pierre":
        cprint(f"Toi: {ChoixJ} \nPC: {ChoixR}   \nVous avez perdu ! :(" , "blue", attrs=["bold"])
        parties_jouees += 1
        replay()
    #cas gagnant (jaune clair)

 if ChoixJ == "Pierre" and ChoixR == "Ciseaux" or ChoixJ == "Feuille" and ChoixR == "Pierre" or ChoixJ == "Ciseaux" and ChoixR == "Feuille":
      cprint(f"Toi: {ChoixJ} \nPC: {ChoixR}   \nVous avez gagné ! :)" , "light_yellow", attrs=["bold"])
      victoires += 1
      parties_jouees += 1
      replay()

 
 
jeux()
