from chip_collector import Chip_Collector
from chip import Chip



A_MATH_MAX_CHIPS_IN_RACK = 8

TOTAL_CHIP_TYPE = [
    Chip("0"), Chip("1"), Chip("2"), Chip("3"), Chip("4"),
    Chip("5"), Chip("6"), Chip("7"), Chip("8"), Chip("9"),
    Chip("10"), Chip("11"), Chip("12"), Chip("13"), Chip("14"),
    Chip("15"), Chip("16"), Chip("17"), Chip("18"), Chip("19"),
    Chip("20"), Chip("+"), Chip("-"), Chip("+/-"), Chip("x"),
    Chip("%"), Chip("x/%"), Chip("="), Chip("Blank")
]

TRADITIONAL_CHIP_COUNTS = [
    Chip_Collector(Chip("0"), 5), Chip_Collector(
        Chip("1"), 6), Chip_Collector(Chip("2"), 6),
    Chip_Collector(Chip("3"), 5), Chip_Collector(
        Chip("4"), 5), Chip_Collector(Chip("5"), 4),
    Chip_Collector(Chip("6"), 4), Chip_Collector(
        Chip("7"), 4), Chip_Collector(Chip("8"), 4),
    Chip_Collector(Chip("9"), 4), Chip_Collector(
        Chip("10"), 2), Chip_Collector(Chip("11"), 1),
    Chip_Collector(Chip("12"), 2), Chip_Collector(
        Chip("13"), 1), Chip_Collector(Chip("14"), 1),
    Chip_Collector(Chip("15"), 1), Chip_Collector(
        Chip("16"), 1), Chip_Collector(Chip("17"), 1),
    Chip_Collector(Chip("18"), 1), Chip_Collector(
        Chip("19"), 1), Chip_Collector(Chip("20"), 1),
    Chip_Collector(Chip("+"), 4), Chip_Collector(Chip("-"),
                                                 4), Chip_Collector(Chip("+/-"), 5),
    Chip_Collector(Chip("x"), 4), Chip_Collector(
        Chip("%"), 4), Chip_Collector(Chip("x/%"), 4),
    Chip_Collector(Chip("="), 11), Chip_Collector(Chip("Blank"), 4),
]
