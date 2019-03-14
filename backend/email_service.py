from flask_mail import Message

class email_service:
	def __init__(self):
		self.message = ""
		self.senderAddr = "PartaHelpDesk@gmail.com"
		self.receivers = []
		self.email = Message()

	def sendEmail():
		mail.send(self.email)

	def build(emailMessage, recieversAddrs):
		self.message = emailMessage
		self.receivers = recieversAddrs
		self.email = Message(str(self.message), self.senderAddr, self.receivers)

