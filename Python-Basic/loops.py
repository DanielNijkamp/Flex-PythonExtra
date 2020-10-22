#DOEL:
# Een mannetje dat van links naar rechts kan bewegen.

import os
import random

isRunning = True
antwoord = ""

#AVATAR VAN SPELER IS HET VOLGENDE KARAKTER

playerSprite = "@"

  
#POSITIE BIJHOUDEN
positieX = (0)

print("Press ENTER to start the game.")


while ( isRunning == True):

    #REGISTREER INPUT
    antwoord = input()


    #UPDATE DE GAME
    if (antwoord == "quit"):
        isRunning = False
        break; #als je de game quit hoef je de rest ook niet meer uit te voeren
    if (antwoord == "d"):
        positieX += 1
    elif(antwoord == "a"):
        positieX -= 1

    #MAAK EERST HET SCHERM SCHOON:
        os.system("cls")


    #TEKEN DE HUIDIGE STAAT VAN DATA
    for x in range(positieX):
         #zet spaties neer todat we op de speler positie zijn
         print(" ", end= "")
    else:
        print(playerSprite)


    print("-----------------------------")
    
