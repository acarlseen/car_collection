from flask import Blueprint, request, jsonify, render_template
from flask_login import current_user
from helpers import token_required
from models import  db, User, user_schema, users_schema, Car, car_schema, cars_schema

api = Blueprint('api', __name__,
                url_prefix='/api')

@api.route('/tester')
def test_get():
     return {'TEST': 'SUCCESFUL'}

@api.route('/collection/<id>', methods=['POST'])
@token_required
def add_car(current_user_token, id):
    vin = request.json['vin']
    make = request.json['make']
    model = request.json['model']
    year = request.json['year']
    color = request.json['color']
    car_name = request.json['car_name']
    owner = id

    car = Car(vin, make, model, year, color, car_name=car_name, current_owner=owner)

    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)

@api.route('/collection/<id>', methods=['GET'])
@token_required
def get_garage(current_user_token, id):
    garage = Car.query.filter_by(current_owner = id).all()
    response = cars_schema.dump(garage)
    return jsonify(response)

@api.route('/collection/<id>/<car_id>', methods=['GET'])
@token_required
def get_car(current_user_token, id, car_id):
    car = Car.query.get(car_id)
    response = car_schema.dump(car)
    return jsonify(response)

@api.route('/collection/<id>/<car_id>', methods=['POST', 'PUT'])
@token_required
def update_car(current_user_token, id, car_id):
    car = Car.query.get(car_id)
    car.vin = request.json['vin']
    car.make = request.json['make']
    car.model = request.json['model']
    car.year = request.json['year']
    car.color = request.json['color']
    car.car_name = request.json['car_name']

    db.session.commit()

    response = car_schema.dump(car)

    return jsonify(response)

@api.route('/collection/<id>/<car_id>', methods=['DELETE'])
@token_required
def delete_car(current_user_token, id, car_id):
        car = Car.query.get(car_id)
        db.session.delete(car)
        db.session.commit()

        response = car_schema.dump(car)
        return jsonify(response)