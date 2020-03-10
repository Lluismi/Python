import xml.etree.ElementTree as ET


def listaidcanciones():
    try:
        tree = ET.parse('Library.xml')
    except ET.ParseError:
        print("No se ha encontrado el xml")
        exit()
    root = tree.getroot()
    idsong = []
    for track in root.find('cancions'):
        for id in track.findall('id'):
            idsong.append(id.text)
    return idsong


def pathcanciones():
    try:
        tree = ET.parse('Library.xml')
    except ET.ParseError:
        print("No se ha encontrado el xml")
    root = tree.getroot()
    pathsong = []
    for track in root.find('cancions'):
        for path in track.findall('path'):
            pathsong.append(path.text)
    return pathsong


rutacancionesid = {}

rutacancionesid = dict(zip(listaidcanciones(), pathcanciones()))
