import glob
import os

import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')

def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print('Sorry, we cant search that location')
        return
    text = get_search_text_from_user()
    if not folder:
        print('Sorry, we cant search for nothing')
        return

    matches = search_folders(folder, text)
    for m in matches:
        print('--------MATCH--------')
        print('file: ' + m.file)
        print('line: {}'.format(m.line))
        print('match: ' + m.text.strip())
        print()


def print_header():
    print('-----------------------------------')
    print('         FILE SEARCHER APP      ')
    print('-----------------------------------')


def get_folder_from_user():
    folder = input('What folder would you like to start searching from? ')
    print(folder)
    if not folder or not folder.strip():
        return None
    if not os.path.isdir(folder):
        print('not dirre')
        return None
    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What text are you searching for?')
    return text


def search_file(item, text):
    with open(item, 'r', encoding='utf-8') as fin:
        line_num = 0
        for line in fin:
            line_num += 1
            print(line)
            if line.lower().find(text) >= 0:
                m = SearchResult(file=item, line=line_num, text=line)
                yield m


def search_folders(folder, text):
    print('Would search {} for {}'.format(folder, text))
    all_matches = []
    items = os.listdir(folder)
    glob.glob(os.path.join(folder, '*'))
    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            matches = (full_item, text)
            all_matches.extend(matches)
        else:
            matches = search_file(full_item, text)
            all_matches.extend(matches)

    return all_matches


if __name__ == '__main__':
    main()
