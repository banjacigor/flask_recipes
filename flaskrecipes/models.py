from datetime import datetime
from flaskrecipes import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    recipes = db.relationship("Recipe", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    ingredientNumber = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    ingredients = db.relationship("Ingredient", backref="ingr", lazy=True)
    ratings = db.relationship("Rating", backref="rat", lazy=True)

    def __repr__(self):
        return f"Recipe('{self.title}', '{self.date_posted}')"


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable=False)

    def __repr__(self):
        return f"Ingredient('{self.name}')"


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=True)
    who_rated = db.Column(db.String(20), nullable=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id"), nullable=False)

    def __repr__(self):
        return f"Rating('{self.rating}')"
