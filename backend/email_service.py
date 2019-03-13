from flask_mail import Message

class email_service:
	def __init__(message, senderAddr, receivers, email):
		self.message = ""
		self.senderAddr = ""
		self.receivers = []
		self.email = Message()

	def sendEmail():
		mail.send(self.email)

	def build(emailMessage, sendAddr, recieversAddrs, email):
		self.message = emailMessage
		self.senderAddr = sendAddr
		self.receivers = recieversAddrs
		self.email = Message(str(self.message), self.senderAddr, self.receivers)

