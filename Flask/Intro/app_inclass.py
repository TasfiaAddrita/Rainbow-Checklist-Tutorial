from flask import Flask, request, render_template
from random import choice, sample

compliments = ['coolio', 'smashing', 'neato', 'fantabulous']

app = Flask(__name__)

@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return render_template('index.html')

@app.route('/compliment')
def get_compliment():
    name = request.args.get('name')
    num_compliments = int(request.args.get('num_compliments'))
    show_compliments = request.args.get('show_compliments')
    compliments_to_show = sample(compliments, num_compliments)

    return render_template (
        'compliments.html',
        name=name,
        show_compliments=show_compliments,
        compliments=compliments_to_show
    )

if __name__ == "__main__":
    app.run(debug=True)

# SIDE NOTE: to open file in interactive mode python3 -i <file>.py
# SIDE NOTE: f before string makes the string formatted

# def get_horoscope():
#     future = ["You will meet Danny Devito today.", "You will have the opportunity to throw a shoe at Donald Trump soon.", "You're going to be the next Zuckerberg.", "You will star in Family Feud.", "You will finally win that game you always lose at."]
#     return choice(future)
