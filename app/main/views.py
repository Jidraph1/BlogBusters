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

@main.route('/')
def signup():
    asd