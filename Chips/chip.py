# คลาสสำหรับการเก็บเบี้ย


class Chip:

    __ONE_POINT = ["0", "1", "2", "3", "+/-", "x/%", "="]
    __TWO_POINT = ["4", "5", "6", "7", "8", "9", "+", "-", "x", "%"]
    __THREE_POINT = ["10", "12"]
    __FOUR_POINT = ["11", "14", "15", "16", "18"]
    __FIVE_POINT = ["20"]
    __SIX_POINT = ["13", "17"]
    __SEVEN_POINT = ["19"]

    def __init__(self, value):
        self.__VALUE = str(value)
        self.__SCORE = self.__setScore__(self.__VALUE)
        self.__TYPE = self.__setType__(self.__VALUE)

    # ระบุคะแนนของเบี้ยหลังจากที่ได้ค่าของเบี้ยมาทันที
    def __setScore__(self, value):
        if value in self.__ONE_POINT:
            return 1
        elif value in self.__TWO_POINT:
            return 2
        elif value in self.__THREE_POINT:
            return 3
        elif value in self.__FOUR_POINT:
            return 4
        elif value in self.__FIVE_POINT:
            return 5
        elif value in self.__SIX_POINT:
            return 6
        elif value in self.__SEVEN_POINT:
            return 7
        else:
            return 0

    # ไว้ใช้แยกประเภทของเบี้ย (ระบุทันที)
    def __setType__(self, value):
        if value.isnumeric():
            if 0 <= int(value) <= 9:        # ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                return "1_digit"
            elif 10 <= int(value) <= 20:    # ["10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
                return "2_digit"
            else:
                return None
        elif value in ["+", "-", "x", "%", "+/-", "x/%", ]:
            return "Operator"
        elif value is "=":
            return "Equal"
        elif value is "Blank":
            return "Blank"
        else:
            return None

    def getValue(self):
        return self.__VALUE

    def getScore(self):
        return self.__SCORE

    def getType(self):
        return self.__TYPE

    # ใช้สำหรับเช็คเบี้ยเท่ากันหรือเปล่า
    def __eq__(self, o: object) -> bool:
        return self.getValue() == o.getValue()

    # .toString()
    def __str__(self) -> str:
        return str(self.getValue())


# -----------------test data------------------
# a = Chip("4")
# b = Chip("4")
# print(a)
# print(b)
# print(a == b)
