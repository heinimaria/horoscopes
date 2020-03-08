from bs4 import BeautifulSoup
import requests

url_capricorn = requests.get('https://www.astrology.com/horoscope/daily/capricorn.html')
url_gemini = requests.get('https://www.astrology.com/horoscope/daily/today/gemini.html')
url_cancer = requests.get('https://www.astrology.com/horoscope/daily/cancer.html')
url_pisces = requests.get('https://www.astrology.com/horoscope/daily/pisces.html')


def get_capricorn():
    soup_capricorn = BeautifulSoup(url_capricorn.text, 'html.parser')
    daily_capricorn = soup_capricorn.find('p').get_text()
    return daily_capricorn


def get_cancer():
    soup_cancer = BeautifulSoup(url_cancer.text, 'html.parser')
    daily_cancer = soup_cancer.find('p').get_text()
    return daily_cancer


def get_gemini():
    soup_gemini = BeautifulSoup(url_gemini.text, 'html.parser')
    daily_gemini = soup_gemini.find('p').get_text()
    return daily_gemini


def get_pisces():
    soup_pisces = BeautifulSoup(url_pisces.text, 'html.parser')
    daily_pisces = soup_pisces.find('p').get_text()
    return daily_pisces



