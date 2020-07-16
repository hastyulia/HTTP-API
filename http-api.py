import sys
import requests
import argparse

APPID = ""  # Your API key


def get_weather(city, days_count):
    if days_count > 7 or days_count < 1:
        sys.stdout.write('Incorrect days count')
        sys.exit(1)
    r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={APPID}')
    lon = r.json()['coord']['lon']
    lat = r.json()['coord']['lon']
    req = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&appid={APPID}'
    r = requests.get(req)
    for i in range(days_count):
        sys.stdout.write(f"day: {r.json()['daily'][i]['temp']['day']} °C\r\n")
        sys.stdout.write(f"night: {r.json()['daily'][i]['temp']['night']} °C\r\n")
        sys.stdout.write(f"humidity: {r.json()['daily'][i]['humidity']}\r\n")
        sys.stdout.write('\r\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='http-api.py',
                                     description='get weather')
    parser.add_argument('-c', '--city', type=str, default='Moscow')
    parser.add_argument('-r', '--range', type=int, default=1)
    args = parser.parse_args()
    try:
        get_weather(args.city, args.range)
    except KeyboardInterrupt:
        sys.exit(0)
