from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def index():

    return render_template(
        "index.html"
    )

@app.route("/hello")
def hello():
    name = request.args.get("user_name")

    return render_template(
        "hello.html",
        name=name
    )


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")