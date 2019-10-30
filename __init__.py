# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
   sudo pip install <package> -t .

"""

from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains

module = GetParams("module")

if module == "webelementlist":
    webdriver = GetGlobals("web")
    el_ = GetParams("el_")
    type_ = GetParams("type_")
    data_ = GetParams("data_")
    var_ = GetParams("result")

    driver = webdriver.driver_list[webdriver.driver_actual_id]
    global getChild
    def getChild( el):
        res = []
        if len(el) >0:
            for c in el:
                tmp = c.attrs
                tmp["text"] = c.text
                tmp["etype"] = c.name
                tmp['value'] = c.get('value')
                res.append(tmp)
                if len(c.findChildren()) > 1:
                    res.append( getChild(c.findChildren()) )
        else:
            tmp = el.attrs
            tmp["text"] = el.text
            tmp["etype"] = el.name    
            res.append(tmp)
            
        return res
    
    html = BeautifulSoup(driver.page_source, 'html.parser')
    objs = html.find_all(el_, attrs= {type_: data_})
    re = []
    for element in objs:
        if element.findChildren():            
            re.append(getChild(element.findChildren()))
        else:
            re.append( getChild(element))
    
    SetVar(var_, str(re))

        
if module == "CleanInputs":
    webdriver = GetGlobals("web")
    driver = webdriver.driver_list[webdriver.driver_actual_id]
    search = GetParams('search_data')
    texto = GetParams('texto')
    search_type = GetParams("tipo")
    element =  None
    print(search_type)
    if search_type == 'name':
        element = driver.find_element_by_name(search)
    if search_type == 'xpath':
        element = driver.find_element_by_xpath(search)
    if search_type == 'class':
        element = driver.find_element_by_class_name(search)
    if search_type == 'id':
        element = driver.find_element_by_id(search)
    if search_type == 'tag':
        element = driver.find_element_by_tag(search)
        
    if element is not None and texto is not None:
        element.clear()
        element.send_keys(texto)  

if module == "LoadCookies":
    import pickle
    webdriver = GetGlobals("web")
    driver = webdriver.driver_list[webdriver.driver_actual_id]
    file_ = GetParams('file_')
    with open(file_, 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         print(cookies)
         for cookie in cookies:
             driver.add_cookie(cookie)

if module == "SaveCookies":
    import pickle
    webdriver = GetGlobals("web")

    driver = webdriver.driver_list[webdriver.driver_actual_id]
    print(driver.title)
    file_ = GetParams('file_')
    cookies = driver.get_cookies()
    print(cookies)
    with open(file_, 'wb') as filehandler:
        pickle.dump(cookies, filehandler)
        
if module == "reloadPage":
    webdriver = GetGlobals("web")
    driver = webdriver.driver_list[webdriver.driver_actual_id]
    driver.refresh()

if module == "back":
    webdriver = GetGlobals("web")
    driver = webdriver.driver_list[webdriver.driver_actual_id]
    driver.back()


if module == "DoubleClick":
    webdriver = GetGlobals("web")
    driver = webdriver.driver_list[webdriver.driver_actual_id]

    data_ = GetParams("data")
    data_type = GetParams("data_type")

    actionChains = ActionChains(driver)
    elementLocator = driver.find_element(data_type, data_)

    actionChains.double_click(elementLocator).perform()