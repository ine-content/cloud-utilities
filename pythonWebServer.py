#! /usr/bin/python3

# Simple web server. Call with no query string to return an HTML page. use ?api to return a JSON result.
# Default port is 8080.
# This can be changed by setting an environment variable: INE_PORT=8088
#   or adding the port as a command line parameter: python3 pythonWebServer.py 8088
# Created based on the example at https://pythonbasics.org/webserver/
# Created by: Tracy Wallace
# Created on: 2022-07-22

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import socket
import os
import sys

hostName = ''
serverPort = os.getenv('INE_PORT') or 8080
serverPort = sys.argv[1] if len(sys.argv) > 1 else serverPort
serverPort = int(serverPort)

actualHostName = socket.gethostname()
actualhostIp = socket.gethostbyname(actualHostName)

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):

        self.send_response(200)
        if self.path.find('api') == -1:
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>INE Simple web site.</title></head>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<h2>INE Simple Web App</h2>", "utf-8"))
            self.wfile.write(bytes("<p>This web app is written with a simple Python script. It is not robust, so be gentle.</p>", "utf-8"))
            self.wfile.write(bytes("<table><tr style='text-align:left'><th>Setting</th><th>Value</ht></tr>", "utf-8"))
            self.wfile.write(bytes(f"<tr><td>Host name</td><td>{actualHostName}</td></tr>", "utf-8"))
            self.wfile.write(bytes(f"<tr><td>Host IP</td><td>{actualhostIp}</td></tr>", "utf-8"))
            self.wfile.write(bytes(f"<tr><td>Requestor Address</td><td>{self.address_string()}</td></tr>", "utf-8"))
            self.wfile.write(bytes(f"<tr><td>Request date</td><td>{self.date_time_string()}</td></tr>", "utf-8"))
            self.wfile.write(bytes("</table>", "utf-8"))
            
            self.wfile.write(bytes("</body></html>", "utf-8"))
        else:
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes("{", "utf-8"))
            self.wfile.write(bytes(f"'hostName':'{actualHostName}',", "utf-8"))
            self.wfile.write(bytes(f"'hostIp':'{actualhostIp}',", "utf-8"))
            self.wfile.write(bytes(f"'requestorAddress':'{self.address_string()}',", "utf-8"))
            self.wfile.write(bytes(f"'requestDate':'{self.date_time_string()}'", "utf-8"))
            self.wfile.write(bytes("}", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
