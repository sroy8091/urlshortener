from http.server import BaseHTTPRequestHandler
import os
import sys
import json

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urlshortener.settings')

# Import and setup Django
import django
django.setup()

from django.test import RequestFactory
from django.urls import resolve
from django.http import Http404, HttpResponse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Create Django request factory
            factory = RequestFactory()
            
            # Parse the path 
            path = self.path
            if not path.startswith('/'):
                path = '/' + path
                
            # Create Django request
            django_request = factory.get(path)
            
            # Copy headers
            for header, value in self.headers.items():
                django_request.META[f'HTTP_{header.upper().replace("-", "_")}'] = value
            
            # Resolve URL and get response
            try:
                resolver_match = resolve(path)
                view_func = resolver_match.func
                response = view_func(django_request, **resolver_match.kwargs)
            except Http404:
                response = HttpResponse("Page Not Found", status=404, content_type="text/html")
            except Exception as e:
                response = HttpResponse(f"Internal Server Error: {str(e)}", status=500, content_type="text/html")
            
            # Send response
            self.send_response(response.status_code)
            
            # Send headers
            for header, value in response.items():
                self.send_header(header, value)
            self.end_headers()
            
            # Send content
            if hasattr(response, 'content'):
                self.wfile.write(response.content)
            else:
                self.wfile.write(str(response).encode('utf-8'))
                
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(f"Server Error: {str(e)}".encode('utf-8'))
    
    def do_POST(self):
        try:
            # Get POST data
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length) if content_length > 0 else b''
            
            # Create Django request factory
            factory = RequestFactory()
            
            # Parse the path
            path = self.path
            if not path.startswith('/'):
                path = '/' + path
            
            # Create Django request
            content_type = self.headers.get('Content-Type', '')
            django_request = factory.post(path, data=post_data, content_type=content_type)
            
            # Copy headers
            for header, value in self.headers.items():
                django_request.META[f'HTTP_{header.upper().replace("-", "_")}'] = value
            
            # Resolve URL and get response
            try:
                resolver_match = resolve(path)
                view_func = resolver_match.func
                response = view_func(django_request, **resolver_match.kwargs)
            except Http404:
                response = HttpResponse("Page Not Found", status=404, content_type="text/html")
            except Exception as e:
                response = HttpResponse(f"Internal Server Error: {str(e)}", status=500, content_type="text/html")
            
            # Send response
            self.send_response(response.status_code)
            
            # Send headers
            for header, value in response.items():
                self.send_header(header, value)
            self.end_headers()
            
            # Send content
            if hasattr(response, 'content'):
                self.wfile.write(response.content)
            else:
                self.wfile.write(str(response).encode('utf-8'))
                
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(f"Server Error: {str(e)}".encode('utf-8'))
