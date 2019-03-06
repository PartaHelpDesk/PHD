from app import create_app, db
from flask_script import Command, Manager, Shell
from app.models import User



def make_app_context():
    return dict(db=db, User=User)


app = create_app('dev')
manager = Manager(app)
manager.add_command('shell', Shell(make_context=make_app_context))


if __name__ == '__main__':
    manager.run()
