from app import db
from app.models import Base


class Category(Base):
    __tablename__ = 'sakg_categories'

    title = db.Column(db.String, nullable=False)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<Category %r>' % self.title
