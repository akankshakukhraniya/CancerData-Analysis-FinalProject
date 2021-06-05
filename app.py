from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import ML


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb+srv://dbUser:1212@cluster0.iseao.mongodb.net/cancer_db?authSource=admin&replicaSet=atlas-6yeevs-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/phone_app")


@app.route("/")
def index():
    cancer_dict = mongo.db.cancer_db.find_one()
    results = cancer_survival(cancer_dict)
    return render_template("index.html", data = results)

@app.route("/Visuals")
def index():
    # listings = mongo.db.listings.find_one()
    return render_template("Visuals.html")

@app.route("/About_us")
def index():
    # listings = mongo.db.listings.find_one()
    return render_template("About.html")


# @app.route("/scrape")
# def scraper():
#     listings = mongo.db.listings
#     listings_data = scrape_phone.scrape()
#     listings.update({}, listings_data, upsert=True)
#     return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
