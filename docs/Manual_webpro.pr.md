



# WEB Pro
  
Módulo com funcionalidades estendidas para o navegador que funciona como complemento aos comandos da seção web  

*Read this in other languages: [English](Manual_webpro.md), [Português](Manual_webpro.pr.md), [Español](Manual_webpro.es.md)*
  
![banner](imgs/Banner_webpro.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  

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

## Descrição do comando

### Lista de itens
  
Obtém uma lista de todos os elementos e seus filhos de uma classe ou nome, para poder iterar sobre ela.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Tipo de classes ou atributo|Neste campo devemos colocar o tipo de classe ou atributo que usaremos.|name|
|Classes ou atributo|Neste campo devemos colocar o nome da classe ou atributo que usaremos.|col-md-6|
|Tipo do Elemento|Neste campo devemos colocar o tipo de elemento que usaremos.|div|
|Variável onde armazenar o resultado|Neste campo devemos colocar o nome da variável onde armazenaremos o resultado.|Variável|

### Limpa uma entrada e envia o texto
  
Deleta o conteúdo de um objeto tipo input e envia o texto
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Texto para enviar ou variável|Colocamos o texto ou a variável para enviar.|Texto ou Variável|
|Dado a buscar|Colocamos o dado a buscar.|Dado a buscar|
|Tipo de dado|Selecionamos o tipo de dado a buscar. Xpath, class, name, tag o id.|Dado a buscar|
|Enviar com teclas|Apaga e escreve com teclas diretamente.|Texto ou Variável|
|Espera de 1 segundo|Atribui uma espera de 1 segundo entre o apagar e o enviar elemento|True|

### Salvar Cookies
  
Salva os cookies de uma página para que possam ser carregados em outra instância
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho para o arquivo onde os cookies serão salvos|Neste campo indicamos o caminho para o arquivo onde os cookies serão salvos|C:/tmp/etc|
|Variável onde os cookies serão salvos|Neste campo indicamos o nome da variável onde os cookies serão salvos|cookies|

### Carregar Cookies
  
Carrega um arquivo com cookies
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho para o arquivo onde os cookies são armazenados|Selecione o caminho para o arquivo onde os cookies são armazenados|C:/tmp/etc|
|Atribuir resultado à variável|Variável onde True ou False será armazenado dependendo se os cookies podem ser carregados|Variável|

### Recarregar página
  
Recarregar página
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |

### Back
  
retorna à página anterior
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |

### Clique duplo
  
Clique duplo sobre um objeto selecionado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor a buscar|Dado|
|Tipo de dado|Colocamos o tipo de dado a buscar|xpath|

### Scroll
  
Rolar para uma determinada posição
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Posição|Escolhemos a posição em pixels|1500|

### Contar iten
  
Entregar o número total de itens
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da classe|Nome da classe do elemento|Name class|
|Atribuir resultado à variável|Nome da variável onde o resultado será guardado|Variable|

### Selecionar Objeto por Índice
  
Seleciona um objeto passando-lhe o índice
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a Buscar|Colocamos o seletor a buscar|form-control|
|Índice|Colocamos o índice a buscar|1|
|Tipo de dado|Selecionamos o tipo de dado a buscar|name|

### Clique Objeto por Índice
  
Clique em um objeto passando o índice
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a Buscar|Colocamos o seletor do dado a clicar.|form-control|
|Índice|Colocamos o índice do dado a clicar.|1|
|Tipo de dado|Colocamos o tipo do dado a clicar.|class|

### Exportar página para PDF
  
Exporte a página para um arquivo PDF. Se a página contiver elementos fixos, eles podem ser removidos com Javascript para obter uma exportação adequada.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho e nome do arquivo|Selecione o caminho e nome do arquivo a salvar, sem a extensão .pdf|path/to/file.pdf|
|Excluir cabeçalho fixo|Se o site contiver um cabeçalho fixo, marque a caixa para removê-lo para que não se repita em cada captura. O comando procura a tag 'header', se não encontrá-la, dará um erro, se não funcionar, você deve desmarcá-la.|True|
|Atribuir resultado à variável|Selecione o nome da variável para a qual queremos atribuir o resultado|Variável|

### Abrir Chrome em modo headless
  
Abre Chrome em modo headless
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL do Servidor|Escreva a URL da página a abrir.|http://www.rocketbot.co|

### Tomar captura por coordenadas
  
Tira uma foto da tela de uma seção da página usando coordenadas
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Posição|Coordenadas da seção da página|x,y|
|Dimensões|Dimensões da seção da página|largura, altura|
|Caminho e nome onde a imagem será salva|Caminho e nome onde a imagem será salva|/Users/User/folder/image.jpg|

### Obter o retângulo de delimitação
  
Obtém as coordenadas x e y e as dimensões de um objeto.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a Buscar|Colocamos o seletor do elemento a obter.|Data|
|Tipo de dado|Selecionamos o tipo de dado a buscar.|xpath|
|Variável onde armazenar o resultadoo|Nome da variável sem {}|Variável|

### Obter coordenadas de um objeto
  
Obtém as coordenadas x e y de um objeto.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do elemento a selecionar|Data|
|Tipo de dado|Selecionamos o tipo de dado a buscar|xpath|
|Variável onde armazenar o resultado|Nome da variável sem {}|Variável|

### Obter dimensões de um objeto
  
Obtém dimensões de um objeto
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do elemento a selecionar|Data|
|Tipo de dado|Selecionamos o tipo de dado a buscar|xpath|
|Variável onde armazenar o resultado|Nome da variável sem {}|Variável|

### Abrir Chrome modo desenvolvedor
  
Abre o Google Chrome em modo seguro ou debugger
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL do Servidor|URL do servidor a abrir|http://www.rocketbot.co|
|Modo|Selecionamos o modo em que o navegador será aberto.|Debugger|

### Ver Consola
  
Obtém informações do console
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Variável onde armazenar o resultado|Nome da variável onde armazenar o resultado|Variável|
|Nível |Nível de informação a mostrar|Severe|

### Converter página para PNG
  
Ele tira vários instantâneos da página da Web e os concatena em um. Se a página contiver elementos fixos, eles podem ser removidos com Javascript para obter uma exportação correta.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome|Nome da imagem|ImagemWeb|
|Pasta de download|Caminho onde a imagem gerada será baixada|C:/Users/user/Desktop|

### Hover Element
  
Passar o mouse sobre o elemento
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o selecionador do elemento ao qual fazermos hover.|Data|
|Tipo de dado|Colocamos o tipo de dado que queremos buscar.|xpath|

### Abrir Edge (Chromium)
  
Abrir o novo Chromium-based Edge
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL do Servidor|Url da páxina a abrir no Edge|http://www.rocketbot.co|
|Ruta do perfil|Carpeta que contén o perfil a utilizar.|C:/Users/User/AppData/Local/Microsoft/Edge/User Data/Default|
|Comezar no modo Internet Explorer|Comeza o navegador no modo Internet Explorer|True|
|Seleccionar executábel de Edge|Selecciona o executábel de Edge para abrir no modo IE|C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe|

### Clique Pro
  
Clica em um objeto selecionado, esperando que ele se torne clicável.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do elemento a clicar.|Data|
|Tipo de dado|Selecionamos o tipo de dado a buscar.|xpath|
|Esperar|Colocamos o tempo em segundos que esperaremos a que o elemento se torne clicável.|5|

### Extrair Texto Pro
  
Obtém o texto de um objeto esperando que ele esteja disponível.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do elemento a extrair texto.|Data|
|Tipo de dado|Selecionamos o tipo de dado a buscar.|xpath|
|Esperar|Colocamos o tempo em segundos que esperaremos a que o elemento este disponível.|5|
|Variável onde armazenar o resultado|Colocamos o nome da variável onde armazenaremos o resultado.|Variável|

### Selecionar objeto Pro
  
Seleciona um objeto esperando que ele esteja presente
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do elemento a selecionar.|Data|
|Tipo de dado|Selecionamos o tipo de dado a buscar.|xpath|
|Esperar|Colocamos o tempo em segundos que esperaremos a que o elemento apareça.|5|

### Mudar para iframe Pro
  
Troca para um iframe esperando que ele esteja presente
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do iframe|Data|
|Tipo de dado|Selecionamos o tipo de dado|xpath|
|Selecionar por índice|Caixa de seleção para escolher iframe por índice|True|
|Índice|Índice do frame dentro do código HTML da página da web|0|
|Esperar|Colocamos o tempo de espera|5|

### Mudar para iframes aninhados
  
Entrar em varios iframes aguardando que se encontrem presentes
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dados a buscar|Colocar os seletores de cada iframe em formato lista|['Data1', 'Data2']|
|Tipo de dado|Selecionamos o tipo de dado|xpath|
|Esperar|Colocamos o tempo de espera|5|
|Atribuir resultado à variável|Variável onde True ou False será armazenado dependendo se o iframe pode ser introduzido|Variável|

### Enviar Teclas
  
Similar ao Send Web Text, mas em um nível inferior
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Texto|Texto a enviar|Texto|
|Tecla especial|Tecla especial a enviar|SPACE|

### Imprimir como PDF (Chrome)
  
Imprima a página como PDF no Chrome. O PDF é gerado com base no conteúdo disponível da página. Não representa uma cópia verdadeira do site.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|O pdf será baixado para a pasta de downloads padrão do navegador.|||
|Imprimir com design horizontal|Se marcado, o pdf será impresso em formato horizontal.|True|

### Forçar o download
  
Forçando um download
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL de Download|Colocamos a URL de download a forçar|http://www.web.test/file.csv|
|Nome do arquivo|Colocamos o nome do arquivo a forçar|file.csv|

### Abrir Nova Aba
  
Abre uma nova aba com a URL
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL|URL para abrir em uma nova aba|http://www.google.com|

### Abrir navegador
  
Abre o navegador indicando a URL
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Navegador |Navegador para abrir|Google Chrome|
|URL|URL para abrir|http://www.google.com|
|Tempo de espera|Tiempo de espera en segundos|5|
|Id|Id do navegador|4|
|Pasta de perfil|Rota da pasta do perfil do usuário para abrir o navegador|C:/folder|
|Pasta de download|Caminho da pasta de downloads para o navegador aberto|C:/folder|
|Forçar downloads|Forçar downloads para torná-los automáticos|True|
|Opções personalizadas para o navegador|Opções personalizadas no formato dict|{'download.default_directory': download_path}|
|Argumentos para abrir o navegador|Argumentos em formato de lista|['--incognito','--kiosk-printing','--new-window']|

### Drag and drop
  
Fazer um drag and drop
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Origem|Origem do elemento|source|
|Destino|Destino do elemento|target|
|Tipo de dado|Tipo de dado a buscar|Dado a buscar|

### Subir arquivo
  
Comando para fazer upload um ou mais arquivos para um input do tipo file. Basta preencher um único valor, dependendo de quantos arquivos você deseja enviar.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do elemento onde o arquivo será subido|Data|
|Tipo de dado|Tipo de dado a buscar|xpath|
|Carregue apenas um único campo do seguinte. Se quiser fazer upload de um único arquivo, use o primeiro seletor, se quiser fazer upload de mais de um, carregue o segundo seletor com o formato indicado.|||
|Carregar um único arquivo|Selecionamos o arquivo a subir|C:/Users/user/file1.pdf'|
|Carregar vários arquivos|Selecionamos o arquivo a subir|['C:/Users/user/file1.pdf', 'C:/Users/user/file2.pdf']|

### Enviar combinação de teclas
  
Comando para enviar combinação de teclas
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Primeira tecla especial|Primeira tecla especial a combinar com uma letra/numero ou com uma segunda tecla especial|SPACE|
|Letra ou número|Letra ou número para combinar com a primeira tecla se necessário.|A|
|Segunda tecla especial|Segunda tecla especial para combinar com a primeira tecla se necessário.|SPACE|

### Clique direito
  
Clique direito sobre um objeto selecionado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor para pesquisar|Dado|
|Tipo de dado|Colocamos o tipo de dados para procurar|xpath|

### Obter imagem
  
Este comando permite baixar uma imagem de uma tag <img>
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor do elemento a baixar|Data|
|Tipo de dado|Selecionamos o tipo de dado a buscar|xpath|
|Pasta para salvar a imagem|Colocamos a pasta onde a imagem será salva|C:/Users/Usuário/Desktop|
|Nome e extensão da imagem para salvar|Colocamos o nome da imagem para salvar. Se você não colocar o nome da imagem ou a extensão, ela será salva com o nome ou extensão padrão.|imagem.png|

### Selecionar várias opções
  
Selecione várias opções de um seletor
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Tipo de dado|Selecionamos o tipo de dado a buscar.|xpath|
|Dado a buscar|Colocamos o seletor do elemento a selecionar.|Data|
|Tipo de seleção|Selecione o tipo de seleção a ser realizada.|value|
|Opções para selecionar|Colocamos as opções para selecionar. Se selecionarmos o tipo de seleção 'selecionar tudo' ou 'desmarcar tudo', não é necessário colocar as opções.|0,1,2,3|

### Excluir cookies
  
Exclua os cookies do navegador
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |

### Obter Cookies
  
Obtenha os cookies do navegador atual
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Variável onde o resultado será armazenado|Nome da variável onde os cookies serão armazenados|Variável|

### Acessar ao Shadow DOM
  
Acessar um elemento dentro de um Shadow DOM. O dado deve pertencer ao elemento pai do shadow-root.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Dado a buscar|Colocamos o seletor para pesquisar|Dado|

### Zoom
  
Aumente ou diminua o zoom nos navegadores Google Chrome e Firefox.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Tipo de Zoom|Selecione o tipo de zoom a ser realizada.|Zoom In|
