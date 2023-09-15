from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def index():
    name="tom"
    age=7
    email="tom.ipynb@gmail.com"
    return render_template(
        "user.html",
        age=age,
        name=name,
        email=email
    )

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")
