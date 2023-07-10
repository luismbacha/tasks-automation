from trello_connection import getTrelloClient
import sys
import getpass

def main():
    try:
        client = getTrelloClient()
    except Exception as e:
        print("Connection failed, finishing script execution")
        return
    
main()
