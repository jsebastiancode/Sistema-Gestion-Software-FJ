# SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ

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

# Listas en memoria (sin uso de base de datos).
clientes = []
servicios = []
reservas = []


def mostrar_titulo(texto):
    print("\n" + "=" * 55)
    print(texto)
    print("=" * 55)


def ejecutar_sistema():
    mostrar_titulo("SISTEMA INTEGRAL SOFTWARE FJ")

    cliente1 = None
    cliente2 = None
    sala = None
    equipo = None
    asesoria = None
    reserva1 = None
    reserva2 = None

    # OPERACIÓN 1: Registrar cliente válido.
    try:
        cliente1 = Cliente("C001", "Carlos Perez", "carlos@gmail.com", "3001234567")
        clientes.append(cliente1)
        print("1. Cliente registrado correctamente.")
    except ErrorSistema as error:
        registrar_error(str(error))
        print("1. Error:", error)

    # OPERACIÓN 2: Registrar segundo cliente válido.
    try:
        cliente2 = Cliente("C002", "Maria Lopez", "maria@gmail.com", "3101234567")
        clientes.append(cliente2)
        print("2. Segundo cliente registrado.")
    except ErrorSistema as error:
        registrar_error(str(error))
        print("2. Error:", error)

    # OPERACIÓN 3: Intentar registrar cliente inválido.
    try:
        cliente3 = Cliente("C003", "", "correoIncorrecto", "123")
        clientes.append(cliente3)
    except ErrorSistema as error:
        registrar_error(str(error))
        print("3. Cliente inválido rechazado:", error)

    # OPERACIÓN 4: Crear servicio de sala válido.
    try:
        sala = ServicioSala("S001", "Sala de reuniones", 50000, capacidad=12)
        servicios.append(sala)
        print("4. Servicio de sala creado.")
    except ErrorSistema as error:
        registrar_error(str(error))
        print("4. Error:", error)

    # OPERACIÓN 5: Crear servicio de equipo válido.
    try:
        equipo = ServicioEquipo("E001", "Video Beam", 30000, cargo_mantenimiento=5000)
        servicios.append(equipo)
        print("5. Servicio de equipo creado.")
    except ErrorSistema as error:
        registrar_error(str(error))
        print("5. Error:", error)

    # OPERACIÓN 6: Crear servicio de asesoría válido.
    try:
        asesoria = ServicioAsesoria("A001", "Asesoría informática", 80000, modalidad="Presencial")
        servicios.append(asesoria)
        print("6. Servicio de asesoría creado.")
    except ErrorSistema as error:
        registrar_error(str(error))
        print("6. Error:", error)

    # OPERACIÓN 7: Intentar crear servicio inválido (tarifa negativa).
    try:
        servicio_invalido = ServicioSala("S002", "Sala incorrecta", -500)
        servicios.append(servicio_invalido)
    except ErrorSistema as error:
        registrar_error(str(error))
        print("7. Servicio inválido rechazado:", error)

    # OPERACIÓN 8: Crear una reserva válida.
    try:
        reserva1 = Reserva("R001", cliente1, sala, 2)
        reservas.append(reserva1)
        print("8. Reserva creada correctamente.")
    except ErrorSistema as error:
        registrar_error(str(error))
        print("8. Error:", error)

    # OPERACIÓN 9: Procesar/confirmar la primera reserva con descuento e impuesto.
    try:
        if reserva1 is None:
            raise ErrorSistema("La reserva R001 no existe.")

        total = reserva1.procesar(accion="confirmar", descuento=10, impuesto=19)
        print(f"9. Reserva confirmada. Total: ${total:,.2f}")
    except ErrorSistema as error:
        registrar_error(str(error))
        print("9. Error:", error)

    # OPERACIÓN 10: Intentar crear reserva con duración inválida (0).
    try:
        reserva_invalida = Reserva("R002", cliente2, equipo, 0)
        reservas.append(reserva_invalida)
    except ErrorSistema as error:
        registrar_error(str(error))
        print("10. Reserva inválida rechazada:", error)

    # OPERACIÓN 11: Crear y confirmar reserva de equipo sin descuento/impuesto.
    try:
        reserva2 = Reserva("R003", cliente2, equipo, 3)
        reservas.append(reserva2)
        total = reserva2.confirmar()
        print(f"11. Reserva confirmada. Total: ${total:,.2f}")
    except ErrorSistema as error:
        registrar_error(str(error))
        print("11. Error:", error)

    # OPERACIÓN 12: Cancelar reserva confirmada.
    try:
        if reserva2 is None:
            raise ErrorSistema("La reserva R003 no existe.")

        reserva2.procesar(accion="cancelar")
        print("12. Reserva cancelada correctamente.")
    except ErrorSistema as error:
        registrar_error(str(error))
        print("12. Error:", error)

    # OPERACIÓN 13: Intentar cancelar nuevamente una reserva ya cancelada.
    try:
        if reserva2 is None:
            raise ErrorSistema("La reserva R003 no existe.")

        reserva2.cancelar()
    except ErrorSistema as error:
        registrar_error(str(error))
        print("13. Error controlado:", error)

    # OPERACIÓN 14: Calcular costo de asesoría con descuento e impuesto.
    try:
        if asesoria is None:
            raise ErrorSistema("La asesoría no existe.")

        costo = asesoria.calcular_costo(2, descuento=15, impuesto=19)
        print(f"14. Costo de asesoría: ${costo:,.2f}")
    except ErrorSistema as error:
        registrar_error(str(error))
        print("14. Error:", error)

    # OPERACIÓN 15: Consultar clientes registrados usando try / except / else / finally.
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
        registrar_evento("Finalización de consulta de clientes.")
        print("Proceso de consulta finalizado.")

    # OPERACIÓN 16: Consultar reservas creadas.
    mostrar_titulo("RESERVAS DEL SISTEMA")
    for reserva in reservas:
        print(reserva.mostrar_reserva())
        print("-" * 40)

    # Resumen general en consola y en logs.txt.
    mostrar_titulo("RESUMEN DEL SISTEMA")
    print("Clientes registrados:", len(clientes))
    print("Servicios creados:", len(servicios))
    print("Reservas creadas:", len(reservas))

    registrar_evento("Ejecución del sistema finalizada.")
    print("\nEl sistema Software FJ terminó correctamente.")
    print("Los registros se encuentran en logs.txt")


if __name__ == "__main__":
    try:
        ejecutar_sistema()
    except Exception as error:
        registrar_error(f"Error general del programa: {error}")
        print("Error inesperado:", error)
