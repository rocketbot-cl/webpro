



# WEB Pro
  
Modulo con funcionalidades extendidas para el navegador que funciona como complemento a los comandos de la seccion web  

*Read this in other languages: [English](Manual_webpro.md), [Português](Manual_webpro.pr.md), [Español](Manual_webpro.es.md)*
  
![banner](imgs/Banner_webpro.png)

## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  

## Como usar este modulo
Este modulo se complementa con los modulos y comandos nativos Web que ya vienen por defecto en Rocketbot. Para poder usar el modulo debes tener un navegador ya abierto desde Rocketbot con el comando de "Abrir Navegador". Luego de esto ya podremos utilizar los comandos con normalidad.

### Para poder utilizar Edge en modo Internet Explorer, deben realizarse las siguientes configuraciones:
1. Configurar el navegador en base a la siguiente documentación: https://docs.rocketbot.com/?p=169
2. Descargar el driver de Internet Explorer del siguiente link: https://github.com/SeleniumHQ/selenium/releases/download/selenium-3.13.0/IEDriverServer_Win32_3.13.0.zip y ubicarlo en Rocketbot/drivers/win/ie/x86/
3. Para poder acceder a las herramientas de desarrollador, se debe abrir IEChooser.exe. Para realizarlo presionar la tecla Windows + R y colocar lo siguiente: %systemroot%\system32\f12\IEChooser.exe  luego apretar aceptar. Seleccione la ventana de su navegador, y podrá explorar los elementos de la página

### Consejos para manejar elementos dentro de un shadow root:
1. Manejo de iframes:
Primero localiza todos los shadow-root a los que debes ingresar para llegar al iframe que debes acceder. Por ejemplo si tienes esta estructura:

```html
<div id="div1">
  shadow-root(open)
    <div id="div2">
      <div id="div3">
        shadow-root(open)
          <div id="div4">
            <iframe id="id_iframe">
                <div id="div_shadow">
                  shadow-root(open)
                    <a id="link1">
                    <input id="input1">
                    <p id="parrafo">Texto</p>
```

Debes ingresar al primer shadow-root, y luego al segundo.
Para lograr esto debes utilizar el comando Ejecutar Python. Primero debes importar todo lo necesario para manejar los elementos web, y luego accedes a cada shadow root, para finalizar accediendo al iframe que necesitas:

```python
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

webdriver = GetGlobals("web")
if webdriver.driver_actual_id in webdriver.driver_list:
    driver = webdriver.driver_list[webdriver.driver_actual_id]
    
# Primero seleccionas el padre del primer shadow-root
shadow_host = driver.find_element(By.ID, '#div1') 

# Estas siguientes tres líneas son siempre igual
shadow_root_dict = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
shadow_root_id = shadow_root_dict['shadow-6066-11e4-a52e-4f735466cecf']
shadow_root = WebElement(driver, shadow_root_id, w3c=True)

# Aca seleccionas el elemento dentro del primer shadow-root que sea el padre del segundo shadow-root
shadow_content = shadow_root.find_element(By.ID, '#div3')


shadow_host = shadow_content

# Estas siguientes tres líneas son siempre igual
shadow_root_dict = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
shadow_root_id = shadow_root_dict['shadow-6066-11e4-a52e-4f735466cecf']
shadow_root = WebElement(driver, shadow_root_id, w3c=True)

# Cuando ingresas al ultimo shadow-root, solo debes obtener el elemento que corresponda con el iframe al que debes ingresar
shadow_content = shadow_root.find_element(By.ID, '#id_iframe')

# Y para finalizar, utilizas el comando que cambia al iframe
driver.switch_to_frame(shadow_content)
```

#### Tener en cuenta que si necesitas acceder a mas elementos para llegar al iframe, solo es necesario seguir los mismos pasos las veces que haga falta
Una vez tengas acceso al iframe, podrás interactuar con todos los elementos utilizando javascript, independientemente si tengan shadow-root o no.

