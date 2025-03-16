import mysql.connector
from database import DatabaseConnection
import logging

def setup_logger():
    """Set up the logger for the application."""
    logger = logging.getLogger('producto_dao')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()

class ProductoDAO:
    """Clase de acceso a datos para productos."""

    @staticmethod
    def obtener_productos():
        """Consulta todos los productos."""
        try:
            conexion = DatabaseConnection().get_connection()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM products;")
            productos = cursor.fetchall()
            return productos
        except Exception as e:
            logger.error(f"❌ Error al obtener productos: {e}")
            return []

    @staticmethod
    def obtener_producto_por_id(product_id):
        """Obtiene un producto específico por su ID."""
        try:
            conexion = DatabaseConnection().get_connection()
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM products WHERE id = %s;", (product_id,))
            producto = cursor.fetchone()
            return producto
        except Exception as e:
            logger.error(f"❌ Error al obtener producto por ID: {e}")
            return None

    @staticmethod
    def agregar_producto(nombre, precio, descripcion, imagen):
        """Inserta un nuevo producto en la base de datos."""
        try:
            if not nombre or not isinstance(nombre, str):
                logger.error("El campo 'name' es obligatorio y debe ser una cadena")
                return
            if not precio or not isinstance(precio, (int, float)):
                logger.error("El campo 'price' es obligatorio y debe ser un número")
                return
            if not descripcion or not isinstance(descripcion, str):
                logger.error("El campo 'description' es obligatorio y debe ser una cadena")
                return
            if not isinstance(imagen, bytes):
                logger.error("El campo 'image' debe ser de tipo bytes")
                return

            conexion = DatabaseConnection().get_connection()
            cursor = conexion.cursor()
            consulta = """
                INSERT INTO products (name, price, description, image)
                VALUES (%s, %s, %s, %s);
            """
            cursor.execute(consulta, (nombre, precio, descripcion, imagen))
            conexion.commit()
            logger.info("✅ Producto agregado correctamente.")
        except Exception as e:
            logger.error(f"❌ Error al agregar producto: {e}")
