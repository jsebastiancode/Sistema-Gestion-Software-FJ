
import logging

# Configuración del archivo donde se guardan los eventos y errores.
logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)
# Función para registrar los eventos del sistema.
def registrar_evento(mensaje):
    logging.info(mensaje)

# Función para registrar los errores.
def registrar_error(mensaje):
    logging.error(mensaje)


# Excepción general del sistema.
class ErrorSistema(Exception):
    pass


# Excepción para datos incorrectos.
class DatosInvalidos(ErrorSistema):
    pass


# Excepción para operaciones no permitidas.
class OperacionNoPermitida(ErrorSistema):
    pass


# Excepción cuando un servicio no está disponible.
class ServicioNoDisponible(ErrorSistema):
    pass


# Excepción para reservas incorrectas.
class ReservaInvalida(ErrorSistema):
    pass
