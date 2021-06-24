

class ChipManaging:
    def __init__(self, chips) -> None:
        self.__chips = chips

    # ตัวเบี้ยที่ใช้ในการต่อสมการ
    def getChips(self):
        return self.__chips

    # จำนวนเบี้ยที่ใช้ในการคำนวน
    def getLength(self):
        return len(self.__chips)

    # แยกประเภทของเบี้ย
    def getTypeofEachChips(self):
        typeofChips = []
        for i in range(self.getLength()):
            typeofChips.append(self.__chips[i].getType())
        return typeofChips

    # array ระหว่าง "ตัวเลข" หรือ "เท่ากับ" สำหรับในการคำนวณต่อไป *
    def separateString(self, type):
        string = ""
        number = []
        condition = []
        # เก็บค่า Boolean ใน array
        for k in range(self.getLength()):
            if type is "1_digit":
                condition.append(self.getChips()[k].getType() is type)
            elif type is "Equal":
                condition.append(self.getChips()[k].getType() is not type)
        # รวมค่าแล้ว push ใน array ใหม่
        for i in range(self.getLength()):
            if condition[i]:
                string = string + self.getChips()[i].getValue()
            else:
                if string is not "":
                    number.append(string)
                    string = ""
        # push ขั้นสุดท้าย
        if string is not "":
            number.append(string)
        return number

    # array "เท่ากับ" สำหรับในการแยกแต่ละสมการออกจากกัน
    def separateEquation(self):
        return self.separateString("Equal")

    # array "เท่ากับ" สำหรับในการคำนวณต่อไป และรวม "ตัวเลข 1 หลัก" ที่ติดกันเข้าด้วยกันเป็นเลขเดียว
    def adjustSeparated(self, separated):
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
