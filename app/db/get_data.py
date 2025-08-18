import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import logging
import psycopg2
import numpy as np
import pandas as pd
from app import Config
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
config = Config()

# Database connection function
def get_connection():
    return psycopg2.connect(
        host=config.DB_HOST,
        database=config.DB_DATABASE,
        user=config.DB_USER,
        password=config.DB_PASSWORD
    )