2. Manejo de elementos dentro de un shadow-root:
Para realizar un click, copia el js path del elemento. Luego en Rocketbot utiliza el comando Ejecuta JS. En este comando, pega el js_path y al final agrégale .click()
Utilizando el ejemplo del comienzo, para darle click a la etiqueta \<a> dentro del iframe, deberia quedarte similar a esto:

```javascript
document.querySelector("#div_shadow").shadowRoot.querySelector("#link1").click()
```

Si por ejemplo quieres completar un input, puede variar dependiendo el formato del input de la página.
La mayoría de inputs puedes completarlos utilizando Javascript y el comando Ejecuta JS de la siguiente forma:

```javascript
document.querySelector("#div_shadow").shadowRoot.querySelector("#input1").value = "tu_valor"
```

En otros casos, es necesario que el input tenga foco para poder ingresarle un valor. Para esto debes hacer los siguientes pasos:
En un comando de JS coloca lo siguiente:

```javascript
// Con esto le das foco al input
document.querySelector("#div_shadow").shadowRoot.querySelector("#input1").setAttribute('focused', '')
document.querySelector("#div_shadow").shadowRoot.querySelector("#input1").focus()
```

Al tenerlo en foco, puedes utilizar el comando Enviar Teclas del módulo webpro y escribirá lo que necesites.
Para finalizar, puedes obtener el texto de un elemento también con javascript, de la siguiente forma:
Ejecuta un comando JS con lo siguiente:
    
```javascript
return document.querySelector("#div_shadow").shadowRoot.querySelector("#parrafo").innerHTML
```
A esto lo asignas a la variable que quieras, y en la misma tendrás el valor codificado. Para obtenerlo limpio, ejecuta un comando de Asignar variable con lo siguiente: {var}.decode('latin-1')



### Cómo utilizar perfil de usuario existente en el navegador Edge
1. Abra el navegador Edge con el perfil que desea utilizar.
2. En la barra de direcciones, escriba lo siguiente: edge://version
3. En la sección "Ruta de acceso al perfil" se encuentra la carpeta que contiene el perfil que está utilizando. Copie la ruta de la carpeta y péguela en el campo "Ruta del perfil" del comando "Abrir Edge (Chromium)" del módulo webpro.

### Cómo utilizar perfil de usuario en navegador Firefox
Firefox no permite ingresar una carpeta en blanco para crear un perfil como en Chrome, se le debe asignar la ruta a un perfil existente. Puedes ubicar la ruta de un perfil ya existente o crear uno debes ir a Firefox y buscar en el buscador lo siguiente: about:profiles. Debes utilizar la ruta indicada en Directorio Raíz del perfil con el cual quieras abrir el navegador.

### Cómo actualizar Firefox en LINUX
Si presenta errores en cuanto a la versión de Firefox en Linux, por favor siga los siguientes pasos:
1. Descargue el último paquete tar de Firefox: navegue a la página oficial de descarga de Firefox y obtenga la última versión para Linux, o use wget en la terminal:

        wget -O firefox-latest.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US" 

2. Extrae el tarball

        tar xjf firefox-latest.tar.bz2 

3. Mueva los archivos extraídos: mueva los archivos extraídos al directorio /opt, que es un directorio estándar para guardar software opcional en Linux.

        sudo mv firefox /opt/firefox-latest 

4. Cree un enlace simbólico: para asegurarse de que el sistema utilice la última versión, cree un enlace simbólico.

        sudo ln -s /opt/firefox-latest/firefox /usr/bin/firefox 

Link: https://tecadmin.net/how-to-install-firefox-on-ubuntu/  => Metodo 2

## Descripción de los comandos

### Lista de elementos
  
