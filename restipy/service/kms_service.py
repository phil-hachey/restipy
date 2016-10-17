import boto3

from base64 import b64decode
from botocore.exceptions import ClientError

class KmsService:
    def __init__(self, session):
        self.session = session

    def decrypt(self, ciphertext_blob):
        client = self.session.client('kms')

        try:
            decoded_ciphertext_blob = b64decode(ciphertext_blob)
            response = client.decrypt(
                CiphertextBlob=decoded_ciphertext_blob
            )
            plain_text = response['Plaintext']
        except(ClientError, TypeError):
            pass

        return ciphertext_blob
