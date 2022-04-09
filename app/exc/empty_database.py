class EmptyDatabase(Exception):
    def __init__(self):
        self.message = {"Error": "The database is empty"}