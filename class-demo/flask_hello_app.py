from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:85037279af@localhost:5432/example'

db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'Person ID:{self.id}, name: {self.name}'


with app.app_context():
    db.create_all()


@app.route('/')
def index():
    # person = Person.query.first()
    persons = Person.query.all()
    for person in persons:
        return f'Hello,{person.name}'


if __name__ == '__main__':
    app.run(host="0.0.0.0")
