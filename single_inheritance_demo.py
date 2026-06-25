# 1. THE BASE CLASS (PARENT)
class Notification:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver

    def send(self):
        # General action every notification does
        print(f"Alert: New notification from {self.sender} to {self.receiver}!")


# 2. THE DERIVED CLASS (CHILD) - Single Inheritance in action!
class EmailNotification(Notification):
    def __init__(self, sender, receiver, email_subject):
        # The 'super()' method calls the Parent's __init__ to handle sender & receiver
        super().__init__(sender, receiver)
        # Unique variable just for emails
        self.email_subject = email_subject

    # METHOD OVERRIDING: Changing how 'send' works specifically for emails
    def send(self):
        print(f"📧 Sending Email to {self.receiver}...")
        print(f"Subject: {self.email_subject}")
        print(f"From: {self.sender}")
        print("---------------------------------------")


# ==========================================
# EXECUTING THE LOGIC
# ==========================================

# Let's create a standard notification object
generic_alert = Notification("System_Bot", "User123")
generic_alert.send() 
# Output: Alert: New notification from System_Bot to User123!

print("\n")

# Now let's create our single inheritance child object
welcome_email = EmailNotification("Welcome_Team", "lokesh16215@gemail.com", "Welcome to our Platform!")
welcome_email.send()