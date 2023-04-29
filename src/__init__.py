from flask import Flask

class App(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, import_name=__name__, **kwargs)