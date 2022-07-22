# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import socket

hostName = "localhost"
serverPort = 8080

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
            self.wfile.write(bytes("<table><tr><th>Setting</th><th>Value</ht></tr>", "utf-8"))
            self.wfile.write(bytes(f"<tr><td>Host name</td><td>{socket.gethostname()}</td></tr>", "utf-8"))
            self.wfile.write(bytes(f"<tr><td>Host IP</td><td>{self.server.server_address[0]}</td></tr>", "utf-8"))
            self.wfile.write(bytes(f"<tr><td>Requestor Address</td><td>{self.address_string()}</td></tr>", "utf-8"))
            self.wfile.write(bytes(f"<tr><td>Request date</td><td>{self.date_time_string()}</td></tr>", "utf-8"))
            self.wfile.write(bytes("</table>", "utf-8"))
            
            self.wfile.write(bytes("</body></html>", "utf-8"))
        else:
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes("{", "utf-8"))
            self.wfile.write(bytes(f"'hostName':'{socket.gethostname()}',", "utf-8"))
            self.wfile.write(bytes(f"'hostIp':'{self.server.server_address[0]}',", "utf-8"))
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