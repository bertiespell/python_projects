import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, temp, scale, loc')

def main():
    print_header()
    city = input('What city do you want to use? ')
    html = get_html_from_web(city)
    report = get_weather_from_html(html)
    print('The temperature in {} is {} and {} {}'.format(
        report.loc,
        report.cond,
        report.temp,
        report.scale
    ))


def print_header():
    print('------------------------------')
    print('         WEATHER APP')
    print('------------------------------')
    print('')

def get_html_from_web(city):
    url = 'https://www.wunderground.com/weather/gb/{}'.format(city)
    response = requests.get(url)
    # print(response.text[0:250])
    return response.text


def get_weather_from_html(html):
    # cityCss = '.region-content-header h1'
    # weatherScaleCss = '.wu-unit-temperature .wu-label'
    # weatherTempCss = '.wu-unit-temperature .wu-value'
    # weatherConditionCss = '.condition-icon'
    soup = bs4.BeautifulSoup(html, 'html.parser')

    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = clean_text(loc)
    loc = find_city_from_text(loc)
    condition = clean_text(condition)
    temp = clean_text(temp)
    scale = clean_text(scale)
    print(loc, condition, temp, scale)
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def find_city_from_text(txt : str):
    parts = txt.split(',')
    return parts[0]


def clean_text(text : str):
    if not text:
        return text
    text = text.strip()

    return text


if __name__ == '__main__':
    main()