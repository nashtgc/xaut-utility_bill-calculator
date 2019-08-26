from flask import Flask, render_template, request, session, make_response
from models.calculate import Calculate

app = Flask(__name__)
@app.route("/")
def home_template():
    return render_template("home.html")

@app.route("/water_form", methods= ['GET', "POST"])
def water_form():
    return render_template("water.html")

@app.route("/recv/water_input", methods=['POST'])
def calc_water():
    k_old = request.form["kit_old"]
    k_old = int(k_old)
    k_new = request.form["kit_new"]
    k_new = int(k_new)

    b_old = request.form["bath_old"]
    b_old = int(b_old)
    b_new = request.form["bath_new"]
    b_new = int(b_new)
    
    
    k = Calculate.water_bill_kit(k_new, k_old)
    b = Calculate.water_bill_kit(b_new, b_old)

    tt = k + b 

    return render_template("water.html", tt = tt )


@app.route("/electricity_form", methods=["GET", "POST"])
def electricity_form():
    return render_template("electricity.html")

@app.route("/recv/e_input", methods=["POST"])
def calc_electric():
    e_old = request.form["e_old"]
    e_old = int(e_old)
    e_new = request.form["e_new"]
    e_new = int(e_new)

    e_bill = Calculate.electric_bill(e_new, e_old)
    return render_template("electricity.html", e_bill = e_bill )


@app.route("/return_home")
def return_home():
    return render_template("home.html")





if __name__ == "__main__":
    app.run(port = 4995)