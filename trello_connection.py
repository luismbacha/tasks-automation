from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
import getpass
from trello import TrelloClient

def getTrelloClient():
    try:
        pwd = getpass.getpass("Enter your password: ")
        salt = getpass.getpass("Enter your salt: ")
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt.encode(),
            iterations=100000
        )
        fernetKey = Fernet(base64.urlsafe_b64encode(kdf.derive(pwd.encode())))
        pwd = "x" * len(pwd)
        del pwd
        salt = "y" * len(salt)
        del salt
    except Exception as e:
        print("Error initializing connection")
        print("Error", str(e))
        raise
    try:
        trelloKey = fernetKey.decrypt(os.environ["T_KEY"].encode()).decode()
        trelloToken = fernetKey.decrypt(os.environ["T_TOKEN"].encode()).decode()
        trelloSecret = fernetKey.decrypt(os.environ["T_SECRET"].encode()).decode()
        client = TrelloClient(
            api_key=trelloKey,
            api_secret=trelloSecret,
            token=trelloToken
        )
        trelloKey = "w" * len(trelloKey)
        del trelloKey
        trelloToken = "x" * len(trelloToken)
        del trelloToken
        trelloSecret = "y" * len(trelloSecret)
        fernetKey = "y" * len(trelloSecret)
        del trelloSecret
        del fernetKey
        print(str(client.list_boards()))
    except Exception as e:
        print("Connection error")
        print(str(e))
        raise
    return client
