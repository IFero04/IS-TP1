import xmlrpc.client
from functions.menu import menu
from functions.encode_file import encode_csv
from csv import DictReader

print("Connecting to server...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000', allow_none=True)

response = server.ping('Ping')
if response != 'Pong':
    raise ValueError("Unexpected response from server: " + response)

op = 'not 0'

while op != '0':
    op = menu()

    if op == '1':
        try:
            with open("/data/input/NBA_all_seasons.csv", "rb") as file:
                encode_file = encode_csv(file)
        except Exception as e:
            print(f"An error occurred: {e}")

        try:
            response = server.import_csv(encode_file)
            print(response)
        except Exception as e:
            print(f"An error occurred sending to server: {e}")



