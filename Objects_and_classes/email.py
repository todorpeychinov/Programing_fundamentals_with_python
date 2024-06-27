class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


mails = []

while True:
    current_mail = input().split()

    if current_mail[0] == "Stop":
        break

    sender = current_mail[0]
    receiver = current_mail[1]
    content = current_mail[2]

    mail = Email(sender, receiver, content)
    mails.append(mail)

indices = input().split(', ')

for index in indices:
    mails[int(index)].send()

for email in mails:
    print(email.get_info())