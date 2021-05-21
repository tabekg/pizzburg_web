from app import db
from app.models import Base
from flask_login import UserMixin


class Admin(Base, UserMixin):
    __tablename__ = 'sakg_admins'

    full_name = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False, unique=True)
    last_action = db.Column(db.DateTime, nullable=True)
    password_hash = db.Column(db.String, nullable=False)
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, full_name, phone_number, password_hash, last_action=None):
        self.full_name = full_name
        self.phone_number = phone_number
        self.last_action = last_action
        self.password_hash = password_hash

    def __repr__(self):
        return '<Admin %r>' % self.full_name

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
