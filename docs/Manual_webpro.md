



# WEB Pro
  
Module with extended functionalities for the browser that works as a complement to the commands of the web section  

*Read this in other languages: [English](Manual_webpro.md), [Português](Manual_webpro.pr.md), [Español](Manual_webpro.es.md)*
  
![banner](imgs/Banner_webpro.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module
This module complements the native Web modules and commands that come by default in Rocketbot. In order to use the module you must have a browser opened from Rocketbot with the "Open Browser" command. After that, you will be able to use the commands.

### In order to use Edge in Internet Explorer mode, the following settings must be made:
1. Configure the browser based on the following documentation: https://docs.rocketbot.com/?p=169
2. Download the Internet Explorer driver from the link below: https://github.com/SeleniumHQ/selenium/releases/download/selenium-3.13.0/IEDriverServer_Win32_3.13.0.zip and place it in Rocketbot/drivers/win/ie/x86/
3. To be able to access the developer tools, IEChooser.exe must be opened. To do so, press the Windows key + R and type the following: %systemroot%\system32\f12\IEChooser.exe and then press accept. Select the window of your browser, and you will be able to explore the elements of the page.

### Tips for handling elements within a shadow root:
1. Handling iframes:
First locate all the shadow-root you need to enter to get to the iframe you need to access. For example if you have this structure:

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
                    <p id="paragraph">Text</p>.
```

You must enter the first shadow-root, and then the second.
To accomplish this you must use the Run Python command. First you must import everything you need to handle the web elements, and then access each shadow root, and finish by accessing the iframe you need:

```python
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

webdriver = GetGlobals("web")
if webdriver.driver_actual_id in webdriver.driver_list:
    driver = webdriver.driver_list[webdriver.driver_actual_id].
    
# First you select the parent of the first shadow-root
shadow_host = driver.find_element(By.ID, '#div1') 

# These next three lines are always the same
shadow_root_dict = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
shadow_root_id = shadow_root_dict['shadow-6066-11e4-a52e-4f735466cecf']
shadow_root = WebElement(driver, shadow_root_id, w3c=True)

# Here you select the element inside the first shadow-root that is the parent of the second shadow-root.
shadow_content = shadow_root.find_element(By.ID, '#div3')


shadow_host = shadow_content

# These next three lines are always the same
shadow_root_dict = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
shadow_root_id = shadow_root_dict['shadow-6066-11e4-a52e-4f735466cecf']
shadow_root = WebElement(driver, shadow_root_id, w3c=True)

# When you enter the last shadow-root, you should only get the element that corresponds to the iframe that you should enter
shadow_content = shadow_root.find_element(By.ID, '#id_iframe')

# Y para finalizar, utilizas el comando que cambia al iframe
driver.switch_to_frame(shadow_content)
```

#### Keep in mind that if you need to access more elements to get to the iframe, you only need to follow the same steps as many times as necessary.
Once you have access to the iframe, you will be able to interact with all elements using javascript, regardless of whether they have shadow-root or not.

2. Handling of elements within a shadow-root:
To perform a click, copy the js path of the element. Then in Rocketbot use the Run JS command. In this command, paste the js_path and at the end add .click()
Using the example at the beginning, to click on the \<a> tag inside the iframe, it should look something like this:

```javascript
document.querySelector("#div_shadow").shadowRoot.querySelector("#link1").click()
```

If for example you want to complete an input, it may vary depending on the input format of the page.
Most inputs can be completed using Javascript and the Execute JS command as follows:

```javascript
document.querySelector("#div_shadow").shadowRoot.querySelector("#input1").value = "your_value"
```

In other cases, it is necessary that the input has focus to be able to enter a value. For this you must do the following steps:
In a JS command place the following:

```javascript
// With this you give focus to the input
document.querySelector("#div_shadow").shadowRoot.querySelector("#input1").setAttribute('focused', '')
document.querySelector("#div_shadow").shadowRoot.querySelector("#input1").focus()
```

When you have it in focus, you can use the Send Keys command of the webpro module and it will write what you need.
Finally, you can get the text of an element also with javascript, in the following way:
Run a JS command with the following:
    
```javascript
return document.querySelector("#div_shadow").shadowRoot.querySelector("#paragraph").innerHTML
```
To this you assign it to the variable that you want, and in the same one you will have the coded value. To get it clean, run an Assign Variable command with the following: {var}.decode('utf-8')


### How to use existing user profile in Edge browser
1. Open the Edge browser with the profile you want to use.
2. In the address bar, type the following: edge://version
3. In the "Profile Path" section you will find the folder containing the profile you are using. Copy the path of the folder and paste it in the "Profile Path" field of the "Open Edge (Chromium)" command of the webpro module.

### How to use user profile in Firefox browser
Firefox does not allow you to enter a blank folder to create a profile like in Chrome, you must assign the path to an existing profile. You can locate the path of an existing profile or create one by going to Firefox and searching in the search engine for the following: about:profiles. You must use the path indicated in the Root Directory of the profile with which you want to open the browser.

### How to update Firefox on LINUX
If you have errors regarding the version of Firefox on Linux, please follow the following steps:
1. Download the latest Firefox tar package: Navigate to the official Firefox download page and get the latest version for Linux, or use wget in the terminal:

        wget -O firefox-latest.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US"

2. Extract the tarball

        tar xjf firefox-latest.tar.bz2

3. Move the extracted files: Move the extracted files to the /opt directory, which is a standard directory for saving optional software in Linux.

       sudo mv firefox /opt/firefox-latest

4. Create a symbolic link: To ensure that the system uses the latest version, create a symbolic link.

        sudo ln -s /opt/firefox-latest/firefox /usr/bin/firefox

Link: https://tecadmin.net/how-to-install-firefox-on-ubuntu/ => Method 2

## Como usar este modulo
Este modulo se complementa con los modulos y comandos nativos Web que ya vienen por defecto en Rocketbot. Para poder usar el modulo debes tener un navegador ya abierto desde Rocketbot con el comando de "Abrir Navegador". Luego de esto ya podremos utilizar los comandos con normalidad.

### Para poder utilizar Edge en modo Internet Explorer, deben realizarse las siguientes configuraciones:
1. Configurar el navegador en base a la siguiente documentación: https://docs.rocketbot.com/?p=169
2. Descargar el driver de Internet Explorer del siguiente link: https://github.com/SeleniumHQ/selenium/releases/download/selenium-3.13.0/IEDriverServer_Win32_3.13.0.zip y ubicarlo en Rocketbot/drivers/win/ie/x86/
3. Para poder acceder a las herramientas de desarrollador, se debe abrir IEChooser.exe. Para realizarlo presionar la tecla Windows + R y colocar lo siguiente: %systemroot%\system32\f12\IEChooser.exe  luego apretar aceptar. Seleccione la ventana de su navegador, y podrá 
explorar los elementos de la página

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
from 
selenium.webdriver.support.ui import WebDriverWait
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
shadow_root_id = 
shadow_root_dict['shadow-6066-11e4-a52e-4f735466cecf']
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
Utilizando el ejemplo del comienzo, para darle click a la etiqueta \<a> 
dentro del iframe, deberia quedarte similar a esto:

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
Para 
finalizar, puedes obtener el texto de un elemento también con javascript, de la siguiente forma:
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
Firefox no permite ingresar una carpeta en blanco para crear un 
perfil como en Chrome, se le debe asignar la ruta a un perfil existente. Puedes ubicar la ruta de un perfil ya existente o crear uno debes ir a Firefox y buscar en el buscador lo siguiente: about:profiles. Debes utilizar la ruta indicada en Directorio Raíz del perfil con el cual quieras abrir el navegador.

### Cómo actualizar Firefox en LINUX
Si presenta errores en cuanto a la versión de Firefox en Linux, por favor siga los siguientes pasos:
1. Descargue el último paquete tar de Firefox: navegue a la página oficial de descarga de Firefox y obtenga la última versión para Linux, o use wget en la terminal:

        wget -O firefox-latest.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US" 

2. Extrae el tarball

        tar xjf firefox-latest.tar.bz2 

3. Mueva los archivos extraídos: mueva los archivos extraídos al directorio /opt, que es un directorio estándar para guardar software opcional en Linux.

        sudo mv firefox /opt/firefox-latest 

4. 
Cree un enlace simbólico: para asegurarse de que el sistema utilice la última versión, cree un enlace simbólico.

        sudo ln -s /opt/firefox-latest/firefox /usr/bin/firefox 

Link: https://tecadmin.net/how-to-install-firefox-on-ubuntu/  => Metodo 2


## Description of the commands

### List of items
  
Gets a list of all elements and their children from a class or name in order to iterate over it.
|Parameters|Description|example|
| --- | --- | --- |
|Type Classes or attribute|In this field we should put the type of class or attribute we will use.|name|
|Classes or attribute|In this field we should put the name of the class or attribute we will use.|col-md-6|
|Element Type|In this field we should put the type of element we will use.|div|
|Variable where to store the result|In this field we should put the name of the variable where we will store the result.|Variable|

### Clean input and send text
  
Deletes the contents of an input object and sends the text
|Parameters|Description|example|
| --- | --- | --- |
|Text to send or variable|We put the text or the variable to send.|Text or Variable|
|Data to search|We put the data to search.|Data to search|
|Data type|We select the type of data to search. Either xpath, class, name, tag or id.|Data to search|
|Send with keys|Erase and write with keys.|Text or Variable|
|Wait 1 second|Assigns a 1 second wait between the erase and the send element|True|

### Save Cookies
  
Saves the cookies of a page so that it can be loaded in another instance
|Parameters|Description|example|
| --- | --- | --- |
|Path to file where cookies will be saved|In this field we indicate the path to the file where the cookies will be saved|C:/tmp/etc|
|Variable where cookies will be stored|In this field we indicate the name of the variable where the cookies will be stored|cookies|

### Load Cookies
  
Loads a file with cookies
|Parameters|Description|example|
| --- | --- | --- |
|Path to the file where cookies are stored|Select the path to the file where cookies are stored|C:/tmp/etc|
|Assign result to variable|Variable where True or False will be stored depending on whether the cookies could be loaded|Variable|

### Reload Page
  
Reload Page
|Parameters|Description|example|
| --- | --- | --- |

### Back
  
Back to previous page
|Parameters|Description|example|
| --- | --- | --- |

### Double Click
  
Double click on a selected object
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|We put the selector to search|Data|
|Data type|We put the type of data to search|xpath|

### Scroll
  
Scroll to a specific position
|Parameters|Description|example|
| --- | --- | --- |
|Position|Choose the position in pixels|1500|

### Count Elements
  
Delivers the total number of elements
|Parameters|Description|example|
| --- | --- | --- |
|Class Name|Class name of element|Name class|
|Assign result to variable|Name of the variable where the result will be stored|Variable|

### Select Object by Index
  
Select an object by passing it the index
|Parameters|Description|example|
| --- | --- | --- |
|Data to Search|We put the selector to search|form-control|
|Index|We put the index to search|1|
|Data type|We select the type of data to search|name|

### Click Object by Index
  
Click an object by passing it the index
|Parameters|Description|example|
| --- | --- | --- |
|Data to Search|We put the selector of the data to click.|form-control|
|Index|We put the index of the data to click.|1|
|Data type|We put the type of the data to click.|class|

### Export page to PDF
  
Export the page to a PDF file. If the page contains sticky elements, they can be removed with Javascript to get a proper export.
|Parameters|Description|example|
| --- | --- | --- |
|File path and name|Select the path and name of the file to save, without the extension .pdf|path/to/file.pdf|
|Delete sticky header|If the website contains a fixed header, check the box to remove it so it doesn't repeat itself on each capture. The command looks for the header tag, if it doesn't find it it will throw an error, if this doesn't work you have to uncheck it.|True|
|Assign result to variable|Select the name of the variable to which we want to assign the result|Variable|

### Open Chrome headless
  
Open Chrome in headless mode
|Parameters|Description|example|
| --- | --- | --- |
|Server URL|Write the URL of the page to open.|http://www.rocketbot.co|

### Take screenshot from coordinates
  
Take a screenshot to a section of the page by coordinates
|Parameters|Description|example|
| --- | --- | --- |
|Position|Page section coordinates|x,y|
|size|Page section dimensions|width, height|
|Path and name where the image will be saved|Path and name where the image will be saved|/Users/User/folder/image.jpg|

### Get bounding rectangle
  
Obtains x and y coordinates and dimensions of an object
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|We put the selector of the element to get.|Data|
|Data type|We select the type of data to search.|xpath|
|Variable where to store result|Variable name without {}|Variable|

### Get location of an object
  
Get x and y coordinates of an object
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the element to select|Data|
|Data type|Select the type of data to search|xpath|
|Variable where to store result|Variable name without {}|Variable|

### Get size of an object
  
Get size of an object
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the element to select|Data|
|Data type|Select the type of data to search|xpath|
|Variable where to store result|Variable name without {}|Variable|

### Open Chrome developer mode
  
Open Google Chrome with unsafe mode or debugger mode
|Parameters|Description|example|
| --- | --- | --- |
|Server URL|Server URL to open|http://www.rocketbot.co|
|Mode|Select the mode in which the browser will be opened.|Debugger|

### See Console
  
Get info from console
|Parameters|Description|example|
| --- | --- | --- |
|Variable where to store result|Variable name where to store the result|Variable|
|Level |Level of information to show|Severe|

### WebPage to PNG
  
It takes multiple snapshots of the web page and concatenates them into one. If the page contains fixed elements, they can be removed with Javascript to obtain a correct export.
|Parameters|Description|example|
| --- | --- | --- |
|Name|Name of the image to save|WebImage|
|Download folder|Path where the generated image will be downloaded|C:/Users/user/Desktop|

### Hover Element
  
Move mouse over the element
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|We put the selector of the element to which we will make hover.|Data|
|Data type|We put the type of data we want to search.|xpath|

### Open Edge (Chromium)
  
Open the new Edge based on Chromium
|Parameters|Description|example|
| --- | --- | --- |
|Server URL|Url of the page to open in Edge|http://www.rocketbot.co|
|Profile path|Folder containing the profile to use.|C:/Users/User/AppData/Local/Microsoft/Edge/User Data/Default|
|Start in Internet Explorer mode|Starts the browser in Internet Explorer mode|True|
|Select Edge executable|Select the Edge executable to open in IE mode|C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe|

### Click Pro
  
Click on a selected object waiting that it's clickeable
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the element to click.|Data|
|Data type|Select the type of data to search.|xpath|
|Wait|Put the time in seconds that we will wait for the element to be clickeable.|5|

### Extract text Pro
  
Get a text object waiting that it's present
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the element to extract text.|Data|
|Data type|Select the type of data to search.|xpath|
|Wait|Put the time in seconds that we will wait for the element to be available.|5|
|Variable where to store result|Put the name of the variable where we will store the result.|Variable|

### Select object Pro
  
Select an object waiting that it's present
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the element to select.|Data|
|Data type|Select the type of data to search.|xpath|
|Wait|Put the time in seconds that we will wait for the element to appear.|5|

### Change to iframe Pro
  
Change to iframe waiting that it's present
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the iframe|Data|
|Data type|Select the type of data|xpath|
|Select by index|Checkbox to choose iframe by index|True|
|Index|Frame index within the HTML code of the web page|0|
|Wait|Put the time of wait|5|

### Change to iframes nested
  
Enter multiple iframes waiting for them to appear
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selectors of each iframe in a list format|['Data1', 'Data2']|
|Data type|Select the type of data|xpath|
|Wait|Put the time of wait|5|
|Assign result to variable|Variable where True or False will be stored depending on whether the iframe could be entered|Variable|

### Send Keys
  
Similar to Send keys web, but low level
|Parameters|Description|example|
| --- | --- | --- |
|Text|Text to send|Text|
|Special Key|Special key to send|SPACE|

### Print to PDF (Chrome)
  
Print the page as a PDF in Chrome. The PDF is generated based on the available content of the page. It does not represent a true copy of the site.
|Parameters|Description|example|
| --- | --- | --- |
|The pdf will be downloaded to the browser's default downloads folder.|||
|Print with horizontal design|If checked, the pdf will be printed in horizontal format.|True|

### Force Download
  
Force Download
|Parameters|Description|example|
| --- | --- | --- |
|Download URL|Put the URL of the download to force|http://www.web.test/file.csv|
|File Name|Put the name of the file to force|file.csv|

### Open New Tab
  
Open new tab with the URL
|Parameters|Description|example|
| --- | --- | --- |
|URL|URL to open in a new tab|http://www.google.com|

### Open Browser
  
Open a browser the URL
|Parameters|Description|example|
| --- | --- | --- |
|Browser |Browser to open|Google Chrome|
|URL|URL to open|http://www.google.com|
|Timeout|Timeout in seconds|5|
|Id|Id of the browser|4|
|Profile folder|Profile folder to open the opened browser|C:/folder|
|Download Folder|Download folder for the opened browser|C:/folder|
|Force downloads|Force the downloads to make them automatically|True|
|Custom options for the browser|Custom options in dict format|{'download.default_directory': download_path}|
|Arguments to open the browser|Arguments in list format|['--incognito','--kiosk-printing','--new-window']|

### Drag and drop
  
Do a drag and drop
|Parameters|Description|example|
| --- | --- | --- |
|Source|Source element|source|
|Target|Target element|target|
|Data type|Data type to search|Data to search|

### Upload files
  
Command to upload one or more files to an input of type file. Just complete a single value depending on how many files you want to upload.
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|We put the selector of the element where the file will be uploaded|Data|
|Data type|Data type to search|xpath|
|Load only a single field of the following. If you want to upload a single file, use the first selector, if you want to upload more than one, load the second selector with the indicated format.|||
|Load a single file|Select the file to upload|C:/Users/user/file1.pdf|
|Load multiple files|Select the file to upload|['C:/Users/user/file1.pdf', 'C:/Users/user/file2.pdf']|

### Send key combination
  
Command to send key combination
|Parameters|Description|example|
| --- | --- | --- |
|First special Key|First special key to combine with a letter/number or with a second special key|SPACE|
|Letter or number|Letter or number to combine with the first key if necessary.|A|
|Second special key|Second special key to combine with the first key if necessary.|SPACE|

### Right Click
  
Right click on a selected object
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|We put the selector to search|Data|
|Data type|We put the type of data to search|xpath|

### Get image
  
This command allows you to download an image from an <img> tag
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|Put the selector of the element to download|Data|
|Data type|Select the type of data to search|xpath|
|Folder to save the image|We put the folder where the image will be saved|C:/Users/User/Desktop|
|Name and extension of the image to save|We put the name of the image to save. If you do not put the name of the image or the extension, it will be saved with the name or extension by default.|image.png|

### Select multiple options
  
Select multiple options from a select
|Parameters|Description|example|
| --- | --- | --- |
|Data type|Select the type of data to search.|xpath|
|Data to search|Put the selector of the element to select.|Data|
|Selection type|Select the type of selection to perform.|value|
|Options to select|We put the options to select. If we select the type of selection 'select all' or 'deselect all', it is not necessary to put the options.|0,1,2,3|

### Delete cookies
  
Delete browser cookies
|Parameters|Description|example|
| --- | --- | --- |

### Get Cookies
  
Get the current browser cookies
|Parameters|Description|example|
| --- | --- | --- |
|Variable where the result will be stored|Name of the variable where the cookies will be stored|Variable|

### Access Shadow DOM
  
Access an element within a Shadow DOM. The data must belong to the parent element of the shadow-root.
|Parameters|Description|example|
| --- | --- | --- |
|Data to search|We put the selector to search|Data|

### Zoom
  
Zoom In or Zoom Out in Google Chrome and Firefox browsers.
|Parameters|Description|example|
| --- | --- | --- |
|Zoom type|Select the type of zoom to perform.|Zoom In|
