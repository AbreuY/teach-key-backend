"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from logging import raiseExceptions
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import Professor, db, User, Student, Professor
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('FLASK_APP_KEY')
jwt = JWTManager(app)
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# endpoint para crear el registro de usuario usando metodo post
# Debe recibir un objeto JSON con los datos de correo, 
# nombre de usuario, fecha de nacimiento, contraseña, país.
@app.route('/register/student', methods=['POST'])
def handle_register_student():
    if request.json is None:
        return jsonify({'message':'The request was invalid'}), 400
    body = request.json
    user = Student.create(body)
    return jsonify(user.serialize()), 201

@app.route('/register/professor', methods=['POST'])
def handle_register_professor():
    if request.json is None:
        return jsonify({'message':'The request was invalid'}), 400

    body = request.json
    user = Professor.create(body)
    return jsonify(user.serialize()), 201

@app.route('/login/<string:role>', methods=['POST'])
def handle_login(role):
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = None
    if role == "student":
        user = Student.query.filter_by(email=email, password=password).one_or_none()
    else:
        user = Professor.query.filter_by(email=email, password=password).one_or_none()

    if user is None:
        return ({"msg": "Something went wrong, please try again"}), 401
    
    token = create_access_token(identity=user.id)
    return jsonify({"message": "Login successfully", 
    "token": token}), 200


    
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
