from chip import Chip
from chip_collector import Chip_Collector


class Bag:
    
    def __init__(self) -> None:
        self.__chips = [ # จำนวนตัวเบี้ยของแต่ละตัว
            Chip_Collector("0", 5), Chip_Collector("1", 6), Chip_Collector("2", 6),
            Chip_Collector("3", 5), Chip_Collector("4", 5), Chip_Collector("5", 4),
            Chip_Collector("6", 4), Chip_Collector("7", 4), Chip_Collector("8", 4),
            Chip_Collector("9", 4), Chip_Collector("10", 2), Chip_Collector("11", 1),
            Chip_Collector("12", 2), Chip_Collector("13", 1), Chip_Collector("14", 1),
            Chip_Collector("15", 1), Chip_Collector("16", 1), Chip_Collector("17", 1),
            Chip_Collector("18", 1), Chip_Collector("19", 1), Chip_Collector("20", 1),
            Chip_Collector("+", 4), Chip_Collector("-", 4), Chip_Collector("+/-", 5),
            Chip_Collector("x", 4), Chip_Collector("%", 4), Chip_Collector("x/%", 4),
            Chip_Collector("=", 11), Chip_Collector("Blank", 4),
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
