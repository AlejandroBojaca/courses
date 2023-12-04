class register:
    def __init__(self, loonies=0, toonies=0, fives=0, tens=0, twenties=0):
        #register(int)
        self.loonies = loonies
        self.toonies = toonies
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
        self.currencies = {
            'toonies': 2,
            'fives': 5,
            'tens': 10,
            'twenties': 20,
        }
        self.loonies = loonies
        self.toonies = toonies
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def getTotal(self):
        return self.loonies + (self.toonies * self.currencies['toonies']) + (self.fives * self.currencies['fives']) + (self.tens * self.currencies['tens']) + (self.twenties * self.currencies['twenties'])

    def add(self, count, denomination):
        setattr(self, denomination, getattr(self, denomination) + count)

    def subtract(self, count, denomination):
        setattr(self, denomination, getattr(self, denomination) - count)

    def showAll(self):
        print({'loonies': self.loonies, 'toonies': self.toonies, 'fives': self.fives, 'tens': self.tens, 'twenties': self.twenties})

instance = register()
instance.loonies = 2
print(instance.getTotal())
instance.add(2, 'twenties')
instance.showAll()
