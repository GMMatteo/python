from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'sdfjnh'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit_form():
    print("Submitted Form Info")
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    session['course'] = request.form['course']
    session['experience'] = request.form['exp']
    return redirect("/result")

@app.route('/result')
def sresults_form():
    print("Displaying the Results")
    print(request.form)
    return render_template("result.html", name=session['name'], location=session['location'], language=session['language'], comments=session['comments'], courses=session['course'], experience=session['experience'] )

if __name__=="__main__":
    app.run(debug=True)