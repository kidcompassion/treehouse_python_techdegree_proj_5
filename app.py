from flask import (render_template, url_for, request, redirect)
from models import db, Project, app, datetime


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/project/new', methods=['GET', 'POST'])
def add_project():
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
    return render_template('projectform.html')





@app.route('/project/<id>')
def project(id):
    project = Project.query.get_or_404(id)
    # format date for the details page
    project.date = project.date.strftime("%b %Y")

    # format skills for a bulleted list
    project.skills = project.skills.split(",")
    

    return render_template('detail.html', project = project)





@app.route('/project/<id>/edit', methods = ['GET', 'POST'])
def edit_project(id):
    print("fires")
    project = Project.query.get(id)
    starting_project_date = project.date
    project.date = project.date.strftime("%Y-%m")
    
    # if project.date has changed
    # convert it to a datetime obj
    

    if request.form:
        print("fires inside request")
        project.title = request.form['title']
        
        if project.date == request.form['date']:
            project.date = starting_project_date
        else:
            print("fires in else")
            split_date = request.form['date'].split("-")
            
            project.date = datetime.date(year=int(split_date[0]), month=int(split_date[1]), day = 1)
            
        
        
        project.skills = request.form['skills']
        project.description = request.form['desc']
        project.url = request.form['url']

        db.session.add(project)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('editproject.html', project=project)
    



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
