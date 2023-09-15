from flask import Flask,request,render_template,make_response
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    counter = request.cookies.get("cnt")
    if counter is None:
        counter=0
    else:
        counter=int(counter)
    counter+=1
    response = make_response(
        render_template(
            "index.html",
            counter=counter
        )
    )
    max_age = 60*60*24*1 #1日
    expires = int(datetime.datetime.now().timestamp())+max_age
    response.set_cookie(
        "cnt",
        value=str(counter),
        max_age=max_age,
        expires=expires
    )
    return response

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")