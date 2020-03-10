# casos test
from main import *


def test_aged_brie():
    aged = AgedBrie('AgedBrie', 2, 0)
    assert aged.sell_in == 2
    aged.update_quality()
    assert aged.quality == 1


def test_normal_item():
    elixir = NormalItem('Elixir of the Moongose', 5, 7)
    assert elixir.quality == 7
    elixir.set_sellIn()
    assert elixir.sell_in == 4


def test_sulfuras():
    sulfuras = Sulfuras('Sulfuras, Hand of Ragnaros', 0, 80)
    sulfuras.set_sellIn()
    sulfuras.update_quality()
    assert sulfuras.sell_in == 0
    assert sulfuras.quality == 80


def test_backstage():
    backstage = BackstagePass('Backstage passes', 4, 48)
    backstage_two = BackstagePass('Backstage', 0, 46)
    backstage.set_sellIn()
    backstage.update_quality()
    backstage.set_quality()
    assert backstage.quality == 50
    backstage_two.set_sellIn()
    backstage_two.update_quality()
    assert backstage_two.quality == 0


def test_conjured():
    conjured = Conjured('Conjured Mana Cake', 3, 4)
    conjured.set_sellIn()
    conjured.update_quality()
    conjured.set_quality()
    assert conjured.quality == 2

# Ahora toca hacer un inyector para el test de gilded_rose
