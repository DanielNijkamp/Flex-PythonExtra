import os
 
mapnaam = "mapding"

lengte_mapnaam = 0

werkmap = os.getcwd()

while lengte_mapnaam == 0:
    lengte_mapnaam = len(mapnaam)


if lengte_mapnaam > 0:
    os.mkdir(mapnaam)
else:
    print("Je hebt geen naam ingevoerd")

print("De map " + mapnaam + " is gemaakt")
