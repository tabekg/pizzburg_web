from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.errorhandler(404)
def not_found(error):
    return {"status": "not_found", "result": -1}, 404


from app.mod_category.controllers import mod_category as category_module

app.register_blueprint(category_module)


@app.route('/')
def index():
    return render_template('index.html')


db.create_all()
