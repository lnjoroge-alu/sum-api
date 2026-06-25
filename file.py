from http.server import BaseHTTPRequestHandler, HTTPServer
from logging import Handler
from urllib.parse import urlparse, parse_qs
import json
 
def calculate(op, a, b):
    if op == 'add':
        return a + b
    elif op == 'subtract':
        return a - b
    elif op == 'multiply':
        return a * b
    elif op == 'divide':
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")
    else:
        raise ValueError("Invalid operation")
    
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        op = url.path.strip("/")
        params = parse_qs(url.query)
        a = int(params["a"][0])
        b = int(params["b"][0])
 
        result = calculate(op, a, b)
 
        body = json.dumps({"a": a, "b": b, "operation": op, "result": result})
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body.encode())


HTTPServer(("localhost", 5000), Handler).serve_forever()