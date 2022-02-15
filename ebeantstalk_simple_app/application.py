from flask import Flask,render_template
application = Flask(__name__)

@application.route('/')
def hello_world():
    return render_template('frontpage.html')


@application.route("/information")
def info():
    return render_template("information.html")



@application.route("/reviews")
def review():
    return render_template("reviews.html")
