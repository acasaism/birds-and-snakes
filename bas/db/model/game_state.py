from sqlalchemy import Column, Integer, String, Sequence

from bas.db.database import Base


class GameState(Base):
    __tablename__ = 'game_states'
    id = Column(Integer, Sequence('game_state_id_seq'), primary_key=True)
    name = Column(String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<GameState(id={}, name={})>'.format(self.id, self.name)

    def __str__(self):
        return self.name