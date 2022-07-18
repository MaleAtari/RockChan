from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

login_manager = LoginManager()
app = Flask(__name__)

# # # CONFIG APP
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///baza.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # # BAZA
db = SQLAlchemy(app)
Migrate(app, db)

# # # BLUEPRINTS
from meine.chan.views import chan_blueprint
from meine.users.views import users_blueprint

app.register_blueprint(chan_blueprint, url_prefix='/chan')
app.register_blueprint(users_blueprint, url_prefix='/users')

# # # LOGIN MANAGER
login_manager.init_app(app)
