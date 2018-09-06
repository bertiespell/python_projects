import os
import cats_service

def download_cats(folder):
    cat_count = 8
    for i in range(1, cat_count+1):
        name = 'lolcat_{}'.format(i)
        print('Dowloading cat' + name)
        print(folder)
        cats_service.get_cat(folder, name)


def main():
    print_header()
    folder = get_or_create_output_folder()
    download_cats(folder)



def print_header():
    print('------------------------------')
    print('            LOL CATS    ')
    print('------------------------------')


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cats'
    fullpath = os.path.join(base_folder, folder)

    if not os.path.exists(fullpath) or not os.path.isdir(fullpath):
        print('Creating new directory at {}'.format(fullpath))
        os.mkdir(fullpath)

    return fullpath


if __name__ == '__main__':
    main()