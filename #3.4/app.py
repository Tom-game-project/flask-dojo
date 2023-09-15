from flask import Flask,render_template,redirect,request
import os

app = Flask(__name__)

@app.route("/")
def index():
    msg_box="まだ書き込みがされていません"
    with open(os.path.join("db_folder","data.txt"),mode="rt") as f:
        msg_box = f.read()
    return render_template(
        "index.html",
        msg_box=msg_box,
    )


@app.route("/write",methods=["POST"])
def write():
    if "msg" in request.form:
        msg = str(request.form["msg"])
        with open(os.path.join("db_folder","data.txt"),mode="w") as f:
            f.write(msg)
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")
