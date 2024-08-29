



# WEB Pro
  
Módulo com funcionalidades estendidas para o navegador que funciona como complemento aos comandos da seção web  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Overview


1. Lista de itens  
Obtém uma lista de todos os elementos e seus filhos de uma classe ou nome, para poder iterar sobre ela.

2. Limpa uma entrada e envia o texto  
Deleta o conteúdo de um objeto tipo input e envia o texto

3. Salvar Cookies  
Salva os cookies de uma página para que possam ser carregados em outra instância

4. Carregar Cookies  
Carrega um arquivo com cookies

5. Recarregar página  
Recarregar página

6. Back  
retorna à página anterior

7. Clique duplo  
Clique duplo sobre um objeto selecionado

8. Scroll  
Rolar para uma determinada posição

9. Contar iten  
Entregar o número total de itens

10. Selecionar Objeto por Índice  
Seleciona um objeto passando-lhe o índice

11. Clique Objeto por Índice  
Clique em um objeto passando o índice

12. Exportar página para PDF  
Exporte a página para um arquivo PDF. Se a página contiver elementos fixos, eles podem ser removidos com Javascript para obter uma exportação adequada.

13. Abrir Chrome em modo headless  
Abre Chrome em modo headless

14. Tomar captura por coordenadas  
Tira uma foto da tela de uma seção da página usando coordenadas

15. Obter o retângulo de delimitação  
Obtém as coordenadas x e y e as dimensões de um objeto.

16. Obter coordenadas de um objeto  
Obtém as coordenadas x e y de um objeto.

17. Obter dimensões de um objeto  
Obtém dimensões de um objeto

18. Abrir Chrome modo desenvolvedor  
Abre o Google Chrome em modo seguro ou debugger

19. Ver Consola  
Obtém informações do console

20. Converter página para PNG  
Ele tira vários instantâneos da página da Web e os concatena em um. Se a página contiver elementos fixos, eles podem ser removidos com Javascript para obter uma exportação correta.

21. Hover Element  
Passar o mouse sobre o elemento

22. Abrir Edge (Chromium)  
Abrir o novo Chromium-based Edge

23. Clique Pro  
Clica em um objeto selecionado, esperando que ele se torne clicável.

24. Extrair Texto Pro  
Obtém o texto de um objeto esperando que ele esteja disponível.

25. Selecionar objeto Pro  
Seleciona um objeto esperando que ele esteja presente

26. Mudar para iframe Pro  
Troca para um iframe esperando que ele esteja presente

27. Mudar para iframes aninhados  
Entrar em varios iframes aguardando que se encontrem presentes

28. Enviar Teclas  
Similar ao Send Web Text, mas em um nível inferior

29. Imprimir como PDF (Chrome)  
Imprima a página como PDF no Chrome. O PDF é gerado com base no conteúdo disponível da página. Não representa uma cópia verdadeira do site.

30. Forçar o download  
Forçando um download

31. Abrir Nova Aba  
Abre uma nova aba com a URL

32. Abrir navegador  
Abre o navegador indicando a URL

33. Drag and drop  
Fazer um drag and drop

34. Subir arquivo  
Comando para fazer upload um ou mais arquivos para um input do tipo file. Basta preencher um único valor, dependendo de quantos arquivos você deseja enviar.

35. Enviar combinação de teclas  
Comando para enviar combinação de teclas

36. Clique direito  
Clique direito sobre um objeto selecionado

37. Obter imagem  
Este comando permite baixar uma imagem de uma tag <img>

38. Selecionar várias opções  
Selecione várias opções de um seletor

39. Excluir cookies  
Exclua os cookies do navegador

40. Obter Cookies  
Obtenha os cookies do navegador atual

41. Acessar ao Shadow DOM  
Acessar um elemento dentro de um Shadow DOM. O dado deve pertencer ao elemento pai do shadow-root.

42. Zoom  
Aumente ou diminua o zoom nos navegadores Google Chrome e Firefox.  




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