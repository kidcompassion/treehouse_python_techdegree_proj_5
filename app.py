from flask import (render_template, url_for, request)
from models import db, Project, app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/project/new')
def add_new_projects():
    return 'new projects'


@app.route('/project/<id>')
def project_by_id(id):
    return id


@app.route('/project/<id>/edit')
def edit_project_by_id(id):
    return id

@app.route('/project/<id>/delete')
def delete_project_by_id(id):
    return id

if __name__ =='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
