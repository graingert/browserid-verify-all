#browserid verify all



import string,cgi,time

from os import curdir, sep

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

#import pri



class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
       self.send_response(200)

       self.send_header('Content-type',	'application/json')

       self.end_headers()

       self.wfile.write('{"status": "okay",    "email": "tagrain@gmail.com",    "audience": "http://localhost:8080",    "expires": 99999999999999999,    "issuer": "browserid.org"}')

       return

    def do_POST(self):

       self.send_response(200)

       self.send_header('Content-type',	'application/json')

       self.end_headers()

       self.wfile.write('{"status": "okay",    "email": "tagrain@gmail.com",    "audience": "http://localhost:8080",    "expires": 99999999999999999,    "issuer": "browserid.org"}')

       return



def main():

    try:

        server = HTTPServer(('', 8080), MyHandler)

        print 'started httpserver...'

        server.serve_forever()

    except KeyboardInterrupt:

        print '^C received, shutting down server'

        server.socket.close()



if __name__ == '__main__':

    main()


