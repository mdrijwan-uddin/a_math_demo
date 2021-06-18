from chip_collector import Chip_Collector

# setup เฉยๆ
# จำนวนตัวเบี้ยสูงสุดที่อยู่บนแป้นวาง
A_MATH_MAX_CHIPS_IN_RACK = 8

# จำนวนตัวเบี้ยของแต่ละตัว
TRADITIONAL_CHIP_COUNTS = [
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


# -----------------test data------------------
# for i in range(len(TRADITIONAL_CHIP_COUNTS)):
#     print(TRADITIONAL_CHIP_COUNTS[i])
