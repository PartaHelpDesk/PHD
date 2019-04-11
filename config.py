class BaseConfig:
    DEBUG = True


class Product(BaseConfig):
    SECRET_KEY = 'Lp7dZry7DcURWMoG'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://phdadmin@partahelpdeskserver:Capstone2019!@partahelpdeskserver.database.windows.net:1433/PartaHelpDesk'

    DEBUG = False


class Development(BaseConfig):
    SECRET_KEY = 'WelcomePartaHelpDesk'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://hliu32:123456@120.79.9.56/partahelpdesk?charset=utf8'

    DEBUG = True


config = {
    'product': Product,
    'dev': Development,
    'default': Development
}
