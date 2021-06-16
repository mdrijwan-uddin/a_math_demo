import total_ruled_chip as rule
import random


class Rack:
    __MAX_CHIPS = rule.A_MATH_MAX_CHIPS_IN_RACK

    def __init__(self) -> None:
        self.__chipsInRack = []

    def __str__(self) -> str:
        return (self.__chipsInRack)


print(random.randint(1, 100))
