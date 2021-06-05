from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import ML
from config import usr, pwd


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = f"mongodb+srv://{usr}:{pwd}@cluster0.iseao.mongodb.net/cancer_db?authSource=admin&replicaSet=atlas-6yeevs-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
mongo = PyMongo(app)

@app.route("/")
def index():

    # Use the 'cancer_db' database from Mongo
    db = mongo.cancer_db
    cancer_dict = db.breast_data.find()
    results = ML.cancer_survival(cancer_dict)
    return render_template("index.html", data=results)

@app.route("/Visuals")
def visuals():
    return render_template("Visuals.html")

@app.route("/About_us")
def about():
    return render_template("About.html")


if __name__ == "__main__":
    app.run(debug=True)
