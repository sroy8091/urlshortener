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

            # Check database connection
            from django.db import connection
            from django.core.management import call_command
            from io import StringIO
            
            # Test database connection
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            
            # Run migrations
            migration_output = StringIO()
            call_command('migrate', stdout=migration_output, verbosity=2)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                'status': 'success',
                'message': 'Database connected and migrations completed',
                'database': str(connection.settings_dict['ENGINE']),
                'output': migration_output.getvalue()
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
                'traceback': traceback.format_exc()
            }
            
            self.wfile.write(json.dumps(response, indent=2).encode())
