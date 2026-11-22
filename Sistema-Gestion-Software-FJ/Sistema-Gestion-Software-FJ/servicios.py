from abc import ABC, abstractmethod
from entidades import Entidad
from excepciones import DatosInvalidos, ServicioNoDisponible, registrar_evento


# Clase abstracta base para todos los servicios ofrecidos por Software FJ.
class Servicio(Entidad, ABC):

    def __init__(self, identificacion, nombre, tarifa_base, disponible=True):
        super().__init__(identificacion)
        self.nombre = nombre
        self.tarifa_base = tarifa_base
        self.disponible = disponible

        # Valida los atributos básicos del servicio.
        self.validar_parametros()
        registrar_evento(f"Servicio creado: {self.nombre} ({self.identificacion})")

    # Valida parámetros comunes y permite que cada subclase añada reglas propias.
    def validar_parametros(self):
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise DatosInvalidos("El nombre del servicio no puede estar vacío.")

        if not isinstance(self.tarifa_base, (int, float)) or isinstance(self.tarifa_base, bool) or self.tarifa_base <= 0:
            raise DatosInvalidos("La tarifa base debe ser un número mayor que cero.")

        if not isinstance(self.disponible, bool):
            raise DatosInvalidos("La disponibilidad del servicio debe ser booleana.")

        self.nombre = self.nombre.strip()

    # Verifica que el servicio esté disponible antes de operar con él.
    def verificar_disponibilidad(self):
        if not self.disponible:
            raise ServicioNoDisponible(f"El servicio '{self.nombre}' no está disponible.")

    # Método auxiliar reutilizable para calcular costo con descuento e impuesto opcionales.
    def _calcular_con_ajustes(self, subtotal, descuento=0, impuesto=0):
        if subtotal < 0:
            raise DatosInvalidos("El subtotal no puede ser negativo.")

        if not isinstance(descuento, (int, float)) or isinstance(descuento, bool) or not (0 <= descuento <= 100):
            raise DatosInvalidos("El descuento debe estar entre 0 y 100.")

        if not isinstance(impuesto, (int, float)) or isinstance(impuesto, bool) or not (0 <= impuesto <= 100):
            raise DatosInvalidos("El impuesto debe estar entre 0 y 100.")

        con_descuento = subtotal * (1 - descuento / 100)
        total = con_descuento * (1 + impuesto / 100)
        return round(total, 2)

    # Calcula el costo según duración y parámetros opcionales (variantes de cálculo).
    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    # Devuelve una descripción legible del servicio.
    @abstractmethod
    def describir(self):
        pass

    # Implementación del método abstracto heredado de Entidad.
    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"[{self.identificacion}] {self.describir()} | Tarifa base: ${self.tarifa_base:,.2f} | {estado}"


# Servicio especializado 1: Reserva de salas.
class ServicioSala(Servicio):

    def __init__(self, identificacion, nombre, tarifa_base, capacidad=10, disponible=True):
        self.capacidad = capacidad
        super().__init__(identificacion, nombre, tarifa_base, disponible)

    def validar_parametros(self):
        super().validar_parametros()
        if not isinstance(self.capacidad, int) or isinstance(self.capacidad, bool) or self.capacidad <= 0:
            raise DatosInvalidos("La capacidad de la sala debe ser un entero positivo.")

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.verificar_disponibilidad()
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidos("La duración en horas para la sala debe ser mayor que cero.")

        # Recargo leve si la sala supera 15 personas.
        recargo_capacidad = 1.15 if self.capacidad > 15 else 1.0
        subtotal = self.tarifa_base * duracion * recargo_capacidad
        return self._calcular_con_ajustes(subtotal, descuento, impuesto)

    def describir(self):
        return f"Reserva de Sala: {self.nombre} (capacidad: {self.capacidad} personas)"


# Servicio especializado 2: Alquiler de equipos.
class ServicioEquipo(Servicio):

    def __init__(self, identificacion, nombre, tarifa_base, cargo_mantenimiento=5000, disponible=True):
        self.cargo_mantenimiento = cargo_mantenimiento
        super().__init__(identificacion, nombre, tarifa_base, disponible)

    def validar_parametros(self):
        super().validar_parametros()
        if (
            not isinstance(self.cargo_mantenimiento, (int, float))
            or isinstance(self.cargo_mantenimiento, bool)
            or self.cargo_mantenimiento < 0
        ):
            raise DatosInvalidos("El cargo de mantenimiento no puede ser negativo.")

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.verificar_disponibilidad()
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidos("La duración del alquiler debe ser mayor que cero.")

        subtotal = (self.tarifa_base * duracion) + self.cargo_mantenimiento
        return self._calcular_con_ajustes(subtotal, descuento, impuesto)

    def describir(self):
        return f"Alquiler de Equipo: {self.nombre}"


# Servicio especializado 3: Asesorías especializadas.
class ServicioAsesoria(Servicio):

    def __init__(self, identificacion, nombre, tarifa_base, modalidad="Remota", disponible=True):
        self.modalidad = modalidad
        super().__init__(identificacion, nombre, tarifa_base, disponible)

    def validar_parametros(self):
        super().validar_parametros()
        if not isinstance(self.modalidad, str) or not self.modalidad.strip():
            raise DatosInvalidos("La modalidad de la asesoría no puede estar vacía.")
        self.modalidad = self.modalidad.strip()

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.verificar_disponibilidad()
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidos("La duración en horas de la asesoría debe ser mayor que cero.")

        subtotal = self.tarifa_base * duracion
        return self._calcular_con_ajustes(subtotal, descuento, impuesto)

    def describir(self):
        return f"Asesoría Especializada: {self.nombre} ({self.modalidad})"
