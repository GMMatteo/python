from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def hello_world():
    return render_template("index.html", num=3, color="cornflowerblue")

@app.route('/play/<int:num>')
def number(num):
    return render_template("index.html", num=num, color="cornflowerblue")

@app.route('/play/<int:num>/<string:color>')
def color(num, color):
    return render_template("index.html", num=num, color=color)

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again later."

if __name__=="__main__":
    app.run(debug=True)