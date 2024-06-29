from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')


def index():
    return render_template('index.html')


@app.route('/projects/new')

def new_projects():
    return 'new projects'


@app.route('/projects/<id>')
def project_by_id(id):
    return id


@app.route('/projects/<id>/edit')
def edit_project_by_id(id):
    return id

@app.route('/projects/<id>/delete')
def delete_project_by_id(id):
    return id

if __name__ =='__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')