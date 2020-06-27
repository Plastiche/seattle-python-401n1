from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    def __init__(self, roll_function=None):

        self.roll_function = roll_function or GameLogic.roll_dice
        self.banker = Banker()

    def play(self):
        print("Welcome to Game of Greed")
        response = input("Wanna play?")

        if response == "n":
            print("OK. Maybe another time")
        else:
            round = 1
            num_dice = 6

            while True:
                print(f"Starting round {round}")
                print(f"Rolling {num_dice} dice...")

                roll = self.roll_function(num_dice)

                vals_as_strings = [str(i) for i in roll]

                pretty_roll = ",".join(vals_as_strings)

                # print(pretty_roll)

                response = input("Enter dice to keep (no spaces), or (q)uit: ")

                if response == "q":
                    pass
                else:
                    digits = tuple(int(char) for char in response)
                    num_dice -= len(digits)
                    score_for_kept_dice = GameLogic.calculate_score(digits)
                    self.banker.shelf(score_for_kept_dice)
                    print(
                        f"You have {score_for_kept_dice} unbanked points and {num_dice} dice remaining"
                    )

                    roll_again_response = input(
                        "(r)oll again, (b)ank your points or (q)uit "
                    )

                    if roll_again_response == "b":
                        banked = self.banker.bank()
                        print(f"You banked {banked} points in round {round}")
                        print(f"Total score is {self.banker.balance} points")
                        round += 1
                        num_dice = 6
                    elif roll_again_response == "q":
                        break

            print(f"Total score is {total_score} points")
            print(f"Thanks for playing. You earned {total_score} points")


# Welcome to Game of Greed
# Wanna play?y
# Starting round 1
# Rolling 6 dice...
# 5,2,3,4,6,6
# Enter dice to keep (no spaces), or (q)uit: 5
# You have 50 unbanked points and 5 dice remaining
# (r)oll again, (b)ank your points or (q)uit b
# You banked 50 points in round 1
# Total score is 50 points
# Starting round 2
# Rolling 6 dice...
# 6,5,1,6,6,6
# Enter dice to keep (no spaces), or (q)uit: q
# Total score is 50 points
# Thanks for playing. You earned 50 points

if __name__ == "__main__":
    game = Game()
    game.play()
