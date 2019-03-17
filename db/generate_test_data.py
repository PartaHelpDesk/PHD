from app import create_app, db

app = create_app("dev")
app.app_context().push()


from app.models import User, Category, Ticket

db.create_all()

db.session.execute("SET FOREIGN_KEY_CHECKS=0")
# User Generate
db.session.execute('truncate table users')
u = User(first_name='admin', last_name='admin', email='exqlnet@gmail.com', active=True)
u.password = '123456'
db.session.add(u)
db.session.commit()

# Category generate
db.session.execute('truncate table categories')
c = Category(description='Network')
db.session.add(c)
db.session.commit()

# Tickets Generate
db.session.execute('truncate table tickets')
t = Ticket(title='test tickets', created_user_id=u.id, status="New", category_id=c.id,
           description='no problem', priority="Low")
db.session.add(t)
db.session.commit()

