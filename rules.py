from chip import Chip


class Rules():
    def __init__(self, chips) -> None:
        self.__chips = chips

    # จำนวนเบี้ยที่ใช้ในการคำนวน
    def getLength(self):
        return len(self.__chips)

    # แยกประเภทของเบี้ย
    def getTypeofEachChips(self):
        typeofChips = []
        for i in range(self.getLength()):
            typeofChips.append(self.__chips[i].getType())
        return typeofChips

    # (กฏ) มี เท่ากับ อยู่ในสมการหรือไม่
    def __isEquation(self):
        return Chip("=") in self.__chips

    # (กฏ) มีจำนวนเบี้ยเกิน 15 ตัวหรือไม่
    def __isLimitedLength(self):
        return 0 < len(self.__chips) <= 15

    # (กฏ) มี "เท่ากับ" อยู่ต้นหรือท้ายสุดของสมการหรือไม่
    def __isEqualInBegOrEnd(self):
        return self.__chips[0].getValue() is "=" \
            or self.__chips[self.getLength() - 1].getValue() is "="

    # (กฏ) มี "เท่ากับ" อยู่ติดกันหรือไม่
    def __AreEqualsJoint(self):
        for i in range(self.getLength() - 1):
            if self.__chips[i].getType() is "Equal" \
                    and self.__chips[i+1].getType() is "Equal":
                return True
        return False

    # (กฏ) มี "เครื่องหมาย" อยู่ติดกันหรือไม่
    def __AreOperatorsJoint(self):
        for i in range(self.getLength() - 1):
            if self.__chips[i].getType() is "Operator" \
                    and self.__chips[i+1].getType() is "Operator":
                return True
        return False

    # (กฏ) มีการ "หารด้วยศูนย์" เกิดขึ้นหรือไม่
    def __AreDivideZero(self):
        for i in range(self.getLength() - 1):
            if self.__chips[i].getValue() is "%" \
                    and self.__chips[i+1].getValue() is "0":
                return True
        return False

    # (กฏ) "เลข 2 หลัก" อยู่ติดกับเลขตัวอื่นหรือไม่ 
    def __have2DigitStaked(self):
        _2DigitIndex = []
        number = ["1_digit", "2_digit"]

        # เก็บ index ที่่มี "เลข 2 หลัก"
        for index in range(self.getLength()):
            if self.__chips[index].getType() is "2_digit":
                _2DigitIndex.append(index)

        # หากมีมากกว่า 1 ตัว จะเข้าเงื่อนไขตรวจสอบนี้
        if len(_2DigitIndex) > 0:
            for i in range(len(_2DigitIndex)):
                # อยู่ index แรก เช็คตัวหลังอย่างเดียว
                if _2DigitIndex[i] is 0: 
                    if self.__chips[1].getType() in number:
                        return True
                # อยู่่ index สุดท้าย เช็คตัวหน้าอย่างเดียว
                elif _2DigitIndex[i] is self.getLength() - 1:
                    if self.__chips[_2DigitIndex[i] - 1].getType() in number:
                        return True
                # อยู่่ index อื่น เช็คตัวหน้าหลัง
                else:
                    if self.__chips[_2DigitIndex[i] + 1].getType() in number \
                            and self.__chips[_2DigitIndex[i] - 1].getType() in number:
                        return True
        return False

    # (กฏ) "เลข 1 หลัก" อยู่ติดกันเกิน 3 ตัวหรือไม่  
    def __have4OrMoreDigit(self):
        number = self.__separateString("1_digit")
        for k in range(len(number)):
            if len(number[k]) > 3:
                return True
        return False

    # (กฏ) "0" อยู่ด้านหน้าของ "เลข 1 หลัก" ที่ติดกันอยู่หรือไม่ 
    def __have0AtTheFirst(self):
        number = self.__separateString("1_digit")
        for k in range(len(number)):
            if len(number[k]) in [2, 3] and number[k][0] is '0':
                return True
        return False

    # (กฏ) "เครื่องหมาย" อยู่ในตำแหน่งที่ผิดปกติหรือไม่ 
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

    # (แยก) array ระหว่าง "ตัวเลข" หรือ "เท่ากับ" สำหรับในการคำนวณต่อไป *
    def __separateString(self, type):
        string = ""
        number = []
        condition = []
        # เก็บค่า Boolean ใน array 
        for k in range(self.getLength()):
            if type is "1_digit":
                condition.append(self.__chips[k].getType() is type)
            elif type is "Equal":
                condition.append(self.__chips[k].getType() is not type)
        # รวมค่าแล้ว push ใน array ใหม่
        for i in range(self.getLength()):
            if condition[i]:
                string = string + self.__chips[i].getValue()
            else:
                if string is not "":
                    number.append(string)
                    string = ""
        # push ขั้นสุดท้าย
        if string is not "":
            number.append(string)
        return number

    # (แยก) array "เท่ากับ" สำหรับในการแยกแต่ละสมการออกจากกัน 
    def __separateEquation(self):
        return self.__separateString("Equal")

    # (แยก) array "เท่ากับ" สำหรับในการคำนวณต่อไป และรวม "ตัวเลข 1 หลัก" ที่ติดกันเข้าด้วยกันเป็นเลขเดียว
    def __adjustSeparated(self, separated):
        Operator = ["+", "-", "x", "%"]
        temp = []
        string = ""
        for i in range(len(separated)):
            for j in range(len(separated[i])):
                # หากเป็น "ตัวเลข" ให้รวมกันก่อนใน String 
                if separated[i][j].isnumeric():
                    string = string + separated[i][j]
                # หากตัวแรกเป็น "เครื่องหมายลบ" ใส่เข้าไปได้เลย
                elif j is 0 and separated[i][j] is "-":
                    temp.append(separated[i][j])
                # หากเป็น "เครื่องหมาย" ใส่ String เข้าไปและใส่ "เครื่องหมาย" เข้าไปด้วย
                elif separated[i][j] in Operator and string is not "":
                    temp.append(string)
                    temp.append(separated[i][j])
                    string = ""
            # เพิ่มขั้นตอนสุดท้าย
            if string is not "":
                temp.append(string)
                string = ""
            separated[i] = temp
            temp = []
        return separated

    # ตรวจสอบกฏทั้งหมดก่อนจะนำไปคำนวณ
    def __rulesCheck(self):
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
        elif self.__isSignInWrongPlace(self.__separateEquation()):
            return "Atlease One Operator(s)(+, -, x, %) is/are in the Wrong Place"
        else:
            return self.__adjustSeparated(self.__separateEquation())

    # (คำนวณ) แปลงค่า String ให้เป็นตัวเลข ทั้งแบบ float และ integer
    def __stringtoFloatOrInt (self, string):
        return float(string) if '.' in string else int(string)

    # (คำนวณ) คำนวณระหว่างตัวเลข 2 ตัว
    def __operation(self, first, second, sign):
        
        # แปลง String เป็น integer หรือ float
        firstNum = self.__stringtoFloatOrInt(first)
        secondNum = self.__stringtoFloatOrInt(second)

        if sign is "+":
            result = str(firstNum + secondNum)
        elif sign is "-":
            result = str(firstNum - secondNum)
        elif sign is "x":
            result = str(firstNum * secondNum)
        elif sign is "%":
            result = str(firstNum / secondNum)

        return str(self.__stringtoFloatOrInt(result))

    # (คำนวณ) รวมผลทั้งสมการเดียว 
    def __decreaseCalculationIndex(self, list, firstSign, secondSign):
        temp = []
        # ทำการแทนที่ผลลัพท์ที่ได้ลงไปใน index ของ "เครื่องหมาย" แล้วแปลง index ด้านข้างเป็น ""
        for j in range(len(list)):
            if list[j] in [firstSign, secondSign]:
                if list[j] is firstSign:
                    list[j] = self.__operation(list[j-1], list[j+1], firstSign)
                elif list[j] is secondSign:
                    list[j] = self.__operation(list[j-1], list[j+1], secondSign)
                list[j-1] = ""
                list[j+1] = ""
        # คัดมาเฉพาะ index ที่ไม่ใช่ "" 
        for j in range(len(list)):
            if list[j] is not "":
                temp.append(list[j])
        return temp

    # ตรวจสอบความถูกต้องของคำตอบสุดท้ายของแต่ละสมการ รวมไปถึงหาคะแนนที่ได้จากทั้งสมการ
    def __getScore(self, result):
        
        # หากคำตอบผิด
        for i in range(len(result) - 1):
            if result[i] != result[i+1]:
                return "The Answer is Not Correct"
        # หากคำตอบถูกต้อง
        score = 0
        for j in range(self.getLength()):
            score = score + self.__chips[j].getScore()
        return "The Answer is Correct. You got " + str(score) + " score(s)"

    # คำนวณรวม 
    def calculation(self):

        calculateList = self.__rulesCheck()

        if type(calculateList) is not str:
            for i in range(len(calculateList)):
                # รวม "เครื่องหมายลบ" กับ "ตัวเลขถัดไป"
                if calculateList[i][0] is "-":
                    calculateList[i][1] = str(
                        int(calculateList[i][1]) * (-1))
                    calculateList[i].pop(0)
                # ทำการ คูณ หาร ก่อน
                calculateList[i] = self.__decreaseCalculationIndex(
                    calculateList[i], "x", "%")
                # ทำการ บวก ลบ ทีหลัง
                calculateList[i] = self.__decreaseCalculationIndex(
                    calculateList[i], "+", "-")
            # ถอด index ซ้อนทั้งหมดออก แล้วเก็บแค่ค่าที่ได้มาเท่านั้น
            for j in range(len(calculateList)):
                calculateList[j] = self.__stringtoFloatOrInt(calculateList[j][0])
            
            return self.__getScore(calculateList)
        
        return calculateList

    # .toString()
    def __str__(self) -> str:
        string = ""
        for i in range(self.getLength()):
            string = string + "[" + str(self.__chips[i]) + "]"
        return string


# สำหรับ dubug การเช็คกฏ
inputList = ["-", "1", "6", "%", "4", "+", "0", "x", "3",  "=", "-", "4"]
input = []
for i in range(len(inputList)):
    input.append(Chip(inputList[i]))
_34 = Rules(input)
# print(_34)
# print(_34.getTypeofEachChips())
print(_34.calculation())
