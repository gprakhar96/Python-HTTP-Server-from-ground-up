# server.py will contain class that will be running our server
from http.server import BaseHTTPRequestHandler

""" BaseHTTPRequestHandler class is used to handle the HTTP requests that arrives at the server. It must be subclassed by your own class to handle each HTTP request method. 

The BaseHTTPRequestHandler class parses the HTTP request & headers, then call a method specific to the request type(GET, POST etc.)

It provides classes, instance variables & methods that can be used by subclass.

"""
class ServerRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """ HTTP Response = Response + Headers + Body(containing the resource to be share in bytes)"""
        self.send_response(200) # Adds response type (200 OK) to the HTTP Response
        self.send_header('Content-type', 'text/html') # Adds headers to the HTTP Response
        self.end_headers() # Ends headers
        no_of_bytes = self.wfile.write(bytes("Hello World","UTF-8")) # Adds content to be send to the HTTP Response
        print(no_of_bytes)

    def do_POST(self):
        print("POST HTTP request recieved")

    def do_HEAD(self):
        print("HEAD HTTP request recieved")
    