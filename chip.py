class Chip:

    __ONE_POINT = ["0", "1", "2", "3", "+/-", "x/%", "="]
    __TWO_POINT = ["4", "5", "6", "7", "8", "9", "+", "-", "x", "%"]
    __THREE_POINT = ["10", "12"]
    __FOUR_POINT = ["11", "14", "15", "16", "18"]
    __FIVE_POINT = ["20"]
    __SIX_POINT = ["13", "17"]
    __SEVEN_POINT = ["19"]

    def __init__(self, value):
        self.__VALUE = value
        self.__SCORE = self.__setScore(self.__VALUE)

    def __setScore(self, value):
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

    def getScore(self):
        return self.__SCORE

    def getValue(self):
        return self.__VALUE

    def __eq__(self, o: object) -> bool:
        if self.getValue() == o.getValue():
            return True
        else: 
            return False

    def __str__(self) -> str:
        return str(self.getValue()) + "(" + str(self.getScore()) +  ")"

# a = Chip("4")
# print(a)