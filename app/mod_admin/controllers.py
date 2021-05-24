from flask import Blueprint, render_template, request, redirect, flash
from app.mod_admin.models import Admin
from app.mod_category.models import Category
from app.mod_product.models import Product
from app import bcrypt
from flask_login import login_user, current_user

mod_admin = Blueprint('admin', __name__, url_prefix='/admin')


@mod_admin.route('/')
def index():
    if current_user.is_authenticated:
        categories = Category.query.count()
        products = Product.query.count()
        admins = Admin.query.count()
        return render_template(
            'admin/index.html',
            admins=admins,
            products=products,
            categories=categories,
        )
    else:
        return render_template(
            'admin/login.html'
        )


@mod_admin.route('/password', methods=['GET'])
def password_get():
    password = request.args['password']
    return bcrypt.generate_password_hash(password)


@mod_admin.route('/login', methods=['POST'])
def login_post():
    phone_number = request.form['phone_number']
    password = request.form['password']

    user = Admin.query.filter_by(phone_number=phone_number).first()

    if user and bcrypt.check_password_hash(user.password_hash, password):
        flash('Добро пожаловать!')
        login_user(user, True)
    else:
        flash('Неверный телефон номер или пароль!')

    return redirect('/admin')
