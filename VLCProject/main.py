import xml.etree.ElementTree as ET
from accesodatos import listaidcanciones
from accesodatos import pathcanciones
from logica import randompath
from logica import listaleatoria
from sistemas import main


if __name__ == "__main__":
    listaidcanciones()
    pathcanciones()
    listaleatoria()
    randompath()
    main()
