from app import db
from app.models import Base


class Product(Base):
    __tablename__ = 'sakg_products'

    title = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    ingredients = db.Column(db.Text, nullable=True)
    image = db.Column(db.String, nullable=False)


    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Product %r>' % self.title
