class BaseConfig:

    DEBUG = True


class Product(BaseConfig):

    SQLALCHEMY_DATABASE_URI = 'mssql+pymssql://phdadmin@partahelpdeskserver:Capstone2019!@partahelpdeskserver.database.windows.net/@PartaHelpDesk'

    DEBUG = False


class Development(BaseConfig):

    SQLALCHEMY_DATABASE_URI = 'mssql+pymssql://phdadmin@partahelpdeskserver:Capstone2019!@partahelpdeskserver.database.windows.net/PartaHelpDesk'

    DEBUG = True


config = {
    'product': Product,
    'dev': Development,
    'default': Development
}
