import xmlrpc.client

from functions.menu import menu
from functions.send_csv import send_csv


print("Connecting to server...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')

response = server.ping('Ping')
if response != 'Pong':
    raise ValueError("Unexpected response from server: " + response)

op = 'not 0'

while op != '0':
    op = menu()

    if op == '1':
        send_csv(server)

    if op == '2':
        print(server.teste())




