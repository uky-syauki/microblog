from flask_mail import Message
from app import mail

def send_email(subject, sender, recipients,
