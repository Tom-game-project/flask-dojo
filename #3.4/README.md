# Post

urlのリクエストのやつとは違う

比較的大きなデータを送信する時に使う

ルーティングを指定する必要がある

```python
@app.route("write",methods=["POST"])
def write():
    posted_data = request.form.get("変数名")
```
