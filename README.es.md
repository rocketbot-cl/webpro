



# WEB Pro
  
Modulo con funcionalidades extendidas para el navegador que funciona como complemento a los comandos de la seccion web  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Overview


1. Lista de elementos  
Obtiene una lista de todos los elementos y sus hijos a partir de una clase o nombre para poder iterar sobre ella.

2. Limpia un input y envia el texto  
Borra el contenido de un objeto tipo input y envia el texto

3. Guardar Cookies  
Guarda las cookies de una página para poder ser cargada en otra instancia

4. Cargar Cookies  
Carga un archivo con las cookies

5. Recargar Página  
Recarga una página

6. Volver atrás  
Volver a la página anterior

7. Doble Click  
Hace doble click sobre un objeto seleccionado

8. Scroll  
Hace scroll hasta una posición determinada

9. Contar Elementos  
Entrega el total de elementos

10. Seleccionar Objeto por Index  
Selecciona un objeto pasándole el index

11. Clickear Objeto por Index  
Clickea un objeto pasándole el index

12. Exportar página a PDF  
Exporta la página a un archivo PDF. Si la página contiene elementos fijos, pueden eliminarse con Javascript para obtener una correcta exportación.

13. Abrir Chrome en modo headless  
Abre Chrome en modo Headless

14. Tomar captura por coordenadas  
Toma una captura de pantalla a una sección de la página mediante coordenadas

15. Obtener rectangulo delimitador  
Obtiene coordenadas x e y, y dimensiones de un objeto

16. Obtener coordenadas de un objeto  
Obtiene coordenadas x e y de un objeto

17. Obtener dimensiones de un objeto  
Obtiene dimensiones de un objeto

18. Abrir Chrome modo desarrollador   
Abre Google Chrome en modo seguro o modo debugger

19. Ver Consola  
Obtiene información desde la consola

20. Convertir página a PNG  
Toma multiples capturas de la página web y las concatena en una sola. Si la página contiene elementos fijos, pueden eliminarse con Javascript para obtener una correcta exportación.

21. Mover encima  
Mueve el mouse encima de un elemento

22. Abrir Edge (Chromium)  
Abre el nuevo Edge basado en Chromium

23. Click Pro  
Hace click sobre un objeto seleccionado esperando que se encuentre cliqueable

24. Extraer texto Pro  
Obtiene el texto de un objeto esperando que este se encuentre disponible

25. Seleccionar objeto Pro  
Selecciona un objeto esperando que se encuentre presente

26. Cambiar a iframe Pro  
Cambia a un iframe esperando que se encuentre presente

27. Cambiar a iframes anidados  
Ingresa a multiples iframes esperando que se encuentren presentes

28. Enviar Teclas  
Similar a Enviar texto web, pero a más bajo nivel

29. Imprimir como PDF (Chrome)  
Imprimir la página como PDF en Chrome. El PDF se genera en base al contenido disponible de la página. No representa una copia fiel del sitio.

30. Forzar Descarga  
Forzar una descarga

31. Abrir Nueva Pestaña  
Abre una nueva pestaña indicando la URL

32. Abrir navegador  
Abre el navegador indicando la URL

33. Drag and drop  
Realiza un drag and drop

34. Subir Archivo  
Comando para subir uno o más archivos a un input de tipo file. Solo completar un unico valor según cuántos archivos se deseen subir.

35. Enviar combinacion de teclas  
Comando para enviar combinacion de dos teclas

36. Click Derecho  
Hace click derecho sobre un objeto seleccionado

37. Obtener imagen  
Este comando permite descargar una imagen a partir de una etiqueta <img>

38. Seleccionar múltiples opciones  
Selecciona múltiples opciones de un select

39. Borrar cookies  
Borra las cookies del navegador

40. Obtener Cookies  
Obtiene las cookies actuales del navegador

41. Acceder a Shadow DOM  
Acceder a un elemento dentro de un Shadow DOM. El dato debe pertenecer al elemento padre del shadow-root.

42. Zoom  
Realiza Zoom In o Zoom Out en los navegadores Google Chrome y Firefox.  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**beautifulsoup4**](https://pypi.org/project/beautifulsoup4/)- [**requests**](https://pypi.org/project/requests/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)