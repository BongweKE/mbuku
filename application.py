import os, json
import requests



from flask import Flask,render_template , request, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
# res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "3qfqwwHp1C9JIXkkIKfMg", "isbns": "0593192575"})
# https://www.goodreads.com/book/show/50.xml?key=3qfqwwHp1C9JIXkkIKfMg
#
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/fetchLogin",  methods=["GET", "POST"])
def fetchLogin():
    return render_template("login.html")



@app.route("/fetchSignup",  methods=["GET", "POST"])
def fetchSignup():
    return render_template("signup.html")

@app.route("/home")
def homepage():
    return render_template("homepage.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/book/<int:isbn>")
def book(isbn):

    url = (f"https://www.goodreads.com/book/isbn/{isbn}?format=json&user_id=116241268")
    res = requests.get(url)
    json_data = res.json()
    template = json_data['reviews_widget']
    return render_template("book.html" , isbn=isbn)

@app.route("/mbuku/<int:isbn>")
def my_book(isbn):
    url = (f"https://www.goodreads.com/book/isbn/{isbn}?format=json&user_id=116241268")
    res = requests.get(url)
    json_data = res.json()
    template = json_data['reviews_widget']
    return template

@app.route("/mbuku/rate/<int:isbn>")
def rate(isbn):
    return render_template("rate.html")
