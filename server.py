from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def show_homepage():
    """Show IM_melon homepage"""

    return render_template('homepage.html')

@app.route('/login')
def show_login():
    """Show user login page"""

    return render_template('login.html')

@app.route('/login', methods=["POST"])
def enter_login_info():
    """Signing in, checks if user exists"""

    email_address = request.get_json().get("email_address")
    password = request.get_json().get("password")
    admin_email = "easha@gmail.com"
    admin_password = "abcde"
    #subscriber = crud.get_user_by_email(email)
    if email_address==admin_email and password==admin_password:
        """Redirects user to admin page"""

        return redirect('/admin')
    if subscriber and subscriber.password == password:
        session['subscriber_number'] = subscriber.subscriber_number


@app.route('/admin')
def show_admin_page():
    """Renders admin page"""
    return render_template('admin.html')

@app.route('/admin', methods=["POST"])
def update_melons_database():
    """Admin can now update database"""

@app.route('/create_account')
def show_create_account():
    """Show new account page"""

    return render_template('new_account.html')

@app.route('/create_account', methods=["POST"])
def add_new_subscriber():
    """Adding a new subscriber to database"""

    name = request.get_json().get("name")
    email_address = request.get_json().get("email_address")
    phone_number = request.get_json().get("phone_number")
    password = request.get_json().get("password")
    #check if user exists

    return redirect('/login')

@app.route('/subscriber/<subscriber_name>')
def view_subscriber():
    """View subscriber page with what they have signed up for"""

    return render_template("subscriber.html")

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')