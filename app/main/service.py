from flask_login import current_user
from app import db
from app.models import Ticket


def get_my_tickets():
    return Ticket.query.filter_by(create_user_id=current_user.id).all()


def get_tickets_queue():
    return Ticket.query.filter(Ticket.create_user_id != current_user.id).all()
