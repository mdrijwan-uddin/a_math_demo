from bag import Bag
from rack import Rack
from Chips.chip import Chip
import random

# print(random.randint(1, 100))


class DrawPhase():
    def __init__(self) -> None:
        self.__bag = Bag()
        self.__1st_rack = Rack()
        self.__2nd_rack = Rack()

    # จั่วเบี้ยจยกว่าจะเต็มแป้น
    def draw(self, rack):
        if type(rack) is Rack:
            for j in range(rack.getChipNeeded()):
                if 0 < self.__bag.getTotalChipsLeft() <= 100:
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
                            rack.pushInChip(drawedChip) 
                            self.__bag.popOutChip(drawedChip) 
                            break
    
    # สับเปลี่ยนเบี้ย และจั่วเบี้ยใหม่
    def shuffle(self, rack, drawer=[]):
        if type(rack) is Rack and type(drawer) is list:
            for i in range(len(drawer)):
                if drawer[i] in rack.getChipInRack():
                    rack.popOutChip(drawer[i])
            self.draw(rack)
            for j in range(len(drawer)):
                self.__bag.pushInChip(drawer[j])
         
    def getCurrentBag(self):
        return self.__bag

    def getFirstRack(self):
        return self.__1st_rack

    def getSecondRack(self):
        return self.__2nd_rack

    def __str__(self) -> str:
        return str(self.__bag) + "\n1st Rack: " + str(self.__1st_rack) + "\nSecond Rack: " + str(self.__2nd_rack)


# # สำหรับ Debug การจั่วเบี้ยตาแรก
# a = DrawPhase()
# a1rack = a.getFirstRack()
# a2rack = a.getSecondRack()
# a.draw(a1rack)
# print(a.getCurrentBag())
# print(a1rack)
# print()
# a.draw(a2rack)
# print(a.getCurrentBag())
# print(a2rack)
# print()

# สำหรับ Debug การจั่วเบี้ยจนหมดถุง
# b = DrawPhase()
# b1rack = b.getFirstRack()
# for i in range(13):
#     b.getFirstRack().clearRack()
#     b.draw(b1rack)
#     print(b.getCurrentBag())
#     print(b1rack)

# สำหรับ Debug การจั่วเบี้ยขณะที่มีเบี้ยอยู่ในแป้น
# c = DrawPhase()
# c2rack = c.getFirstRack()
# c2rack.pushInChip(Chip("+"))
# c2rack.pushInChip(Chip("-"))
# c2rack.pushInChip(Chip("4"))
# c.getCurrentBag().popOutChip(Chip("+"))
# c.getCurrentBag().popOutChip(Chip("-"))
# c.getCurrentBag().popOutChip(Chip("4"))
# print(c.getCurrentBag())
# c.draw(c2rack)
# print(c.getCurrentBag())
# print(c2rack)

# สำหรับ Debug การเปลี่ยนเบี้ย
# d = DrawPhase()
# d2rack = d.getFirstRack()
# d2rack.pushInChip(Chip("9"))
# d.getCurrentBag().popOutChip(Chip("9"))
# d2rack.pushInChip(Chip("3"))
# d.getCurrentBag().popOutChip(Chip("3"))
# d2rack.pushInChip(Chip("7"))
# d.getCurrentBag().popOutChip(Chip("7"))
# d2rack.pushInChip(Chip("="))
# d.getCurrentBag().popOutChip(Chip("="))
# d2rack.pushInChip(Chip("15"))
# d.getCurrentBag().popOutChip(Chip("15"))
# d2rack.pushInChip(Chip("0"))
# d.getCurrentBag().popOutChip(Chip("0"))
# d2rack.pushInChip(Chip("1"))
# d.getCurrentBag().popOutChip(Chip("1"))
# d2rack.pushInChip(Chip("+/-"))
# d.getCurrentBag().popOutChip(Chip("+/-"))
# print(d.getCurrentBag())
# print(d2rack)
# d.shuffle(d2rack, [Chip("15"), Chip("9"), Chip("7")])
# print(d.getCurrentBag())
# print(d2rack)

