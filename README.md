# UNIVERSIDAD ESTATAL AMAZÓNICA

## CARRERA DE TECNOLOGÍAS DE LA INFORMACIÓN

### PROGRAMACIÓN ORIENTADA A OBJETOS

### SEMANA 04

### TEMA: Sistema de Gestión de Restaurante

**Alumno:** Danny Henry Betancourt Luzón
**Año:** 2026

---

# Sistema de Gestión de Restaurante

## Descripción del sistema

El presente proyecto consiste en el desarrollo de un sistema básico de gestión de restaurante utilizando Programación Orientada a Objetos (POO) en Python. El sistema permite administrar productos y clientes registrados, además de realizar pedidos seleccionando clientes y productos existentes mediante un menú interactivo en consola.

La aplicación tiene como finalidad poner en práctica los conceptos fundamentales de la programación orientada a objetos, tales como clases, objetos, atributos, métodos, encapsulación, abstracción y modularización del software.

# Estructura del Proyecto

restaurante_app/
├── modelos/
│   ├── producto.py
│   └── cliente.py
├── servicios/
│   └── restaurante.py
└── main.py


## Explicación de la estructura

### modelos/producto.py

Contiene la clase `Producto`, encargada de representar los productos disponibles en el restaurante, tales como platos principales, bebidas y postres.

### modelos/cliente.py

Contiene la clase `Cliente`, utilizada para almacenar la información de los clientes registrados en el sistema.

### servicios/restaurante.py

Contiene la clase `Restaurante`, responsable de gestionar las operaciones principales del sistema, incluyendo el registro de productos, clientes y la toma de pedidos.

### main.py

Es el punto de entrada de la aplicación. Desde este archivo se crean los objetos, se registran los datos iniciales y se ejecuta el menú principal del sistema.


# Funcionalidades implementadas

* Registro de productos.
* Registro de clientes.
* Visualización de productos disponibles.
* Visualización de clientes registrados.
* Selección de clientes para realizar pedidos.
* Registro de pedidos mediante un ciclo repetitivo.
* Cálculo automático del total de la orden.
* Presentación organizada de la información en consola.
* Uso de constructores `__init__()`.
* Uso del método especial `__str__()`.
* Aplicación de importaciones entre módulos.


# Comentarios relevantes del código

El proyecto incluye comentarios que facilitan la comprensión del funcionamiento de cada componente:

* Definición de clases y atributos.
* Métodos para registrar y mostrar información.
* Gestión de pedidos mediante ciclos repetitivos.
* Importación de módulos y creación de objetos.
* Organización de la lógica principal del programa.

Estos comentarios permiten identificar claramente la responsabilidad de cada sección del código.

# Reflexión

La modularización del software es una práctica fundamental en el desarrollo de aplicaciones porque permite dividir un sistema en componentes independientes y organizados. Esta separación de responsabilidades facilita la comprensión del código, mejora su mantenimiento y favorece la reutilización de funcionalidades en futuros proyectos.

En este sistema de gestión de restaurante, la división en carpetas y módulos permitió mantener una estructura clara, donde cada clase cumple una función específica. Gracias a ello, el programa resulta más ordenado, escalable y fácil de modificar sin afectar el funcionamiento general de la aplicación.

# Repositorio

Para la entrega de esta actividad, el proyecto se almacena en un repositorio público de GitHub que contiene todos los archivos requeridos, respetando la estructura solicitada y permitiendo el acceso para revisión y evaluación.
