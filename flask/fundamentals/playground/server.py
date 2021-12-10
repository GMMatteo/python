from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def hello_world():
    return render_template("index.html")

@app.route('/play/<int:num>')
def number(num):
    return render_template("number.html", num=num)

@app.route('/play/<int:num>/<string:change_color>')
def color(num, change_color):
    color = change_color
    return render_template("color.html", num=num, color=color)

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again later."

if __name__=="__main__":
    app.run(debug=True)