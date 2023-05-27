from flask import render_template, request,Blueprint
from lioli import app, mail
from datetime import datetime, date
from datetime import date
from flask_mail import Message

import os
import base64

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

now = datetime.now()
today = date.today()
current_time = now.strftime("%H:%M:%S")

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
career_bp = Blueprint('career',__name__)




def send_email(first_name,last_name,email,phone,address,city,state,pincode,location,post,file_name2):
    html_msg = f'''
            <html>
            <body>
                <div class="container">
                    <table class="table" style="border-collapse: collapse;width: 60%;font-family: Arial, Helvetica, sans-serif;">
                        <thead>
                            <tr style="">
                                <th style="padding-top: 12px;padding-bottom: 12px;text-align: left;background-color: #04AA6D;color: white;">Field Name</th>
                                <th style="padding-top: 12px;padding-bottom: 12px;text-align: left;background-color: #04AA6D;color: white;">Value</th>
                            </tr>
                        </thead>
                        <tbody>
                        <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Post </td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{post}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Location Type </td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{location}</td>
                                
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">First Name </td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{first_name}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Last Name </td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{last_name}</td>
                                
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Email </td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{email}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Mobile Number</td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{phone}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Address</td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{address}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">City</td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{city}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">State</td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{state}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Pincode</td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{pincode}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Date</td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{today}</td>
                                
                            </tr>
                        </tbody>
                    </table>
                </div>
            </body>
            </html>
        
            '''
    # msg_admin =  Message('User Form Deatils', sender=email, recipients=["hr@lioliceramica.com"])
    # msg_admin.html = html_msg
    # msg_admin.body = f'''
    #     Hello, 
    #     Please find the document attached with the email.
    # '''
    
    # with app.open_resource(file_name2) as fp_2:
    #     msg_admin.attach(file_name2.split("/")[-1],"application/pdf",fp_2.read())
    #     mail.send(msg_admin)
    


    msg_admin = Mail(
        from_email='info.lioliceramica@gmail.com',
        to_emails='careers@lioliceramica.com',
        subject='User Form Deatils',
        html_content=html_msg
    )

    with open(file_name2, 'rb') as f:
        data = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()

    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName(file_name2.split("/")[-1]),
        FileType('application/pdf'),
        Disposition('attachment')
    )
    msg_admin.attachment = attachedFile

    sg =SendGridAPIClient('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')
    response = sg.send(msg_admin)
    print(response.status_code, response.body, response.headers)
