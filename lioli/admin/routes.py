from flask import render_template, url_for, flash, redirect, request,Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from lioli.models import Download, Gallery, User,Product,Collection,Thickness,Size,Surface,Catalogue,Career,Resume,Contact
from lioli import app, db
from datetime import datetime, date
from datetime import date
from werkzeug.utils import secure_filename
import secrets
from PIL import Image
import secrets
import os



now = datetime.now()
today = date.today()
current_time = now.strftime("%H:%M:%S")

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

        

admin_bp = Blueprint('admin',__name__)





# --------------------- ADMIN Users---------------------------




@admin_bp.route('/admin/users')
def users():
    if current_user.is_authenticated:
        if current_user.permission == 0:

            users = User.query.all()
            return render_template('admin/users.html',users=users)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))


@admin_bp.route('/admin/deactivate_user/<int:user_id>')
def deactivate_user(user_id):
    if current_user.is_authenticated:
        if current_user.permission == 0:
            user = User.query.filter_by(id=user_id).first()
            user.is_active = False
            db.session.commit()
            flash('Your Users is Deativate!','success')
            return redirect(request.referrer)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))



@admin_bp.route('/admin/activate_user/<int:user_id>')
def activate_user(user_id):
    if current_user.is_authenticated:
        if current_user.permission == 0:
            user = User.query.filter_by(id=user_id).first()
            user.is_active = True
            db.session.commit()
            flash('Your users is Activate!','success')
            return redirect(request.referrer)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))



@admin_bp.route('/admin/delete_user/<int:user_id>',methods=['POST','GET'])
def delete_user(user_id):
    if current_user.is_authenticated:
        if current_user.permission == 0:
            user = User.query.filter_by(id=user_id).first()
            db.session.delete(user)
            db.session.commit()
            flash('Your User is deleted!','success')
            return redirect(request.referrer)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))


@admin_bp.route('/admin/add_user',methods=['POST','GET'])
def add_user():
    if current_user.is_authenticated:
        if current_user.permission == 0:
            if request.method == 'POST':
                first_name = request.form.get('first_name')
                last_name = request.form.get('last_name')
                mobile_number = request.form.get('mobile_number')
                email = request.form.get('email')
                password = request.form.get('password')
                permission = request.form.get('permission')
                conpassword = request.form.get('conpassword')
                if password == conpassword:
                    user = User(first_name=first_name,last_name=last_name,mobile_number=mobile_number,email=email,password=password,permission=permission,date_added=today)
                    db.session.add(user)
                    db.session.commit()
                    if user:
                        flash('Your User Is Added !','success')
                        return redirect(url_for('admin.users'))
                    else:
                        flash('Unable To Add User !','danger')
                        return redirect(request.referrer)
                else:
                    flash('Password Does Not Mach !','danger')
                    return redirect(request.referrer)
            return render_template('admin/add-user.html')
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))
        
        





@admin_bp.route('/admin/edit_user/<int:user_id>',methods=['POST','GET'])
def edit_user(user_id):
    if current_user.is_authenticated:
        if current_user.permission == 0:
                
            user = User.query.filter_by(id=user_id).first()
            if request.method == 'POST':
                user = User.query.filter_by(id=user_id).first()
                user.first_name = request.form.get('first_name')
                user.last_name = request.form.get('last_name')
                user.email = request.form.get('email')
                user.mobile_number = request.form.get('mobile_number')
                user.permission = request.form.get('permission')
                password= request.form.get('password')
                conpassword= request.form.get('conpassword')
                if password != user.password:
                    if password == conpassword:
                        user.password= password
                        db.session.commit()
                        return redirect(url_for('admin.users'))
                    else:
                        flash('Password Does Not Mach !','danger')
                        return redirect(request.referrer)
                db.session.commit()
                return redirect(url_for('admin.users'))
            return render_template('admin/add-user.html',user=user,user_id=user_id)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
        
    else:
        return redirect(url_for('admin.admin_login'))
    

















# def save_picture(form_picture,picture_path):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(form_picture.filename)
#     picture_fn = random_hex + f_ext
#     picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

#     output_size = (125, 125)
#     i = Image.open(form_picture)
#     i.thumbnail(output_size)
#     i.save(picture_path)

#     return picture_fn












@admin_bp.route("/admin", methods=['GET', 'POST'])
def admin():
    if current_user.is_authenticated:
        return render_template('admin/dashbord.html')
    else:
        return redirect(url_for('admin.admin_login'))


