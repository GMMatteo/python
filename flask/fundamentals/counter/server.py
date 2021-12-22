from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '24681012'



@app.route('/')
def counter():
    if 'count' in session:
        session['count']+=1
        session['visit']+=1
    else:
        session['count']=0
        session['visit']=0
    return render_template("index.html")

@app.route('/destroy_session')
def destroy():
    session['count']=0
    return redirect('/')

@app.route('/add')
def add():
    session['count']+=2
    return redirect('/')

@app.route('/increment', methods =["POST"])
def increment():
    session['count']+=int(request.form['value'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)