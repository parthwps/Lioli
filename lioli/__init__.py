import os
from flask import Flask,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail,Message





UPLOAD_FOLDER = '/static/admin/uploads/products/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['SECRET_KEY'] = 'fbd830be0e683acd1c8b1ee199adce24'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@127.0.0.1:3306/lioli_website'





db = SQLAlchemy(app)


migrate = Migrate(app,db)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "info.lioliceramica@gmail.com"
app.config['MAIL_PASSWORD'] = "touchmate3300"
mail = Mail(app)


from lioli.career.routes import career_bp
from lioli.blog.routes import blog_bp
from lioli.main.routes import main_bp
from lioli.product.routes import product_bp
from lioli.admin.routes import admin_bp
from lioli.errors.handlers import errors


app.register_blueprint(career_bp)
app.register_blueprint(blog_bp)
app.register_blueprint(main_bp)
app.register_blueprint(product_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(errors)



# from lioli import routes
