
class Crypto:

    uuid="-"
    name="-"
    price=0.0
    rank="-"

    def __init__(self):
        pass

    def __init__(self, uuid, name, price):
        self.uuid = uuid
        self.name = name
        self.price = price

    def __init__(self, uuid, name, price, rank):
        self.uuid = uuid
        self.name = name
        self.price = price
        self.rank = rank

    

    
    def __str__(self) -> str:
        return "Crypto[uuid:{}, name:{}, price:{}, rank:{}]".format(self.uuid, self.name, self.price, self.rank)