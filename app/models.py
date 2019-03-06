from app import db
from datetime import datetime

relatedTickets = db.Table(
    'related_tickets',
    db.Column('TicketId1', db.Integer, db.ForeignKey('tickets.id')),
    db.Column('TicketId2', db.Integer, db.ForeignKey('tickets.id')),
)


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.VARCHAR(128))
    last_name = db.Column(db.VARCHAR(128))
    email = db.Column(db.VARCHAR(128))
    password = db.Column(db.VARCHAR(256), nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    level_id = db.Column(db.Integer, db.ForeignKey('user_level.id'))

    # relationship
    level = db.relationship('UserLevel')


class UserLevel(db.Model):

    __tablename__ = 'user_level'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.Integer, nullable=False)
    description = db.Column(db.VARCHAR(256))


class Ticket(db.Model):

    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.VARCHAR(256), nullable=False)
    created_user_id = db.Column(db.Integer, nullable=False)
    category = db.Column(db.VARCHAR(256))
    status = db.Column(db.VARCHAR(256))
    created_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    closed_date = db.Column(db.DateTime)
    location = db.Column(db.VARCHAR(256))
    description = db.Column(db.VARCHAR(256))


class TicketHistory(db.Model):

    __tablename__ = 'ticket_history'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.id'))
    category = db.Column(db.VARCHAR(256))
    title = db.Column(db.VARCHAR(256))
    status = db.Column(db.VARCHAR(256))
    Department = db.Column(db.VARCHAR(256))
    Location = db.Column(db.VARCHAR(256))
    Description = db.Column(db.VARCHAR(256))
    DateChanged = db.Column(db.DateTime, default=datetime.utcnow)


class Status(db.Model):

    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.VARCHAR(256))


class Categories(db.Model):

    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.VARCHAR(256))


class Location(db.Model):

    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.VARCHAR(256))


class Department(db.Model):

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.VARCHAR(256))


