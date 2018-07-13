from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import bas.db.model as model


class Database:
    def __init__(self, database_name, metadata):
        self.database_name = database_name
        self.metadata = metadata
        self.engine = create_engine('sqlite:///{}.sqlite'.format(database_name))
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        self.session = Session()
        self.metadata.bind = self.engine

    def create_all(self):
        self.metadata.create_all(self.engine)

    def first(self, model_class, **kwargs):
        if kwargs:
            return self.session.query(model_class).filter_by(**kwargs).all()
        return self.session.query(model_class).first()

    def all(self, model_class, **kwargs):
        if kwargs:
            return self.session.query(model_class).filter_by(**kwargs).all()
        return self.session.query(model_class).all()


db = Database('database_bas', model.metadata)
