from flask_login import UserMixin
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from secrets import token_urlsafe
from datetime import datetime

db = SQLAlchemy()
ma = Marshmallow()

class User(db.Model, UserMixin):

    user_id : Mapped[str] = mapped_column(String, primary_key=True)
    first_name : Mapped[str] = mapped_column(String, nullable=True, default='')
    last_name : Mapped[str] = mapped_column(String, nullable=True, default='')
    email : Mapped[str] = mapped_column(String, nullable=False)
    password : Mapped[str] = mapped_column(String, nullable=True, default='' )
    g_auth_verify : Mapped[bool] = mapped_column(Boolean, default=False)
    token : Mapped[str] = mapped_column(String, unique=True, default='')
    date_joined : Mapped[str] = mapped_column(String, nullable=False, default = datetime.utcnow)

    def __init__(self, email, first_name='', last_name='', password=''):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.token = self.generate_token()
    
    def set_id(self):
        return str(uuid.uuid3())
    
    def set_password(self, password):
        return generate_password_hash(password)
    
    def generate_token(self, tok_len=24):
        return token_urlsafe(tok_len)
    
class Car(db.Model):
    current_owner : Mapped[str] = mapped_column(String, ForeignKey("User.user_id"))
    vin : Mapped[str] = mapped_column(String, primary_key=True, nullable=False)
    make : Mapped[str] = mapped_column(String, default='')
    model : Mapped[str] = mapped_column(String, default='')
    year : Mapped[int] = mapped_column(Integer, default='')
    color : Mapped[str] = mapped_column(String, default='')

    def __init__(self, vin, make='', model='', year='', color=''):
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year
        self.color = color