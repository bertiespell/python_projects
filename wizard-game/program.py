import random
import time

from actors import Wizard, Creature


def print_header():
    print('------------------------------')
    print('          WIZARD GAME')
    print('------------------------------')


def game_loop():


    creatures = [
        Creature('Toad', 1),
        Creature('Bat', 5),
        Creature('Tiger', 12),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000),
    ]

    hero = Wizard('Gandolf', 27)



    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared...'.format(active_creature.name, active_creature.level))

        cmd = input("Do you [a]ttack, [r]unaway or [l]ook around? ")

        if cmd == 'a':
            print('attack')
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('Wizard was defeated and must take time to recover')
                time.sleep(5)
        elif cmd == 'l':
            print('The wizard {} takes a look around and sees...'.format(hero.name))
            for creature in creatures:
                print(creature)
        elif cmd == 'r':
            print('run')
        else:
            print('K, exiting')
            break

        if not creatures:
            print('You defeated all the creatures!')
            break

def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()

