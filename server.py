"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page. 
            <a href="http://localhost:5000/hello">
            Tell us more about you</a></html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          <p>Choose a compliment</p><br>
          <input type="radio" name="choose-greeting" id="awesome" 
          value="awesome">
          <label for="awesome">Awesome</label>
          <input type="radio" name="choose-greeting" id="terrific" 
          value="terrific">
          <label for="terrific">Terrific</label>
          <input type="radio" name="choose-greeting" id="fantastic" 
          value="fantastic">
          <label for="fantastic">Fantastic</label>
          <input type="radio" name="choose-greeting" id="neato" 
          value="neato">
          <label for="neato">Neato</label>
          <input type="radio" name="choose-greeting" id="fantabulous" 
          value="fantabulous">
          <label for="fantabulous">Fantabulous</label><br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("choose-greeting")

    # compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """
#comment

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
