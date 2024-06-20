from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///airbnb.db"  # Replace with your database URI
)
db = SQLAlchemy(app)


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date_range = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)


@app.route("/")
def home():
    properties = Property.query.all()
    return render_template("index.html", properties=properties)


if __name__ == "__main__":
    app.run(debug=True)