@admin_bp.route("/admin/login", methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.admin'))

    elif request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password') 
        
        user = User.query.filter_by(email=email).first()
        if user and password==user.password and user.is_active == True:
            flash('Login SucessFull', 'success')
            login_user(user)
            return redirect(url_for('admin.admin'))
        else:
            flash('Login Unsuccessful. Please Check Email And Password or Contact To The Administrator', 'danger')
            return render_template('admin/login.html', title='Login')
    return render_template('admin/login.html', title='Login')
            






@admin_bp.route("/admin/logout")
def admin_logout():
    logout_user()
    return redirect(url_for('admin.admin_login'))




# ====================================== COLLECTION =======================================


@admin_bp.route("/admin/collection")
def collection():
    if current_user.is_authenticated:
        if current_user.permission != 3:

            collection = Collection.query.all()
            return render_template('admin/collection.html', title='Collection',collections=collection)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    
    else:
        return redirect(url_for('admin.admin_login'))




@admin_bp.route("/admin/add_collection",methods=['POST','GET'])
def add_collection():
    if current_user.is_authenticated:
        if current_user.permission != 3:
            if request.method == 'POST':
                collection_name = request.form.get('collection_name')
                collection = Collection(collection=collection_name)
                db.session.add(collection)
                db.session.commit() 
                if collection:
                    flash('Your Collection Is Added !','success')
                    return redirect(url_for('admin.collection'))
                else:
                    flash('Unable To Add Collection !','danger')
                    return redirect(request.referrer)
            return render_template('admin/add-collection.html')
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))



@admin_bp.route('/admin/edit_collection/<int:collection_id>',methods=['POST','GET'])
def edit_collection(collection_id):
    if current_user.is_authenticated:
        if current_user.permission != 3:
            print(collection_id)
            collection = Collection.query.filter_by(id=collection_id).first()
            if request.method == 'POST':
                collection = Collection.query.filter_by(id=collection_id).first()
                collection.collection = request.form.get('collection_name')
                db.session.commit()
                return redirect(url_for('admin.collection'))
            return render_template('admin/add-collection.html',collection_id=collection.id,collection=collection)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))




@admin_bp.route('/admin/delete_collection/<int:collection_id>',methods=['POST','GET'])
def delete_collection(collection_id):
    if current_user.is_authenticated:
        if current_user.permission != 3:
            print(collection_id)
            collection = Collection.query.filter_by(id=collection_id).first()
            product = Product.query.filter_by(collection_id=collection_id)
            products = []
            for product_id in product:
                products.append(product_id.id)
            if len(products) == 0:
                db.session.delete(collection)
                db.session.commit()
                flash('Your collection is deleted!','success')
                return redirect(request.referrer)
            else:
                flash('First Delete The Product Of This Collection!','danger')
                return redirect(request.referrer)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))




















# ====================================== Surface =======================================


@admin_bp.route("/admin/surface")
def surface():
    if current_user.is_authenticated:
        if current_user.permission != 3:
            surface = Surface.query.all()
            return render_template('admin/surface.html', title='Finish',surfaces=surface)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))




@admin_bp.route("/admin/add_surface",methods=['POST','GET'])
def add_surface():
    if current_user.is_authenticated:
        if current_user.permission != 3:
            if request.method == 'POST':
                surface_name = request.form.get('surface_name')
                surface = Surface(surface=surface_name)
                db.session.add(surface)
                db.session.commit() 
                if surface:
                    flash('Your Finish Is Added !','success')
                    return redirect(url_for('admin.surface'))
                else:
                    flash('Unable To Add Finish !','danger')
                    return redirect(request.referrer)
            return render_template('admin/add-surface.html')
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))



@admin_bp.route('/admin/edit_surface/<int:surface_id>',methods=['POST','GET'])
def edit_surface(surface_id):
    if current_user.is_authenticated:
        if current_user.permission != 3:

            print(surface_id)
            surface = Surface.query.filter_by(id=surface_id).first()
            if request.method == 'POST':
                surface = Surface.query.filter_by(id=surface_id).first()
                surface.surface = request.form.get('surface_name')
                db.session.commit()
                return redirect(url_for('admin.surface'))
            return render_template('admin/add-surface.html',surface_id=surface.id,surface=surface)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))




@admin_bp.route('/admin/delete_surface/<int:surface_id>',methods=['POST','GET'])
def delete_surface(surface_id):
    if current_user.is_authenticated:
        if current_user.permission != 3:
            print(surface_id)
            surface = Surface.query.filter_by(id=surface_id).first()
            product = Product.query.filter_by(surface_id=surface_id)
            products = []
            for product_id in product:
                products.append(product_id.id)
            if len(products) == 0:
                db.session.delete(surface)
                db.session.commit()
                flash('Your Finish is deleted!','success')
                return redirect(request.referrer)
            else:
                flash('First Delete The Product Of This Finish!','danger')
                return redirect(request.referrer)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))



