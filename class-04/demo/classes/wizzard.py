class PlayerCharacter:

    # Class Object
    membership = True

    def __init__(self, name, energy):
        """
        This is my docstring
        """
        self.name = name
        self.is_tired = False
        self.energy = energy

    def __repr__(self):
        return {'name':{self.name}, 'is_tired':{self.is_tired}, 'energy':{self.energy}}

    def __str__(self):
        return f'PlayerCharacter(name={self.name} is_tired={self.is_tired} energy={self.energy})'

    def running(self):
        print(f'{self.name} is running!')
        self.is_tired = True

    def jumping(self):
        """
        Doc String
        :return:
        """
        if self.is_tired == False:
            print(f'Was not tired, so i jumped')
            self.is_tired = True
        elif self.is_tired == True:
            print(f'I was tired already')


class Wizzard(PlayerCharacter):

    def spells(self):
        print(f'{self.name} has 20 spells to cast')


class Archer(PlayerCharacter):

    def arrow_attack(self):
        print(f'{self.name} has shot you')


# player1 = Wizzard('Merlin', 100)
player2 = Archer('Oliver', 100)
# print(player1.energy)
# player2.arrow_attack()
# print(player1.running())
# player1.running()
# player1.jumping()
print(player2)
# print(player2.
