from models.email import EmailContent
from operations.email import EmailSender, EmailValidator
from operations.notification import EmailNotification, SMSNotification

# Single Responsibility Principle
email_content = EmailContent("Python Engineer Application Response", "Could you send us a CV?")
email_sender = EmailSender()
email_validator = EmailValidator()

recipient = "maxim.plamadeala@gmail.com"

if email_validator.validate_email(recipient):
    email_sender.send_email(email_content, recipient)
else:
    print("Invalid email address")

print("\n")

# Open-Closed Principle
email_notifier = EmailNotification()
sms_notifier = SMSNotification()

email_notifier.send_notification("You have a new message")
sms_notifier.send_notification("You have a new message")