import signal, sys
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

from server_functions.ping import ping
from server_functions.manage_files import import_csv, list_files, remove_file
from server_functions.querys import team_season_stats, team_players


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


with SimpleXMLRPCServer(('0.0.0.0', 9000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()


    def signal_handler(signum, frame):
        print("received signal")
        server.server_close()

        # perform clean up, etc. here...

        print("exiting, gracefully")
        sys.exit(0)


    # signals
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGHUP, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    # register server_functions
    server.register_function(ping)
    server.register_function(import_csv)
    server.register_function(list_files)
    server.register_function(remove_file)
    server.register_function(team_season_stats)
    server.register_function(team_players)

    # start the server
    print("Starting the RPC Server...")
    server.serve_forever()
