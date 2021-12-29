from flask import Flask, render_template, request, redirect, session
import random  # import the random module



app = Flask(__name__)
app.secret_key = 'alligator2'

@app.route("/")
def index():
    if 'result' not in session:
        session['result'] = ""
    if 'winner' not in session:
        session['winner'] = False
    if 'count' not in session:
        session['count'] = 0
    if 'number' not in session:
        session['number'] = random.randint(1,100)
        print(session['number'])
        return render_template("index.html")
    else:
        print(session['number'])
        print(session['count'])
        return render_template("index.html")

@app.route("/process", methods=['POST'])
def guess():
    guess = int(request.form['guessNumber'])
    if guess == session['number']:
        session['result'] = "Correct"
        session['winner'] = True
        session['count'] += 1
        return redirect("/")
    elif guess > session['number']:
        session['result'] = "Too High"
        session['count'] += 1
        return redirect("/")
    else:
        session['result'] = "Too Low"
        session['count'] += 1
        return redirect("/")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

@app.route("/score", methods=['POST'])
def winner():
    print("Got Score Info")
    print(request.form)
    session['f_name'] = request.form["f_name"]
    session['l_name'] = request.form["l_name"]
    count = session['count']
    return render_template("/leaderboard.html")

# @app.route("/leaderboard")
# def records():
#     return render_template("leaderboard.html")

@app.route("/winner")
def score():
    return render_template("/winner.html")


if __name__ == "__main__":
    app.run(debug=True)
