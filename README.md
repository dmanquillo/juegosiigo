# Customer Reference AG PAPI API

>La función principal es buscar referencias del cliente en todos los legados de Teco dependiendo del parámetro de búsqueda.

## Funcionamiento:

Vamos a tener 5 parámetros de búsqueda en el API, cada parámetro tiene un respectivo flujo en la lógica para obtener información de referencia para cada legado, los siguientes parámetros de búsqueda son los siguientes:

** 1. Búsqueda DNI: **  

    Si hay información en el queryParam de "document type", "document number" y "gender"; se va a proceder en hacer las búsquedas en los tres sistemas que son FAN, OPEN y TABLÓN; donde vamos a hacer después un mapeo de los datos para tener un response unificado.

2. Búsqueda customerId:

    Si hay información en el queryParam de "customer id" se va a proceder en hacer una búsqueda en FAN para obtener el número y tipo de documento, así como el género para hacer las búsquedas en los tres sistemas que son FAN, OPEN y TABLÓN; donde después se hace un mapeo de los datos para tener un response unificado.

3. Busqueda DUID: 

    Si hay información en el queryParam de "duid" se va a proceder en hacer una búsqueda en FAN para obtener el número y tipo del documento así como el género para hacer las búsquedas en los tres sistemas que son FAN, OPEN y TABLÓN; donde vamos hacer después un mapeo de los datos para tener un response unificado.

4. Búsqueda SuscriberId:

    Si hay información en el queryParam de "subscriber id", entonces se debe proceder en hacer un búsqueda en OPEN para obtener el número y tipo del documento así como el género para hacer las búsquedas en los tres sistemas que son: FAN, OPEN y TABLÓN; donde vamos hacer después un mapeo de los datos para tener un response unificado.

5. Busquedad idCliente:

    Si hay información en el queryParam de "id client" se va a proceder en hacer las búsquedas en los tres sistemas que son: FAN, OPEN y TABLÓN donde vamos hacer después un mapeo de los datos para tener un response unificado.

## Estructuración de proyecto en Mulesoft:

* global.xml:

    Tenemos las configuraciones del api y manejo de errores.

* implementation.xml:

    Tenemos el flujo principal que llama a otros flujos de los archivos de lógica y válida que halla data para mostrar.

* integrations.xml:

    Aquí tenemos las integraciones de Fan, Open, Tablón.

* logic.xml:
   
    Aquí tenemos la lógica de negocio de cada búsqueda que se llegara hacer.

* commons.xml:

    Aquí tenemos la flujos donde estan constantes o enums donde podemos consultarlas

* logicSearchbyDniOtherSystems.xml
   
    Hacemos la lógica de búsqueda de Dni para los legados.

* customer-reference-ag-papi-api.xml

    Aquí tenemos la configuración inicial, adicional tendremos nuestros métodos Api definidos antes por RAML aquí es donde empieza todo.
