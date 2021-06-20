from chip import Chip
from chip_collector import ChipCollector


class Bag:
    
    def __init__(self) -> None:
        self.__chips = [ # จำนวนตัวเบี้ยของแต่ละตัว
            ChipCollector("0", 5), ChipCollector("1", 6), ChipCollector("2", 6),
            ChipCollector("3", 5), ChipCollector("4", 5), ChipCollector("5", 4),
            ChipCollector("6", 4), ChipCollector("7", 4), ChipCollector("8", 4),
            ChipCollector("9", 4), ChipCollector("10", 2), ChipCollector("11", 1),
            ChipCollector("12", 2), ChipCollector("13", 1), ChipCollector("14", 1),
            ChipCollector("15", 1), ChipCollector("16", 1), ChipCollector("17", 1),
            ChipCollector("18", 1), ChipCollector("19", 1), ChipCollector("20", 1),
            ChipCollector("+", 4), ChipCollector("-", 4), ChipCollector("+/-", 5),
            ChipCollector("x", 4), ChipCollector("%", 4), ChipCollector("x/%", 4),
            ChipCollector("=", 11), ChipCollector("Blank", 4),
        ]
        self.__MAX_CHIPS = self.getTotalChipsLeft()

    # รับค่าเบี้ยทั้งหมดที่อยู่ในถุง
    def getTypeofChipLeft(self):
        return self.__chips

    # จำนวนตัวเบี้ยที่เหลืออยู่ภายในถุง
    def getTotalChipsLeft(self):
        total = 0
        for i in range(len(self.__chips)):
            total = total + (self.__chips[i].getQuantity())
        return total

    # ระบุตัวเบี้ย 1 ตัว แยกออกจากถุง
    def popOutChip(self, inputChip):
        if type(inputChip) is Chip and 0 < self.getTotalChipsLeft():
            for i in range(len(self.__chips)):
                if self.__chips[i].getChip() == inputChip:
                    self.__chips[i].decreasingQuantity()

    # ระบุตัวเบี้ย 1 ตัว ใส่เข้าไปในถุง
    def pushInChip(self, inputChip):
        if type(inputChip) is Chip and self.getTotalChipsLeft() <= self.__MAX_CHIPS:
            for i in range(len(self.__chips)):
                if self.__chips[i].getChip() == inputChip:
                    self.__chips[i].increasingQuantity()

    # สรุปตัวเบี้ยแต่ละตัวที่เหลืออยู่ในถุง .toString()
    def __str__(self) -> str:
        string = "Total Chips: " + str(self.getTotalChipsLeft())
        for i in range(len(self.__chips)):
            string = string + ("\n" if i % 5 == 0 else "\t") + \
                "[" + str(self.__chips[i].getChipValue()) + "]\t: " + \
                str(self.__chips[i].getQuantity())
        return string


# -----------------test data------------------
# a = Bag()
# print(a)
# print(a.popOutChip(Chip("=")))
# print(a)
# print(a.pushInChip(Chip("=")))
# print(a)
