class MissingKey(Exception):
    def __init__(self, valid_keys, missing_keys):
        self.message =  { "error":
                 f"the keys {valid_keys} are required. But the key(s) {missing_keys} is(are) not found "
                 }, 400

