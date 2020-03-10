# Clase NormalItem, hereda de Updateable e Item
# será la base para casi todos los items de la tienda.

from Item import Item
from Updateable import Updateable


class NormalItem(Item, Updateable):

    def set_quality(self):
        if self.quality < 0:
            self.quality = 0
        elif self.quality > 50:
            self.quality = 50
        else:
            self.quality = self.quality

    def set_sellIn(self):
        self.sell_in -= 1

    def update_quality(self):
        if self.sell_in > 0:
            self.quality -= 1
        if self.sell_in < 0:
            self.quality -= 2


if __name__ == '__main__':
    elixir = NormalItem('Elixir of the Mongoose', 7, 87)
    elixir.set_quality()
    print(elixir)
