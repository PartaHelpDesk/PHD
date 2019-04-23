from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, RadioField

from wtforms.validators import DataRequired
#from app import DatabaseMethods as dm
#import DatabaseMethods as dm

class EmailForm(FlaskForm):
    Addr = StringField('Reciever Address:', validators=[DataRequired()])
    emailBody = StringField('Email Body', validators=[DataRequired()])
    submit = SubmitField('Submit')

class TicketForm(FlaskForm):
	ticketDepartment = SelectField('Department:', choices=[],validators=[DataRequired()])
	ticketTitle = StringField('Ticket Title: ', validators=[DataRequired()])
	ticketDescription = StringField('Description of problem: ', validators=[DataRequired()])
	ticketCategory = SelectField('Category: ', choices=[], validators=[DataRequired()])
	#ticketStatus = StringField('Status: ', validators=[DataRequired()])
	submit = SubmitField('Send Ticket')

class ReportForm(FlaskForm):
	reportChoice = RadioField('Label', choices=[('Category','Report By Category'),('Department','Report By Department'),('Status','Report By Ticket Status')])
	submit = SubmitField('Get Report')

class PasswordResetForm(FlaskForm):
	accUsername = StringField('Account Username: ', validators=[DataRequired()])
	submit = SubmitField('Send New Password to Account Email')
