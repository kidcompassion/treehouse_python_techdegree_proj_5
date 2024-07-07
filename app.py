from flask import (render_template, url_for, request, redirect)
from models import db, Project, app, datetime


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html',projects=projects)


@app.route('/project/new', methods=['GET', 'POST'])
def add_project():

    #Query all projects so that the drop down menu will work on interior pages
    projects = Project.query.all()
    if request.form:

        # Format incoming date string as datetime object
        date_split = request.form['date'].split("-")
        
        new_project = Project(
            title = request.form['title'],
            date = datetime.date(year=int(date_split[0]), month=int(date_split[1]), day = 1),
            skills = request.form['skills'],
            description = request.form['desc'],
            url = request.form['url']
        )
    
        db.session.add(new_project)
        db.session.commit()
        print(request.form)
        return redirect(url_for('index'))
    return render_template('projectform.html', projects=projects)


@app.route('/project/<id>')
def project(id):
    # Query for all projects so the dropdown nav will work on this route
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    # format date for the details page
    project.date = project.date.strftime("%b %Y")

    # format skills for a bulleted list
    project.skills = project.skills.split(",")
    
    return render_template('detail.html', project = project, projects=projects)


@app.route('/project/<id>/edit', methods = ['GET', 'POST'])
def edit_project(id):
    projects = Project.query.all()
    project = Project.query.get(id)
    # incoming date from DB is an object.
    starting_project_date = project.date
    # Convert incoming date to correct format for value of datepicker
    project.date = project.date.strftime("%Y-%m")

    #on Form submit
    if request.form:
        project.title = request.form['title']
        # If date picker value has not changed, just pass back the date obj we started with
        if project.date == request.form['date']:
            project.date = starting_project_date
        
        else:
            # If date picker has changed, split the value from the date picker
            split_date = request.form['date'].split("-")
            # Pass split value into date obj and store it in database
            project.date = datetime.date(year=int(split_date[0]), month=int(split_date[1]), day = 1)
        project.skills = request.form['skills']
        project.description = request.form['desc']
        project.url = request.form['url']

        db.session.add(project)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('editproject.html', project=project, projects=projects)
    

@app.route('/project/<id>/delete')
def delete_project(id):
    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ =='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000, host='127.0.0.1')
