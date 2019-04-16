from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired
#from app import DatabaseMethods as dm
import DatabaseMethods as dm

class EmailForm(FlaskForm):
    Addr = StringField('Reciever Address:', validators=[DataRequired()])
    emailBody = StringField('Email Body', validators=[DataRequired()])
    submit = SubmitField('Submit')

class TicketForm(FlaskForm):
	
	catagories = []
	
	def __init__(self):
		dbm = dm.DatabaseMethods()
		categories_dt = dbm.GetCategories()
		for category in categories_dt.data_rows:
			self.catagories.append(category)

	department = StringField('Department:', validators=[DataRequired()])
	ticketTitle = StringField('Ticket Title: ', validators=[DataRequired()])
	ticketDescription = StringField('Description of problem: ', validators=[DataRequired()])
	ticketCategory = SelectField('Category: ', choices=catagories, validators=[DataRequired()])
	#ticketStatus = StringField('Status: ', validators=[DataRequired()])
	submit = SubmitField('Send Ticket')
