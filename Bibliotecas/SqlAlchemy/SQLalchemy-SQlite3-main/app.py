from flask import Flask, render_template
import sqlite3
from connect_sqlite3 import consulta_Flask_list, consulta_Flask_dict


app = Flask(__name__)

@app.route("/")
def home():
    resultslist = consulta_Flask_list()
    resultsdict = consulta_Flask_dict()
    return render_template("home.html", resultslist = resultslist, resultsdict = resultsdict)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True) 