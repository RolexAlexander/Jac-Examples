import http.server
import socketserver
from jaseci.actions.live_actions import jaseci_action

@jaseci_action(act_group=["Serv"], allow_remote=True)

def Serv_File():
    # Set the port number for the file server
    PORT = 8080

    # Create a handler for the file server
    Handler = http.server.SimpleHTTPRequestHandler

    # Create a socketserver instance
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        # Print a message to the console
        print("Serving files at port", PORT)
        
        # Start the file server
        httpd.serve_forever()
