from flask import Flask
from flask import render_template
from dictionary import object
list_of_stories = object()
sto1 = list_of_stories[0]
sto2 = list_of_stories[1]
sto3 = list_of_stories[2]
sto4 = list_of_stories[3]
sto5 = list_of_stories[4]
sto6 = list_of_stories[5]
sto7 = list_of_stories[6]
sto8 = list_of_stories[7]
sto9 = list_of_stories[8]
sto10 = list_of_stories[9]


app = Flask(__name__)
@app.route("/")
def home(name = None,story2 = None):
    return render_template("main.html",story1 = sto1, story2 = sto2, story3 = sto3,story4 = sto4,story5 = sto5,story6 = sto6,story7 = sto7,story8 = sto8,story9 = sto9,story10 = sto10)

