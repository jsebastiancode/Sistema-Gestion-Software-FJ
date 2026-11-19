
# SISTEMA INTEGRAL DE GESTION SOFTWARE FJ

# Importacion de las clases necesarias.
from entidades import Cliente

from servicios import (
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria
)

from reservas import Reserva

from excepciones import (
    ErrorSistema,
    registrar_evento,
    registrar_error
)


# Listas para almacenar los datos en memoria.
clientes = []
servicios = []
reservas = []


# Funcion para mostrar titulos.
def mostrar_titulo(texto):
    print("\n" + "=" * 55)
    print(texto)
    print("=" * 55)


# Funcion principal del sistema.
def ejecutar_sistema():

    mostrar_titulo("SISTEMA INTEGRAL SOFTWARE FJ")

    reserva1 = None
    reserva2 = None
    cliente1 = None
    cliente2 = None
    sala = None
    equipo = None
    asesoria = None

    # OPERACION 1: Registrar cliente valido.
    try:
        cliente1 = Cliente(
            "C001",
            "Carlos Perez",
            "carlos@gmail.com",
            "3001234567"
        )
        clientes.append(cliente1)
        print("1. Cliente registrado correctamente.")

    except ErrorSistema as error:
        registrar_error(str(error))
        print("1. Error:", error)

    # OPERACION 2: Registrar segundo cliente.
    try:
        cliente2 = Cliente(
            "C002",
            "Maria Lopez",
            "maria@gmail.com",
            "3101234567"
        )
        clientes.append(cliente2)
        print("2. Segundo cliente registrado.")

    except ErrorSistema as error:
        registrar_error(str(error))
        print("2. Error:", error)

    # OPERACION 3: Intentar registrar cliente invalido.
    try:
        cliente3 = Cliente(
            "C003",
            "",
            "correoIncorrecto",
            "123"
        )
        clientes.append(cliente3)

    except ErrorSistema as error:
        registrar_error(str(error))
        print("3. Cliente invalido rechazado:", error)

    # OPERACION 4: Crear servicio de sala.
    try:
        sala = ServicioSala("Sala de reuniones", 50000)
        servicios.append(sala)
        print("4. Servicio de sala creado.")

    except ErrorSistema as error:
        registrar_error(str(error))
        print("4. Error:", error)

    # OPERACION 5: Crear servicio de equipo.
    try:
        equipo = ServicioEquipo("Video Beam", 30000)
        servicios.append(equipo)
        print("5. Servicio de equipo creado.")

    except ErrorSistema as error:
        registrar_error(str(error))
        print("5. Error:", error)

    # OPERACION 6: Crear servicio de asesoria.
    try:
        asesoria = ServicioAsesoria(
            "Asesoria informatica", 80000
        )
        servicios.append(asesoria)
        print("6. Servicio de asesoria creado.")

    except ErrorSistema as error:
        registrar_error(str(error))
        print("6. Error:", error)

    # OPERACION 7: Intentar crear servicio invalido.
    try:
        servicio_invalido = ServicioSala(
            "Sala incorrecta", -500
        )
        servicios.append(servicio_invalido)

    except ErrorSistema as error:
        registrar_error(str(error))
        print("7. Servicio invalido rechazado:", error)

    # OPERACION 8: Crear una reserva.
    try:
        if cliente1 is None or sala is None:
            raise ErrorSistema(
                "No existen datos para crear la reserva."
            )

        reserva1 = Reserva(
            "R001", cliente1, sala, 2
        )
        reservas.append(reserva1)
        print("8. Reserva creada correctamente.")

    except ErrorSistema as error:
        registrar_error(str(error))
        print("8. Error:", error)

    # OPERACION 9: Confirmar la primera reserva.
    try:
        if reserva1 is None:
            raise ErrorSistema("La reserva no existe.")

        total = reserva1.confirmar(10, 19)
        print(f"9. Reserva confirmada. Total: ${total:,.2f}")

    except ErrorSistema as error:
        registrar_error(str(error))
        print("9. Error:", error)

    # OPERACION 10: Crear reserva con duracion incorrecta.
    try:
        reserva_invalida = Reserva(
            "R002", cliente2, equipo, 0
        )
        reservas.append(reserva_invalida)

    except ErrorSistema as error:
        registrar_error(str(error))
        print("10. Reserva invalida rechazada:", error)

    # OPERACION 11: Crear y confirmar reserva de equipo.
    try:
        if cliente2 is None or equipo is None:
            raise ErrorSistema("Faltan datos para la reserva.")

        reserva2 = Reserva(
            "R003", cliente2, equipo, 3
        )
        reservas.append(reserva2)

        total = reserva2.confirmar()
        print(f"11. Reserva confirmada. Total: ${total:,.2f}")

    except ErrorSistema as error:
        registrar_error(str(error))
        print("11. Error:", error)

    # OPERACION 12: Cancelar reserva.
    try:
        if reserva2 is None:
            raise ErrorSistema("La reserva no existe.")

        reserva2.cancelar()
        print("12. Reserva cancelada correctamente.")

    except ErrorSistema as error:
        registrar_error(str(error))
        print("12. Error:", error)

    # OPERACION 13: Intentar cancelar nuevamente.
    try:
        if reserva2 is None:
            raise ErrorSistema("La reserva no existe.")

        reserva2.cancelar()

    except ErrorSistema as error:
        registrar_error(str(error))
        print("13. Error controlado:", error)

    # OPERACION 14: Calcular costo de asesoria.
    try:
        if asesoria is None:
            raise ErrorSistema("La asesoria no existe.")

        costo = asesoria.calcular_costo(2, 15, 19)
        print(f"14. Costo de asesoria: ${costo:,.2f}")

    except ErrorSistema as error:
        registrar_error(str(error))
        print("14. Error:", error)

    # OPERACION 15: Consultar clientes registrados.
    try:
        mostrar_titulo("CLIENTES REGISTRADOS")

        for cliente in clientes:
            print(cliente.mostrar_informacion())

    except Exception as error:
        registrar_error(str(error))
        print("Error al consultar clientes:", error)

    else:
        print("Consulta realizada correctamente.")

    finally:
        registrar_evento(
            "Finalizacion de consulta de clientes."
        )
        print("Proceso de consulta finalizado.")

    # OPERACION 16: Consultar reservas.
    mostrar_titulo("RESERVAS DEL SISTEMA")

    for reserva in reservas:
        print(reserva.mostrar_reserva())
        print("-" * 40)

    # Resumen general.
    mostrar_titulo("RESUMEN DEL SISTEMA")

    print("Clientes registrados:", len(clientes))
    print("Servicios creados:", len(servicios))
    print("Reservas creadas:", len(reservas))

    registrar_evento(
        "Ejecucion del sistema finalizada."
    )

    print("\nEl sistema Software FJ termino correctamente.")
    print("Los registros se encuentran en logs.txt")


# Bloque principal de ejecucion.
if __name__ == "__main__":

    try:
        ejecutar_sistema()

    except Exception as error:
        registrar_error(
            f"Error general del programa: {error}"
        )
        print("Error inesperado:", error)
