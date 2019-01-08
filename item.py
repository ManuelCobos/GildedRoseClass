class Item():

    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self.quality = quality 

    def getName(self):
        return self.name

    def getSellIn(self):
        return self.sellIn

    def getQuality(self):
        return self.quality

    def __repr__(self):
        return '%s, %s, %s' % (self.getName(), self.getSellIn(), self.getQuality())

if __name__ == "__main__":


    pato = Item("pato",100,20)
    assert pato.getName() == "pato"  

    sandra = Item("Sandra",52,10)
    assert sandra.getQuality() == 10, "Eh, mi Quality es superior a eso!"
