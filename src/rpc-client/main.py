import xmlrpc.client

from functions.menu import menu, second_menu
from functions.send_csv import send_csv
from functions.requests import query_team_season_stats


print("Connecting to server...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')

response = server.ping('Ping')
if response != 'Pong':
    raise ValueError("Unexpected response from server: " + response)

op = None
second_op = None

while op != '0':
    op = menu()

    if op == '1':
        send_csv(server)

    elif op == '2':
        pass

    elif op == '3':
        pass

    elif op == '4':
        second_op = second_menu()

        if second_op == '1':
            query_team_season_stats(server)

        elif second_op == '2':
            pass

    if op != '0' and not (op == '4' and second_op == '0'):
        input('PRESS ENTER TO CONTINUE')
