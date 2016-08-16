from jose import jwt

class JwtService:

    def __init__(self, token_expiry = 1000, token_signing_algorithm = 'HS256'):
        self.token_expiry = token_expiry
        self.token_signing_algorithm = token_signing_algorithm

    def encode(self, private_key, payload):
        return jwt.encode(payload, private_key, algorithm=self.token_signing_algorithm)
