# Doel:
# maak hoger/ lager spel moet als volgt werken.
# De speler wordt een getal getoond van 1 t/m 10
# De speler moet daarna raden of het volgende random getal hoger of lager wordt
# Aan het einde moet de speler weten of hij/zij gewonnen heeft

#stappenplan
# -. random number gemaakt
# -. toon de speler en vraag hij/ zij en vraag om te raden of het hoger of lager wordt.
# -. speler voert in hoger of lager
# -. er moet een volgend getal gegenereerd worden
#   -. als het nieuwe getal hoger is dan het oude getal dan moet er worden gekeken of 
#    -. als de input hoger is, dan is het antwoord goed.
# -. dan moet er gekeken worden of de input hoger of lager is dan de getal.
# -. De speler moet wewten of hij/zij gewonnen of veloren heeft.

import random


willekeur = random.randrange(1, 11)

print("Het getal van 1 t/m 10 is momenteel", willekeur)
print("Wordt het volgende getal hoger [H] of lager [L] ?")

antwoord = input()

nieuweGetal = random.randrange(1, 11)

if (nieuweGetal > willekeur):
    if (antwoord == "H"):
        print("Ja! Het is inderdaad hoger")
        print("Het nieuwe getal is", nieuweGetal)
