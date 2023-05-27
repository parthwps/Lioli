from email import message
from flask import render_template,Blueprint,request,redirect,url_for,send_file
from sqlalchemy import desc
from lioli.models import Contact, Download, Gallery,Size,Catalogue
import os
from lioli import app, db
from .utils import send_email,download_email,comming_soon_email
main_bp = Blueprint('main',__name__)




@main_bp.route("/")
@main_bp.route("/home")
def home():
    sizes = Size.query.order_by(Size.order_by.asc()).all()
    return render_template('home.html',sizes=sizes,title="Lioli Ceramica - Asia's Biggest Porcelain Slab Manufacturers",desc="Lioli Ceramica takes pride in being Asia's biggest porcelain slab manufacturer in India. Looking for a porcelain tile manufacturer in India, get a quote now from us!")





# @main_bp.route("/")
@main_bp.route("/comming-soon",methods=['GET','POST'])
def comming_soon():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        messages = request.form.get('message')
        
        comming_soon_email(name,email,messages)
        return redirect(url_for('main.comming_soon'))
    return render_template('comming-soon.html')


@main_bp.route("/about-lioli-ceramica/")
def about():
    return render_template('about.html',title="About Lioli Ceramica Being Largest Porcelain Slab Manufacturers",desc="How Lioli Ceramica in 4 years time has become the largest porcelain slab manufacturer across Asia. Here let's unveil the journey of these 4 years in the porcelain manufacturing market.")


@main_bp.route("/contact/thank-you/",methods=['GET','POST'])
def contact_thank_you():
    return render_template('thank-2.html')




@main_bp.route("/contact-lioli-ceramica/",methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        assistence= request.form.get('assistence')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        profession = request.form.get('profession')
        company = request.form.get('company')
        city = request.form.get('city')
        country = request.form.get('country')
        messages = request.form.get('messages')
        contacts = Contact(assistence=assistence,first_name=first_name,last_name=last_name,email=email,phone=phone,profession=profession,representing_company=company,city=city,country=country,message=messages)
        db.session.add(contacts)
        db.session.commit()
        send_email(assistence,first_name,last_name,email,phone,profession,company,city,country,messages)
        return redirect(url_for('main.contact_thank_you'))
    return render_template('contact.html',title="Contact Lioli Ceramica, the Biggest Porcelain Tile Manufacturer Across World",desc="Contact Lioli Ceramica, one of the biggest porcelain slab manufacturers globally with four years of experience in producing esthetic, intuitive & marvellous looking porcelain slabs.")



@main_bp.route("/download-lioli-ceramica-latest-catalogue-and-tile-manuals/",methods=['GET','POST'])
def download():
    catalogues = Catalogue.query.order_by(Catalogue.id.desc()).all()
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        messages = request.form.get('messages')
        catalogue_name = request.form.get('catalogue_name')
        city = request.form.get('city')
        pdf = request.form.get('pdf')
        downloads = Download(full_name=full_name,email=email,phone=phone,message=messages,catalogue=catalogue_name,city=city)
        db.session.add(downloads)
        db.session.commit()
        path = url_for('static',filename='admin/uploads/catalogue/pdf/'+pdf,_external = True)
        print(path)
        download_email(full_name,email,phone,messages,catalogue_name,city)
        return redirect(path)
    return render_template('download.html',catalogues=catalogues,title="Download the Latest Catalogues of Lioli Ceramica's Designs & Tile Manuals to Maintain Tiles",desc="Here you can download the latest catalogues of lioli Ceramica's new designs, followed by tile manuals that help you maintain your tiles and keep them beautiful, durable and stunning as ever.")



@main_bp.route("/lioli-ceramica-gallery/")
def gallery():
    gallery = Gallery.query.all()
    return render_template('gallery.html',gallerys=gallery,title="Gallery of Lioli Ceramica - Porcelain Tile Manufacturing Company",desc="Lioli Ceramica Gallery contains what is happening in the organization, what technologies we are using, any awards we won or any new updates for our clients, vendors, and customers.")




@main_bp.route("/faqs-by-lioli-ceramica/")
def faqs():
    return render_template('faqs.html',title="FAQs by Lioli Ceramica for Porcelain Tile Manufacturing",desc="Do you have any questions you wanted to ask LioliCeramica? Well, guess what we have already answered a few questions about the Porcelain tiles manufacturing process and the benefits of using Lioli's Porcelain Slabs for your needs.")



@main_bp.route("/privacy-policy-lioli-ceramica/")
def privacy():
    return render_template('privacy.html',title="Privacy Policy of Lioli Ceramica, a Leading Porcelain Slabs Manufacturers in India",desc="This page consists of Lioli Ceramica's privacy policies to maintain top-end security while dealing with domestic and international organizations as leading porcelain slab manufacturers in India.")
