class RetailItem:

    #initializer method
    #initializer decription, units, price
    def __init__(self,description,units,price):
        self.__description=description
        self.__units=units
        self.__price=price


    def get_description(self):
        return self.__description

    def set_description(self,decription):
        self.__description=decription

    def get_units(self):
        return self.__units

    def set_units(self,units):
        self.__units=units

    def get_price(self):
        return self.__price

    def set_price(self,price):
        self.__price=price

    #str
    #returns description, units and price
    def __str__(self):
        return "TetailItem"+"\n\t description:" + self.get_description() +"\n\t Unit:" + str(self.get_units()) +"\n\t Price: $" +str(self.get_price())





