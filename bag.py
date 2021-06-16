# from chip import Chip
import total_ruled_chip as rule

class Bag:

    def __init__(self) -> None:
        self.__chips = rule.TRADITIONAL_CHIP_COUNTS

    def getChipsLeft(self):
        total = 0
        for i in range(len(self.__chips)):
            total = total + (self.__chips[i].getQuantity())
        return total

    def popOutChip (self, inputChip):   
        for i in range(len(self.__chips)):
            if self.__chips[i].getCHIP() == inputChip:
                self.__chips[i].decreasingQuantity()
                return "One [" + str(self.__chips[i].getCHIP()) + "] has been draw."

    def pushInChip (self, inputChip):   
        for i in range(len(self.__chips)):
            if self.__chips[i].getCHIP() == inputChip:
                self.__chips[i].increasingQuantity()
                return "One [" + str(self.__chips[i].getCHIP()) + "] has been put in the bag."

    def __str__(self) -> str:
        string = "Total Chips: " + str(self.getChipsLeft()) + \
            "\n------------------------------------------------------------------------------"
        for i in range(len(self.__chips)):
            string = string + ("\n" if i % 5 == 0 else "\t") + \
                "[" + str(self.__chips[i].getCHIP()) + "]\t: " + str(self.__chips[i].getQuantity())
        return string


# a = Bag()
# print(a)
# print(a.popOutChip(Chip("=")))
# print(a)
# print(a.pushInChip(Chip("=")))
# print(a)
