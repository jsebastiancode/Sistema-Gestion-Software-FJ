from entidades import Cliente
from servicios import Servicio
from excepciones import (
    ReservaInvalida,
    OperacionNoPermitida,
    registrar_evento,
    registrar_error
)


class Reserva:

    def __init__(self, identificacion, cliente, servicio, duracion):
        if not isinstance(identificacion, str) or not identificacion.strip():
            raise ReservaInvalida("El identificador de la reserva es obligatorio.")

        if not isinstance(cliente, Cliente):
            raise ReservaInvalida("Debe asociarse un cliente válido a la reserva.")

        if not isinstance(servicio, Servicio):
            raise ReservaInvalida("Debe asociarse un servicio válido a la reserva.")

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ReservaInvalida("La duración debe ser un número positivo.")

        # Verifica disponibilidad al momento de crear la reserva.
        servicio.verificar_disponibilidad()

        self.identificacion = identificacion.strip()
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.total = 0.0

        registrar_evento(
            f"Reserva {self.identificacion} creada para {self.cliente.nombre} - Servicio: {self.servicio.nombre}"
        )

    # Confirma la reserva y calcula su valor usando parámetros opcionales.
    def confirmar(self, descuento=0, impuesto=0):
        if self.estado != "Pendiente":
            raise OperacionNoPermitida(
                f"Solo se pueden confirmar reservas pendientes. Estado actual: {self.estado}."
            )

        try:
            self.total = self.servicio.calcular_costo(
                self.duracion, descuento=descuento, impuesto=impuesto
            )
            self.estado = "Confirmada"
            registrar_evento(
                f"Reserva {self.identificacion} confirmada por un total de ${self.total:,.2f}."
            )
            return self.total

        except Exception as error:
            registrar_error(f"Error al confirmar reserva {self.identificacion}: {error}")
            # Encadenamiento explícito de excepciones (raise ... from ...).
            raise ReservaInvalida(
                f"No fue posible confirmar la reserva {self.identificacion}."
            ) from error

    # Cancela una reserva pendiente o confirmada.
    def cancelar(self):
        if self.estado == "Cancelada":
            raise OperacionNoPermitida(
                f"La reserva {self.identificacion} ya se encuentra cancelada."
            )

        self.estado = "Cancelada"
        registrar_evento(f"Reserva {self.identificacion} cancelada.")

    # Procesa la reserva según la acción solicitada ('confirmar' o 'cancelar').
    def procesar(self, accion="confirmar", descuento=0, impuesto=0):
        accion_normalizada = accion.lower().strip() if isinstance(accion, str) else ""

        if accion_normalizada == "confirmar":
            return self.confirmar(descuento=descuento, impuesto=impuesto)
        elif accion_normalizada == "cancelar":
            self.cancelar()
            return self.estado
        else:
            raise OperacionNoPermitida(f"Acción de procesamiento no válida: '{accion}'.")

    # Muestra la información completa de la reserva.
    def mostrar_reserva(self):
        return (
            f"Reserva: {self.identificacion}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.describir()}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}\n"
            f"Total: ${self.total:,.2f}"
        )