# ====================================== Thickness =======================================


@admin_bp.route("/admin/thickness")
def thickness():
    if current_user.is_authenticated:
        if current_user.permission != 3:
            thickness = Thickness.query.all()
            return render_template('admin/thickness.html', title='Finish',thicknesses=thickness)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))




@admin_bp.route("/admin/add_thickness",methods=['POST','GET'])
def add_thickness():
    if current_user.is_authenticated:
        if current_user.permission != 3:
            if request.method == 'POST':
                thickness_name = request.form.get('thickness_name')
                thickness = Thickness(thickness=thickness_name)
                db.session.add(thickness)
                db.session.commit() 
                if thickness:
                    flash('Your Thickness Is Added !','success')
                    return redirect(url_for('admin.thickness'))
                else:
                    flash('Unable To Add Thickness !','danger')
                    return redirect(request.referrer)
            return render_template('admin/add-thickness.html')
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))



@admin_bp.route('/admin/edit_thickness/<int:thickness_id>',methods=['POST','GET'])
def edit_thickness(thickness_id):
    if current_user.is_authenticated:
        if current_user.permission != 3:
            print(thickness_id)
            thickness = Thickness.query.filter_by(id=thickness_id).first()
            if request.method == 'POST':
                thickness = thickness.query.filter_by(id=thickness_id).first()
                thickness.thickness = request.form.get('thickness_name')
                db.session.commit()
                return redirect(url_for('admin.thickness'))
            return render_template('admin/add-thickness.html',thickness_id=thickness.id,thickness=thickness)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))




@admin_bp.route('/admin/delete_thickness/<int:thickness_id>',methods=['POST','GET'])
def delete_thickness(thickness_id):
    if current_user.is_authenticated:
        if current_user.permission != 3:
            print(thickness_id)
            thickness = Thickness.query.filter_by(id=thickness_id).first()
            product = Product.query.filter_by(thickness_id=thickness_id)
            products = []
            for product_id in product:
                products.append(product_id.id)
            if len(products) == 0:
                db.session.delete(thickness)
                db.session.commit()
                flash('Your Thickness is deleted!','success')
                return redirect(request.referrer)
            else:
                flash('First Delete The Product Of This Thickness!','danger')
                return redirect(request.referrer)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))
















# ====================================== Sizes =======================================


@admin_bp.route("/admin/size")
def admin_size():
    if current_user.is_authenticated:
        if current_user.permission != 3:
            size = Size.query.all()
            return render_template('admin/size.html', title='Finish',sizes=size)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))




@admin_bp.route("/admin/add_size",methods=['POST','GET'])
def add_size():
    if current_user.is_authenticated:
        if current_user.permission != 3:
            if request.method == 'POST':
                size_name = request.form.get('size_name')
                size_image = request.files['size_image']
                size_order = Size.query.order_by(Size.order_by.desc()).first()
                order_by = int(size_order.order_by)+1
                if size_image:
                    random_hex = secrets.token_hex(8)
                    _, f_ext = os.path.splitext(size_image.filename)
                    picture_fn = random_hex + f_ext
                    picture_path = os.path.join(app.root_path, 'static/admin/uploads/size', picture_fn)
                    i = Image.open(size_image)
                    i.save(picture_path)
                    size = Size(size = size_name,size_image=picture_fn,order_by=order_by)
                    db.session.add(size)
                    db.session.commit()
                    if size:
                        flash('Your Size Is Added !','success')
                        return redirect(url_for('admin.admin_size'))
                    else:
                        flash('Unable To Add Size !','danger')
                        return redirect(request.referrer)
                else:
                    flash('Please Check The Uploaded File Properly','danger')
                    return redirect(request.referrer)
            return render_template('admin/add-size.html')
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))





