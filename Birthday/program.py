import datetime

def print_header():
    print('-----------------------')
    print('   Days until birthday')
    print('-----------------------')


def get_birthday_from_user():
    print('when were you born')
    year = input('year YYYY: ')
    month = input('month MM: ')
    day = input('day DD: ')
    birthday = datetime.date(int(year), int(month), int(day))
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_information(number_of_days):
    if number_of_days < 0:
        print('you had you birthday {} number of days ago'.format(-number_of_days))
    elif number_of_days > 0:
        print('your birthday is in {} number of days'.format(number_of_days))


def main():
    print_header()
    bday = get_birthday_from_user()
    now = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_information(number_of_days)


main()