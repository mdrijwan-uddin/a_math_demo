from chip import Chip

class Chip_Collector:
    def __init__(self, chip, quantity) -> None:
        self.__CHIP = chip
        self.__MAX_QUANTITY = self.__quantity = quantity

    def increasingQuantity(self):
        if (self.__quantity < self.__MAX_QUANTITY):
            self.__quantity = self.__quantity + 1

    def decreasingQuantity(self):
        if(self.__quantity > 0):
            self.__quantity = self.__quantity - 1

    def getCHIP (self):
        return self.__CHIP

    def getMaxQuantity(self):
        return self.__MAX_QUANTITY
        
    def getQuantity (self):
        return self.__quantity

    def __str__(self) -> str:
        return "Value: " + str(self.__CHIP) + "\tQuantity: " + str(self.__quantity)
    