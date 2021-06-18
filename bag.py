# from chip import Chip
import total_ruled_chip as rule


class Bag:

    # รับตัวเบี้ยมาจาก Setup
    def __init__(self) -> None:
        self.__chips = rule.TRADITIONAL_CHIP_COUNTS
        self.__MAX_CHIPS = self.getTotalChipsLeft()

    # จำนวนตัวเบี้ยที่เหลืออยู่ภายในถุง
    def getTotalChipsLeft(self):
        total = 0
        for i in range(len(self.__chips)):
            total = total + (self.__chips[i].getQuantity())
        return total

    # ระบุตัวเบี้ย 1 ตัว แยกออกจากถุง
    def popOutChip(self, inputChip):
        if 0 < self.getTotalChipsLeft():
            for i in range(len(self.__chips)):
                if self.__chips[i].getChip() == inputChip:
                    self.__chips[i].decreasingQuantity()
                    return "One [" + self.__chips[i].getChipValue() + "] has been draw."

    # ระบุตัวเบี้ย 1 ตัว ใส่เข้าไปในถุง
    def pushInChip(self, inputChip):
        if self.getTotalChipsLeft() <= self.__MAX_CHIPS:
            for i in range(len(self.__chips)):
                if self.__chips[i].getChip() == inputChip:
                    self.__chips[i].increasingQuantity()
                    return "One [" + self.__chips[i].getChipValue() + "] has been put in the bag."

    # สรุปตัวเบี้ยแต่ละตัวที่เหลืออยู่ในถุง .toString()
    def __str__(self) -> str:
        string = "Total Chips: " + str(self.getTotalChipsLeft()) + \
            "\n------------------------------------------------------------------------------"
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
