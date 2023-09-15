# app.py@#4.0
"""
# urlパラメタとフォームの取得

urlパラメタa,bを掛け合わせてgcdを返すプログラム

"""
from flask import Flask,request
from function import gcd

app = Flask(__name__)



@app.route("/")
def index():
    a = request.args.get("a")
    b = request.args.get("b")
    if a is None:
        return "パラメータ'a'が足りません"
    if b is None:
        return "パラメータ'b'が足りません"
    result = gcd(int(a),int(b))
    return f"gcd -> {result}"

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")