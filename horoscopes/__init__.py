from flask import Flask

app = Flask(__name__)
app.secret_key = "ea6cbad80cc85e506e01c3a8e0f545c7"


from horoscopes import routes
