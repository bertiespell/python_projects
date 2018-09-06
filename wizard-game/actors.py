import random



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


class Wizard(Creature):
    def attack(self, other_creature):
        print('Wizard {} attacks {}'.format(
            self.name,
            other_creature.name
        ))

        my_roll = self.get_defensive_role()
        creature_roll = other_creature.get_defensive_role()

        print('Wizard roled {} and the creature rolled {}'.format(my_roll, creature_roll))
        if my_roll >= creature_roll:
            return True
        else:
            return False


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breathes_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breathes_fire = breathes_fire

    def get_defensive_role(self):
        #  here we can use the base class to get the defensive roll code
        baseroll = super().get_defensive_role()
        fire_modifier = 5 if self.breathes_fire else 1
        scale_modifier =  self.scaliness / 10
        # fire_modifier = VALUE_IF_TRUE if CONDITIONAL else VALUE_IF_CALSE
        return baseroll * fire_modifier * scale_modifier


class SmallAnimal(Creature):
    # this replaces and overwrites the method in Creature
    def get_defensive_role(self):
        #  here we can use the base class to get the defensive roll code
        baseroll = super().get_defensive_role()
        return baseroll / 2