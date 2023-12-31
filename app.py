from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import json
from dotenv import load_dotenv
import os

app = Flask(__name__)
api = Api(app)

db_uri = os.getenv('db_uri')
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




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
    return 'Hello you! are you looking for /api?'

@app.route('/api', methods=['GET'])
def get_all():
    persons = Person.query.all()
    return jsonify([person.to_json() for person in persons])

@app.route('/api/<int:id>', methods=['GET'])
def get_one(id):
    person = Person.query.get(id)
    if person:
        return jsonify(person.to_json())
    else:
        return jsonify({'error': 'Person not found'}), 404

@app.route('/api', methods=['POST'])
def create_person():
    try:
        data = request.get_json()
        person = Person(name=data['name'], age=data.get('age'))
        db.session.add(person)
        db.session.commit()
        return jsonify({'message': 'Person created successfully', 'person': person.to_json()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/<int:id>', methods=['PUT'])
def update(id):
    try:
        person = Person.query.get(id)

        if person is None:
            return jsonify({'error': 'Person not found'}), 404

        data = request.get_json()
        if 'name' in data:
            person.name = data['name']
        if 'age' in data:
            person.age = data['age']

        db.session.commit()

        return jsonify({'message': 'Person updated successfully', 'person': person.to_json()})

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        person = Person.query.get(id)

        if person is None:
            return jsonify({'error': 'Person not found'}), 404

        db.session.delete(person)
        db.session.commit()

        return jsonify({'message': 'Person deleted successfully'})

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 



if __name__ == '__main__':
    app.run(debug=True)
