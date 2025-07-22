import os
import sys
import traceback

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urlshortener.settings')

# Import and setup Django
import django
django.setup()

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application

# Create the WSGI app
app = get_wsgi_application()
