class InvalidKey(Exception):
    def __init__(self, valid_keys, invalid_keys):
        self.message = {"error": f"The keys {valid_keys} are valid, but the invalid keys {invalid_keys} are found"}
