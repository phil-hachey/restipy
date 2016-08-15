from jose import jwt

class JwtService:
    def __init__(self, private_key, token_expiry, token_signing_algorithm):
        self.private_key = private_key
        self.token_expiry = token_expiry
        self.token_signing_algorithm = token_signing_algorithm
    
    def encode(self, payload = {}):
        return jwt.encode(payload, self.private_key, algorithm=self.token_signing_algorithm)
