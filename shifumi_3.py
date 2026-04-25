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

    
    
 if ChoixJ == "Pierre" and ChoixR == "Pierre":
        cprint("Toi: Pierre \nPC: Pierre  \nIl y'a égalité ! -_-" , "red" , attrs=["italic"])
        parties_jouees += 1

        replay()



 if ChoixJ == "Feuille" and ChoixR == "Feuille":
        cprint("Toi: Feuille \nPC: Feuille \nIl y'a égalité ! -_-" , "red" , attrs=["italic"])
        parties_jouees += 1
        replay()




    #cas gagnant (jaune_clair)


 if ChoixJ == "Pierre" and ChoixR == "Ciseaux":
            cprint("Toi : Pierre \nPC : Ciseaux \nVous avez gagné! :)" , "light_yellow" , attrs=["bold"])
            victoires += 1
            parties_jouees += 1
            replay()

 if ChoixJ == "Feuille" and ChoixR == "Pierre":
            cprint("Toi : Feuille \nPC : Pierre \nVous avez gagné! :)" , "light_yellow" , attrs=["bold"])
            victoires += 1
            parties_jouees += 1
            replay()


 if ChoixJ == "Ciseaux" and ChoixR == "Feuille":
            cprint("Toi : Ciseaux \nPC : Feuille \nVous avez gagné! :)" , "light_yellow" , attrs=["bold"])
            victoires += 1
            parties_jouees += 1
            replay()


    #cas perdant (bleu foncé)

 if ChoixJ == "Pierre" and ChoixR == "Feuille":
            cprint("Toi : Pierre  \nPC : Feuille \nVous avez perdu ! :(" , "blue", attrs=["bold"])
            parties_jouees += 1
            replay()

 if ChoixJ == "Feuille" and ChoixR == "Ciseaux":
            cprint("Toi : Feuille \nPC : Ciseaux \nVous avez perdu ! :(" , "blue" , attrs=["bold"])
            parties_jouees += 1
            replay()

 if ChoixJ == "Ciseaux" and ChoixR ==  "Pierre":
            cprint("Toi : Ciseaux \nPC : Pierre \nVous avez perdu ! :(" , "blue" , attrs=["bold"])
            parties_jouees += 1
            replay()

jeux()
