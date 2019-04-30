from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, RadioField, validators

from wtforms.validators import DataRequired

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
	submit = SubmitField('Create Ticket')

class ReportForm(FlaskForm):
	reportChoice = RadioField('Label', choices=[('Category','Report By Category'),('Department','Report By Department'),('Status','Report By Ticket Status')])
	submit = SubmitField('Get Report')

class PasswordResetForm(FlaskForm):
	accUsername = StringField('Account Username: ', validators=[DataRequired()])
	submit = SubmitField('Send New Password to Account Email')

class UpdateTicketForm(FlaskForm):
	ticketDepartment = SelectField('Department:', choices=[],validators=[DataRequired()])
	ticketTitle = StringField('Ticket Title: ', validators=[DataRequired()])
	ticketDescription = StringField('Description of problem: ', validators=[DataRequired()])
	ticketCategory = SelectField('Category: ', choices=[], validators=[DataRequired()])
	ticketStatus = SelectField('Status: ', choices=[('New','New'), ('In Process', 'In Process'), ('Escalated', 'Escalated'), ('Closed', 'Closed'), ('On Hold', 'On Hold')], validators=[DataRequired()])
	ticketComment = StringField('Comment on the Update: ', validators=[DataRequired()])
	submit = SubmitField('Update Ticket')

class UpdatePasswordForm(FlaskForm):
	oldpassword = PasswordField('Old Password: ', validators=[DataRequired()])
	# newpassword = PasswordField('New Password: ', validators=[DataRequired()])
	newpassword = PasswordField('New Password: ',  
	[
        validators.DataRequired()
    ])
	verifypassword = PasswordField('Verify Password: ',
	[
        validators.DataRequired(),
        validators.EqualTo('newpassword', message='Passwords must match')
    ])
	submit = SubmitField('Update Password')


