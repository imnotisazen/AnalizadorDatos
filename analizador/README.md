# Analizador de Representación de Datos

## Descripción del proyecto

Esta aplicación web fue desarrollada utilizando Python 3.12 y Django. Su propósito es facilitar la conversión de números entre diferentes sistemas numéricos y analizar cómo se representan los caracteres mediante Unicode y UTF-8.

## Funcionalidades principales

- Conversión de números entre binario, octal, decimal y hexadecimal.
- Validación de números dentro del rango de 0 a 65535.
- Identificación de dígitos inválidos y números negativos.
- Cálculo de bits significativos y bytes necesarios.
- Representación binaria ajustada a bytes completos.
- Análisis de textos de hasta 20 caracteres.
- Visualización de códigos decimales, Unicode, hexadecimales y bytes UTF-8.
- Mensajes de error para entradas incorrectas.

## Tecnologías utilizadas

- Python 3.12
- Django 5.2
- HTML5
- CSS3
- SQLite, como base de datos predeterminada de Django.

## Instalación y ejecución

1. Descargar el proyecto desde GitHub.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Crear un entorno virtual:

   `py -3.12 -m venv venv`

4. Activar el entorno virtual en PowerShell:

   `.\venv\Scripts\Activate.ps1`

5. Instalar Django:

   `pip install "Django>=5.2,<6"`

6. Aplicar las migraciones:

   `python manage.py migrate`

7. Iniciar el servidor:

   `python manage.py runserver`

8. Abrir en el navegador:

   `http://127.0.0.1:8000/`

## Pruebas automatizadas

Se desarrollaron 14 pruebas automatizadas utilizando el sistema de pruebas de Django.

Las pruebas verifican las conversiones entre bases, la validación de entradas, el cálculo de bits y bytes y el análisis UTF-8 de caracteres especiales, como la letra ñ.

Para ejecutar las pruebas:

`python manage.py test`

**Resultado obtenido:** 14 pruebas ejecutadas correctamente, sin errores.

## Relación con la arquitectura de Von Neumann

La aplicación utiliza diferentes recursos relacionados con la arquitectura de Von Neumann.

**Unidad Central de Procesamiento (CPU):** ejecuta las instrucciones de Python y realiza las operaciones necesarias para convertir los números y analizar los caracteres.

**Memoria RAM:** almacena temporalmente los datos ingresados por el usuario, las variables y los resultados de las operaciones mientras se ejecuta la aplicación.

**Dispositivos de entrada y salida:** el teclado permite ingresar números y textos, mientras que la pantalla muestra los formularios y resultados.

**Almacenamiento:** guarda los archivos del proyecto, incluyendo el código Python, las plantillas HTML y la configuración de Django.

La arquitectura de Von Neumann se caracteriza por almacenar instrucciones y datos en memoria, permitiendo que el procesador los utilice durante la ejecución de los programas.

## Docker y contenedores

El proyecto puede prepararse para ejecutarse mediante Docker utilizando una imagen basada en Python 3.12.

Los contenedores comparten el kernel del sistema operativo anfitrión porque Docker utiliza mecanismos de aislamiento del sistema operativo, como namespaces y cgroups, en lugar de ejecutar un sistema operativo completo dentro de cada contenedor.

En Windows, Docker Desktop normalmente utiliza un entorno Linux mediante WSL 2 para ejecutar contenedores Linux.

La ejecución del contenedor y la evidencia de consumo de recursos quedan pendientes de verificación.

## Conclusión

Este proyecto permitió aplicar conocimientos sobre sistemas numéricos, representación binaria, codificación de caracteres y desarrollo web con Django.

También permitió comprender cómo se utilizan los recursos de una computadora durante la ejecución de una aplicación y la importancia de realizar pruebas para comprobar su funcionamiento.