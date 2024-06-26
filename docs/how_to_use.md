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

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Como usar este módulo
Este módulo é complementado pelos módulos e comandos nativos da Web que vêm por padrão no Rocketbot. Para usar o módulo você deve ter um navegador já aberto do Rocketbot com o comando "Open Browser". Depois disso, podemos usar os comandos normalmente.

### Para usar o Edge no modo Internet Explorer, as seguintes configurações devem ser feitas:
1. Configure o navegador com base na seguinte documentação: https://docs.rocketbot.com/?p=169
2. Baixe o driver do Internet Explorer a partir do link abaixo: https://github.com/SeleniumHQ/selenium/releases/download/selenium-3.13.0/IEDriverServer_Win32_3.13.0.zip e colocá-lo em Rocketbot/drivers/win/ie/x86/
3. Para acessar as ferramentas de desenvolvimento, você deve abrir o IEChooser.exe. Para fazer isso, pressione a tecla Windows + R e digite o seguinte: %systemroot%\system32\f12\IEChooser.exe e depois clique em "accept". Selecione sua janela do navegador, e você poderá explorar os elementos da página

### Dicas para lidar com elementos em uma raiz de sombra:
1. Manipulação de iframes:
Primeiro, localize todo shadow root na qual precisa entrar para chegar ao iframe que precisa acessar. Por exemplo, se você tiver esta estrutura:

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
                    <p id="paragraph">Texto</p>
```

Deve inserir o primeiro shadow-root e, em seguida, o segundo.
Para fazer isso, deve usar o comando Run Python. Primeiro, deve importar tudo o que precisa para manipular os elementos da Web e, em seguida, acessar cada shadow root e, finalmente, acessar o iframe necessário:

```python
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

webdriver = GetGlobals("web")
if webdriver.driver_actual_id in webdriver.driver_list:
    driver = webdriver.driver_list[webdriver.driver_actual_id].
    
# Primeiro seleciona o pai do primeiro shadow-root
shadow_host = driver.find_element(By.ID, '#div1') 

# As próximas três linhas são sempre as mesmas
shadow_root_dict = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
shadow_root_id = shadow_root_dict['shadow-6066-11e4-a52e-4f735466cecf']
shadow_root = WebElement(driver, shadow_root_id, w3c=True)

# Aqui seleciona o elemento na primer shadow-root que é o pai da segundo shadow-root.
shadow_content = shadow_root.find_element(By.ID, '#div3')


shadow_host = shadow_content

# As próximas três linhas são sempre as mesmas
shadow_root_dict = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
shadow_root_id = shadow_root_dict['shadow-6066-11e4-a52e-4f735466cecf']
shadow_root = WebElement(driver, shadow_root_id, w3c=True)

# Ao inserir o último shadow-root, deve obter apenas o elemento que corresponde ao iframe que deve inserir
shadow_content = shadow_root.find_element(By.ID, '#id_iframe')

# E, finalmente, usa o comando que altera o iframe
driver.switch_to_frame(shadow_content)
```

#### Observe que, se for necessário acessar mais elementos para chegar ao iframe, basta seguir as mesmas etapas quantas vezes forem necessárias.
Quando tiver acesso ao iframe, poderá interagir com todos os elementos usando javascript, independentemente de eles terem shadow-root ou não.

2. Manipulação de elementos em um shadow root:
Para executar um clique, copie o caminho js do elemento. Em seguida, no Rocketbot, use o comando Execute JS. Nesse comando, cole o js_path e, no final, adicione .click()
Usando o exemplo do início, para clicar na tag \<a> dentro do iframe, ela deve ter a seguinte aparência:

```javascript
document.querySelector("#div_shadow").shadowRoot.querySelector("#link1").click()
```

Se, por exemplo, quiser completar um input, isso pode variar dependendo do formato do input na página.
A maioria dos inputs pode ser completada usando Javascript e o comando Execute JS da seguinte forma:

```javascript
document.querySelector("#div_shadow").shadowRoot.querySelector("#input1").value = "your_value"
```

Em outros casos, é necessário que a entrada tenha foco para que seja possível inserir um valor. Para isso, deve executar as seguintes etapas:
Em um comando JS, coloque o seguinte:

```javascript
// Com isso, você dá foco ao input
document.querySelector("#div_shadow").shadowRoot.querySelector("#input1").setAttribute('focused', '')
document.querySelector("#div_shadow").shadowRoot.querySelector("#input1").focus()
```

Quando estiver em foco, poderá usar o comando Send Keys do módulo webpro e ele escreverá o que precisa.
Por fim, pode obter o texto de um elemento também com javascript, da seguinte forma:
Execute um comando JS com o seguinte:
    
```javascript
return document.querySelector("#div_shadow").shadowRoot.querySelector("#paragraph").innerHTML
```

Atribua isso à variável de sua escolha e, nessa variável, você terá o valor codificado. Para obter um valor limpo, execute um comando Assign Variable com o seguinte: {var}.decode('latin-1')


### Como usar o perfil de usuário existente no navegador Edge
1. Abra o navegador Edge com o perfil que deseja usar.
2. Na barra de endereços, digite o seguinte: edge://version
3. Na seção "Caminho do perfil", você encontrará a pasta que contém o perfil que está usando. Copie o caminho da pasta e cole-o no campo "Caminho do perfil" do comando "Abrir Edge (Chromium)" do módulo webpro.

### Como usar o perfil de usuário no navegador Firefox
O Firefox não permite que você insira uma pasta em branco para criar um perfil como no Chrome, você deve atribuir o caminho a um perfil existente. Você pode localizar o caminho de um perfil existente ou criar um acessando o Firefox e pesquisando no mecanismo de busca o seguinte: 'about:profiles'. Você deve utilizar o caminho indicado no diretório raiz do perfil com o qual deseja abrir o navegador.

### Como atualizar o Firefox no LINUX
Se você tiver erros relacionados à versão do Firefox no Linux, siga as seguintes etapas:
1. Baixe o pacote tar mais recente do Firefox: Navegue até a página oficial de download do Firefox e obtenha a versão mais recente para Linux ou use wget no terminal:

        wget -O firefox-latest.tar.bz2 "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US"

2. Extraia o tarball

        tar xjf firefox-latest.tar.bz2

3. Mova os arquivos extraídos: Mova os arquivos extraídos para o diretório /opt, que é um diretório padrão para salvar software opcional no Linux.

         sudo mv firefox /opt/firefox-latest

4. Crie um link simbólico: Para garantir que o sistema utilize a versão mais recente, crie um link simbólico.

        sudo ln -s /opt/firefox-latest/firefox /usr/bin/firefox

Link: https://tecadmin.net/how-to-install-firefox-on-ubuntu/ => Método 2
