from flask import Flask, render_template, flash, redirect, url_for
from forms import RegistrationForm, LoginForm
from flask_wtf import CSRFProtect


from dotenv import load_dotenv

load_dotenv()
import os


app = Flask(__name__)
csrf = CSRFProtect(app)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


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


if __name__ == "__main__":
    app.run(debug=True)