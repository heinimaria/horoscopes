from horoscopes import app
from flask import Flask, render_template, url_for, request
from horoscopes.scraper import get_capricorn, get_cancer, get_gemini, get_pisces
from horoscopes.alt_horoscopes import get_alt_cancer, get_alt_capricorn, get_alt_gemini, get_alt_pisces


@app.route('/')
def home():
    return render_template('home.html', title='Team UK Daily Horoscopes')


@app.route('/capricorn')
def capricorn():
    text = get_capricorn()
    alt_text = get_alt_capricorn()
    return render_template('capricorn.html', text=text, alt_text=alt_text, title='Capricorn')


@app.route('/cancer')
def cancer():
    text = get_cancer()
    alt_text = get_alt_cancer()
    return render_template('cancer.html', text=text, alt_text=alt_text, title='Cancer')


@app.route('/gemini')
def gemini():
    text = get_gemini()
    alt_text = get_alt_gemini()
    return render_template('gemini.html', text=text, alt_text=alt_text, title='Gemini')


@app.route('/pisces')
def pisces():
    text = get_pisces()
    alt_text = get_alt_pisces()
    return render_template('pisces.html', text=text, alt_text=alt_text, title='Pisces')
