# main.py scripts will act as our execution script 
from http.server import HTTPServer
from server import ServerRequestHandler

# We define the host & port no where we will be launching our web server.
HOST_NAME = 'localhost'
PORT = 8000

if __name__ == '__main__':
    """ HTTPServer object which takes in two arguments
        1. Tuple containing (HOST_NAME, PORT_NUM) 
        2. Request Handler """ 
    server = HTTPServer((HOST_NAME, PORT), ServerRequestHandler)
    print("SERVER IS UP")
    server.serve_forever()


    