Obtiene una lista de todos los elementos y sus hijos a partir de una clase o nombre para poder iterar sobre ella.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tipo Clases o atributo|En este campo debemos poner el tipo de clase o atributo que usaremos.|name|
|Clases o atributo|En este campo debemos poner el nombre de la clase o atributo que usaremos.|col-md-6|
|Tipo de Elemento/Objeto web|En este campo debemos poner el tipo de elemento que usaremos.|div|
|Variable donde almacenar resultado|En este campo debemos poner el nombre de la variable donde almacenaremos el resultado.|Variable|

### Limpia un input y envia el texto
  
Borra el contenido de un objeto tipo input y envia el texto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Texto a enviar o variable|Colocamos el texto o la variable a enviar.|Texto o Variable|
|Dato a buscar|Colocamos el dato a buscar.|Dato a buscar|
|Tipo de dato|Seleccionamos el tipo de dato a buscar. Ya sea xpath, class, name, tag o id.|Dato a buscar|
|Enviar con teclas|Borra y escribe con teclas directamente.|Texto o Variable|
|Espera de 1 segundo|Asigna una espera de 1 segundo entre el borrar y el enviar elemento|True|

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
|Asignar resultado a variable|Variable donde se almacenará True o False dependiendo si se pudieron cargar las cookies|Variable|

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
|Dato a buscar|Colocamos el selector a buscar|Dato|
|Tipo de dato|Colocamos el tipo de dato a buscar|xpath|

### Scroll
  
Hace scroll hasta una posición determinada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Posición|Elegimos la posición en píxeles|1500|

### Contar Elementos
  
Entrega el total de elementos
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de la clase|Nombre de la clase del elemento|Name class|
|Asignar resultado a variable|Nombre de la variable donde se guardará el resultado|Variable|

### Seleccionar Objeto por Index
  
Selecciona un objeto pasándole el index
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a Buscar|Colocamos el selector a buscar|form-control|
|Index|Colocamos el index a buscar|1|
|Tipo de dato|Seleccionamos el tipo de dato a buscar|name|

### Clickear Objeto por Index
  
Clickea un objeto pasándole el index
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a Buscar|Colocamos el selector del dato a clickear.|form-control|
|Index|Colocamos el index del dato a clickear.|1|
|Tipo de dato|Colocamos el tipo de dato a clickear.|class|

### Exportar página a PDF
  
Exporta la página a un archivo PDF. Si la página contiene elementos fijos, pueden eliminarse con Javascript para obtener una correcta exportación.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta y nombre del Archivo|Seleccionamos la ruta y el nombre del archivo a guardar, sin la extension .pdf|path/to/file.pdf|
|Borrar cabecera fija|Si el sitio web contiene una cabecera fija, marca la casilla para eliminarla y que no se repita en cada captura. El comando busca la etiqueta header, si no la encuentra arrojará un error, en caso de que no funcione hay que desmarcarla.|True|
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
|Dato a buscar|Colocamos el selector del elemento a obtener.|Data|
|Tipo de dato|Seleccionamos el tipo de dato a buscar.|xpath|
|Variable donde almacenar resultado|Nombre de variable sin {}|Variable|

### Obtener coordenadas de un objeto
  
Obtiene coordenadas x e y de un objeto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a seleccionar|Data|
|Tipo de dato|Seleccionamos el tipo de dato a buscar|xpath|
|Variable donde almacenar resultado|Nombre de variable sin {}|Variable|

### Obtener dimensiones de un objeto
  
Obtiene dimensiones de un objeto
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a seleccionar|Data|
|Tipo de dato|Seleccionamos el tipo de dato a buscar|xpath|
|Variable donde almacenar resultado|Nombre de variable sin {}|Variable|

### Abrir Chrome modo desarrollador 
  
Abre Google Chrome en modo seguro o modo debugger
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Url de Servidor|Url de la pagina a abrir|http://www.rocketbot.co|
|Modo|Seleccionamos el modo en que se va abrir el navegador.|Debugger|

### Ver Consola
  
