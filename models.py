from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('__name__')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)

class Project(db.Model):
    project_id = db.Column(db.Integer, primary_key=True)
    project_title = db.Column('project_title', db.String)
    project_description = db.Column('project_description', db.String)
    project_instructions = db.Column('project_instructions', db.String)
    project_lessons = db.Column('project_lessons', db.String)


    def __repr__(self):
        return f''' <Project (
        Project Title: {self.project_title} | 
        Project Description {self.project_description} | 
        Project Instructions: {self.project_instructions} | 
        Project Lessons: {self.project_lessons})>'''
