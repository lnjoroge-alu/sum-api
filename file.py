from http.server import BaseHTTPRequestHandler, HTTPServer
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
   