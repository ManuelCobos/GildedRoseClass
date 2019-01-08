class Updatable():
    def updateQuality(self):
        pass


if __name__ == "__main__":
    
    toni = Updatable()
    assert toni.updateQuality() == None, "help!"