# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:32:23 2021

@author: arhan
"""

import os
from http.server import HTTPServer, CGIHTTPRequestHandler
# Make sure the server is created at current directory
os.chdir('.')
# Create server object listening the port 8080
server_object = HTTPServer(server_address=('', 8080), RequestHandlerClass=CGIHTTPRequestHandler)
# Start the web server
server_object.serve_forever()