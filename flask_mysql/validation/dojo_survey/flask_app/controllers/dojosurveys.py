from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojosurvey import Dojo

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add_survey',methods=['POST'])
def create():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    Dojo.save_all(request.form)
    return redirect('/results')

@app.route('/results')
def results():
    return render_template("result.html", results=Dojo.get_one())

# @app.route('/add_location')
# def location():
#     return render_template("add_location.html")

# @app.route('/select_location', methods=['POST'])
# def sel_location():
#     if not Dojo.validate_location(request.form):
#         return redirect('/select_location')
#     Dojo.save_dojo(request.form)
#     return redirect('/')

# @app.route('/add_lang')
# def language():
#     return render_template("add_lang.html")

# @app.route('/select_lang', methods=['POST'])
# def sel_lang():
#     if not Dojo.validate_language(request.form):
#         return redirect('/select_lang')
#     Dojo.save_lang(request.form)
#     return redirect('/')