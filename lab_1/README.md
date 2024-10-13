# Laboratory Work 0: SOLID Principles

## Student Information
- **Name:** Maxim Plămădeală
- **Group:** FAF-222

## Overview
This laboratory work focuses on implementing two SOLID principles in a Python project. The chosen principles are:
1. Single Responsibility Principle (SRP)
2. Open/Closed Principle (OCP)

## Project Description
The project implements a simple email system with notification capabilities. It demonstrates how SOLID principles can be applied to create a modular and extensible codebase.

## SOLID Principles Implementation

### 1. Single Responsibility Principle (SRP)

#### Implemented Classes:
- `EmailContent`: Manages email content (subject and body)
- `EmailSender`: Handles email sending logic
- `EmailValidator`: Validates email addresses

#### SRP Demonstration:
Each class has a single, well-defined responsibility:
- `EmailContent` only deals with storing email data
- `EmailSender` is solely responsible for the email sending process
- `EmailValidator` focuses exclusively on email validation

### 2. Open/Closed Principle (OCP)

#### Implemented Classes:
- `NotificationSender`: Base class for notifications
- `EmailNotification`: Handles email notifications
- `SMSNotification`: Manages SMS notifications

#### OCP Demonstration:
- The `NotificationSender` base class is open for extension
- New notification types can be added by inheriting from `NotificationSender`
- Existing code doesn't need modification when adding new notification types

## Code Snippets

### EmailContent (SRP Example)
```python
class EmailContent:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body
```

### NotificationSender (OCP Example)
```python
class NotificationSender:
    def send_notification(self, message):
        pass

class EmailNotification(NotificationSender):
    def send_notification(self, message):
        print(f"Sending email notification: {message}")

class SMSNotification(NotificationSender):
    def send_notification(self, message):
        print(f"Sending SMS notification: {message}")
```

## Project Structure
```
lab_1/
├── main.py
├── models/
│   └── email.py
└── operations/
    ├── email.py
    └── notification.py
```

## How to Run
1. Navigate to the `lab_1` directory
2. Execute: `python main.py`

## Conclusions
This laboratory work successfully demonstrates the application of SRP and OCP in a practical scenario. The resulting code is more organized, extensible, and adheres to good software design principles. The implementation showcases how SOLID principles can improve code quality even in relatively simple applications.


