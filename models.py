from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('title', db.String)
    date = db.Column('date', db.DateTime)
    skills = db.Column('skills', db.String)
    description = db.Column('description', db.Text)
    url = db.Column('url', db.String)


    def __repr__(self):
        return f''' <Project (
        Project Title: {self.title} | 
        Project Date: {self.date} | 
        Project Skills: {self.skills} | 
        Project Description {self.description} | 
        Project url: {self.url} | )>'''
