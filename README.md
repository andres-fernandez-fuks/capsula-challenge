# capsula-challenge
 
Ejercicio para la empresa Corporación Cápsula.

## Enunciado

Este desafío consta en desarrollar un software emulando ser una cuenta corriente de saldos.

Debe desarrollar un servidor HTTP con dos endpoints: Uno para insertar una nueva transacción monetaria, entrada o salida de dinero, para un usuario determinado; Uno para devolver el saldo actual de un usuario. Puede usar el lenguaje y la plataforma con los que se sienta más cómodo.

Requisitos:

No debe ser posible retirar dinero para un usuario dado cuando no tiene suficiente saldo;
Debe tener en cuenta los problemas de simultaneidad;
Debe ser ejecutable en máquinas Linux y MacOS;
No tiene que preocuparse por las bases de datos; está bien usar almacenamiento en memoria en proceso;
Utilizar buenas prácticas según su comprensión de estas: Tests, REAME, etc.
Notas generales: Usted y un ingeniero de Corporación Capsula extenderán este desafío en un paso diferente del proceso.

Asegúrese de anonimizar su envío eliminando su nombre de los encabezados de los archivos y demás; Siéntase libre de expandir su diseño por escrito; Nos enviará el código fuente de su solución como un archivo comprimido que contiene todo el código y la posible documentación.

Asegúrese de no incluir archivos innecesarios como el repositorio de Git, binarios compilados, etc.;

No cargue su solución en repositorios públicos en GitHub, BitBucket, etc.

Cosas que estamos buscando:

Inmutabilidad;
Separación de intereses;
Pruebas unitarias y de integración;
diseño de API;
Manejo correcto de valores decimales;
Manejo de errores.

## Corrida del programa y pruebas:

## Prerequisitos:
    - [Python 3.6](https://www.python.org/downloads/)
    - [Pip](https://pip.pypa.io/en/stable/installing/)

## Setup:
    - Clonar el repositorio
    - (Opcional) Levantar un entorno virtual 
    - Instalar los requisitos: pip install -r requirements.txt

## Ejecución:
    - Exportar las variables de entorno: export $(cat .env | xargs)
    - Ejecutar el programa: python3 app.py
    - Para correr pruebas unitarias:
        $ python3 -m pytest
    - Para correr pruebas de integración:
        $ behave

