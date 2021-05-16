from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def show_homepage():
    "Show IM_melon homepage"

    return render_template('homepage.html')

@app.route('/login')
def show_login():
    "Show user login page"

    return render_template('login.html')

@app.route('/create_account')
def show_create_account():
    "Show new account page"

    return render_template('new_account.html')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')