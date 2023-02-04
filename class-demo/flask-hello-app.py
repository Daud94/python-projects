from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:85037279af@localhost:5432/example'


@app.route('/')
def hello():
    return f'Hello, World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0")
