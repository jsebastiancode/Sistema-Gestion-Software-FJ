
from abc import ABC, abstractmethod
from excepciones import DatosInvalidos, ServicioNoDisponible


# Clase abstracta de los servicios.
class Servicio(ABC):

    def __init__(self, nombre, precio, disponible=True):
        self.nombre = nombre
        self.precio = precio
        self.disponible = disponible

        if not isinstance(precio, (int, float)) or precio <= 0:
            raise DatosInvalidos("El precio debe ser mayor que cero.")

    # Método abstracto para calcular costos.
    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    # Método abstracto para describir el servicio.
    @abstractmethod
    def describir(self):
        pass

    # Validación general de los servicios.
    def validar_parametros(self, duracion):

        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise DatosInvalidos("La duración debe ser mayor que cero.")

        if not self.disponible:
            raise ServicioNoDisponible(
                f"El servicio {self.nombre} no está disponible."
            )


# Servicio para reservar salas.
class ServicioSala(Servicio):

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)

        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise DatosInvalidos("Descuento o impuesto inválido.")

        subtotal = self.precio * duracion
        subtotal -= subtotal * descuento / 100

        return subtotal + (subtotal * impuesto / 100)

    def describir(self):
        return f"Reserva de sala: {self.nombre}"


# Servicio para alquilar equipos.
class ServicioEquipo(Servicio):

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)

        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise DatosInvalidos("Descuento o impuesto inválido.")

        subtotal = self.precio * duracion
        subtotal -= subtotal * descuento / 100

        return subtotal + (subtotal * impuesto / 100)

    def describir(self):
        return f"Alquiler de equipo: {self.nombre}"


# Servicio para asesorías especializadas.
class ServicioAsesoria(Servicio):

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)

        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise DatosInvalidos("Descuento o impuesto inválido.")

        subtotal = self.precio * duracion
        subtotal -= subtotal * descuento / 100

        return subtotal + (subtotal * impuesto / 100)

    def describir(self):
        return f"Asesoría especializada: {self.nombre}"
