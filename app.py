from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import ML


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb+srv://dbUser:1212@cluster0.iseao.mongodb.net/cancer_db?authSource=admin&replicaSet=atlas-6yeevs-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
mongo = PyMongo(app)



@app.route("/")
def index():
<<<<<<< HEAD
    # listings = mongo.db.listings.find_one()
    cancer_dict = cancer_survival()
    return render_template("index.html", data=cancer_dict)
=======
    cancer_dict = mongo.db.cancer_db.find_one()
    results = cancer_survival(cancer_dict)
    return render_template("index.html", data = results)
>>>>>>> fa8f2cd16fb35e5a0637c30bf7ca56324dbc67cb

@app.route("/Visuals")
def index():
    # listings = mongo.db.listings.find_one()
    return render_template("Visuals.html")

@app.route("/About_us")
def index():
    # listings = mongo.db.listings.find_one()
    return render_template("About.html")




if __name__ == "__main__":
    app.run(debug=True)
