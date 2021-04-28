from flaskrecipes.models import User, Recipe
from flaskrecipes import app
from flaskrecipes.forms import RegistrationForm, LoginForm
from flask import render_template, flash, redirect, url_for

posts = [
    {
        "author": "John Doe",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 23, 2021",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 24, 2021",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # WILL BE REMOVED WITH NEXT PUSH (DB CREATED)
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password.")
    return render_template("login.html", title="Login", form=form)
