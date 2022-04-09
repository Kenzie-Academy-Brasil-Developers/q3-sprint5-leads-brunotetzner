class EmailAlrealyExists(Exception):
    def __init__(self, email):
        self.message = {"error": f"The email {email} alrealy exists"}