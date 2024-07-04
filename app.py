from flask import (render_template, url_for, request, redirect)
from models import db, Project, app, datetime


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/project/new', methods=['GET', 'POST'])
def add_new_project():
    if request.form:
        new_project = Project(
            title = request.form['title'],
            date = datetime.datetime.now(),#request.form['date'],
            skills = request.form['skills'],
            description = request.form['desc'],
            url = request.form['url']
        )
    
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('projectform.html')


    return render_template('projectform.html')


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
