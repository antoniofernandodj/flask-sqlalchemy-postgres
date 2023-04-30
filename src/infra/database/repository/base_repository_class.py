from src.infra.database import session
from werkzeug.security import generate_password_hash as gen_hash
from copy import deepcopy
from uuid import uuid4


class BaseRepositoryClass:

    @classmethod
    def find_one(cls, **kwargs):
        with session.get() as db:
            item = db.query(cls.model_class) \
                .filter_by(**kwargs) \
                .first()
        
            if item:
                return item

    @classmethod
    def find_all(cls, **kwargs):
        with session.get() as db:
            items = db.query(cls.model_class) \
                .filter_by(**kwargs) \
                .all()
        
            if items:
                return items

    @classmethod
    def create(cls, **kwargs):
        kwargs['password_hash'] = gen_hash(kwargs['password_hash'])
        kwargs['uuid'] = uuid4()

        with session.get() as db:
            item = cls.model_class(**kwargs)
            db.add(item)
            db.commit()
            db.refresh(item)
            return item