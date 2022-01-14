from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect ("/dojos")

@app.route('/dojos')
def dojos():
    dojo = Dojo.get_all()
    print(dojo)
    return render_template("index.html", dojos = dojo)

@app.route('/newDojo', methods=["POST"])
def add_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show(id):
    data ={
        "id":id
    }
    return render_template("show.html", dojo=Dojo.get_ninjas_in_dojo(data))

# @app.route('/ninjas')
# def ninjas():
#     return render_template("/ninjas.html")