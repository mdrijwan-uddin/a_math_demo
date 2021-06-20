from chip import Chip


class CalculationRule:
    def __init__(self, chips) -> None:
        self.__chips = chips

    def getLength(self):
        return len(self.__chips)

    def getTypeofEachChips(self):
        typeofChips = []
        for i in range(self.getLength()):
            typeofChips.append(self.__chips[i].getType())
        return typeofChips

    def isEquation(self):
        return Chip("=") in self.__chips

    def isLimitedLength(self):
        return len(self.__chips) <= 15

    def AreEqualsJoint(self):
        for i in range(self.getLength() - 1):
            if self.__chips[i].getType() is "Equal" \
            and self.__chips[i+1].getType() is "Equal":
                return True
        return False

    def AreOperatorJoint(self):
        for i in range(self.getLength() - 1):
            if self.__chips[i].getType() is "Operator" \
                and self.__chips[i+1].getType() is "Operator":
                return True
        return False

    def have2DigitStaked(self):
        _2DigitIndex = []
        number = ["1_digit", "2_digit"]
        for index in range(self.getLength()):
            if self.__chips[index].getType() is "2_digit":
                _2DigitIndex.append(index)
        if len(_2DigitIndex) > 0:
            for i in range(len(_2DigitIndex)):
                if _2DigitIndex[i] is 0:
                    if self.__chips[1].getType() in number:
                        return True
                elif _2DigitIndex[i] is self.getLength() - 1:
                    if self.__chips[_2DigitIndex[i] - 1].getType() in number:
                        return True
                else:
                    if self.__chips[_2DigitIndex[i] + 1].getType() in number \
                            and self.__chips[_2DigitIndex[i] - 1].getType() in number:
                        return True
        else:
            return False
    
    def have3MoreDigit(self):
        number = []
        for i in range(self.getLength() - 1):
            if self.__chips[i].getType() is "Operator" \
                and self.__chips[i+1].getType() is "Operator":
                return True
        return False
        

    def __str__(self) -> str:
        string = ""
        for i in range(self.getLength()):
            string = string + "[" + str(self.__chips[i]) + "]"
        return string


# Name = input("Please enter your name?")

# สำหรับ dubug การเช็คกฏ
inputList = ["15", "1", "-", "3", "7", "4", "=", "0", "6"]
input = []
for i in range(len(inputList)):
    input.append(Chip(inputList[i]))
_34 = CalculationRule(input)
print(_34)
# print(_34.getTypeofEachChips())
# print(_34.AreEqualsJoint())
# print(_34.AreOperatorJoint())
# print(_34.have2DigitStaked())
