from flask import Flask
# ----------------- databases ---------------
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# --------------- login ------------
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


#---------------------- upload a picture --------------
import os
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/img/')



app=Flask(__name__)

app.config['SECRET_KEY']='mimlmimg7'

# ------------databases---------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resault.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#---------------- login-----------
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)

# -----------upload a picture-----------
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


from postd import routes