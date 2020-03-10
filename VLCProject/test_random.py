from accesodatos import listaidcanciones
from accesodatos import pathcanciones
from logica import listaleatoria
from logica import randompath


def test_listrandomid():
    assert len(listaleatoria()) == len(listaidcanciones())


def test_listrandompath():
    assert len(randompath()) == len(pathcanciones())


def test_norepeat():
    listanorepeat = listaleatoria()
    for id in listanorepeat:
        if listanorepeat.count(id) > 1:
            assert False
    assert True
