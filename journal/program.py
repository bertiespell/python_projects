def main():
    print_header()
    run_event_loop()
import journal


def print_header():
    print('------------------------')
    print('    Journal')
    print('------------------------')

def run_event_loop():
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name) # this style is refereed to as namespaces.....
    print('What do you want to do with your jounral?')
    while cmd != 'x' and cmd:
        cmd = input('[L]ist, [A]dd, [e[X]it')
        cmd = cmd.lower().strip()
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry we dont understand '{}'.".format(cmd))

    print('Done, goodbye')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal Entries...')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print("* [{}]{}".format(idx, entry))


def add_entries(data):
    text = input('Type your entry')
    journal.add_entry(text, data)
    # journal.add_entry(text)  use alt+ enter to autocreate methods


print('__file__ ' + __file__)
print('__name__ ' + __name__)

if __name__ == '__main__':
    main()
