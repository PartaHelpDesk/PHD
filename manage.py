from app import create_app

app = create_app('product')


if __name__ == '__main__':
    app.run()
