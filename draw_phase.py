from bag import Bag
from rack import Rack
from chip import Chip
import random

# print(random.randint(1, 100))


class Draw_Phase():
    def __init__(self) -> None:
        self.__bag = Bag()
        self.__1st_rack = Rack()
        self.__2nd_rack = Rack()

    def draw(self, rack):
        for j in range(rack.getChipNeeded()):
            rng = random.randint(1, self.__bag.getTotalChipsLeft())
            specificChipLeft = 0
            result = 0
            for i in range(len(self.__bag.getTypeofChipLeft())):
                specificChipLeft = self.__bag.getTypeofChipLeft()[i].getQuantity()
                result = rng - specificChipLeft
                if result > 0:
                    rng = result
                else:
                    drawedChip = Chip(self.__bag.getTypeofChipLeft()[i].getChipValue())
                    if rack.pushInChip(drawedChip) == "Success":
                        self.__bag.popOutChip(drawedChip)
                    break

    def getCurrentBag(self):
        return self.__bag

    def getFirstRack(self):
        return self.__1st_rack

    def getSecondRack(self):
        return self.__2nd_rack

    def __str__(self) -> str:
        return str(self.__bag) + "\n1st Rack: " + str(self.__1st_rack) + "\nSecond Rack: " + str(self.__2nd_rack)


a = Draw_Phase()
a1rack = a.getFirstRack()
a2rack = a.getSecondRack()

a.draw(a1rack)
print(a.getCurrentBag())
print(a1rack)
print()
a.draw(a2rack)
print(a.getCurrentBag())
print(a2rack)
print()