@admin_bp.route("/admin/edit_size/<int:size_id>",methods=['POST','GET'])
def edit_size(size_id):
    if current_user.is_authenticated:
        if current_user.permission != 3:
            size = Size.query.filter_by(id=size_id).first()
            if request.method == 'POST':
                size = Size.query.filter_by(id=size_id).first()
                size.order_by = request.form.get('order_by')
                size.size = request.form.get('size_name')
                size_image = request.files.get('size_image')
                if size_image:
                    if os.path.isfile(os.path.join(app.root_path, 'static/admin/uploads/size', size.size_image)):
                        os.remove(os.path.join(app.root_path, 'static/admin/uploads/size', size.size_image))
                    random_hex = secrets.token_hex(8)
                    _, f_ext = os.path.splitext(size_image.filename)
                    picture_fn = random_hex + f_ext
                    picture_path = os.path.join(app.root_path, 'static/admin/uploads/size', picture_fn)
                    i = Image.open(size_image)
                    i.save(picture_path)

                    size.size_image=picture_fn
                else:
                    size.size_image = size.size_image
                db.session.commit()
                return redirect(url_for('admin.admin_size'))
            return render_template('admin/add-size.html',size=size,size_id=size_id)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)        
    else:
        return redirect(url_for('admin.admin_login'))




@admin_bp.route('/admin/delete_size/<int:size_id>',methods=['POST','GET'])
def delete_size(size_id):
    if current_user.is_authenticated:
        if current_user.permission:
            print(size_id)
            size = Size.query.filter_by(id=size_id).first()
            product = Product.query.filter_by(size_id=size_id)
            products = []
            for product_id in product:
                products.append(product_id.id)
            if len(products) == 0:
                if os.path.isfile(os.path.join(app.root_path, 'static/admin/uploads/size', size.size_image)):
                    os.remove(os.path.join(app.root_path, 'static/admin/uploads/size', size.size_image))
                db.session.delete(size)
                db.session.commit()
                flash('Your Size is deleted!','success')
                return redirect(request.referrer)
            else:
                flash('First Delete The Product Of This Size!','danger')
                return redirect(request.referrer)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))









# ====================================== Products =======================================


@admin_bp.route("/admin/product")
def product():
    if current_user.is_authenticated:
        if current_user.permission != 3:
            size = Size.query.all()
            collection = Collection.query.all()
            thickness = Thickness.query.all()
            surface = Surface.query.all()
            product = Product.query.all()
            return render_template('admin/products.html', title='Finish',sizes=size,collections=collection,thicknesses=thickness,surfaces=surface,products=product)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)    
    else:
        return redirect(url_for('admin.admin_login'))







@admin_bp.route("/admin/add_product",methods=['POST','GET'])
def add_product():
    if current_user.is_authenticated:
        if current_user.permission != 3:
            size = Size.query.all()
            collection = Collection.query.all()
            thickness = Thickness.query.all()
            surface = Surface.query.all()
            if request.method == 'POST':
                product_name = request.form.get('product_name')
                collection_name = request.form.get('collection_name')
                thickness_name = request.form.get('thickness_name')
                size_name = request.form.get('size_name')
                surface_name = request.form.get('surface_name')  
                uploaded_files = request.files.getlist("file[]")
                filenames = []
                random_hex = secrets.token_hex(4)
                for file in uploaded_files:
                    if file and allowed_file(file.filename):
                        filename = random_hex+secure_filename(file.filename)
                        file.save(os.path.join(app.root_path, 'static/admin/uploads/product/random', filename))
                        filenames.append(filename)
                xxx = filenames
                produc_img = ','.join(map(str, xxx))       
                preview = request.files['preview']
                if preview:
                    random_hex = secrets.token_hex(8)
                    _, f_ext = os.path.splitext(preview.filename)
                    picture_fn = random_hex + f_ext
                    picture_path = os.path.join(app.root_path, 'static/admin/uploads/product/preview', picture_fn)
                    i = Image.open(preview)
                    i.save(picture_path)
                    product = Product(product_name=product_name,product_image=produc_img,collection_id=collection_name,thickness_id=thickness_name,size_id=size_name,surface_id=surface_name, preview=picture_fn)
                        
                    db.session.add(product)
                    db.session.commit()
                    if product:
                        flash('Your Product Is Added !','success')
                        return redirect(url_for('admin.product'))
                    else:
                        flash('Unable To Add Product !','danger')
                        return redirect(request.referrer)
                else:
                    flash('Please Check The Uploaded File Properly','danger')
                    return redirect(request.referrer)
            return render_template('admin/add-products.html',sizes=size,collections=collection,thicknesses=thickness,surfaces=surface)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))








