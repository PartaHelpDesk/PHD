class BaseConfig:

    DEBUG = True


class Product(BaseConfig):

    DEBUG = False


class Development(BaseConfig):

    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://PartaHelpDesk:Capstone2019!@PartaHelpDesk'

    DEBUG = True

    pass


config = {
    'product': Product,
    'dev': Development,
    'default': Development
}
