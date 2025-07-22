import os
import sys
import json
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Add the project root to Python path
            project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            if project_root not in sys.path:
                sys.path.insert(0, project_root)

            # Set Django settings
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urlshortener.settings')

            # Import and setup Django
            import django
            django.setup()

            from django.db import connection
            from django.conf import settings
            
            # Test database connection
            with connection.cursor() as cursor:
                cursor.execute("SELECT version()")
                db_version = cursor.fetchone()[0] if cursor.fetchone else "Unknown"
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                'status': 'success',
                'database_engine': settings.DATABASES['default']['ENGINE'],
                'database_name': settings.DATABASES['default']['NAME'],
                'postgres_url_present': bool(os.environ.get('POSTGRES_URL')),
                'connection_successful': True
            }
            
            self.wfile.write(json.dumps(response, indent=2).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            import traceback
            response = {
                'status': 'error',
                'message': str(e),
                'postgres_url_present': bool(os.environ.get('POSTGRES_URL')),
                'traceback': traceback.format_exc()
            }
            
            self.wfile.write(json.dumps(response, indent=2).encode())
