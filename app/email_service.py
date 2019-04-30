from flask_mail import Message
from app import mail

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

def format_email(ticketTitle, ticketDepartment, ticketCategory, ticketStatus, ticketDescription, ticketLink, email):
	result = '' 
	result += ('Ticket Title:\t\t' + ticketTitle + '\n\n')
	result += ('Department:\t\t' + ticketDepartment + '\n\n')
	result += ('Category:\t\t' + ticketCategory + '\n\n')
	result += ('Status of Ticket:\t\t' + ticketStatus + '\n\n')
	result += ('What\'s the problem?:\n' + ticketDescription + '\n\n')
	result += ('User\'s email: ' + email + '\n\n')
	result += ('View ticket: ' + ticketLink)
	return result



def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)

def send_group_email(sender, email_recipients, email_message, html_body, ticketTitle):
	with mail.connect() as conn:
		for user in email_recipients:
			message = email_message
			subject = ticketTitle
			msg = Message(recipients=[user],
						body=message,
						subject=subject,
						sender = sender)

			conn.send(msg)

