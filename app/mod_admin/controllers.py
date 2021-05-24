from flask import Blueprint, render_template, request, redirect, flash
from app.mod_admin.models import Admin
from app.mod_category.models import Category
from app.mod_product.models import Product
from app import bcrypt
from flask_login import login_user, current_user, login_required

mod_admin = Blueprint('admin', __name__, url_prefix='/admin')


@mod_admin.route('/')
def index_get():
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


@mod_admin.route('/products')
@login_required
def products_get():
    count = Product.query.count()
    items = Product.query.all()
    return render_template(
        'admin/products.html',
        count=count,
        items=items,
    )


@mod_admin.route('/categories')
@login_required
def categories_get():
    count = Category.query.count()
    items = Category.query.all()
    return render_template(
        'admin/categories.html',
        count=count,
        items=items,
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
