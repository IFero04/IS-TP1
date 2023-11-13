import xmlrpc.client
from functions.menu import menu

print("Connecting to server...")
server = xmlrpc.client.ServerProxy('http://is-rpc-server:9000')

response = server.ping('Ping')
if response != 'Pong':
    raise ValueError("Unexpected response from server: " + response)

op = 'not 0'

while op != '0':
    op = menu()
    print(op)


