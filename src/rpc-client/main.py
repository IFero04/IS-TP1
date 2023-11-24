import xmlrpc.client

from functions.menu import menu, second_menu
from functions.send_csv import send_csv
from functions.list_files import list_files
from functions.remove_file import remove_file
from functions.requests import *


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
        list_files(server)

    elif op == '3':
        remove_file(server)

    elif op == '4':
        second_op = second_menu()

        if second_op == '1':
            query_team_season_stats(server)

        elif second_op == '2':
            query_team_players(server)

        elif second_op == '3':
            query_top_players(server)

    if op != '0' and not (op == '4' and second_op == '0'):
        input('PRESS ENTER TO CONTINUE')
