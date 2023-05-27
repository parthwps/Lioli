from flask import render_template, request,Blueprint
from sqlalchemy import desc
from lioli.models import Career,Resume
from lioli import app, db
from werkzeug.utils import secure_filename
import os
from .utils import send_email

career_bp = Blueprint('career',__name__)




@career_bp.route("/career/thank-you/",methods=['GET','POST'])
def career_thank_you():
    return render_template('thank.html')






@career_bp.route("/career-opportunities-at-lioli-ceramica/",methods=['GET','POST'])
def careers():
    career = Career.query.all()
    if request.method == 'POST':
        post = request.form.get('designation')
        location = request.form.get('location')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')
        pincode = request.form.get('pincode')
        resume = request.files['resume']
        resume_name = secure_filename(resume.filename)
        resume.save(os.path.join(app.root_path, 'static/admin/uploads/resume', resume_name))
        file_name2 = app.root_path+"/static/admin/uploads/resume/"+resume_name
        print(file_name2)
        send_email(first_name,last_name,email,phone,address,city,state,pincode,post,location,file_name2)
        resume_add = Resume(first_name=first_name,last_name=last_name,email=email,mobile=phone,address=address,city=city,state=state,postal_code=pincode,location=location,post=post,resume=resume_name)
        db.session.add(resume_add)
        db.session.commit()
        return redirect(url_for('career_bp.career_thank_you'))
    return render_template('career.html',careers=career,title="Recent Career Opportunities @Lioli Ceramica - Porcelain Tile Manufacturing Company",desc="Recent careers opportunities @LioliCeramica, Asia's largest porcelain tile manufacturing company in India, send us your resume through this page.")

@career_bp.route("/career-deatils/<int:career_id>/<location>",methods=['GET','POST'])
def careers_details(career_id,location):
    career = Career.query.filter_by(id=career_id).first()
    if career:
        if request.method == 'POST':
            post = request.form.get('post')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            address = request.form.get('address')
            city = request.form.get('city')
            state = request.form.get('state')
            pincode = request.form.get('pincode')
            resume = request.files['resume']
            resume_name = secure_filename(resume.filename)
            resume.save(os.path.join(app.root_path, 'static/admin/uploads/resume', resume_name))
            file_name2 = app.root_path+"/static/admin/uploads/resume/"+resume_name
            print(file_name2)
            send_email(first_name,last_name,email,phone,address,city,state,pincode,post,location,file_name2)
            resume_add = Resume(first_name=first_name,last_name=last_name,email=email,mobile=phone,address=address,city=city,state=state,postal_code=pincode,location=location,post=post,resume=resume_name)
            db.session.add(resume_add)
            db.session.commit()
            return render_template('thank.html')
    else:
        return render_template('errors/404.html'), 404

    return render_template('career_inside.html',career=career,career_id=career_id,location=location)

