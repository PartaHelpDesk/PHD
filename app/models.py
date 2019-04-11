
from app.initialization import db, login_manager
from datetime import datetime
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


relatedTickets = db.Table(
    'related_tickets',
    db.Column('TicketId1', db.Integer, db.ForeignKey('tickets.id')),
    db.Column('TicketId2', db.Integer, db.ForeignKey('tickets.id')),
)


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.VARCHAR(128))
    last_name = db.Column(db.VARCHAR(128))
    email = db.Column(db.VARCHAR(128))
    password_hash = db.Column('password', db.VARCHAR(256), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=1)

    level_id = db.Column(db.Integer, db.ForeignKey('user_level.id'))

    # relationship
    level = db.relationship('UserLevel')

    @property
    def password(self):
        raise AttributeError('Not allowed to read password!')

    @password.setter
    def password(self, pwd):
        self.password_hash = generate_password_hash(pwd)

    def verify_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)


class UserLevel(db.Model):

    __tablename__ = 'user_level'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.Integer, nullable=False)
    description = db.Column(db.VARCHAR(256))


class Ticket(db.Model):

    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.VARCHAR(256), nullable=False)
    created_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # category = db.Column(db.VARCHAR(256))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    status = db.Column(db.VARCHAR(256))
    created_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    closed_date = db.Column(db.DateTime)
    location = db.Column(db.VARCHAR(256))
    description = db.Column(db.VARCHAR(256))
    priority = db.Column(db.VARCHAR(128), default="Low", nullable=False)

    # relation
    author = db.relationship('User', primaryjoin=created_user_id==User.id, uselist=False)
    category = db.relationship('Category', uselist=False, backref='tickets')


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


class Category(db.Model):

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


