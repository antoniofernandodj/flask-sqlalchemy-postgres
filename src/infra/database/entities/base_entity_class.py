from uuid import uuid4
from copy import deepcopy

class BaseEntityClass:
    
    def __repr__(self):
        cls = type(self)
        attrs = vars(self)
        attrs_str = ', '.join(
            f"{k}={v!r}" for k, v in attrs.items()
            if k != '_sa_instance_state'
        )
        
        return f"EntityClass::{cls.__name__}({attrs_str})"
    
    def save(self):
        from src.infra import database
        cls = type(self)
        
        with database.session.get() as session:
            try:
                data = deepcopy(self.__dict__)
                data.pop('_sa_instance_state', None)
                object = cls(uuid=uuid4(), **data)
                session.add(object)
                session.commit()
                session.refresh(object)
            except:
                session.rollback()
                raise
            
    
    def update(self, **kwargs: dict):
        from src.infra import database
        cls = type(self)
        
        with database.session.get() as session:
            try:
                user = session.query(cls).filter_by(uuid=self.uuid).first()
                for key, value in kwargs.items():
                    if key != '_sa_instance_state':
                        setattr(user, key, value)
                    
                session.commit()
            except:
                session.rollback()
                raise
            
    def delete(self):
        from src.infra import database
        cls = type(self)
        
        with database.session.get() as session:
            try:
                user = session.query(cls).filter_by(uuid=self.uuid).first()
                session.delete(user)
                session.commit()
            except:
                session.rollback()
                raise