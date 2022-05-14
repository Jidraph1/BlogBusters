from flask import render_template
from app import app

#Views

@main.route('/')
def index():
    """"View root page that returns the index page"""
    title= "BlogBusters"
    return render_template('index.html', title=title)