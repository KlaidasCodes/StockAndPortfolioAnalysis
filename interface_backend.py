from flask import Flask, render_template

app = Flask("__name__")

@app.route("/home")
def home():
    return render_template("/index.html")

@app.route("/stock_analysis")
def stocks():
    return render_template("/stock_analysis.html")

@app.route("/about_me")
def about_me():
    return render_template("/about_me.html")

@app.route("/contacts")
def contacts():
    return render_template("/contacts.html")

@app.route("/portfolio_backtesting")
def portfolio():
    return render_template("/portfolio.html")

@app.route("/test")
def test():
    return render_template("/test.html")


if __name__ == "__main__":
    app.run(debug=True)

