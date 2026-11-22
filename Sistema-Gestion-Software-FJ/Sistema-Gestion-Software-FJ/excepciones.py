import logging

# Configura el archivo donde se guardarán los eventos y errores de la aplicación.
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


# Registra eventos normales o relevantes del sistema en logs.txt.
def registrar_evento(mensaje):
    logging.info(mensaje)


# Registra errores controlados o inesperados en logs.txt.
def registrar_error(mensaje):
    logging.error(mensaje)


# Excepción base para todos los errores de dominio de Software FJ.
class ErrorSistema(Exception):
    pass


# Se lanza cuando los datos ingresados no cumplen las reglas de validación.
class DatosInvalidos(ErrorSistema):
    pass


# Se lanza cuando se intenta ejecutar una acción no permitida por el estado actual.
class OperacionNoPermitida(ErrorSistema):
    pass


# Se lanza cuando un servicio no existe o no está disponible.
class ServicioNoDisponible(ErrorSistema):
    pass


# Se lanza cuando una reserva tiene datos inválidos o falla su confirmación/procesamiento.
class ReservaInvalida(ErrorSistema):
    pass