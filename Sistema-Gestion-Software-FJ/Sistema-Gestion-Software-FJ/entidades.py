
from abc import ABC, abstractmethod
from excepciones import DatosInvalidos, registrar_evento


# Clase abstracta para las entidades del sistema.
class Entidad(ABC):

    def __init__(self, identificacion):
        self.identificacion = identificacion

    @abstractmethod
    def mostrar_informacion(self):
        pass


# Clase Cliente que hereda de Entidad.
class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):
        super().__init__(identificacion)

        # Los atributos privados protegen los datos personales.
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

        self.validar_datos()
        registrar_evento(f"Cliente registrado: {nombre}")

    # Validación de los datos del cliente.
    def validar_datos(self):

        if not self.__nombre.strip():
            raise DatosInvalidos("El nombre no puede estar vacío.")

        if "@" not in self.__correo or "." not in self.__correo:
            raise DatosInvalidos("El correo electrónico no es válido.")

        if not self.__telefono.isdigit() or len(self.__telefono) < 7:
            raise DatosInvalidos("El teléfono debe tener mínimo 7 dígitos.")

    # Métodos para consultar los atributos privados.
    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    # Método sobrescrito de la clase abstracta.
    def mostrar_informacion(self):
        return (
            f"ID: {self.identificacion} | "
            f"Nombre: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )
