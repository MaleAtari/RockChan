from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# # # CONFIG APP
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baza.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # # BAZA
db = SQLAlchemy(app)
Migrate(app, db)

# # # BLUEPRINTS
from meine.blog.views import blog_blueprint

app.register_blueprint(blog_blueprint, url_prefix='/blog')
