class Producto:
    """Clase que representa un producto en la tienda."""
    def __init__(self, id, nombre, descripcion, precio, imagen):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.imagen = imagen

    def get_details(self):
        """Devuelve los detalles del producto."""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "imagen": self.imagen
        }

    def set_details(self, nombre, descripcion, precio, imagen):
        """Establece los detalles del producto."""
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.imagen = imagen
