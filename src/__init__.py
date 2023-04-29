from flask import Flask
from werkzeug.security import generate_password_hash as gen_hash


class App(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, import_name=__name__, **kwargs)
        
        from src.infra import database
        # from src.main import routes
        # from src.ext import auth
        
        database.config.init_database()
        # routes.init_app(self)
        # auth.init_app(self)
        
        user = database.entities.User(
            name='Ricardo',
            email='ricardo@email.com',
            password_hash=gen_hash('asdasdasdasa'),
        )
        
        user.save()

        print(user)
        