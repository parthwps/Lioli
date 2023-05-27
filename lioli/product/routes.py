from distutils.log import error
from email import message
from flask import render_template, request,Blueprint,json
from lioli.models import Product,Collection,Thickness,Size,Surface
from datetime import datetime, date
from datetime import date


now = datetime.now()
today = date.today()
current_time = now.strftime("%H:%M:%S")

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


product_bp = Blueprint('product',__name__)







@product_bp.route("/search",methods=['GET','POST'])
def search():
    if request.method== 'POST':
        data = request.form.get('search')
        product = Product.query.filter(Product.product_name.like('%'+data+'%')).all()
        unq_list = []
        for x in product:
            if x.product_name not in unq_list:
                unq_list.append(x.product_name)
        print(unq_list)
        product_list = []
        for p in unq_list:
            products = Product.query.filter_by(product_name = p).first()
            product_list.append(products)
        print(product_list)
        product_size = Size.query.order_by(Size.order_by.asc()).all()
        print("\n\n\n",product)
        if not product:
            size = Size.query.filter(Size.size.like('%'+data+'%')).all()
            print("\n\n\n",size)
            if not size:
                return render_template('search.html',title='Search List',data=data)
            return render_template('search.html',title='Search List',sizes=size,data=data)
        return render_template('search.html',title='Search List',products=product_list,data=data,product_sizes=product_size)

@product_bp.route("/product/sizes")
def size():
    sizes = Size.query.order_by(Size.order_by.asc()).all()
    return render_template('size.html',sizes=sizes)



@product_bp.route("/product/<size>", methods=['GET', 'POST'])
def products(size):
    print(size)
    size_id = Size.query.filter_by(size=size).first()
    collections = Collection.query.all()
    sizes = Size.query.order_by(Size.order_by.asc()).all()
    thicknesses = Thickness.query.all()
    finishes = Surface.query.all()
    # products = Product.query.filter_by(size_id = size_id.id)
    products = Product.query.filter_by(size_id = size_id.id)
    latest_products = Product.query.order_by(Product.id.desc()).limit(12).all()
    product_id_arry = [latest_product.id for latest_product in latest_products]
    unq_list = []
    for x in products:
        if x.product_name not in unq_list:
            unq_list.append(x.product_name)
    print(unq_list)
    product_list = []
    for p in unq_list:
        products = Product.query.filter_by(size_id = size_id.id,product_name = p).first()
        product_list.append(products)
    
    return render_template('products.html',size_id=size_id,collections=collections,sizes=sizes,thicknesses=thicknesses,finishes=finishes,products=product_list,size=size,unq_list=unq_list,product_id_arry=product_id_arry)




@product_bp.route("/product/<size>/<int:product_id>/<product_name>")
def product_inside(size,product_name,product_id):
    product = Product.query.filter_by(id = product_id).first()
    collection = Collection.query.filter_by(id=product.collection_id).first()
    thickness = Thickness.query.filter_by(id=product.thickness_id).first()
    finish = Surface.query.filter_by(id=product.surface_id).first()
    product_images=product.product_image.split(',')
    similiar_products = Product.query.filter_by(product_name = product_name)
    similiar_size = []
    for similiar in similiar_products:
        print(similiar.size_id)
        sizes = Size.query.filter_by(id = similiar.size_id).first()
        print(sizes.size)
        if sizes.size not in similiar_size:
            similiar_size.append(sizes.size)  
    print(similiar_size)
    products = Product.query.filter_by(collection_id = product.collection_id, size_id = product.size_id,surface_id=product.surface_id).limit(4)
    collections = Collection.query.all()
    return render_template('product_inside.html',product_images=product_images,size=size,collection=collection,thickness=thickness,finish=finish,product=product,product_name=product_name,products=products,collections=collections,similiar_sizes=similiar_size)


@product_bp.route("/product/<int:product_id>/<product_name>")
def product_search_inside(product_name,product_id):
    product = Product.query.filter_by(id = product_id, product_name = product_name).first()
    if not product:
        return render_template('errors/404.html'), 404
    collection = Collection.query.filter_by(id=product.collection_id).first()
    thickness = Thickness.query.filter_by(id=product.thickness_id).first()
    finish = Surface.query.filter_by(id=product.surface_id).first()
    product_images=product.product_image.split(',')
    size = Size.query.filter_by(id = product.size_id).first()
    products = Product.query.filter_by(collection_id = product.collection_id, size_id = product.size_id,surface_id=product.surface_id).limit(4)
    collections = Collection.query.all()
    similiar_products = Product.query.filter_by(product_name = product_name)
    similiar_size = []
    for similiar in similiar_products:
        print(similiar.size_id)
        sizes = Size.query.filter_by(id = similiar.size_id).first()
        print(sizes.size)
        if sizes.size not in similiar_size:
            similiar_size.append(sizes.size)  
    print(similiar_size)
    return render_template('product_inside.html',product_images=product_images,size=size.size,collection=collection,thickness=thickness,finish=finish,product=product,product_name=product_name,products=products,collections=collections,similiar_sizes=similiar_size)




