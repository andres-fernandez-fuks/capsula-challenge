## Algunos comentarios de la realización del ejercicio:

### Decisiones tomadas:
    - Creé las clases Account y Transaction. Account modelaría lo que el enunciado describe como "usuario", pero Account (Cuenta) me pareció un término más acertado para su funcionamiento en el modelo.
    - Decidí utilizar Behave (Gherkin) para realizar las pruebas de integración.
    - Mockeé una "base de datos" en memoria, y un repositorio que interactúa con ella, para no alejarme demasiado del flujo de un procedimiento que sí utilizara una.

### Concurrencia:
    - Agregué locks directamente en la clase Accoun tanto a la hora de manejar una transacción (operación de escritura) como a la hora de solicitar el balance de una cuenta (operación de lectura). La idea es asegurar la atomicidad de las operaciones realizada en esos dos procesos.
    - Al estar la base de datos en memoria, esto tiene sentido, ya que una misma instancia de Account puede ser accedida desde varias requests concurrentes, lo cual podría ser un problema de no utilizar locks en operaciones no atómicas.
    - Sin embargo, si se utilizara una base de datos real, los posibles problemas de concurrencia surgirían dentro de la misma base de datos a la hora de escribir/leer un recurso, por lo que debería ser la misma base de datos quien los maneje, y los locks implementados en la clase Account no tendrían sentido.
    - Una de las pruebas de integración busca comprobar que no haya problemas de concurrencia en operaciones de modificación y obtención del saldo de una cuenta. La idea fue utilizar un thread para ir modificando el saldo mientras otro lo iba obteniendo. Lo que busco es intentar asegurarme (sabiendo que los errores de concurrencia no aparecen de forma determinística) de que en ningún momento se obtenga un saldo inconsistente con respecto a los posibles saldos válidos.

