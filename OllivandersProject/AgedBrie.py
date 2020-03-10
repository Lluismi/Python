# Clase para los items AgedBrie

from NormalItem import NormalItem


class AgedBrie(NormalItem):

    def AgedQuality(self, valor):
        if self.quality + valor <= 50:
            self.quality = self.quality + valor
        else:
            self.quality = 50

    def update_quality(self):
        if self.sell_in > 0:
            self.quality += 1
        if self.sell_in < 0:
            self.quality += 2


if __name__ == '__main__':
    Brie = AgedBrie('AgedBrie', 20, 33)
    print(Brie.sell_in, Brie.quality)
    Brie.update_quality()
    Brie.set_sellIn()
    print(Brie.sell_in, Brie.quality)
