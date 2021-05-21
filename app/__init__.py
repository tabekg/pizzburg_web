from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)

app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.mod_category.models import Category
from app.mod_product.models import Product
from app.mod_admin.models import Admin

from app.mod_category.controllers import mod_category
from app.mod_product.controllers import mod_product
from app.mod_admin.controllers import mod_admin

app.register_blueprint(mod_category)
app.register_blueprint(mod_product)
app.register_blueprint(mod_admin)


@app.errorhandler(404)
def not_found(error):
    return {"status": "not_found", "result": -1}, 404


@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(user_id)


@app.route('/')
def index():
    categories = [i.as_dict() for i in Category.query.all()]
    products = [i.as_dict() for i in Product.query.all()]
    return render_template(
        'index.html',
        _categories=categories,
        products=products
    )


db.create_all()
