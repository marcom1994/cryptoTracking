
from unicodedata import name


class CryptoLimit:
    
    id = ""
    name = ""
    limitBuy = -1.0
    limitSell = -1.0

    def __init__(self):
        pass

    def __init__(self, id, name, limitBuy, limitSell):
        self.id = id
        self.name = name
        self.limitBuy = limitBuy
        self.limitSell = limitSell

    def __str__(self) -> str:
        return "CryptoLimit[id:{}, name:{}, limitBuy:{}, limitSell:{}]".format(self.id, self.name, self.limitBuy, self.limitSell)