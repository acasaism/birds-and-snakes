from bas.db.database import db
from bas.db.model import User
import bas.manager as manager


class Message:
    def __init__(self, message, username=None):
        self.__message = message
        self.__username = username
        self.__user = None
        self.__get_existing_user_or_create_new()

    @property
    def message(self):
        return self.__message

    @property
    def username(self):
        return self.__username

    @property
    def user(self):
        return self.__user

    def __str__(self):
        return '{}: {}'.format(self.user, self.message)

    @classmethod
    def from_string(cls, message):
        username, message = message.split(':', 1)
        return cls(message.lstrip(), username)

    def __get_existing_user_or_create_new(self):
        user = db.first(User, username=self.username)
        if user is None:
            user = manager.create_user(self.username)
        self.__user = user
