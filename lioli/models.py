from datetime import datetime
from email.policy import default
from lioli import db,migrate,login_manager


# # Adds required attributes and methods to our class
from flask_login import UserMixin




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    mobile_number = db.Column(db.String(10),nullable=False,unique=True)
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(120),unique=True)
    password = db.Column(db.String(60), nullable=False)
    is_active = db.Column(db.Boolean,nullable=False,default=True)
    permission = db.Column(db.Integer,default=1)
    date_added = db.Column(db.DateTime,default=datetime.utcnow,nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    product_name = db.Column(db.String(200))
    collection_id = db.Column(db.Integer,db.ForeignKey('collection.id'),nullable=False)
    surface_id =  db.Column(db.Integer,db.ForeignKey('surface.id'),nullable=False)
    thickness_id =  db.Column(db.Integer,db.ForeignKey('thickness.id'),nullable=False)
    size_id =  db.Column(db.Integer,db.ForeignKey('size.id'),nullable=False)
    product_image = db.Column(db.Text,nullable=False,default='default.jpg')
    preview = db.Column(db.String(30),nullable=False,default='default.jpg')
    is_deleted = db.Column(db.Boolean,default=False)


class Surface(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    surface = db.Column(db.String(200))



class Thickness(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    thickness = db.Column(db.String(200))



class Size(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    size = db.Column(db.String(200))
    size_image = db.Column(db.Text,nullable=False,default='default.jpg')
    order_by =  db.Column(db.Integer,default=0,nullable=True)


class Collection(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    collection = db.Column(db.String(200))
    


class Catalogue(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    pdf = db.Column(db.Text)
    preview = db.Column(db.Text,nullable=False,default='default.jpg')
    catalogue_name = db.Column(db.String(200))


class Gallery(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    link = db.Column(db.Text)
    preview = db.Column(db.Text,default='default.jpg')
    video = db.Column(db.Text)


class Career(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    post = db.Column(db.Text,nullable=False)
    location = db.Column(db.Text,nullable=False)
    experience =  db.Column(db.Text,nullable=False)
    salary =  db.Column(db.Text,nullable=False)
    description =  db.Column(db.Text,nullable=False)
    requirements =  db.Column(db.Text,nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)



class Resume(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    location = db.Column(db.Text)
    post = db.Column(db.Text)
    first_name = db.Column(db.Text,nullable=False)
    last_name = db.Column(db.Text,nullable=False)
    email = db.Column(db.Text,nullable=False)
    mobile = db.Column(db.Text,nullable=False)
    address = db.Column(db.Text,nullable=False)
    city = db.Column(db.Text,nullable=False)
    state = db.Column(db.Text,nullable=False)
    postal_code = db.Column(db.Text,nullable=False)
    resume = db.Column(db.Text,nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Download(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    full_name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    phone = db.Column(db.String(200))
    catalogue= db.Column(db.String(200))
    city = db.Column(db.Text)
    message = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Contact(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    assistence = db.Column(db.String(200))
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    phone = db.Column(db.String(200))
    profession= db.Column(db.String(200))
    representing_company= db.Column(db.String(200))
    city= db.Column(db.String(200))
    country = db.Column(db.Text)
    message = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)