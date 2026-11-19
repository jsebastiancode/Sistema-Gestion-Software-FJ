
from excepciones import (
    ReservaInvalida,
    OperacionNoPermitida,
    registrar_evento,
    registrar_error
)


class Reserva:

    def __init__(self, identificacion, cliente, servicio, duracion):
        self.identificacion = identificacion
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.total = 0

        if duracion <= 0:
            raise ReservaInvalida("La duración debe ser positiva.")

        registrar_evento(
            f"Reserva {identificacion} creada para {cliente.nombre}"
        )

    # Confirma la reserva y calcula su valor.
    def confirmar(self, descuento=0, impuesto=0):

        if self.estado != "Pendiente":
            raise OperacionNoPermitida(
                "Solo se pueden confirmar reservas pendientes."
            )

        try:
            self.total = self.servicio.calcular_costo(
                self.duracion, descuento, impuesto
            )

            self.estado = "Confirmada"
            registrar_evento(
                f"Reserva {self.identificacion} confirmada."
            )

            return self.total

        except Exception as error:
            registrar_error(
                f"Error al confirmar reserva: {error}"
            )
            raise ReservaInvalida(
                "No fue posible confirmar la reserva."
            ) from error

    # Cancela una reserva pendiente o confirmada.
    def cancelar(self):

        if self.estado == "Cancelada":
            raise OperacionNoPermitida(
                "La reserva ya se encuentra cancelada."
            )

        self.estado = "Cancelada"

        registrar_evento(
            f"Reserva {self.identificacion} cancelada."
        )

    # Muestra la información de la reserva.
    def mostrar_reserva(self):

        return (
            f"Reserva: {self.identificacion}\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.describir()}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}\n"
            f"Total: ${self.total:,.2f}"
        )
