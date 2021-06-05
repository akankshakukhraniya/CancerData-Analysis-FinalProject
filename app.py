from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/Breast_Cancer_db"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/phone_app")


@app.route("/")
def index():
    # listings = mongo.db.listings.find_one()
    return render_template("index.html")

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
