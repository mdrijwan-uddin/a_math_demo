# from bag import Bag
# from rack import Rack
# import random

# # print(random.randint(1, 100))

# class Draw_Phase(Bag, Rack):
#     def __init__(self) -> None:
#         super().__init__()

class First():
    def __init__(self):
        print ("first")

class Second(First):
    def __init__(self):
        print ("second")

class Third(First):
    def __init__(self):
        print ("third")

class Fourth(Second, Third):
    def __init__(self):
        super(Fourth, self).__init__()
        print ("that's it")

print(Fourth.__mro__)


# class First(object):
#     def __init__(self):
#         print ("first")

# class Second(object):
#     def __init__(self):
#         print ("second")

# class Third(First, Second):
#     def __init__(self):
#         super(Third, self).__init__()
#         super(Second, self).__init__()
#         print ("that's it")
# Third()
