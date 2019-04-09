from flask_mail import Message
from frontend import mail

#class email_service:
	#def __init__(self):
		#self.message = ""
		#self.senderAddr = "PartaHelpDesk@gmail.com"
		#self.receivers = []
		#self.email = Message()

	#def sendEmail():
		#mail.send(self.email)

	#def build(emailMessage, recieversAddrs):
		#self.message = emailMessage
		#self.receivers = recieversAddrs
		#self.email = Message(str(self.message), self.senderAddr, self.receivers)

def format_email(department, date, description):
	result = '' 
	result += ('Department:\t\t' + department + '\n\n')
	result += ('Date:\t\t' + date + '\n\n')
	result += ('What\'s the problem?:\n' + description + '\n\n')
	return result


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def send_group_email(sender, email_recipients, email_message, html_body):
	with mail.connect() as conn:
		for user in email_recipients:
			message = email_message
			subject = "Hello, %s" % user
			msg = Message(recipients=[user],
						body=message,
						subject=subject,
						sender = sender)

			conn.send(msg)

