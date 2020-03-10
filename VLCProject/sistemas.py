import subprocess
from subprocess import Popen
from logica import randompath


def main():
    try:
        vlc = "C:/Program Files/VideoLAN/VLC/vlc.exe"
    except FileNotFoundError:
        print("No se ha encontrado el vlc.exe en la ruta indicada")
        exit()
    path = randompath()
    rutapath = " ".join(path)
    subprocess.Popen([vlc, [rutapath]])
    