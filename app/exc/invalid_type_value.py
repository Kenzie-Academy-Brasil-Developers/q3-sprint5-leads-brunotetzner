class InvalidTypeValue(Exception):
    def __init__(self,  invalid_keys):
        self.message = {"error": f"All the keys need to have string values. But the keys {invalid_keys} do not have string value"}

