from jose import jwt

class JwtService:

    def encode(self, payload, private_key, token_expiry, token_signing_algorithm):
        return jwt.encode(payload, private_key, algorithm=token_signing_algorithm)
