from flask import render_template, request, redirect, url_for
from . import main
from flask_login import login_required

#Views

@main.route('/')
def index():
    """"
    View root page that returns the index page
    """
    title= "BlogBusters"
    return render_template('index.html', title=title)

@main.route('/login')
def login():
    
    return render_template('login.html')


@main.route('/')
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():

        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect('/success')
    return render_template('signup.html')