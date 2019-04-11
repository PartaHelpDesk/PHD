import sqlalchemy
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker, Query
import urllib
from datetime import datetime
import pyodbc
import re
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, VARCHAR, Boolean, ForeignKey



Base = declarative_base()


class User(Base):
    
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(VARCHAR(128))
    last_name = Column(VARCHAR(128))
    email = Column(VARCHAR(128))
    password_hash = Column('password', VARCHAR(256), nullable=False)
    active = Column(Boolean, nullable=False, default=1)

    level_id = Column(Integer, ForeignKey('user_level.id'))

    # relationship
    #level = relationship('UserLevel')

    @property
    def password(self):
        raise AttributeError('Not allowed to read password!')

    @password.setter
    def password(self, pwd):
        self.password_hash = generate_password_hash(pwd)

    def verify_password(self, pwd):
        return check_password_hash(self.password_hash, pwd)



conn_string = "DRIVER={ODBC Driver 13 for SQL Server};Database=PartaHelpDesk;PORT=1433;SERVER=partahelpdeskserver.database.windows.net;UID=phdadmin;PWD=Capstone2019!"
conn_string = urllib.quote_plus(conn_string)
conn_string = "mssql+pyodbc:///?odbc_connect=%s" % conn_string
engine = sqlalchemy.create_engine(conn_string, pool_size=3, pool_recycle=3600)

#sess = sessionmaker(bind=engine)


Session = sessionmaker(bind=engine)

# later, some unit of code wants to create a
# Session that is bound to a specific Connection
conn = engine.connect()
session = Session(bind=conn)


#conn = engine.connect()

print(session.query(User).filter_by(id='*').all())


penguins = []

penguins.append(text("select * from Users"))

conn.execute(penguins)
  

conn.close()