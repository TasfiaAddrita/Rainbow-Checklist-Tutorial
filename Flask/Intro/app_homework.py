from flask import Flask, request
from random import choice

app = Flask(__name__)

@app.route('/')
def home():
    """Show the homepage and ask the user's name."""
    return """
    <form action='/future' name="future">
        <p>
            What is your name?
            <input type="text" name="name"/>
        </p>
        <p>
            What reading would you like today?<br>
        </p>
        <form name="future">
            <input type="radio" name="quote" value="motivational"> Motivational<br>
            <input type="radio" name="quote" value="funny"> Funny<br>
            <input type="radio" name="quote" value="random"> Random<br><br>
            <input type="submit">
        </form>
    </form>
    """

@app.route('/future')
def fortune_cookie():
    future = {
        "funny": [
            "Someone is looking up at you. Don't let that person down.",
            "No snowflake in an avalanche ever feels responsible",
            "If you eat something and nobody sees you eat it, it has no calories.",
            "Your heart will skip a beat.",
            "You will marry a professional athlete - if competitive eating can be considered a sport.",
            "Perhaps you've been focusing too much on spending.",
            "In youth and beauty, wisdom is rare.",
            "You are not illiterate.",
            "I see money in your future. It's not yours though.",
            "Three can keep a secret, if you get rid of two.",
            "This cookie is never gonna give you up, never gonna let you down.",
            "If you think nobody cares if you are alive, try missing a couple of car payments.",
            "Catch on fire with enthusiasm and people will come for miles to watch you burn.",
            "Love is on the horizon. The stars predict he will be tall, dark, and a centaur.",
            "You are about to finish reading a forture cookie."
        ],
        "motivational": [
            '“You cannot save people, you can just love them.” — Anaïs Nin',
            '“It wasn’t raining when Noah built the ark.” — Howard Ruff',
            '“Holding onto anger is like drinking poison and expecting the other person to die.”— Buddha',
            '“The journey of a thousand miles begins with one step.” — Lao Tzu',
            '“Even if you’re on the right track, you’ll get run over if you just sit there.”— Will Rogers',
            '“Even if you fall on your face, you’re still moving forward.”—Victor Kiam',
            '“If you can’t outplay them, outwork them.”— Ben Hogan',
            '“Obsessed is just a word the lazy use to describe the dedicated.”— Russell Warren',
            '“Never apologize for having high standards. People who really want to be in your life will rise up to meet them.” — Ziad K. Abdelnour',
            '“Don’t live the same year 75 times and call it a life.” — Robin Sharma',
            '“If you want to live a happy life, tie it to a goal, not to people or objects.” — Albert Einstein',
            '“Instead of wondering when your next vacation is, maybe you should set up a life you don’t need to escape from.” — Seth Godin',
            '“I destroy my enemies when I make them my friends.” — Abraham Lincoln',
            '“The best dreams happen when you’re awake.”— Cherie Gilderbloo'

        ]
    }
    name = request.args.get('name')
    requested_future = request.args.get('future')
    random_motivation = choice(future['motivational'])
    random_funny = choice(future['funny'])
    random = choice(future[choice (list (future.keys()) ) ] )

    if requested_future == "motivational":
        return f'Hi { name }! Your fortune cookie says: { random_motivation }'
    elif requested_future == "funny":
        return f'Hi { name }! Your fortune cookie says: { random_funny }'
    else:
        return f'Hi { name }! Your fortune cookie says: { random }'

if __name__ == "__main__":
    app.run(debug=True)
