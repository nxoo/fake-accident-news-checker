import joblib
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/check", methods=["GET", "POST"])
def check():
    if request.method == "POST":
        model = joblib.load('model.pkl')
        tweet = request.form["tweet"]
        probability = model.predict([tweet])
        if probability == 'Real':
            message = "20% probability tweet is Fake (Real tweet)."
            return render_template("index.html", message=message, tweet=tweet)
        else:
            error = "80% probability tweet is Fake"
            return render_template("index.html", error=error, tweet=tweet)
    else:
        return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)
