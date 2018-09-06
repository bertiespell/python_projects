import os


def load(name):
    """
    This method creats and loads a new journal

    :param name: The base name of the journal to load
    :return: A new jornal data structure populated with the file data
    """
    data = []
    filename = get_full_path(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry)

    return data


def save(name, journal_data):
    filename = get_full_path(name)
    print('saving to....  : {}'.format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_path(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)