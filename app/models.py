from . import db, login_manager
from flask_login import UserMixin
from . import login_manager

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15),unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String())
    # posts = db.relationship('Post', backref='poster')
    # comments = db.relationship('Comment', backref='commentor')

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def _repr__(self):
        return f'User {self.username}'

class Post(db.Model):
    __tablename__= 'posts'