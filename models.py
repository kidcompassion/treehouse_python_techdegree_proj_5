from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///projects.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base

class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True)
    project_title = Column('project_title', String)
    project_description = Column('project_description', String)
    project_instructions = Column('project_instructions', String)
    project_lessons = Column('project_lessons', String)


    def __repr__(self):
        return f'Project Title: {self.project_title} | Project Description {self.project_description} | Project Instructions: {self.project_instructions} | Project Lessons: {self.project_lessons})>'
