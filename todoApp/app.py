from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:85037279af@localhost:5432/todoapp'

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'Todo {self.id} {self.description}'


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())


@app.route('/todos/create', methods=['POST'])
def create():
    # description = request.form.get('description', '')
    description = request.get_json()['description']
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()

    # return redirect(url_for('index'))
    return jsonify({
        'description': todo.description
    })
