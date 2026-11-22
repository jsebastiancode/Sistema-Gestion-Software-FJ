# Sistema Integral de Gestión - Software FJ

## Descripción
Aplicación desarrollada en Python bajo el paradigma orientado a objetos para gestionar clientes, servicios (salas, equipos y asesorías especializadas) y reservas de la empresa **Software FJ**, sin utilizar bases de datos.

## Estructura del proyecto
- `main.py`: ejecución principal y simulación de operaciones válidas e inválidas.
- `entidades.py`: clase abstracta `Entidad` y clase `Cliente` con encapsulación y validaciones.
- `servicios.py`: clase abstracta `Servicio` y clases derivadas `ServicioSala`, `ServicioEquipo` y `ServicioAsesoria`.
- `reservas.py`: clase `Reserva` con confirmación, cancelación, procesamiento y encadenamiento de excepciones.
- `excepciones.py`: excepciones personalizadas y registro de eventos/errores en `logs.txt`.
- `logs.txt`: archivo generado automáticamente con eventos y errores.

## Ejecución
1. Contar con Python 3 instalado.
2. Abrir la carpeta del proyecto en Visual Studio Code o terminal.
3. Ejecutar `python main.py`.