class EmailSender:
    def send_email(self, email_content, recipient):
        print(f"Sending email to {recipient}")
        print(f"Subject: {email_content.subject}")
        print(f"Body: {email_content.body}")

class EmailValidator:
    def validate_email(self, email):
        return '@' in email