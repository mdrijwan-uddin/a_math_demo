import total_ruled_chip as rule
from chip import Chip


class Rack:
    __MAX_CHIPS = rule.A_MATH_MAX_CHIPS_IN_RACK

    def __init__(self) -> None:
        self.__chipsInRack = []

    def getTotalChip(self):
        return len(self.__chipsInRack)

    def pushInChip(self, inputChips=[]):
        if type(inputChips) is list and 0 < len(inputChips) <= self.__MAX_CHIPS:
            for i in range(len(inputChips)):
                self.__chipsInRack.append(inputChips[i])
            return "In Rack: " + self.__str__()

    def popOutChip(self, inputChips):
        if type(inputChips) is list and 0 < len(inputChips) <= self.__MAX_CHIPS:
            for i in range(len(inputChips)):
                if inputChips[i] in self.__chipsInRack:
                    index = self.__chipsInRack.index(inputChips[i])
                    self.__chipsInRack.pop(index)
            return "In Rack: " + self.__str__()

    def __str__(self) -> str:
        string = ""
        for i in range(self.getTotalChip()):
            string = string + "[" + str(self.__chipsInRack[i]) + "]"
        return string


# a = Rack()
# input = [Chip("15"), Chip("+"), Chip("="), Chip("9"),
#          Chip("2"), Chip("8"), Chip("+/-"), Chip("4")]
# print(a.pushInChip(input))
# print(a.getTotalChip())
# print(a)
# print(a.popOutChip([Chip("9"), Chip("5")]))
