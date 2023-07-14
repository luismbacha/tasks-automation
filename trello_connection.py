from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
import getpass
from trello import TrelloClient

def get_trello_client():
    try:
        pwd = getpass.getpass("Enter your password: ")
        salt = getpass.getpass("Enter your salt: ")
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt.encode(),
            iterations=100000
        )
        fernet_key = Fernet(base64.urlsafe_b64encode(kdf.derive(pwd.encode())))
        pwd = "x" * len(pwd)
        del pwd
        salt = "y" * len(salt)
        del salt
    except Exception as e:
        print("Error initializing connection")
        print("Error", str(e))
        raise
    try:
        trello_key = fernet_key.decrypt(os.environ["T_KEY"].encode()).decode()
        trello_token = fernet_key.decrypt(os.environ["T_TOKEN"].encode()).decode()
        trello_secret = fernet_key.decrypt(os.environ["T_SECRET"].encode()).decode()
        client = TrelloClient(
            api_key=trello_key,
            api_secret=trello_secret,
            token=trello_token
        )
        trello_key = "w" * len(trello_key)
        del trello_key
        trello_token = "x" * len(trello_token)
        del trello_token
        trello_secret = "y" * len(trello_secret)
        fernet_key = "y" * len(trello_secret)
        del trello_secret
        del fernet_key
    except Exception as e:
        print("Connection error")
        print(str(e))
        raise
    return client
