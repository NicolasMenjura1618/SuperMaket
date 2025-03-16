import logging

# Usa el patrón Singleton para evitar múltiples conexiones a MySQL.
import mysql.connector

def setup_logger():
    """Set up the logger for the application."""
    logger = logging.getLogger('database_connection')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

class DatabaseConnection:
    logger = setup_logger()

    """Clase Singleton para manejar la conexión a MySQL."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                database="superMarket"
            )
        return cls._instance

    def test_connection(self):
        """Test the database connection."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT 1")
            cursor.close()
            self.logger.info("Database connection successful.")
            return True

        except mysql.connector.Error as err:
            self.logger.error(f"Error: {err}")
            self.logger.error("Database connection failed.")

            return False

    def get_connection(self):

        """Devuelve la conexión a la base de datos."""
        return self.connection
