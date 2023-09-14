import json
from email_sender.sender import EmailSender

# Load SMTP configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

smtp_server = config["smtp_server"]
smtp_port = config["smtp_port"]
sender_email = config["sender_email"]
sender_password = config["sender_password"]

# Initialize the EmailSender
email_sender = EmailSender(smtp_server, smtp_port, sender_email, sender_password)

# Read the email template from template.txt
with open("email_sender/template.txt", "r", encoding="utf-8") as template_file:
    email_template = template_file.read()

# Example usage
recipient_email = "gabrielpires@discente.ufg.br"
subject = "Olá, Mundo!"

# Use the email template as the message content
message = email_template

email_sender.send_email(recipient_email, subject, message)
