# Clase para los Backstage

from NormalItem import NormalItem


class BackstagePass(NormalItem):

    def update_quality(self):
        if self.sell_in > 10:
            self.quality += 1
        if self.sell_in <= 10 and self.sell_in > 5:
            self.quality += 2
        if self.sell_in <= 5 and self.sell_in >= 0:
            self.quality += 3
        if self.sell_in < 0:
            self.quality = 0


if __name__ == '__main__':
    ticket = BackstagePass('Backstage passes to a TAFKAL80ETC concert', 15, 20)
    print(ticket.sell_in, ticket.quality)
    ticket.set_sellIn()
    ticket.update_quality()
    print(ticket.sell_in, ticket.quality)
    ticket2 = BackstagePass('Backstage passes to a TAFKAL80ETC concert', 4, 20)
    print(ticket2.sell_in, ticket2.quality)
    ticket2.set_sellIn()
    ticket2.update_quality()
    print(ticket2.sell_in, ticket2.quality)