@admin_bp.route('/admin/edit_product/<int:product_id>',methods=['POST','GET'])
def edit_product(product_id):
    if current_user.is_authenticated:
        if current_user.permission != 3:
            size = Size.query.all()
            collection = Collection.query.all()
            thickness = Thickness.query.all()
            surface = Surface.query.all()
            product = Product.query.filter_by(id=product_id).first()
            product_images=product.product_image.split(',')
            if request.method == 'POST':
                product = Product.query.filter_by(id=product_id).first()
                product.product_name = request.form.get('product_name')
                product.collection_id = request.form.get('collection_name')
                product.thickness_id = request.form.get('thickness_name')
                product.size_id = request.form.get('size_name')
                product.surface_id = request.form.get('surface_name')
                product.product_quantity = request.form.get('product_quantity')
                random_hex = secrets.token_hex(4)
                uploaded_files = request.files.getlist("file[]")
                filenames = []
                for file in uploaded_files:
                    if file and allowed_file(file.filename):
                        filename = random_hex+secure_filename(file.filename)
                        file.save(os.path.join(app.root_path, 'static/admin/uploads/product/random', filename))
                        filenames.append(filename)
                xxx = filenames
                produc_img = ','.join(map(str, xxx))
                if produc_img :
                    if product.product_image == '':
                        product.product_image +=produc_img
                    else:
                        product.product_image +=','+produc_img
                else:
                    product.product_image = product.product_image
                preview = request.files.get('preview')
                if preview:
                    if os.path.isfile(os.path.join(app.root_path, 'static/admin/uploads/product/preview', product.preview)):
                        os.remove(os.path.join(app.root_path, 'static/admin/uploads/product/preview', product.preview))
                    random_hex = secrets.token_hex(8)
                    _, f_ext = os.path.splitext(preview.filename)
                    picture_fn = random_hex + f_ext
                    picture_path = os.path.join(app.root_path, 'static/admin/uploads/product/preview', picture_fn)
                    i = Image.open(preview)
                    i.save(picture_path)
                    product.preview=picture_fn
                else:
                    product.preview = product.preview
                db.session.commit()
                return redirect(url_for('admin.product'))
            return render_template('admin/add-products.html',sizes=size,collections=collection,thicknesses=thickness,surfaces=surface,products=product,product_id=product_id,product_images=product_images)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))




@admin_bp.route('/admin/delete_tile/<int:product_id>/<string:image>',methods=['POST','GET'])
def delete_tiles(product_id,image):
    if current_user.is_authenticated:
        if current_user.permission != 3:
            product = Product.query.filter_by(id=product_id).first()
            product_images=product.product_image.split(',')
            product_images.remove(image)
            product_image = ','.join(map(str, product_images))
            if os.path.isfile(os.path.join(app.root_path, 'static/admin/uploads/product/random', image)):
                os.remove(os.path.join(app.root_path, 'static/admin/uploads/product/random', image))
            product.product_image = product_image
            db.session.commit()
            flash('Your Tile is deleted!','success')
            return redirect(request.referrer)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))








@admin_bp.route('/admin/delete_product/<int:product_id>',methods=['POST','GET'])
def delete_products(product_id):
    if current_user.is_authenticated:
        if current_user.permission != 3:
            product = Product.query.filter_by(id=product_id).first()
            product_image = product.product_image.split(',')
            preview = product.preview
            product.is_deleted = True
            # for image in product_image:
            # 	os.remove(os.path.join(app.root_path, 'static/admin/uploads/products', image))
            # os.remove(os.path.join(app.root_path, 'static/admin/uploads/products', preview))
            # os.rmdir(os.path.join(app.root_path, 'static/admin/uploads/products', product.product_name))
            # db.session.delete(product)
            db.session.commit()
            flash('Your product is deleted!','success')
            return redirect(request.referrer)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))











# ======================= DOWNLOAD ADMIN ============================================






@admin_bp.route('/admin/catalogue')
def catalogue():
    if current_user.is_authenticated:
        if current_user.permission != 3:
            catalogue = Catalogue.query.all()
            return render_template('admin/catalogue.html',catalogues=catalogue)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))










@admin_bp.route('/admin/delete_catalogue/<int:catalogue_id>',methods=['POST','GET'])
def delete_catalogue(catalogue_id):
    if current_user.is_authenticated:
        if current_user.permission != 3:
            catalogue = Catalogue.query.filter_by(id=catalogue_id).first()
            if os.path.isfile(os.path.join(app.root_path, 'static/admin/uploads/catalogue/preview', catalogue.preview)):
                    os.remove(os.path.join(app.root_path, 'static/admin/uploads/catalogue/preview', catalogue.preview))
            if os.path.isfile(os.path.join(app.root_path, 'static/admin/uploads/catalogue/pdf', catalogue.pdf)):
                    os.remove(os.path.join(app.root_path, 'static/admin/uploads/catalogue/pdf', catalogue.pdf))
            db.session.delete(catalogue)
            db.session.commit()
            flash('Your catalogue is deleted!','success')
            return redirect(request.referrer)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))



