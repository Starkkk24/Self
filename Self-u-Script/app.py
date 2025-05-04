from flask import Flask, render_template, request, redirect, url_for, flash
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        # Here you would normally send an email
        try:
            # Example code to send email (commented out)
            # email_message = EmailMessage()
            # email_message['Subject'] = f'Portfolio Contact: {subject}'
            # email_message['From'] = email
            # email_message['To'] = 'your-email@example.com'
            # email_message.set_content(f'From: {name} <{email}>\n\n{message}')
            
            # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            #     smtp.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASSWORD'))
            #     smtp.send_message(email_message)
            
            # For now, just print the message
            print(f"Contact form submission:\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}")
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            print(f"Error sending email: {e}")
            flash('There was an error sending your message. Please try again later.', 'error')
        
        return redirect(url_for('index', _anchor='contact'))

if __name__ == '__main__':
    app.run(debug=True) 