Obtiene información desde la consola
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Variable donde almacenar resultado|Nombre de la variable donde almacenar el resultado|Variable|
|Nivel |Nivel de información a mostrar|Severe|

### Convertir página a PNG
  
Toma multiples capturas de la página web y las concatena en una sola. Si la página contiene elementos fijos, pueden eliminarse con Javascript para obtener una correcta exportación.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre|Nombre de la imagen a guardar|imagenWeb|
|Carpeta de descarga|Ruta donde se descargará la imagen generada|C:/Users/user/Desktop|

### Mover encima
  
Mueve el mouse encima de un elemento
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selecto del elemento al cual le haremos hover.|Data|
|Tipo de dato|Colocamos el tipo de dato que queremos buscar.|xpath|

### Abrir Edge (Chromium)
  
Abre el nuevo Edge basado en Chromium
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Url de Servidor|Url de la pagina a abrir en Edge|http://www.rocketbot.co|
|Ruta del perfil|Carpeta que contiene el perfil a utilizar.|C:/Users/User/AppData/Local/Microsoft/Edge/User Data/Default|
|Iniciar en modo Internet Explorer|Inicia el navegador en modo Internet Explorer|True|
|Seleccionar ejecutable de Edge|Selecciona el ejecutable de Edge para abrir en modo IE|C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe|

### Click Pro
  
Hace click sobre un objeto seleccionado esperando que se encuentre cliqueable
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a hacer click.|Data|
|Tipo de dato|Seleccionamos el tipo de dato a buscar.|xpath|
|Esperar|Colocamos el tiempo en segundos que esperaremos a que el elemento se encuentre clickeable.|5|

### Extraer texto Pro
  
Obtiene el texto de un objeto esperando que este se encuentre disponible
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a extraer text.|Data|
|Tipo de dato|Seleccionamos el tipo de dato a buscar.|xpath|
|Esperar|Colocamos el tiempo en segundos que esperaremos a que el elemento este disponible.|5|
|Variable donde almacenar resultado|Colocamos el nombre de la variable donde almacenaremos el resultado.|Variable|

### Seleccionar objeto Pro
  
Selecciona un objeto esperando que se encuentre presente
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a seleccionar.|Data|
|Tipo de dato|Seleccionamos el tipo de dato a buscar.|xpath|
|Esperar|Colocamos el tiempo en segundos que esperaremos a que el elemento aparezca.|5|

### Cambiar a iframe Pro
  
Cambia a un iframe esperando que se encuentre presente
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del iframe|Data|
|Tipo de dato|Seleccionamos el tipo de dato|xpath|
|Seleccionar por índice|Casilla para elegir iframe por índice|True|
|Índice|Indice del frame dentro del codigo HTML de la pagina web|0|
|Esperar|Colocamos el tiempo de espera|5|

### Cambiar a iframes anidados
  
Ingresa a multiples iframes esperando que se encuentren presentes
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Datos a buscar|Colocar los selectores de cada iframe en formato lista|['Data1', 'Data2']|
|Tipo de dato|Seleccionamos el tipo de dato|xpath|
|Esperar|Colocamos el tiempo de espera|5|
|Asignar resultado a variable|Variable donde se almacenará True o False dependiendo si se pudo ingresar a cada iframe|Variable|

### Enviar Teclas
  
Similar a Enviar texto web, pero a más bajo nivel
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Texto|Texto a enviar|Texto|
|Tecla especial|Tecla especial a enviar|SPACE|

### Imprimir como PDF (Chrome)
  
