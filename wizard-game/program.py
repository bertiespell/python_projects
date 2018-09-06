import random

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
        elif cmd == 'l':
            print('look around')
        elif cmd == 'r':
            print('run')
        else:
            print('K, exiting')
            break

def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()

