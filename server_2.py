from flask import Flask, jsonify, render_template
from model import Subscriber, db, Melon, connect_to_db
from time import sleep

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/subscribers', methods="POST")
def get_subscribers():
    subscriber = Subscriber.query.all()

    # return 
    # thanks for signing up
    # already signed up


if __name__ == '__main__':
    connect_to_db(app)
    app.run('0.0.0.0', debug=True)
