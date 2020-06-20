import random

class Guesser:
    def __init__(self):
        self.fava_color = "green"


    def guess_fave_color(self):
        print("Step right up and guess my favorite color!")
        response = input("What is your guess?")
        while response != self.fava_color:
            print("Nope, that's not it.")
            response = input("What is your guess?")

        print("You got it!")

    def guess_random_number(self):
        num = self.get_random_num()

        print("I am thinking of number between 1 and 5")

        response = int(input("What number am I thinking of?"))

        while response != num:
            print("Nope, try again")
            response = int(input("What number am I thinking of?"))

        print("You got it!")


    def get_random_num(self):
        return random.randint(1,5)


if __name__ == "__main__":
    g = Guesser()
    g.guess_random_number()
