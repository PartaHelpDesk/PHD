from flask_login import current_user
from frontend.models import Ticket
from sqlalchemy import and_


def get_my_tickets():
    return Ticket.query.filter_by(created_user_id=current_user.id).all()


def get_tickets_queue():
    return Ticket.query.filter(and_(Ticket.created_user_id != current_user.id)).all()
