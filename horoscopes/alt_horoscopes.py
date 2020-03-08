import requests
from bs4 import BeautifulSoup

cancer_url = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=4')
capricorn_url = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=10')
gemini_url = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=3')
pisces_url = requests.get('https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=12')


def get_alt_cancer():
    soup_cancer = BeautifulSoup(cancer_url.text, 'html.parser')
    alt_cancer = soup_cancer.find('p').get_text()
    return alt_cancer


def get_alt_capricorn():
    soup_capricorn = BeautifulSoup(capricorn_url.text, 'html.parser')
    alt_capricorn = soup_capricorn.find('p').get_text()
    return alt_capricorn


def get_alt_gemini():
    soup_gemini = BeautifulSoup(gemini_url.text, 'html.parser')
    alt_gemini = soup_gemini.find('p').get_text()
    return alt_gemini


def get_alt_pisces():
    soup_pisces = BeautifulSoup(pisces_url.text, 'html.parser')
    alt_pisces = soup_pisces.find('p').get_text()
    return alt_pisces

