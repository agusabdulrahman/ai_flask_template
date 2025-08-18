import logging
import datetime
from flask import Flask
from .config import Config
from .routers import main_routes
from app.utils import setup_logging

# Setup logger
log_logging = setup_logging()

# Initialize app
app = Flask(__name__)
app.config.from_object(Config)
app.json.sort_keys = False
app.logger.setLevel(logging.DEBUG)
# app.logger.addHandler(log_file_handler)

# Register routes
app.register_blueprint(main_routes.bp)
    
