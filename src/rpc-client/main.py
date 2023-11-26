import xmlrpc.client
import time

from functions.menu import menu, second_menu
from functions.send_csv import send_csv
from functions.list_files import list_files
from functions.remove_file import remove_file
from functions.requests import *


def connect_to_server():
    max_attempts = 10

    for attempt in range(1, max_attempts + 1):
        print(f"Connecting to server... (Attempt {attempt}/{max_attempts})")

        try:
            server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')
            response = server.ping('Ping')
            if response == 'Pong':
                print("Connected to the server successfully!")
                return server
            else:
                print(f"Unexpected response from server on attempt {attempt}: {response}")

        except Exception as e:
            print(f"Attempt {attempt} failed with error: {e}")
            time.sleep(1)

    raise ValueError(f"Failed to connect to the server after {max_attempts} attempts.")


def main():
    server = connect_to_server()

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
                query_avg_stats_players(server)

            elif second_op == '2':
                query_team_players(server)

            elif second_op == '3':
                query_top_players(server)

            elif second_op == '4':
                query_tallest_country(server)

            elif second_op == '5':
                query_team_season_stats(server)

        if op != '0' and not (op == '4' and second_op == '0'):
            input('PRESS ENTER TO CONTINUE')


if __name__ == "__main__":
    main()
