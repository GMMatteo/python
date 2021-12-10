from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/success')
def success():
    return "Success"

@app.route('/hello/<string:fruit>/<int:num>')
def hello(fruit, num):
    return f"Hello {fruit * num}"

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<string:name>')
def name(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num, name):
    return f"{name * num}"

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

