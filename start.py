from trello_connection import get_trello_client

def main():
    try:
        client = get_trello_client()
    except Exception as e:
        print("Connection failed, finishing script execution")
        return
    boards = client.list_boards()
    board = next(filter(lambda x: x.name.startswith("1"), boards))
    print(str(board.name))
    lists = board.all_lists()
    today_list = next(filter(lambda x: x.name.startswith("Hoy"), lists))
    x = today_list.fetch_actions(action_filter='all')
    print(str(today_list.name))
    print(str(x))
    cards = today_list.list_cards()
    pos = len(cards)
    for card in cards:
        print(str(card.name),str(card.due), str(card.pos))
    
main()
