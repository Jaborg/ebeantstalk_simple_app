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


if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
