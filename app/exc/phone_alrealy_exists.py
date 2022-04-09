class PhoneAlrealyExists(Exception):
    def __init__(self, phone):
        self.message = {"error": f"The phone {phone} alrealy exists"}
