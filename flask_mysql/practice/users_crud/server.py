from flask import Flask, request, render_template, redirect, session

from users import User

app = Flask(__name__)
app.secret_key = '598'

@app.route('/')
def index():
    users= User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route('/addUser', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/')

@app.route('/user.html')
def user():
    return render_template("user.html")

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={
        "id":id
    }
    return render_template("edit.html",user=User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data ={
        "id":id
    }
    return render_template("show.html",user=User.get_one(data))

@app.route('/user/update',methods=['POST'])
def update():
    User.edit(request.form)
    return redirect('/')

@app.route('/user/destroy/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    User.delete(data)
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)