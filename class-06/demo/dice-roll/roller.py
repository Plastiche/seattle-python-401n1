import random
from collections import Counter

class GameLogic:
    # @staticmethod
    # def roll_dice(count):
    #     return random.randint(0,6)

    @staticmethod
    def roll_one():
        return random.randint(1,6)


    # [3,5,6]
    # (5,6,7)
    # []
    # tuple()
    @staticmethod
    def calculate_score(rolled_dice): # tuple of rolled dice and/or selected dice
        # 1
        # 1 1
        # 1 1 1

        fake_rolled_dice = (1,1)

        ctr = Counter(fake_rolled_dice)

        print(ctr)



if __name__ == "__main__":
    # fake_rolled_dice = (1,1,5)
    fake_rolled_dice = (3,3,2,2,4,4)
    fake_rolled_dice = (3,3,3,2,4,4)
    fake_rolled_dice = (1,3,2,4,6,5)
    fake_rolled_dice = (5,5,5,1,1)

    ctr = Counter(fake_rolled_dice)

    print(dir(ctr))