@admin_bp.route('/admin/add_catalogue',methods=['POST','GET'])
def add_catalogue():
    if current_user.is_authenticated:
        if current_user.permission != 3:
            if request.method == 'POST':
                catalogue_name = request.form.get('catalogue_name')
                preview = request.files['preview']
                pdf = request.files['pdf']
                if preview and pdf:
                    random_hex = secrets.token_hex(8)
                    _, f_ext = os.path.splitext(preview.filename)
                    picture_fn = random_hex + f_ext
                    picture_path = os.path.join(app.root_path, 'static/admin/uploads/catalogue/preview', picture_fn)
                    i = Image.open(preview)
                    i.save(picture_path)
                    pdf_name = secure_filename(pdf.filename)
                    pdf.save(os.path.join(app.root_path, 'static/admin/uploads/catalogue/pdf', pdf_name))
                    catalogue = Catalogue(catalogue_name=catalogue_name,preview=picture_fn,pdf=pdf_name)
                    db.session.add(catalogue)
                    db.session.commit()
                    if catalogue:
                        flash('Your Catalogue Is Added !','success')
                        return redirect(url_for('admin.catalogue'))
                    else:
                        flash('Unable To Add Catalogue !','danger')
                        return redirect(request.referrer)

                else:
                    flash('Please Check The Uploaded File Properly','danger')
                    return redirect(request.referrer)
            
            return render_template('admin/add-catalogue.html')
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))





@admin_bp.route('/admin/edit_catalogue/<int:catalogue_id>',methods=['POST','GET'])
def edit_catalogue(catalogue_id):
    if current_user.is_authenticated:
        if current_user.permission != 3:
            catalogue = Catalogue.query.filter_by(id=catalogue_id).first()
            if request.method == 'POST':
                catalogue = catalogue.query.filter_by(id=catalogue_id).first()
                catalogue.catalogue_name = request.form.get('catalogue_name')
                preview = request.files.get('preview')
                if preview:
                    if os.path.isfile(os.path.join(app.root_path, 'static/admin/uploads/catalogue/preview', catalogue.preview)):
                        os.remove(os.path.join(app.root_path, 'static/admin/uploads/catalogue/preview', catalogue.preview))
                    random_hex = secrets.token_hex(8)
                    _, f_ext = os.path.splitext(preview.filename)
                    picture_fn = random_hex + f_ext
                    picture_path = os.path.join(app.root_path, 'static/admin/uploads/catalogue/preview', picture_fn)
                    i = Image.open(preview)
                    i.save(picture_path)
                    catalogue.preview=picture_fn
                else:
                    catalogue.preview = catalogue.preview

                pdf = request.files.get('pdf')
                if pdf:
                    if os.path.isfile(os.path.join(app.root_path, 'static/admin/uploads/catalogue/pdf', catalogue.pdf)):
                        os.remove(os.path.join(app.root_path, 'static/admin/uploads/catalogue/pdf', catalogue.pdf))
                    pdf_name = secure_filename(pdf.filename)
                    pdf.save(os.path.join(app.root_path, 'static/admin/uploads/catalogue/pdf', pdf_name))
                    catalogue.pdf = pdf_name
                else:
                    catalogue.pdf = catalogue.pdf
                db.session.commit()

                return redirect(url_for('admin.catalogue'))
            

            return render_template('admin/add-catalogue.html',catalogue=catalogue,catalogue_id=catalogue_id)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))






# ======================= Gallery ADMIN ============================================






@admin_bp.route('/admin/gallery')
def admin_gallery():
    if current_user.is_authenticated:
        if current_user.permission != 3:
            gallery = Gallery.query.all()
            return render_template('admin/gallery.html',gallerys=gallery)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))




@admin_bp.route('/admin/add_gallery/<int:type>',methods=['POST','GET'])
def add_gallery(type):
    if current_user.is_authenticated:
        if current_user.permission != 3:
            if type == 0:
                if request.method == 'POST':
                    link = request.form.get('link')
                    gallery = Gallery(link=link)
                    db.session.add(gallery)
                    db.session.commit()
                    if gallery:
                        flash('Your Video Is Added !','success')
                        return redirect(url_for('admin.admin_gallery'))
                    else:
                        flash('Unable To Add Catalogue !','danger')
                        return redirect(request.referrer)
                return render_template('admin/add-link-gallery.html')
            elif type == 1:
                if request.method == 'POST':
                    preview = request.files['preview']
                    video = request.files['video']
                    if preview and video:
                        random_hex = secrets.token_hex(8)
                        _, f_ext = os.path.splitext(preview.filename)
                        picture_fn = random_hex + f_ext
                        picture_path = os.path.join(app.root_path, 'static/admin/uploads/gallery/preview', picture_fn)
                        i = Image.open(preview)
                        i.save(picture_path)
                        video_name = secure_filename(video.filename)
                        video.save(os.path.join(app.root_path, 'static/admin/uploads/gallery/video', video_name))
                        gallery = Gallery(preview=picture_fn,video=video_name)
                        db.session.add(gallery)
                        db.session.commit()
                        if gallery:
                            flash('Your Video Is Added !','success')
                            return redirect(url_for('admin.admin_gallery'))
                        else:
                            flash('Unable To Add Video !','danger')
                            return redirect(request.referrer)
                return render_template('admin/add-video-gallery.html')
            else:
                flash('Video Type Is Not Perfect !','success')
                return redirect(url_for('admin.admin_gallery'))
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))

                    






