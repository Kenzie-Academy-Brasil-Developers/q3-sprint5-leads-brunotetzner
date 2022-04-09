class InvalidCellphone(Exception):
    def __init__(self):
        self.message = {"error": "The cellphone need to have this format (xx)xxxxx-xxxx"}