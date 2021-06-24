from chip import Chip
from chip_managing import ChipManaging

class Rules(ChipManaging):
    def __init__(self, chips) -> None:
        super().__init__(chips)

    # มี เท่ากับ อยู่ในสมการหรือไม่
    def __isEquation(self):
        return Chip("=") in super().getChips()

    # มีจำนวนเบี้ยเกิน 15 ตัวหรือไม่
    def __isLimitedLength(self):
        return 0 < super().getLength() <= 15

    # มี "เท่ากับ" อยู่ต้นหรือท้ายสุดของสมการหรือไม่
    def __isEqualInBegOrEnd(self):
        return super().getChips()[0].getValue() is "=" \
            or super().getChips()[super().getLength() - 1].getValue() is "="

    # มี "เท่ากับ" อยู่ติดกันหรือไม่
    def __AreEqualsJoint(self):
        for i in range(super().getLength() - 1):
            if super().getChips()[i].getType() is "Equal" \
                    and super().getChips()[i+1].getType() is "Equal":
                return True
        return False

    # มี "เครื่องหมาย" อยู่ติดกันหรือไม่
    def __AreOperatorsJoint(self):
        for i in range(super().getLength() - 1):
            if super().getChips()[i].getType() is "Operator" \
                    and super().getChips()[i+1].getType() is "Operator":
                return True
        return False

    # มีการ "หารด้วยศูนย์" เกิดขึ้นหรือไม่
    def __AreDivideZero(self):
        for i in range(super().getLength() - 1):
            if super().getChips()[i].getValue() is "%" \
                    and super().getChips()[i+1].getValue() is "0":
                return True
        return False

    # "เลข 2 หลัก" อยู่ติดกับเลขตัวอื่นหรือไม่ 
    def __have2DigitStaked(self):
        _2DigitIndex = []
        number = ["1_digit", "2_digit"]

        # เก็บ index ที่่มี "เลข 2 หลัก"
        for index in range(super().getLength()):
            if super().getChips()[index].getType() is "2_digit":
                _2DigitIndex.append(index)

        # หากมีมากกว่า 1 ตัว จะเข้าเงื่อนไขตรวจสอบนี้
        if len(_2DigitIndex) > 0:
            for i in range(len(_2DigitIndex)):
                # อยู่ index แรก เช็คตัวหลังอย่างเดียว
                if _2DigitIndex[i] is 0: 
                    if super().getChips()[1].getType() in number:
                        return True
                # อยู่่ index สุดท้าย เช็คตัวหน้าอย่างเดียว
                elif _2DigitIndex[i] is super().getLength() - 1:
                    if super().getChips()[_2DigitIndex[i] - 1].getType() in number:
                        return True
                # อยู่่ index อื่น เช็คตัวหน้าหลัง
                else:
                    if super().getChips()[_2DigitIndex[i] + 1].getType() in number \
                            and super().getChips()[_2DigitIndex[i] - 1].getType() in number:
                        return True
        return False

    # "เลข 1 หลัก" อยู่ติดกันเกิน 3 ตัวหรือไม่  
    def __have4OrMoreDigit(self):
        number = super().separateString("1_digit")
        for k in range(len(number)):
            if len(number[k]) > 3:
                return True
        return False

    # "0" อยู่ด้านหน้าของ "เลข 1 หลัก" ที่ติดกันอยู่หรือไม่ 
    def __have0AtTheFirst(self):
        number = super().separateString("1_digit")
        for k in range(len(number)):
            if len(number[k]) in [2, 3] and number[k][0] is '0':
                return True
        return False

    # "เครื่องหมาย" อยู่ในตำแหน่งที่ผิดปกติหรือไม่ 
    def __isSignInWrongPlace(self, separated):
        Operator = ["+", "-", "x", "%"]
        for i in range(len(separated)):
            # หากความยาวของ array คือ 1 และเป็น "เครื่องหมาย"
            if len(separated[i]) is 1 and separated[i] in Operator:
                return True
            # หากตัวแรกใน array เป็น "เครื่องหมาย" ที่ไม่ใช่ "เครื่องหมายลบ(-)"
            elif separated[i][0] in Operator and separated[i][0] is not "-":
                return True
            # หากตัวสุดท้ายใน array เป็น "เครื่องหมาย"
            elif separated[i][len(separated[i]) - 1] in Operator:
                return True
            # หากตัวแรกใน array เป็น "เครื่องหมายลบ(-)" แล้วตัวถัดไปเป็น "ศูนย์"
            elif separated[i][0] is "-" and separated[i][1] is "0":
                return True
        return False

    # ตรวจสอบกฏทั้งหมดก่อนจะนำไปคำนวณ
    def rulesCheck(self):
        if not self.__isEquation():
            return "Needs Atlease One Equal(=) in The Equation."
        elif not self.__isLimitedLength():
            return "Can Combined Only 15 Chips in One Equation"
        elif self.__isEqualInBegOrEnd():
            return "This Equation has Equal(=) at the Beginning or The End of The Equation."
        elif self.__AreEqualsJoint():
            return "2 or more Equals(=) Can't be Placed Next to Each Other."
        elif self.__AreOperatorsJoint():
            return "2 or more Operators(+, -, x, %) Can't be Placed Next to Each Other."
        elif self.__AreDivideZero():
            return "The Equation Dividing by Zero(0) Can't be Solved."
        elif self.__have2DigitStaked():
            return "A 2-digit Number Can't be Placed Near Another Number."
        elif self.__have4OrMoreDigit():
            return "Only 3-digit Number or less Can be Placed."
        elif self.__have0AtTheFirst():
            return "A Number with Zero(0) Can't be Placed in Front of Value."
        elif self.__isSignInWrongPlace(super().separateEquation()):
            return "Atlease One Operator(s)(+, -, x, %) is/are in the Wrong Place"
        else:
            return super().adjustSeparated(super().separateEquation())

    