@admin_bp.route('/admin/edit_gallery/<int:gallery_id>',methods=['POST','GET'])
def edit_gallery(gallery_id):
    if current_user.is_authenticated:
        if current_user.permission != 3:
            gallery = Gallery.query.filter_by(id =gallery_id).first()
            if gallery.link == '' or gallery.link == None:
                if request.method == 'POST':
                    gallery = Gallery.query.filter_by(id =gallery_id).first()
                    preview = request.files.get('preview')
                    if preview:
                        if os.path.isfile(os.path.join(app.root_path, 'static/admin/uploads/gallery/preview', gallery.preview)):
                            os.remove(os.path.join(app.root_path, 'static/admin/uploads/gallery/preview', gallery.preview))
                        random_hex = secrets.token_hex(8)
                        _, f_ext = os.path.splitext(preview.filename)
                        picture_fn = random_hex + f_ext
                        picture_path = os.path.join(app.root_path, 'static/admin/uploads/gallery/preview', picture_fn)
                        i = Image.open(preview)
                        i.save(picture_path)
                        gallery.preview=picture_fn
                    else:
                        gallery.preview = gallery.preview

                    video = request.files.get('video')
                    if video:
                        if os.path.isfile(os.path.join(app.root_path, 'static/admin/uploads/gallery/video', gallery.video)):
                            os.remove(os.path.join(app.root_path, 'static/admin/uploads/gallery/video', gallery.video))
                        video_name = secure_filename(video.filename)
                        video.save(os.path.join(app.root_path, 'static/admin/uploads/gallery/video', video_name))
                        gallery.video = video_name
                    else:
                        gallery.video = gallery.video
                    db.session.commit()

                    return redirect(url_for('admin.admin_gallery'))
                
                return render_template('admin/add-video-gallery.html',gallery=gallery,gallery_id=gallery_id)
                
            else:
                if request.method == 'POST':
                    gallery = Gallery.query.filter_by(id =gallery_id).first()
                    gallery.link = request.form.get('link')
                    db.session.commit()
                    return redirect(url_for('admin.admin_gallery'))
                return render_template('admin/add-link-gallery.html',gallery=gallery,gallery_id=gallery_id)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))



@admin_bp.route('/admin/delete_gallery/<int:gallery_id>',methods=['POST','GET'])
def delete_gallery(gallery_id):
    if current_user.is_authenticated:
        if current_user.permission != 3:
            gallery = Gallery.query.filter_by(id=gallery_id).first()
            if gallery.link == '' or gallery.link == None:
                if os.path.isfile(os.path.join(app.root_path, 'static/admin/uploads/gallery/preview', gallery.preview)):
                        os.remove(os.path.join(app.root_path, 'static/admin/uploads/gallery/preview', gallery.preview))
                if os.path.isfile(os.path.join(app.root_path, 'static/admin/uploads/gallery/video', gallery.video)):
                        os.remove(os.path.join(app.root_path, 'static/admin/uploads/gallery/video', gallery.video))
                db.session.delete(gallery)
                db.session.commit()
                flash('Your gallery is deleted!','success')
                return redirect(request.referrer)
            else:
                db.session.delete(gallery)
                db.session.commit()
                flash('Your gallery is deleted!','success')
                return redirect(request.referrer)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))










# ======================= CAREER ADMIN ============================================


@admin_bp.route("/admin/career",methods=['POST','GET'])
def career():
    if current_user.is_authenticated:
        if current_user.permission != 2:
            career = Career.query.all()
            return render_template('admin/career.html', title='Career',careers=career)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))





