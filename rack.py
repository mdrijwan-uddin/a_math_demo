from chip import Chip


class Rack:

    def __init__(self) -> None:
        self.__chipsInRack = []
        self.__MAX_CHIPS = 8 # จำนวนตัวเบี้ยสูงสุดที่อยู่บนแป้นวาง

    # ระบุตัวเบี้ย 1 ตัว ใส่เข้าไปในแป้น
    def pushInChip(self, inputChip):
        if type(inputChip) is Chip and len(self.__chipsInRack) < self.__MAX_CHIPS:
            self.__chipsInRack.append(inputChip)

    # ระบุตัวเบี้ย 1 ตัว เอาออกจากแป้น
    def popOutChip(self, inputChip):
        if type(inputChip) is Chip and 0 < len(self.__chipsInRack) <= self.__MAX_CHIPS:
            if inputChip in self.__chipsInRack:
                index = self.__chipsInRack.index(inputChip)
                self.__chipsInRack.pop(index)

    # รับเบี้ยที่เหลืออยู่ภายในแป้น
    def getChipInRack(self):
        return self.__chipsInRack

    # รับจำนวนตัวเบี้ยที่เหลืออยู่ภายในแป้น
    def getTotalChip(self):
        return len(self.__chipsInRack)

    # รับจำนวนตัวเบี้ยสูงสุดที่สามารถอยู่นแป้นได้
    def getMaxChips(self):
        return self.__MAX_CHIPS

    # รับจำนวนตัวเบี้ยที่ต้องการ
    def getChipNeeded(self):
        return self.__MAX_CHIPS - self.getTotalChip()

    # debug only
    def clearRack (self):
        self.__chipsInRack = []

    # สรุปตัวเบี้ยแต่ละตัวที่อยู่บนแป้น .toString()
    def __str__(self) -> str:
        string = "In Rack: "
        for i in range(self.getTotalChip()):
            string = string + "[" + str(self.__chipsInRack[i]) + "]"
        return string


# -----------------test data------------------

# input = [Chip("15"), Chip("+"), Chip("="), Chip("9"),
#          Chip("2"), Chip("8"), Chip("+/-"), Chip("4")]
# a = Rack()
# print(a.pushInChip(Chip("15")))
# print(a.pushInChip(Chip("+")))
# print(a.pushInChip(Chip("=")))
# print(a.pushInChip(Chip("9")))
# print(a.pushInChip(Chip("2")))
# print(a.pushInChip(Chip("8")))
# print(a.pushInChip(Chip("+/-")))
# print(a.pushInChip(Chip("4")))
# print(a)
# print(a.popOutChip(Chip("9")))
# print(a.popOutChip(Chip("+")))
# print(a)
# print(a.getTotalChip())