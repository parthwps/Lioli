from flask import render_template, request,Blueprint
from lioli import app, mail
from datetime import datetime, date
from datetime import date
# from flask_mail import Message
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail



now = datetime.now()
today = date.today()
current_time = now.strftime("%H:%M:%S")

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
career_bp = Blueprint('career',__name__)




def send_email(assistence,first_name,last_name,email,phone,profession,company,city,country,messages):
    html_msg = f'''
            <html>
            <body>
                <div class="container">
                    <table class="table" style="border-collapse: collapse;width: 60%;font-family: Arial, Helvetica, sans-serif;">
                        <thead>
                            <tr style="">
                                <th style="padding-top: 12px;padding-bottom: 12px;text-align: left;background-color: #000000;color: white;">Field Name</th>
                                <th style="padding-top: 12px;padding-bottom: 12px;text-align: left;background-color: #000000;color: white;">Value</th>
                            </tr>
                        </thead>
                        <tbody>
                        
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Assistence In </td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{assistence}</td>
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
                                <td style="border: 1px solid #ddd;padding: 8px;">Mobile No. </td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{phone}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Profession</td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{profession}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Company</td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{company}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">City</td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{city}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Country</td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{country}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Message</td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{messages}</td>
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

    msg_admin = Mail(
    from_email="info.lioliceramica@gmail.com",
    to_emails='info@lioliceramica.com',
    subject='Inquiry Form Details',
    html_content=html_msg)
    sg = SendGridAPIClient('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')
    response = sg.send(msg_admin)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    # msg_admin =  Message('Inquiry Form Details', sender=email, recipients=["info@lioliceramica.com"])
    # msg_admin.html = html_msg   
    # mail.send(msg_admin)
    







def download_email(full_name,email,phone,messages,catalogue_name,city):
    html_msg2 = f'''
            <html>
            <body>
                <div class="container">
                    <table class="table" style="border-collapse: collapse;width: 60%;font-family: Arial, Helvetica, sans-serif;">
                        <thead>
                            <tr style="">
                                <th style="padding-top: 12px;padding-bottom: 12px;text-align: left;background-color: #000000;color: white;">Field Name</th>
                                <th style="padding-top: 12px;padding-bottom: 12px;text-align: left;background-color: #000000;color: white;">Value</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Name </td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{full_name}</td>
                                
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Email </td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{email}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Mobile No. </td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{phone}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Catalogue</td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{catalogue_name}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">City</td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{city}</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Message</td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{messages}</td>
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
    download_msg = Mail(
    from_email="info.lioliceramica@gmail.com",
    to_emails='info@lioliceramica.com',
    subject='Download Form Details',
    html_content=html_msg2)
    sg = SendGridAPIClient('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')
    response = sg.send(download_msg)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    # download_msg =  Message('Download Form Details', sender=email, recipients=["info@lioliceramica.com"])
    # download_msg.html = html_msg2   
    # mail.send(download_msg)
    






def comming_soon_email(name,email,messages):
    html_msg3 = f'''
            <html>
            <body>
                <div class="container">
                    <table class="table" style="border-collapse: collapse;width: 60%;font-family: Arial, Helvetica, sans-serif;">
                        <thead>
                            <tr style="">
                                <th style="padding-top: 12px;padding-bottom: 12px;text-align: left;background-color: #000000;color: white;">Field Name</th>
                                <th style="padding-top: 12px;padding-bottom: 12px;text-align: left;background-color: #000000;color: white;">Value</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Name </td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{name}</td>
                                
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Email </td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{email}</td>
                            </tr>
                           
                            <tr>
                                <td style="border: 1px solid #ddd;padding: 8px;">Message</td>
                                <td style="border: 1px solid #ddd;padding: 8px;">{messages}</td>
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
    comming_soon_msg = Mail(
    from_email="info.lioliceramica@gmail.com",
    to_emails='info@lioliceramica.com',
    subject='Form Details',
    html_content=html_msg3)
    sg = SendGridAPIClient('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')
    response = sg.send(comming_soon_msg)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    # comming_soon_msg =  Message('Form Details', sender=email, recipients=["info@lioliceramica.com"])
    # comming_soon_msg.html = html_msg3   
    # mail.send(comming_soon_msg)