@product_bp.route("/product/<size>/<product_name>")
def product_size_inside(product_name,size):
    size_id = Size.query.filter_by(size = size).first()
    product = Product.query.filter_by(size_id = size_id.id,product_name = product_name).first()
    
    collection = Collection.query.filter_by(id=product.collection_id).first()
    thickness = Thickness.query.filter_by(id=product.thickness_id).first()
    finish = Surface.query.filter_by(id=product.surface_id).first()
    product_images=product.product_image.split(',')
    size = Size.query.filter_by(id = product.size_id).first()
    products = Product.query.filter_by(collection_id = product.collection_id, size_id = product.size_id,surface_id=product.surface_id).limit(4)
    collections = Collection.query.all()
    similiar_products = Product.query.filter_by(product_name = product_name)
    similiar_size = []
    for similiar in similiar_products:
        print(similiar.size_id)
        sizes = Size.query.filter_by(id = similiar.size_id).first()
        print(sizes.size)
        if sizes.size not in similiar_size:
            similiar_size.append(sizes.size)  
    print(similiar_size)
    return render_template('product_inside.html',product_images=product_images,size=size.size,collection=collection,thickness=thickness,finish=finish,product=product,product_name=product_name,products=products,collections=collections,similiar_sizes=similiar_size)






@product_bp.route("/product/<size>/collection/<collection>", methods=['GET', 'POST'])
def products_collections(size,collection):
    print(size)
    size_id = Size.query.filter_by(size=size).first()
    collection_id = Collection.query.filter_by(collection=collection).first()
    collections = Collection.query.all()
    sizes = Size.query.order_by(Size.order_by.asc()).all()
    thicknesses = Thickness.query.all()
    finishes = Surface.query.all()
    products = Product.query.filter_by(size_id = size_id.id,collection_id = collection_id.id)
    latest_products = Product.query.order_by(Product.id.desc()).limit(12).all()
    product_id_arry = [latest_product.id for latest_product in latest_products]
    error_message = "This Collection is not available in this size"
    unq_list = []
    for x in products:
        if x.product_name not in unq_list:
            unq_list.append(x.product_name)
    print(unq_list)
    product_list = []
    for p in unq_list:
        products = Product.query.filter_by(size_id = size_id.id,collection_id = collection_id.id,product_name = p).first()
        product_list.append(products)
    print(product_list)
    return render_template('products.html',collection_id=collection_id,size_id=size_id,collections=collections,sizes=sizes,thicknesses=thicknesses,finishes=finishes,products=product_list,size=size,collection=collection,error_message=error_message,product_id_arry=product_id_arry)





@product_bp.route("/product/<size>/surface/<surface>", methods=['GET', 'POST'])
def products_surface(size,surface):
    print(size)
    print(surface)
    size_id = Size.query.filter_by(size=size).first()
    surface_id = Surface.query.filter_by(surface=surface).first()
    collections = Collection.query.all()
    sizes = Size.query.order_by(Size.order_by.asc()).all()
    thicknesses = Thickness.query.all()
    finishes = Surface.query.all()
    products = Product.query.filter_by(size_id = size_id.id,surface_id = surface_id.id)
    latest_products = Product.query.order_by(Product.id.desc()).limit(12).all()
    product_id_arry = [latest_product.id for latest_product in latest_products]
    error_message = "This finish is not available in this size"
    unq_list = []
    for x in products:
        if x.product_name not in unq_list:
            unq_list.append(x.product_name)
    print(unq_list)
    product_list = []
    for p in unq_list:
        products = Product.query.filter_by(size_id = size_id.id,surface_id = surface_id.id,product_name = p).first()
        product_list.append(products)
    print(product_list)
    return render_template('products.html',surface_id=surface_id,size_id=size_id,collections=collections,sizes=sizes,thicknesses=thicknesses,finishes=finishes,products=product_list,size=size,surface=surface,error_message=error_message,product_id_arry=product_id_arry)




