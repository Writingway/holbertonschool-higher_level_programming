#!/usr/bin/python3

"""
This module implements a simple HTTP server using the http.server module.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleClassServer(BaseHTTPRequestHandler):
    """
    A simple HTTP server that responds to GET requests with JSON data.
    """
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            data = {
                'message': "Hello, this is a simple API!",
                'status': 'success'
            }
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            data = {
                "message": "OK",
            }
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            data = {
                'message': "Endpoint not found",
                'status': "404 Not Found"
            }
            self.wfile.write(json.dumps(data).encode())


def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleClassServer)
    print("Starting httpd server on port: ", 8080)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
