from app import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=None, nullable=True,
                              onupdate=db.func.current_timestamp())

    def as_dict(self, items=None):
        if items is None:
            items = []
        response = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        for i in items:
            response[i] = getattr(self, i).as_dict()
        return response