@admin_bp.route("/admin/add_career",methods=['POST','GET'])
def add_career():
    if current_user.is_authenticated:
        if current_user.permission != 2:
            if request.method == 'POST':
                post = request.form.get('post')
                experience = request.form.get('experience')
                salary = request.form.get('salary')
                location = request.form.get('location')
                description = request.form.get('description')
                requirements = request.form.get('requirements')
                career = Career(post=post,experience=experience,salary=salary,description=description,requirements=requirements,location=location)
                db.session.add(career)
                db.session.commit()
                if career:
                    flash('Your Post Is Added !','success')
                    return redirect(url_for('admin.career'))
                else:
                    flash('Unable To Add Post !','danger')
                    return redirect(request.referrer)

            return render_template('admin/add-career.html', title='Add Career')
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))




@admin_bp.route("/admin/edit_career/<int:career_id>",methods=['POST','GET'])
def edit_career(career_id):
    if current_user.is_authenticated:
        if current_user.permission != 2:
            career = Career.query.filter_by(id=career_id).first()
            if request.method == 'POST':
                career = Career.query.filter_by(id=career_id).first()
                career.post = request.form.get('post')
                career.experience = request.form.get('experience')
                career.salary = request.form.get('salary')
                career.location = request.form.get('location')
                career.description = request.form.get('description')
                career.requirements = request.form.get('requirements')
                db.session.commit()
            
                flash('Your Post Is Updated !','success')
                return redirect(url_for('admin.career'))
            

            return render_template('admin/add-career.html', title='Add Career',career=career,career_id=career_id)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))



@admin_bp.route("/admin/delete_career/<int:career_id>",methods=['POST','GET'])
def delete_career(career_id):
    if current_user.is_authenticated:
        if current_user.permission != 2:
            career = Career.query.filter_by(id=career_id).first()
            db.session.delete(career)
            db.session.commit()
            flash('Your Post is deleted!','success')
            return redirect(request.referrer)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))






# ======================= CAREER ADMIN ============================================


@admin_bp.route("/admin/resume",methods=['POST','GET'])
def resume():
    if current_user.is_authenticated:
        if current_user.permission != 2:
            resume = Resume.query.all()
            return render_template('admin/resume.html', title='resume',resumes=resume)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)    
    else:
        return redirect(url_for('admin.admin_login'))



@admin_bp.route('/admin/delete_resume/<int:resume_id>',methods=['POST','GET'])
def delete_resume(resume_id):
    if current_user.is_authenticated:
        if current_user.permission != 2:
            resume = Resume.query.filter_by(id=resume_id).first()
            
            if os.path.isfile(os.path.join(app.root_path, 'static/admin/uploads/resume', resume.resume)):
                os.remove(os.path.join(app.root_path, 'static/admin/uploads/resume', resume.resume))
            
            db.session.delete(resume)
            db.session.commit()
            flash('Resume is deleted!','success')
            return redirect(request.referrer)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))







# ======================= DOWNLOAD CATALOGUE ADMIN ============================================


@admin_bp.route("/admin/download_details",methods=['POST','GET'])
def download_details():
    if current_user.is_authenticated:
        if current_user.permission != 2:
            download = Download.query.all()
            return render_template('admin/download_details.html', title='download',downloads=download)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)    
    else:
        return redirect(url_for('admin.admin_login'))



@admin_bp.route('/admin/delete_download_details/<int:download_details_id>',methods=['POST','GET'])
def delete_download_details(download_details_id):
    if current_user.is_authenticated:
        if current_user.permission != 2:
            download_details = Download.query.filter_by(id=download_details_id).first()
            

            db.session.delete(download_details)
            db.session.commit()
            flash('Download Details is deleted!','success')
            return redirect(request.referrer)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))




# ======================= DOWNLOAD CATALOGUE ADMIN ============================================


@admin_bp.route("/admin/contact_details",methods=['POST','GET'])
def contact_details():
    if current_user.is_authenticated:
        if current_user.permission != 2:
            contact = Contact.query.all()
            return render_template('admin/contact_details.html', title='contacts',contacts=contact)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)    
    else:
        return redirect(url_for('admin.admin_login'))



@admin_bp.route('/admin/delete_contact_details/<int:contact_details_id>',methods=['POST','GET'])
def delete_contact_details(contact_details_id):
    if current_user.is_authenticated:
        if current_user.permission != 2:
            contact_details = Contact.query.filter_by(id=contact_details_id).first()
            

            db.session.delete(contact_details)
            db.session.commit()
            flash('Contact Details is deleted!','success')
            return redirect(request.referrer)
        else:
            flash('You Do Not Have Aceess This Page !','success')
            return redirect(request.referrer)
    else:
        return redirect(url_for('admin.admin_login'))