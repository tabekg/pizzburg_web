from flask import request
from app import db, app
from app.mod_category.models import Category


# @mod_app.route('/')
# def index():
#     return {
#         "users": [i.as_dict() for i in Category.query.all()],
#     }


@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    user = Category(
        full_name=data['full_name'],
        phone_number=data['phone_number'],
    )
    db.session.add(user)
    db.session.commit()
    return user.as_dict()


@app.route('/user/<int:id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def dispatcher(id=None):
    user = Category.query.get_or_404(id)

    if request.method == 'GET':
        return {"item": user.as_dict()}

    elif request.method == 'PUT':
        data = request.get_json()
        user.full_name = data['full_name']
        user.phone_number = data['phone_number']
        db.session.add(user)
        db.session.commit()
        return {"item": user.as_dict()}

    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()

    return {"status": "ok"}
