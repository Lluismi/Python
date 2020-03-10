from accesodatos import listaidcanciones
from accesodatos import pathcanciones
from accesodatos import rutacancionesid

def test_listaid():
    assert len(listaidcanciones()) == 50

def test_listapath():
    assert len(pathcanciones()) == 50

def test_diccionario():
    assert len(rutacancionesid) == 50