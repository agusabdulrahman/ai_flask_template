import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import time
import math
import logging
import pandas as pd
from ..config import Config
from flask import Blueprint, request, jsonify, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST


# Initialize the Flask application
bp = Blueprint('main', __name__)

config = Config()

# Metrics
REQUEST_COUNT = Counter(
    "http_requests_total", "Total HTTP Requests",
    ["method", "endpoint", "http_status"]
)
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds", "Request latency",
    ["endpoint"]
)

# Middleware untuk metrics
@bp.before_request
def before_request_func():
    request.start_time = time.time()

@bp.after_request
def after_request_func(response):
    try:
        request_latency = time.time() - request.start_time
        REQUEST_LATENCY.labels(request.path).observe(request_latency)
        REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()
    except Exception as e:
        logging.error(f"Metrics error: {e}")
    return response

@bp.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# Contoh API
@bp.route("/api/ping")
def ping():
    return jsonify({"message": "pong"})

# Flask app
@bp.route('/')
def home():
    """Home route."""
    return "Welcome to the flask framework"
