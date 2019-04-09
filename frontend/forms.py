from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class EmailForm(FlaskForm):
    rAddr = StringField('Reciever Address:', validators=[DataRequired()])
    emailBody = StringField('Email Body', validators=[DataRequired()])
    submit = SubmitField('Submit')

class TicketForm(FlaskForm):
	department = StringField('Department:', validators=[DataRequired()])
	ticketDate = StringField('Todays date: ', validators=[DataRequired()])
	ticketDescription = StringField('Description of problem: ', validators=[DataRequired()])
	submit = SubmitField('Send Ticket')