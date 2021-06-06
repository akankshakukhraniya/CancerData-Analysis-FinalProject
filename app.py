from flask import flash, Flask, render_template, redirect
from flask_pymongo import PyMongo
import ML
from private import usr, pwd, cluster, db_name # private information, cannot be shared
import pandas as pd


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
MONGO_URI = f"mongodb+srv://{usr}:{pwd}@{cluster}/{db_name}"
mongo = PyMongo(app, uri=MONGO_URI)

@app.route("/")
def index():
    cursor = mongo.db.breast_data.find()
    df= pd.DataFrame(list(cursor))
    results = ML.breast_survival_test(df)
    return render_template("index.html", data=results)


if __name__ == "__main__":
    app.run(debug=True)
