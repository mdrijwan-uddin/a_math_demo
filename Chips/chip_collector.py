# คลาสที่เก็บจำนวนของเบี้ย เหมือนเป็น object หลอก ๆ เพราะเกม a-math ของจริงไม่มีตัวนี้อยู่
from chip import Chip


class ChipCollector(Chip):
    
    def __init__(self, chipValue, quantity) -> None:
            super().__init__(chipValue)  # สร้างเบี้ยขึ้นมา
            self.__MAX_QUANTITY = self.__quantity = int(quantity)

    # เพิ่มจำนวนเบี้ย
    def increaseQuantity(self):
        if (self.__quantity < self.__MAX_QUANTITY):
            self.__quantity = self.__quantity + 1

    # ลดจำนวนเบี้ย
    def decreaseQuantity(self):
        if(self.__quantity > 0):
            self.__quantity = self.__quantity - 1

    # รับจำนวนเบี้ยสูงสุด
    def getMaxQuantity(self):
        return self.__MAX_QUANTITY

    # รับตัวเบี้ยใช้ไว้สำหรับเปรียบเทียบกันระหว่าง object
    def getChip(self):
        return super()

    # รับตัวเบี้ยใช้ไว้สำหรับเปรียบเทียบกันระหว่าง string
    def getChipValue(self):
        return super().__str__()

    def getQuantity(self):
        return self.__quantity

    # .toString()
    def __str__(self) -> str:
        return "Value: " + str(super().__str__()) + "\tQuantity: " + str(self.__quantity)
