from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '24681012'

@app.route('/')
def counter():
    session['count']+=1
    return render_template("index.html", count= session['count'])

# @app.route('/')
# def refresh():
#     session['count']+=1
#     return render_template('index.html', visit= session['count'])

@app.route('/destroy_session')
def destroy():
    session['count']=0
    return redirect('/')

@app.route('/add')
def add():
    session['count']+=1
    return redirect('/')

@app.route('/increment', methods =["POST"])
def increment():
    session['count']+=int(request.form['value'])
    return redirect('/')

@app.route('/reset')
def reset():
    session['count']=0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)