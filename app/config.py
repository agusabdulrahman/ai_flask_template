import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_PORT = os.getenv('APP_PORT')
    APP_DEBUG = os.getenv('APP_DEBUG', 'False').lower() == 'true'
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_DATABASE = os.getenv('DB_DATABASE')
    RABBITMQ_URL = os.getenv('RABBITMQ_URL')
    
    # API Headers 
    API_KEY_HEADERS = ""
    
    # API URL
    URL_1 = " "
    URL_2 = " "

    # Sensor model paths
    SENSOR_MODELS = {
        "model_1": {
            "path": os.path.join(os.getenv('BASE_DIR', default='.'),
                                 "app", "services", "model", "model.pkl")
        },
        "model_2": {
            "path": os.path.join(os.getenv('BASE_DIR', default='.'),
                                  "app", "services", "model", "model.pkl")
        }, 
        
    }
    
    def get_model_path(self, sensor_name):
        """
        Retrieves the path to the specified sensor model from the configuration.

        Args:
            sensor_name (str): The name of the sensor (e.g., "model_1", "model_2").

        Returns:
            str: The absolute path to the sensor model file, or None if not found.

        Raises:
            ValueError: If the provided sensor name is not configured.
        """
        if sensor_name not in self.SENSOR_MODELS:
            raise ValueError(f"Invalid sensor name: {sensor_name}")

        return self.SENSOR_MODELS[sensor_name]["path"]
        
