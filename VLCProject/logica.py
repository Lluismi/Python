import random
from accesodatos import listaidcanciones
from accesodatos import rutacancionesid


def listaleatoria():
    listaid = listaidcanciones()
    idaleatorio = []
    for _ in range(len(listaid)):
        numero = random.choice(listaid)
        idaleatorio.append(numero)
        listaid.remove(numero)
    return idaleatorio


def randompath():
    listapathid = listaleatoria()
    path = []
    for id in listapathid:
        path.append(rutacancionesid[id])
    return path
