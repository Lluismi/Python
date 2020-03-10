# Archivo principal
from NormalItem import NormalItem
from AgedBrie import AgedBrie
from BackstagePass import BackstagePass
from Conjured import Conjured
from Sulfuras import Sulfuras
from gilded_rose import GildedRose
# Crear los objetos de las clases
dexterity = NormalItem('+5 Dexterity Vest', 10, 20)
aged = AgedBrie('Aged Brie', 2, 0)
elixir = NormalItem('Elixir of the Mongoose', 5, 7)
sulfuras = Sulfuras('Sulfuras, Hand of Ragnaros', 0, 80)
sulfuras_two = Sulfuras('Sulfuras, Hand of Ragnaros', -1, 80)
first_backstage = BackstagePass(
    'Backstage passes to a TAFKAL80ETC concert', 15, 20)
second_backstage = BackstagePass(
    'Backstage passes to a TAFKAL80ETC concert', 10, 49)
third_backstage = BackstagePass(
    'Backstage passes to a TAFKAL80ETC concert', 5, 49)
conjured = Conjured('Conjured Mana Cake', 3, 6)

stock = GildedRose([dexterity, aged, elixir, sulfuras, sulfuras_two,
                    first_backstage, second_backstage, third_backstage, conjured])
stock.get_items()
stock.update_quality(0)
