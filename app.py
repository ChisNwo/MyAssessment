from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///Hospitalpatient.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db = SQLAlchemy(app)

@app.route("/run")
def run():
    return render_template("add_patients.html")

@app.route("/patients")
def patients():
    return "patients"

@app.route("/")
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()