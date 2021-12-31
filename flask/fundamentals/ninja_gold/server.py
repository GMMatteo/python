from flask import Flask, request, render_template, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = '598'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
        session['count'] = 0
        return render_template("index.html")
    else:
        print(session['gold'])
        return render_template("index.html")

@app.route('/process_money', methods=['post'])
def process_money():
    finding = request.form.get('find')
    date = datetime.datetime.now()
    time = date.strftime('%b %d %Y %H:%M:%S')
    if finding =='farm':
        gold = random.randint(10,20)
        session['gold'] += gold
        session['count'] += 1
        activity = f"<div class='gain'>Earned {gold} pieces of gold from the farm! ({time}) </div>"
    elif finding == 'cave':
        gold = random.randint(5,10)
        session['gold'] += gold
        session['count'] += 1
        activity = f"<div class='gain'>Found {gold} pieces of gold from the cave! ({time}) </div>"
    elif finding == 'house':
        gold = random.randint(2,5)
        session['gold'] += gold
        session['count'] += 1
        activity = f"<div class='gain'>Found {gold} pieces of gold from the house! ({time}) </div>"
    elif finding == 'casino':
        gold = random.randint(-50,50)
        session['gold'] += gold
        session['count'] += 1
        if gold > 0:
            activity = f"<div class='gain'>Entered a Casino and won {gold} pieces of gold... Sweet! ({time}) </div>"
        else:
            activity = f"<div class='loss'>Entered a Casino and lost {gold} pieces of gold... Ouch! ({time}) </div>"
    session['activities'].append(activity)
    session['activities'].reverse()
    return redirect('/')

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

if __name__=='__main__':
    app.run(debug=True)