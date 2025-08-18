import logging
import sys
import os
from logging.handlers import TimedRotatingFileHandler

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logging():
    """Setup scalable logging for big apps."""
    log_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # --- Console handler ---
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(log_formatter)

    # --- File handler (daily rotating) ---
    log_file = os.path.join(LOG_DIR, "app.log")
    file_handler = TimedRotatingFileHandler(
        log_file, when="midnight", interval=1, backupCount=30, encoding="utf-8"
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(log_formatter)

    # --- Root logger ---
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    root_logger.handlers = []  # clear default handlers
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    # Example: silence noisy libraries
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    
    
    
def setup_logging_sub():
    """
    Setup global logging configuration with UTF-8 support for Windows terminals.
    This should be called once during app startup.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)]
    )

    # Reconfigure encoding for StreamHandler (UTF-8)
    for handler in logging.getLogger().handlers:
        if isinstance(handler, logging.StreamHandler) and hasattr(handler.stream, 'reconfigure'):
            handler.stream.reconfigure(encoding='utf-8')
     

def get_logger(name: str):
    """Get a named logger for a module."""
    return logging.getLogger(name)
