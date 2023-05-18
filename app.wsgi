import sys
import os

# Add the directory containing your Flask application to the sys.path
app_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, app_dir)

# Import your Flask application instance
from index import app as application
