import os


def main():
    print_header()
    filename = get_file_data()
    data = load_file(filename)
    query_data(data)
    print(filename)

def print_header():
    print('-------------------------------')
    print('      REAL ESTATE DATA APP')
    print('-------------------------------')


def get_file_data():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        header = fin.readline()
        print('Found Header: ' + header)

        lines = []
        for line in fin:
            line_data = line.strip().split(',')
            lines.append(line_data)

        print(lines[:5])


def query_data(query):
    pass



if __name__ == '__main__':
    main()