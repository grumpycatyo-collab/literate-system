class NotificationSender:
    def send_notification(self, message):
        pass

class EmailNotification(NotificationSender):
    def send_notification(self, message):
        print(f"Sending email notification: {message}")

class SMSNotification(NotificationSender):
    def send_notification(self, message):
        print(f"Sending SMS notification: {message}")
