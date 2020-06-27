class Darkside:
    pass

    force_sensitive = True

    # Will use super later
    # def __init__(self, name, saber_color):
    #     self.name = name
    #     self.saber_color = saber_color

    def __repr__(self):
        return "In the Darkside class"


class Planets:
    def __repr__(self):
        return "In the Planet class"


class Sith(Darkside, Planets):
    def __init__(self, name, saber_color):
        # super().__init__()
        # self.force_choke = force_choke
        self.name = name
        self.saber_color = saber_color

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', '{self.saber_color}')"

    def __str__(self):
        return f"My name is: {self.name} my saber color is: {self.saber_color} Am I force-sensitive: {self.force_sensitive}"


class Accolite(Planets, Darkside):

    force_sensitive = False

    def __init__(self, name, saber_color):
        self.name = name
        self.saber_color = saber_color

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', '{self.saber_color}')"

    def __str__(self):
        return f"My name is: {self.name} my saber color is: {self.saber_color} Am I force-sensitive: {self.force_sensitive}"


if __name__ == '__main__':
    vader = Sith('Darth Vader', 'red')
    # print(vader)
    revan = Accolite('Darth Revan', 'purple')

    print(revan)
    print(repr(vader))
    user = Darkside();
    print(user)
    print(vader)
    print(repr(vader))
    print(Sith.mro())
    print(Accolite.mro())
    print(vader.force_sensitive)
    print(revan.force_sensitive)
    vader.user_armor = True
    print(vader.user_armor)
