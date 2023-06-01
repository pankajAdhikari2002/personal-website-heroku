from flask import Flask, render_template, redirect, url_for, request
import smtplib
from email.message import EmailMessage

USERNAME = "pankajadhikari75@gmail.com"
EMAIL_APP_PSSWD = "dauoxshgxaxembne"


app = Flask(__name__)

msg = EmailMessage()


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html")

@app.route('/send_email', methods=['POST'])
def send_email():
    form_data = request.json
    name = form_data['name']
    email = form_data['email']
    subject = form_data['subject']
    message = form_data['message']
    
    custom_msg = f"Name: {name}\nEmail: {email}\n\nMessage-\n{message}"
    msg.set_content(custom_msg)
    msg['Subject'] = subject
    msg['From'] = USERNAME
    msg['To'] = "pankajadhikari21.06.2002@gmail.com"
    
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=EMAIL_APP_PSSWD)
            connection.send_message(msg)
            print("Mail sent successfully.")
        return "Email sent successfully"
    except smtplib.SMTPException:
        return "Unable to send message"

@app.route("/blog")
def blog():
    return render_template("blog-single.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio-details.html")

