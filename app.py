from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///person.db'

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return 'Hello World'

@app.route('/api', methods=['GET'])
def get_all():
    persons = Person.query.all()
    return jsonify([person.to_json() for person in persons])

@app.route('/api/<int:id>', methods=['GET'])
def get_one(id):
    person = Person.query.get(id)
    return jsonify(person.to_json())

@app.route('/api/', methods=['POST'])
def create_person():
    person = Person(name=request.json['name'], age=request.json['age'])
    db.session.add(person)
    db.session.commit()
    return jsonify(person.to_json())



@app.route('/api/<int:id>', methods=['PUT'])
def update(id):
    person = Person.query.get(id)
    person.name = request.json['name']
    person.age = request.json['age']
    db.session.commit()
    return jsonify(person.to_json())

@app.route('/api/<int:id>', methods=['DELETE'])
def delete(id):
    person = Person.query.get(id)
    db.session.delete(person)
    db.session.commit()
    return jsonify(person.to_json())


if __name__ == '__main__':
    app.run(debug=True)
