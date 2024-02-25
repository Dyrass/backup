from flask import Flask, request, jsonify ,render_template

app = Flask(__name__)

@app.route("/<n>")
def fib(n):
    return str(fibonacchi(int(n)))


@app.route("/")
def hi():
    return render_template('index.html')
def fibonacchi(n,hm = {}):
    if n <= 2:
        return 1
    if n in hm:
        return hm[n]
    ans = fibonacchi(n-1,hm)+fibonacchi(n-2,hm)
    hm[n] = ans
    return ans


if __name__ == "__main__":
    app.run(debug=True)
