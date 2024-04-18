from flask_login import UserMixin
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import secrets
from datetime import datetime

from app import db

ma = Marshmallow()

class User(db.Model, UserMixin):

    id : Mapped[str] = mapped_column('id', String, primary_key=True)
    first_name : Mapped[str] = mapped_column('first_name', String, nullable=True, default='')
    last_name : Mapped[str] = mapped_column('last_name', String, nullable=True, default='')
    email : Mapped[str] = mapped_column('email', String, nullable=False)
    street1 : Mapped[str] = mapped_column('street', String, nullable=True)
    street2 : Mapped[str] = mapped_column('unit', String, nullable=True)
    city : Mapped[str] = mapped_column('city', String, nullable=True)
    state : Mapped[str] = mapped_column('state', String, nullable=True)
    _zip : Mapped[str] = mapped_column('zip', Integer, nullable=True)
    website : Mapped[str] = mapped_column('website', String, nullable=True)
    password : Mapped[str] = mapped_column('password', String, nullable=False, default='')
    g_auth_verify : Mapped[bool] = mapped_column('g_auth_verify', Boolean(), default=False)
    token : Mapped[str] = mapped_column('token', String, unique=True, default='')
    date_joined : Mapped[str] = mapped_column('date_joined', String, nullable=False, default = datetime.now())

    def __init__(self, email, first_name='', last_name='', password=''):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = self.set_id()
        self.password = self.set_password(password)
        self.token = self.generate_token()
    
    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        return generate_password_hash(password)
    
    def generate_token(self, tok_len=24):
        return secrets.token_hex(tok_len)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self): # this will reprint (confirm) the information just entered
        return f'User {self.email} has been added to the database'
    
class Car(db.Model):
    id: Mapped[str] = mapped_column('id', String, primary_key=True, nullable=False)
    current_owner : Mapped[str] = mapped_column(String(), ForeignKey(User.id))
    vin : Mapped[str] = mapped_column(String(), nullable=False)
    make : Mapped[str] = mapped_column(String(), default='')
    model : Mapped[str] = mapped_column(String(), default='')
    year : Mapped[int] = mapped_column(Integer(), default='')
    color : Mapped[str] = mapped_column(String(), default='')
    car_name : Mapped[str] = mapped_column(String(60))
    car_desc : Mapped[str] = mapped_column(String(300))

    def __init__(self, vin, make='', model='', year='', color='', car_name='', car_desc='', current_owner=''):
        self.id = self.set_id()
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.car_name = car_name
        self.car_desc = car_desc
        self.current_owner = current_owner

    def set_id(self):
        return str(uuid.uuid4())


class UserSchema(ma.Schema):
    class Meta:
        fields = ('email', 'first_name', 'last_name', 'date_joined', 'website')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class CarSchema(ma.Schema):
    class Meta:
        fields = ('id', 'make', 'model', 'year', 'color', 'car_name', 'vin')
        
car_schema = CarSchema()
cars_schema = CarSchema(many=True)