Imprimir la página como PDF en Chrome. El PDF se genera en base al contenido disponible de la página. No representa una copia fiel del sitio.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|El pdf se descargará en la carpeta de descargas por defecto del navegador.|||
|Imprimir con diseño horizontal|Si se marca, el pdf se imprimirá en formato horizontal.|True|

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
|Navegador |Navegador a abrir|Google Chrome|
|URL|URL a abrir|http://www.google.com|
|Tiempo de espera|Tiempo de espera en segundos|5|
|Id|Id del navegador|4|
|Carpeta de perfil|Ruta de la carpeta de perfil de usuario para abrir el navegador|C:/folder|
|Carpeta de descargas|Ruta de la carpeta de descargas para el navegador abierto|C:/folder|
|Forzar descargas|Fuerza las descargas para hacerlas automaticas|True|
|Opciones personalizadas para el navegador|Opciones personalizadas en formato dict|{'download.default_directory': download_path}|
|Argumentos para abrir el navegador|Argumentos en formato lista|['--incognito','--kiosk-printing','--new-window']|

### Drag and drop
  
Realiza un drag and drop
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Origen|Origen del elemento|source|
|Destino|Destino del elemento|target|
|Tipo de dato|Tipo de dato a buscar|Dato a buscar|

### Subir Archivo
  
Comando para subir uno o más archivos a un input de tipo file. Solo completar un unico valor según cuántos archivos se deseen subir.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento donde se subira el archivo|Data|
|Tipo de dato|Tipo de dato a buscar|xpath|
|Cargar solo un único campo de los siguientes. Si se desea subir un solo archivo, utilizar el primer selector, si se desean cargar más de uno, cargar el segundo selector con el formato indicado.|||
|Cargar un solo archivo|Seleccionamos los archivos a subir|C:/Users/user/file1.pdf|
|Cargar múltiples archivos|Seleccionamos los archivos a subir|['C:/Users/user/file1.pdf', 'C:/Users/user/file2.pdf']|

### Enviar combinacion de teclas
  
Comando para enviar combinacion de dos teclas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Primera tecla especial|Primer tecla especial a combinar con una letra/numero o con una segunda tecla especial|SPACE|
|Letra o numero|Letra o numero a combinar con la primera tecla de ser necesario.|A|
|Segunda tecla especial|Segunda tecla especial a combinar con la primera tecla de ser necesario.|SPACE|

### Click Derecho
  
Hace click derecho sobre un objeto seleccionado
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector a buscar|Dato|
|Tipo de dato|Colocamos el tipo de dato a buscar|xpath|

### Obtener imagen
  
Este comando permite descargar una imagen a partir de una etiqueta <img>
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector del elemento a descargar|Data|
|Tipo de dato|Seleccionamos el tipo de dato a buscar|xpath|
|Carpeta donde guardar la imagen|Colocamos la carpeta donde se guardará la imagen|C:/Users/Usuario/Desktop|
|Nombre y extensión de la imagen a guardar|Colocamos el nombre de la imagen a guardar. Si no se coloca el nombre de la imagen o la extensión, se guardará con el nombre o extensión por defecto.|imagen.png|

### Seleccionar múltiples opciones
  
Selecciona múltiples opciones de un select
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tipo de dato|Seleccionamos el tipo de dato a buscar.|xpath|
|Dato a buscar|Colocamos el selector del elemento a seleccionar.|Data|
|Tipo de selección|Seleccionamos el tipo de selección a realizar.|value|
|Opciones a seleccionar|Colocamos las opciones a seleccionar. Si seleccionamos el tipo de selección 'select all' o 'deselect all', no es necesario colocar las opciones.|0,1,2,3|

### Borrar cookies
  
Borra las cookies del navegador
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |

### Obtener Cookies
  
Obtiene las cookies actuales del navegador
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Variable donde se almacenará el resultado|Nombre de la variable donde se almacenarán las cookies|Variable|

### Acceder a Shadow DOM
  
Acceder a un elemento dentro de un Shadow DOM. El dato debe pertenecer al elemento padre del shadow-root.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato a buscar|Colocamos el selector a buscar|Dato|

### Zoom
  
Realiza Zoom In o Zoom Out en los navegadores Google Chrome y Firefox.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tipo de Zoom|Seleccionamos el tipo de zoom a realizar.|Zoom In|
