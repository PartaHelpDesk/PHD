from flask_login import current_user
from app.models import Ticket, User
from sqlalchemy import and_


def get_my_tickets():
    return Ticket.query.filter_by(created_user_id=current_user.id).all()


def get_tickets_queue():
    return Ticket.query.filter(and_(Ticket.created_user_id != current_user.id)).all()


def get_active_users():
    return User.query.filter_by(active=True).all()


def get_inactive_users():
    return User.query.filter_by(active=False).all()
