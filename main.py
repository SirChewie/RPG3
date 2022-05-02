
class Character:
    def __init__(self):
        # Damage resist
        self.res = .01
        # Attack
        self.atk = 2
        # Max health
        self.hmax = 10
        # current health
        self.hcurr = 10
        # Armor
        self.armor = 0
        # Magic Shield
        self.mshield = 0
        # Max Mana
        self.mmax = 1
        # current mana
        self.mcurr = 1


class Player(Character):
    def __init__(self):
        super().__init__()


class Loot:
    def __init__(self):
        self.atk = 0
        self.res = 0
        self.mshield = 0
        self.armor = 0
        self.mmax = 0
        self.hmax = 0
        self.iswearing = False

    def is_wearing(self, p):
        """Checks if Character is wearing this item if so it applies stats of item"""
        # Item's attributes
        b = list(self.__dict__.keys())
        # Player's attributes
        p = list(p.__dict__.keys())
        # Filtered list of attributes
        fl = filter(lambda z: z in b, p)

        # if wearing apply stats
        if self.iswearing:
            for x in fl:
                print(x)
        # if not don't apply stats
        else:
            pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # main loop
    p1 = Player()
    print(p1.atk)
    l1 = Loot()
    l1.iswearing = True
    l1.is_wearing(p1)
