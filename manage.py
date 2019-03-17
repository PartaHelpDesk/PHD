from app import create_app, db
from flask_script import Command, Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app.models import User


def make_app_context():
    return dict(db=db, User=User)


app = create_app('dev')
migrate = Migrate(app=app, db=db)
manager = Manager(app)
manager.add_command('shell', Shell(make_context=make_app_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
