



# WEB Pro
  
Módulos para manejo extendido de navegador  
  
![banner](imgs/Banner_webpro.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.  



## Descripción de los comandos

### Lista de elementos
  
Obtiene una lista de todos los elementos y sus hijos a partir de una clase o nombre para poder iterar sobre ella.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tipo Clases o atributo|En este campo debemos poner el tipo de clase o atributo que usaremos.|Tipo de clase o atributo|
|Clases o atributo|En este campo debemos poner el nombre de la clase o atributo que usaremos.|Clases o atributo|
|Tipo de Elemento/Objeto web|En este campo debemos poner el tipo de elemento que usaremos.||
|Variable donde almacenar resultado|En este campo debemos poner el nombre de la variable donde almacenaremos el resultado.||

### Limpia un input y envia el texto
  
Borra el contenido de un objeto tipo input y envia el texto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Texto a enviar o variable|Colocamos el texto o la variable a enviar.|Texto o Variable|
|Dato a buscar|Colocamos el dato a buscar.|Dato a buscar|
|Tipo de dato|Seleccionamos el tipo de dato a buscar. Ya sea xpath, class, name, tag o id.|Dato a buscar|
|Enviar con teclas|Borra y escribe con teclas directamente.|Texto o Variable|

### Guardar Cookies
  
Guarda las cookies de una página para poder ser cargada en otra instancia
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta al archivo donde se guardarán las cookies|En este campo indicamos la ruta al archivo donde se guardarán las cookies|C:/tmp/etc|
|Variable donde se guardará las cookies|En este campo indicamos el nombre de la variable donde se guardarán las cookies|cookies|

### Cargar Cookies
  
Carga un archivo con las cookies
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta al archivo donde están guardadas las cookies|Seleccionamos la ruta del archivo donde están guardadas las cookies|C:/tmp/etc|

### Recargar Página
  
Recarga una página
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |

### Volver atrás
  
Volver a la página anterior
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |

### Doble Click
  
Hace doble click sobre un objeto seleccionado
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector a buscar||
|Tipo de dato|Colocamos el tipo de dato a buscar||

### Scroll
  
Hace scroll hasta una posición determinada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Posición|Elegimos la posición en píxeles||

### Contar Eelementos
  
Entrega el total de elementos
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la clase|Nombre de la clase del elemento||
|Asignar resultado a variable|Nombre de la variable donde se guardará el resultado|Variable|

### Seleccionar Objeto por Index
  
Selecciona un objeto pasándole el index
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a Buscar|Colocamos el selector a buscar|form-control|
|Index|Colocamos el index a buscar|1|
|Tipo de dato|Seleccionamos el tipo de dato a buscar||

### Clickear Objeto por Index
  
Clickea un objeto pasándole el index
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a Buscar|Colocamos el selector del dato a clickear.|form-control|
|Index|Colocamos el index del dato a clickear.|1|
|Tipo de dato|Colocamos el tipo de dato a clickear.||

### Exportar página a PDF
  
Exporta la página a un archivo PDF
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de Archivo|Seleccionamos el nombre del archivo a guardar, sin la extension .pdf||
|Asignar resultado a variable|Seleccionamos el nombre de la variable a la que queremos asignar el resultado|Variable|

### Abrir Chrome en modo headless
  
Abre Chrome en modo Headless
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Url de Servidor|Escribimos la URL de la pagina a abrir.|http://www.rocketbot.co|

### Tomar captura por coordenadas
  
Toma una captura de pantalla a una sección de la página mediante coordenadas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Posición|Coordenadas de la sección de la página|x,y|
|Dimensiones|Dimensiones de la sección de la página|ancho, alto|
|Ruta y nombre donde se guardará la imagen|Ruta y nombre donde se guardará la imagen|/Users/User/folder/image.jpg|

### Obtener rectangulo delimitador
  
Obtiene coordenadas x e y, y dimensiones de un objeto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a obtener.||
|Tipo de dato|Seleccionamos el tipo de dato a buscar.||
|Variable donde almacenar resultado|Nombre de variable sin {}||

### Obtener coordenadas de un objeto
  
Obtiene coordenadas x e y de un objeto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a seleccionar||
|Tipo de dato|Seleccionamos el tipo de dato a buscar||
|Variable donde almacenar resultado|Nombre de variable sin {}||

### Obtener dimensiones de un objeto
  
Obtiene dimensiones de un objeto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a seleccionar||
|Tipo de dato|Seleccionamos el tipo de dato a buscar||
|Variable donde almacenar resultado|Nombre de variable sin {}||

### Abrir Chrome modo desarrollador 
  
Abre Google Chrome en modo seguro o modo debugger
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Url de Servidor|Url de la pagina a abrir|http://www.rocketbot.co|
|Modo|Seleccionamos el modo en que se va abrir el navegador.||

### Ver Consola
  
Obtiene información desde la consola
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Variable donde almacenar resultado|Nombre de la variable donde almacenar el resultado||
|Nivel |Nivel de información a mostrar||

### Convertir página a PNG
  
Toma una captura a la página web completa
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre|Nombre de la imagen a guardar|web|

### Mover encima
  
Mueve el mouse encima de un elemento
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selecto del elemento al cual le haremos hover.||
|Tipo de dato|Colocamos el tipo de dato que queremos buscar.||

### Abrir Edge (Chromium)
  
Abre el nuevo Edge basado en Chromium
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Url de Servidor|Url de la pagina a abrir en Edge|http://www.rocketbot.co|

### Click Pro
  
Hace click sobre un objeto seleccionado esperando que se encuentre cliqueable
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a hacer click.||
|Tipo de dato|Seleccionamos el tipo de dato a buscar.||
|Esperar|Colocamos el tiempo en segundos que esperaremos a que el elemento se encuentre clickeable.|5|

### Extraer texto Pro
  
Obtiene el texto de un objeto esperando que este se encuentre disponible
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a extraer text.||
|Tipo de dato|Seleccionamos el tipo de dato a buscar.||
|Esperar|Colocamos el tiempo en segundos que esperaremos a que el elemento este disponible.|5|
|Variable donde almacenar resultado|Colocamos el nombre de la variable donde almacenaremos el resultado.||

### Seleccionar objeto Pro
  
Selecciona un objeto esperando que se encuentre presente
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a seleccionar.||
|Tipo de dato|Seleccionamos el tipo de dato a buscar.||
|Esperar|Colocamos el tiempo en segundos que esperaremos a que el elemento aparezca.|5|

### Cambiar a iframe Pro
  
Cambia a un iframe esperando que se encuentre presente
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del iframe||
|Tipo de dato|Seleccionamos el tipo de dato||
|Esperar|Colocamos el tiempo de espera|5|

### Enviar Teclas
  
Similar a Enviar texto web, pero a más bajo nivel
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Texto|Texto a enviar||
|Tecla especial|Tecla especial a enviar||

### Imprimir como PDF (Chrome)
  
Imprimir la página como PDF en Chrome
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |

### Forzar Descarga
  
Forzar una descarga
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL Descarga|Colocamos la URL de descarga a forzar|http://www.web.test/file.csv|
|Nombre de archivo|Colocamos el nombre del archivo a forzar|file.csv|

### Abrir Nueva Pestaña
  
Abre una nueva pestaña indicando la URL
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL|URL a abrir en una nueva pestaña|http://www.google.com|

### Abrir navegador
  
Abre el navegador indicando la URL
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|URL|URL a abrir|http://www.google.com|
|Tiempo de espera|Tiempo de espera en segundos|5|
|Id|Id del navegador|4|

### Drag and drop
  
Realiza un drag and drop
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Origen|Origen del elemento|source|
|Destino|Destino del elemento|target|
|Tipo de dato|Tipo de dato a buscar|Dato a buscar|

### Subir Archivo
  
Comando para subir uno o más archivos a un input de tipo file
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento donde se subira el archivo||
|Tipo de dato|Tipo de dato a buscar||
|Archivo(s)|Seleccionamos el archivo a subir|['C:/Users/user/file.pdf']|

### Enviar combinacion de teclas
  
Comando para enviar combinacion de dos teclas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Primera tecla especial|Primer tecla especial a combinar con una letra/numero o con una segunda tecla especial||
|Letra o numero|Letra o numero a combinar con la primera tecla de ser necesario.||
|Segunda tecla especial|Segunda tecla especial a combinar con la primera tecla de ser necesario.||
