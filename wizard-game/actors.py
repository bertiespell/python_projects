import random


class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, other_creature):
        print('Wizard {} attacks {}'.format(
            self.name,
            other_creature.name
        ))

        my_roll = random.randint(1, 12) * self.level
        creature_roll = other_creature.get_defensive_role()

        print('Wizard roled {} and the creature rolled {}'.format(my_roll, creature_roll))
        if my_roll >= creature_roll:
            return True
        else:
            return False


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return 'Creature {} of level {}'.format(
            self.name, self.level
        )

    def get_defensive_role(self):
        return random.randint(1, 12) * self.level