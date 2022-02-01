from config import db

class Category(object):

    @staticmethod
    def get_all_passwords() -> list:
        result = db.passwords.find()
        passwords = [x for x in result]
        return passwords

