class BaseConfig:
    DEBUG = True


class Product(BaseConfig):
    SECRET_KEY = 'Lp7dZry7DcURWMoG'
    SQLALCHEMY_DATABASE_URI = 'mssql+pymssql://phdadmin@partahelpdeskserver:Capstone2019!@partahelpdeskserver.database.windows.net/@PartaHelpDesk'

    DEBUG = False


class Development(BaseConfig):
    SECRET_KEY = 'WelcomePartaHelpDesk'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/partahelpdesk?charset=utf8'

    DEBUG = True


config = {
    'product': Product,
    'dev': Development,
    'default': Development
}
