from item import Item
from updatable import Updatable


class RegularItem(Item, Updatable):

    def update_quality(self):
        if self.sellIn > 0:
            self.quality = self.quality - 1
        else:
            self.quality = self.quality -2
        
        if self.quality < 0:
            self.quality = 0
        elif self.quality > 50:
            self.quality = 50
        

# Casos test para las diferentes actualizaciones.
if __name__ == "__main__":
    
    pato = RegularItem("Pato", 100, 10)
    pato.update_quality()
    assert pato.getQuality() == 9

    pita = RegularItem("Pita", 0, 10)
    pita.update_quality()
    assert pita.getQuality() == 8

    pito = RegularItem("Pito", 100, -1)
    pito.update_quality()
    assert pito.getQuality()==0

    pepota = RegularItem("pepota", 100 , 59)
    pepota.update_quality()
    assert pepota.getQuality() == 50

