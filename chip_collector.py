from chip import Chip

class Chip_Collector(Chip):
    def __init__(self, chipValue, quantity) -> None:
        super().__init__(chipValue)
        self.__MAX_QUANTITY = self.__quantity = quantity

    def increasingQuantity(self):
        if (self.__quantity < self.__MAX_QUANTITY):
            self.__quantity = self.__quantity + 1

    def decreasingQuantity(self):
        if(self.__quantity > 0):
            self.__quantity = self.__quantity - 1

    def getMaxQuantity(self):
        return self.__MAX_QUANTITY

    def getChip (self):
        return super()

    def getChipValue(self):
        return super().__str__()
        
    def getQuantity (self):
        return self.__quantity

    def __str__(self) -> str:
        return "Value: " + str(super().__str__()) + "\tQuantity: " + str(self.__quantity)
    