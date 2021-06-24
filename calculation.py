from chip import Chip
from rules import Rules

class Calculation (Rules):
    def __init__(self, chips) -> None:
        super().__init__(chips)

    # แปลงค่า String ให้เป็นตัวเลข ทั้งแบบ float และ integer
    def __stringtoFloatOrInt (self, string):
        return float(string) if '.' in string else int(string)

    # คำนวณระหว่างตัวเลข 2 ตัว
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

    # รวมผลทั้งสมการเดียว 
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
            score = score + (super().getChips())[j].getScore()
        return "The Answer is Correct. You got " + str(score) + " score(s)"

    # คำนวณรวม 
    def mainCalculation(self):

        calculateList = super().rulesCheck()

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


# สำหรับ dubug การเช็คกฏ
inputList = ["-", "1", "6", "%", "4", "+", "0", "x", "3",  "=", "-", "4"]
input = []
for i in range(len(inputList)):
    input.append(Chip(inputList[i]))
_34 = Calculation(input)
print(_34.mainCalculation())