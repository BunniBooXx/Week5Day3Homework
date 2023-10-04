from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 


db=SQLAlchemy()

class Pokemon1(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Pokemon %r>' % self.id
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(50), nullable=False)
    last_name=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(100),nullable=False)
    date_created=db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

class Sign_Up(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(50), nullable=False)
    last_name=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(100), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)
    def __init__(self):
        return '<Sign_Up %r>' % self.id
    
class Login(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(50), nullable=False)
    last_name=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(100), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)
    def __init__(self):
        return '<Login %r>' % self.id
    
Pokemon_owners = db.Table ('Pokemon_owners',
    db.Column('User_id', db.String(100),db.ForeignKey('user.id'), nullable=False),
    db.Column('Pokemon_id', db.String(100),db.ForeignKey('Pokemon1.id'), nullable=False),

)