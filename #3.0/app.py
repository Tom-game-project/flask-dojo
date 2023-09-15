from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def index():
    name = "tom"
    age = 19
    email = "tom.ipynb@gmail.com"
    return render_template(
        "card.html",
        name=name,
        age=age,
        email=email
    )


if __name__=="__main__":
    app.run(debug=True)
