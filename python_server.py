import http.server
import socketserver


# Python Program to Get IP Address 
import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)    
print("to connect type ipaddress:8000 in web browser")




PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

    
