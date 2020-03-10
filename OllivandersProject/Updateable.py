# Esta será la clase abstracta de la que todas las otras
# clases tendrán que implementar el método update_quality

from abc import ABCMeta, abstractmethod


class Updateable(metaclass=ABCMeta):

    @abstractmethod
    def update_quality():
        pass
