from flask import FLask 


app = Flask(__name__)
@app.route("/")
def home_template():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(port = 4995)