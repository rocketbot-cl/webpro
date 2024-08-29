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

__version__ = '12.4.0'
__author__ = 'Rocketbot <contacto@rocketbot.com>'

import base64
import os
import sys
import shutil
import platform
from io import BytesIO
import traceback

import time
from bs4 import BeautifulSoup
from selenium import webdriver as ws
from selenium.webdriver import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'webpro' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)
print(cur_path)

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from PIL import Image
from pathlib import Path
from pyshadow.main import Shadow

global shadow_root # pylint: disable=global-at-module-level
global element_root # pylint: disable=global-at-module-level

GetGlobals = GetGlobals #pylint: disable=undefined-variable,self-assigning-variable
GetParams = GetParams #pylint: disable=undefined-variable,self-assigning-variable
SetVar = SetVar #pylint: disable=undefined-variable,self-assigning-variable
PrintException = PrintException #pylint: disable=undefined-variable,self-assigning-variable
tmp_global_obj = tmp_global_obj #pylint: disable=undefined-variable,self-assigning-variable

downloads_path = str(Path.home() / "Downloads")

module = GetParams("module")

def makeTmpDir(name):
    try:
        os.mkdir("tmp")
        os.mkdir("tmp" + os.sep + name)
    except:
        try:
            os.mkdir("tmp" + os.sep + name)
        except:
            pass


def getBoundingClientRect(type_element, selector):
    web_driver = GetGlobals("web")
    if web_driver.driver_actual_id in web_driver.driver_list:
        driver = web_driver.driver_list[web_driver.driver_actual_id]
    
    # driver = webdriver.driver_list[webdriver.driver_actual_id]

    if type_element == "xpath":
        rect = driver.execute_script("""element = document.evaluate('{}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; 
        return element.getBoundingClientRect()""".format(selector))
    elif type_element == "id":
        rect = driver.execute_script("element = document.getElementById('{}');return element.getBoundingClientRect() ".format(selector))
    elif type_element == "name":
        rect = driver.execute_script("element = document.getElementsByName('{}')[0];return element.getBoundingClientRect()".format(selector))
    elif type_element == "tag name":
        rect = driver.execute_script("element = document.getElementsByTagName('{}')[0];return element.getBoundingClientRect()".format(selector))
    elif type_element == "class name":
        rect = driver.execute_script(
            "element = document.getElementsByClassName('{}')[0];return element.getBoundingClientRect()".format(selector))
    else:
        return Exception("Invalid type")

    return rect

types = {
        "name": By.NAME,
        "id": By.ID,
        "class name": By.CLASS_NAME,
        "xpath": By.XPATH,
        "tag name": By.TAG_NAME,
        "link text": By.LINK_TEXT,
        "partial link text": By.PARTIAL_LINK_TEXT,
        "css selector": By.CSS_SELECTOR
    }

special_keys = {
    "ADD":u'\ue025',
    "ALT":u'\ue00a',
    "ARROW_DOWN":u'\ue015',
    "ARROW_LEFT":u'\ue012',
    "ARROW_RIGHT":u'\ue014',
    "ARROW_UP":u'\ue013',
    "BACKSPACE":u'\ue003',
    "BACK_SPACE":u'\ue003',
    "CANCEL":u'\ue001',
    "CLEAR":u'\ue005',
    "COMMAND":u'\ue03d',
    "CONTROL":u'\ue009',
    "DECIMAL":u'\ue028',
    "DELETE":u'\ue017',
    "DIVIDE":u'\ue029',
    "DOWN":u'\ue015',
    "END":u'\ue010',
    "ENTER":u'\ue007',
    "EQUALS":u'\ue019',
    "ESCAPE":u'\ue00c',
    "F1":u'\ue031',
    "F10":u'\ue03a',
    "F11":u'\ue03b',
    "F12":u'\ue03c',
    "F2":u'\ue032',
    "F3":u'\ue033',
    "F4":u'\ue034',
    "F5":u'\ue035',
    "F6":u'\ue036',
    "F7":u'\ue037',
    "F8":u'\ue038',
    "F9":u'\ue039',
    "HELP":u'\ue002',
    "HOME":u'\ue011',
    "INSERT":u'\ue016',
    "LEFT":u'\ue012',
    "LEFT_ALT":u'\ue00a',
    "LEFT_CONTROL":u'\ue009',
    "LEFT_SHIFT":u'\ue008',
    "META":u'\ue03d',
    "MULTIPLY":u'\ue024',
    "NULL":u'\ue000',
    "NUMPAD0":u'\ue01a',
    "NUMPAD1":u'\ue01b',
    "NUMPAD2":u'\ue01c',
    "NUMPAD3":u'\ue01d',
    "NUMPAD4":u'\ue01e',
    "NUMPAD5":u'\ue01f',
    "NUMPAD6":u'\ue020',
    "NUMPAD7":u'\ue021',
    "NUMPAD8":u'\ue022',
    "NUMPAD9":u'\ue023',
    "PAGE_DOWN":u'\ue00f',
    "PAGE_UP":u'\ue00e',
    "PAUSE":u'\ue00b',
    "RETURN":u'\ue006',
    "RIGHT":u'\ue014',
    "SEMICOLON":u'\ue018',
    "SEPARATOR":u'\ue026',
    "SHIFT":u'\ue008',
    "SPACE":u'\ue00d',
    "SUBTRACT":u'\ue027',
    "TAB":u'\ue004',
    "UP":u'\ue013'
}

webdriver = GetGlobals("web")
if webdriver.driver_actual_id in webdriver.driver_list:
    driver = webdriver.driver_list[webdriver.driver_actual_id]

if module == "webelementlist":
    
    el_ = GetParams("el_")
    type_ = GetParams("type_")
    data_ = GetParams("data_")
    var_ = GetParams("result")

    try:
    
        global getChild


        def getChild(el):
            import bs4
            
            res = []
            if len(el) > 0:
                for c in el:
                    if isinstance(c, bs4.element.NavigableString):
                        res.append(c)
                        continue
                    tmp = c.attrs
                    tmp["text"] = c.text
                    tmp["etype"] = c.name
                    tmp['value'] = c.get('value')
                    res.append(tmp)
                    if len(c.findChildren()) > 1:
                        res.append(getChild(c.findChildren()))
            else:
                tmp = el.attrs
                tmp["text"] = el.text
                tmp["etype"] = el.name
                res.append(tmp)

            return res


        html = BeautifulSoup(driver.page_source, 'html.parser')
        objs = html.find_all(el_, attrs={type_: data_})
        re = []
        for element in objs:
            if element.findChildren():
                re.append(getChild(element.findChildren()))
            else:
                re.append(getChild(element))

        SetVar(var_, str(re))
    
    except Exception as e:
        traceback.print_exc()
        raise e

if module == "CleanInputs":
    
    search = GetParams('search_data')
    texto = GetParams('texto')
    search_type = GetParams("tipo")
    element = None

    try:
        simulationKey = eval(GetParams("simulationKey"))
    except:
        simulationKey = False

    try:
        sleep_ = eval(GetParams('sleep_'))
    except:
        sleep_ = False
    
    search_type = {"tag": "tag name", "class": "class name"}.get(search_type, search_type)
    
    element = driver.find_element(search_type, search)

    if element is not None:
        element.clear()
        if sleep_:
            time.sleep(1)
        if simulationKey:
            element.send_keys(Keys.SHIFT, Keys.ARROW_UP)
            element.send_keys(Keys.DELETE)
        if texto is not None:
            element.send_keys(texto)

if module == "LoadCookies":
    import pickle

    file_ = GetParams('file_')
    var_ = GetParams('var_')
    
    
    try:
        with open(file_, 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
            print(cookies)
            for cookie in cookies:
                driver.add_cookie(cookie)
        SetVar(var_, "True")
    except Exception as e:
        PrintException()
        SetVar(var_, "False")
        raise e
        

if module == "SaveCookies":
    import pickle

    

    file_ = GetParams('file_')
    result = GetParams('result')

    try:
        
        cookies = driver.get_cookies()
        print("--*", cookies)
        with open(file_, 'wb') as filehandler:
            pickle.dump(cookies, filehandler)

        if result:
            SetVar(result, str(cookies))  
            
    except Exception as e:
        PrintException()
        raise e

if module == "reloadPage":
    
    
    driver.refresh()

if module == "back":
    
    
    driver.back()

if module == "DoubleClick":
    
    

    data_ = GetParams("data")
    data_type = GetParams("data_type")

    actionChains = ActionChains(driver)
    elementLocator = driver.find_element(data_type, data_)

    actionChains.double_click(elementLocator).perform()

if module == "Scroll":
    
    

    position = GetParams("position")

    if position == "end":
        last_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, {})".format(last_height))
    else:
        driver.execute_script("window.scrollTo(0, {})".format(position))

if module == "length_":

    
    
    search = GetParams('search_data')
    var_ = GetParams("var_")

    try:
        element = driver.execute_script(" return document.getElementsByClassName('"+search+"').length")
        print(element)
    except:
        PrintException()

    SetVar(var_, element)

if module == "selectElement":

    
    
    option_ = GetParams('option_')
    search = GetParams('search_data')
    index_ = GetParams("index_")
    print(option_,index_)
    element = None
    index_ = eval(index_)
    res = False

    try:

        if option_ is None:
            raise Exception('Debe seleccionar una opcion')

        if option_ == 'name':
            element = driver.find_elements_by_name(search)[index_]
        if option_ == 'class':
            elements = driver.find_elements_by_xpath(f'//*[contains(@class,"{search}")]')[index_]
            webdriver._object_selected = elements

    except Exception as e:
        PrintException()
        raise e

if module == "clickElement":

    option_ = GetParams('option_')
    search = GetParams('search_data')
    index_ = GetParams("index_")
    element = None
    if index_:
        index_ = eval(index_)
    else:
        raise Exception("Debe ingresar un indice")
    res = False
    cont_ = 0

    try:

        if option_ is None:
            raise Exception('Debe seleccionar una opcion')

        if option_ == 'name':
            element = driver.find_elements("name", search)

            for ele in element:
                if cont_ == index_:
                    ele.click()
                    webdriver._object_selected = ele
                    break
                else:
                    cont_ += 1

        if option_ == 'class':
            elements = driver.find_elements("xpath", f'//*[contains(@class,"{search}")]')[index_]
            elements.click()
            webdriver._object_selected = elements

        if option_ == 'xpath':
            elements = driver.find_elements("xpath", search)[index_]
            
            wait = WebDriverWait(driver, int(5))
            elements = wait.until(EC.visibility_of(elements))
            try:
                elements.click()
            except:
                driver.execute_script("arguments[0].click();", elements)
            webdriver._object_selected = elements
            

    except Exception as e:
        PrintException()
        raise e

if module == "html2pdf":
    path_ = GetParams("path_")
    if path_:
        path_ = path_.replace("/", os.sep)
    var_ = GetParams("var_")
    del_header = GetParams("del_header")

    try:


        tmp_path = "tmp/webpro/screenshot.png"
        makeTmpDir("webpro")
        images = []
        
        
        total_height = driver.execute_script("return document.body.scrollHeight")
        actual_height = 0
        image_count = 1
        driver.execute_script("window.scrollTo(0, 0)")
        
        
        while int(actual_height) < int(total_height):
            driver.get_screenshot_as_file(tmp_path)
            

            if image_count == 1:
                
                image = Image.open(tmp_path)
                width, height = image.size
                im_1 = image.convert('RGB')
                
                image.close()
                if del_header == "True":
                    driver.execute_script("""var header = document.querySelector('header');
                                             header.style.visibility = 'hidden'
                                          """)
            else:
                image_ = Image.open(tmp_path)
                im_ = image_.convert('RGB')
                
                if total_height - actual_height <= height:
                    last_height = total_height - actual_height
                    y = height - last_height
                    
                    im_ = im_.crop((0, y, width, height))
                    
                images.append(im_)
                image_.close()
            
            
            # Scrolleo hasta la proxima screen
            driver.execute_script("window.scrollTo(0, {})".format((height * image_count)))
            time.sleep(1)
            actual_height += height
            image_count += 1

        im_1.save(path_, save_all=True, append_images=images)
            
        if del_header == "True":
            driver.execute_script("""var header = document.querySelector('header');
                                    header.style.visibility = 'inherit'
                                  """)
        res = True
        

    except Exception as e:
        PrintException()
        res = False
        raise e

    SetVar(var_,res)

if module == "chromeHeadless":

    url = GetParams("url")
    print(url)
    try:
        base_path = tmp_global_obj["basepath"]

        web = GetGlobals("web")

        platform_ = platform.system()

        if platform_.endswith('dows'):
            chrome_driver = os.path.join(base_path, os.path.normpath(r"drivers\win\chrome"), "chromedriver.exe")
        else:
            chrome_driver = os.path.join(base_path, os.path.normpath(r"drivers/mac/chrome"), "chromedriver")

        chrome_options = Options()

        chrome_options.add_argument('headless')
        web.driver_list[web.driver_actual_id] = Chrome(options=chrome_options, executable_path=chrome_driver)
        if url:
            web.driver_list[web.driver_actual_id].get(url)

    except Exception as e:
        PrintException()
        raise e

if module == "Edge_":
    
    from selenium.webdriver.edge.options import Options as EdgeOptions

    url = GetParams("url")
    ie_mode = GetParams("ie_mode")
    edge_exe = GetParams("edge_exe")
    if edge_exe != None or edge_exe != "":
        edge_exe = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
    platform_ = platform.system()
    user_data_dir = GetParams("user_data_dir")

    try:
        base_path = tmp_global_obj["basepath"]

        web = GetGlobals("web")

        if ie_mode == "True":
            if not edge_exe:
                raise Exception("Debe seleccionar el ejecutable de Edge")
            else:
                caps = DesiredCapabilities.INTERNETEXPLORER
                caps['ignoreProtectedModeSettings'] = True
                caps['ENABLE_PERSISTENT_HOVERING'] = False
                caps['REQUIRE_WINDOW_FOCUS'] = False
                caps['UNEXPECTED_ALERT_BEHAVIOR'] = True
                caps['ACCEPT_SSL_CERTS'] = True
                caps['INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS'] = True
                
                # Se debe tener instalado el driver de Edge en la version de Edge que se esta usando y el driver de IE de https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.3.0/IEDriverServer_Win32_4.3.0.zip
                ieOptions = ws.IeOptions()
                ieOptions.add_additional_option("ie.edgechromium", True)
                ieOptions.add_additional_option("ie.edgepath", edge_exe)

                driver = ws.Ie(executable_path=f'{base_path}/drivers/win/ie/x86/IEDriverServer.exe', options=ieOptions, capabilities=caps)

                driver.maximize_window()
                web.driver_list[web.driver_actual_id] = driver
                time.sleep(1)
                driver.get(url)

        else:
            if platform_.lower() == "windows":
                edge_driver = os.path.join(cur_path, os.path.normpath(r"drivers\edge"), "msedgedriver.exe")
            else:
                edge_driver = os.path.join(cur_path, os.path.normpath(r"drivers/edge"), "msedgedriver")
            
            edge_options = EdgeOptions()

            if user_data_dir:
                data_dir = os.path.dirname(user_data_dir)
                edge_profile = os.path.basename(user_data_dir)

                edge_options.use_chromium = True
                edge_options.add_argument('--no-sandbox')
                edge_options.add_argument('user-data-dir={}'.format(data_dir))
                edge_options.add_argument('profile-directory={}'.format(edge_profile))


            edge_options.add_argument('start-maximized')
            try:
                driver = ws.Edge(edge_driver, options=edge_options, keep_alive=True)
                
                web.driver_list[web.driver_actual_id] = driver
                if url:
                    web.driver_list[web.driver_actual_id].get(url)
            except:
                edge_driver = os.path.join(base_path, os.path.normpath(r"drivers\win\edge\x86"), "msedgedriver.exe")
                driver = ws.Edge(edge_driver, options=edge_options, keep_alive=True)

                web.driver_list[web.driver_actual_id] = driver
                if url:
                    web.driver_list[web.driver_actual_id].get(url)
        


    except Exception as e:
        PrintException()
        raise e


if module == "screenshot":
    path = GetParams("path")
    location = GetParams("location")
    size = GetParams("size")


    tmp_path = "tmp/webpro/screenshot.png"
    try:
        element = driver.find_element("xpath", "/html/body")

        makeTmpDir("webpro")
        driver.save_screenshot(tmp_path)

        print(location, size)

        location = eval(location)
        size = eval(size)

        x = location[0]
        y = location[1]
        w = size[0]
        h = size[1]
        try:
            if _platform == "darwin":
                if subprocess.call("system_profiler SPDisplaysDataType | grep 'Retina'", shell=True) == 0:
                    x = x * 2
                    y = y * 2
                    w = w * 2
                    h = h * 2
        except:
            pass
        width = x + w
        height = y + h

        im = Image.open(tmp_path)
        im = im.crop((int(x), int(y), int(width), int(height)))
        im = im.convert("RGB")
        im.save(path)

    except Exception as e:
        PrintException()
        raise e

if module == "getBoundingClientRect":
    data = GetParams("data")
    type_ = GetParams("data_type")
    result = GetParams("result")

    
    

    try:
        rect = getBoundingClientRect(type_, data)
        if result:
            SetVar(result, rect)

    except Exception as e:
        PrintException()
        raise e

if module == "getLocation":
    data = GetParams("data")
    type_ = GetParams("data_type")
    result = GetParams("result")

    
    

    try:
        rect = getBoundingClientRect(type_, data)
        location = {"x": rect["x"], "y": rect["y"]}
        if result:
            SetVar(result, location)

    except Exception as e:
        PrintException()
        raise e

if module == "getSize":
    data = GetParams("data")
    type_ = GetParams("data_type")
    result = GetParams("result")

    
    

    try:
        rect = getBoundingClientRect(type_, data)
        size = {"width": rect["width"], "height": rect["height"]}
        if result:
            SetVar(result, size)

    except Exception as e:
        PrintException()
        raise e

if module == "chromeMode":
    url = GetParams("url")
    mode = GetParams("mode")
    base_path = tmp_global_obj["basepath"]

    web = GetGlobals("web")
    platform_ = platform.system()
    try:
        if platform_.endswith('dows'):
            chrome_driver = os.path.join(base_path, os.path.normpath(r"drivers\win\chrome"), "chromedriver.exe")
        else:
            chrome_driver = os.path.join(base_path, os.path.normpath(r"drivers/mac/chrome"), "chromedriver")

        if mode == "unsafe":
            chrome_options = Options()
            chrome_options.add_experimental_option("prefs", {'safebrowsing.enabled': 'false',
                                                             'profile.default_content_setting_values.automatic_downloads': 1})
            web.driver_list[web.driver_actual_id] = Chrome(desired_capabilities=chrome_options.to_capabilities(),
                                                           executable_path=chrome_driver)
        elif mode == "debugger":
            d = DesiredCapabilities.CHROME
            d['loggingPrefs'] = {'browser': 'ALL'}
            web.driver_list[web.driver_actual_id] = Chrome(desired_capabilities=d, executable_path=chrome_driver)

        if url:
            web.driver_list[web.driver_actual_id].get(url)

    except Exception as e:
        PrintException()
        raise e

if module == "debugger":
    result = GetParams("result")
    level = GetParams("level")
    web = GetGlobals('web')
    try:
        driver = web.driver_list[web.driver_actual_id]
        # print messages
        logs = driver.get_log('browser')
        r = []
        if level != "ALL":
            for entry in logs:
                if entry['level'] == level:
                    r.append(entry)
        else:
            r = logs

        if result:
            SetVar(result, r)

    except Exception as e:
        PrintException()
        raise e

if module == "fullScreenshot":
    name = GetParams("name")
    web = GetGlobals('web')
    path_ = GetParams("path_")
    if path_:
        path_ = path_.replace("/", os.sep)

    try:
        
        tmp_path = "tmp/webpro/screenshot.png"
        images = []
        makeTmpDir("webpro")
        
        total_height = driver.execute_script("return document.body.scrollHeight")
        actual_height = 0
        image_count = 1
        driver.execute_script("window.scrollTo(0, 0)")
        
        while int(actual_height) < int(total_height):
            driver.get_screenshot_as_file(tmp_path)
            

            if image_count == 1:
                
                image = Image.open(tmp_path)
                width, height = image.size
                im_1 = image.convert('RGB')
                images.append(image)
                
                try:
                    driver.execute_script("""var header = document.querySelector('header');
                                            if (header != null) {header.style.visibility = 'hidden'};
                                        """)
                except:
                    pass
                
            else:
                image_ = Image.open(tmp_path)
                im_ = image_.convert('RGB')
                
                if total_height - actual_height <= height:
                    last_height = total_height - actual_height
                    y = height - last_height
                    
                    im_ = im_.crop((0, y, width, height))
                    
                images.append(im_)
                
            
            
            # Scrolleo hasta la proxima screen
            driver.execute_script("window.scrollTo(0, {})".format((height * image_count)))
            time.sleep(1)
            # actual_height = driver.execute_script("return window.pageYOffset")
            actual_height += height
            image_count += 1
        
        try:
            driver.execute_script("""var header = document.querySelector('header');
                                    if (header != null) {header.style.visibility = 'inherit'};
                                """)
        except:
            pass
        
        img = Image.new('RGB', (width, total_height))
        
        
        height_ = 0
        
        for image in images:
            img.paste(image, (0, height_))
            
            height_ += height
        
        if path_:
            img.save(f'{path_}/{name}.png')
        else:
            img.save(f'{downloads_path}/{name}.png')
        
    except Exception as e:
        PrintException()
        raise e

if module == "Hover":
    
    

    data_ = GetParams("data")
    data_type = GetParams("data_type")

    actionChains = ActionChains(driver)
    elementLocator = driver.find_element(data_type, data_)
    actionChains.move_to_element(elementLocator).perform()

if module == "clickPro":
    
    data_ = GetParams("data")
    wait_ = GetParams("wait")
    data_type = GetParams("data_type")
    shadow_element = GetParams("shadow_element")
    if shadow_element == None or shadow_element == False:
        shadow_element = False
    else:
        shadow_element = True

    try:
        if not wait_:
            wait_ = 5
        if not shadow_element:
            actionChains = ActionChains(driver)
            wait = WebDriverWait(driver, int(wait_))
            try:
                elementLocator = wait.until(EC.element_to_be_clickable((types[data_type], data_)))
                webdriver._object_selected = elementLocator
                actionChains.click(elementLocator).perform()
            except TimeoutException:
                PrintException()
                raise Exception("The item is not available to be clicked")
        else:
            try:
                shadow_root.find_element(element_root, data_).click()
            except:
                traceback.print_exc()
                PrintException()
                raise Exception("The item is not available to be clicked")


    except Exception as e:
        PrintException()
        raise e

if module == "getText":
    
    data_ = GetParams("data")
    wait_ = GetParams("wait")
    data_type = GetParams("data_type")
    result = GetParams("result")
    shadow_element = GetParams("shadow_element")
    if shadow_element == None or shadow_element == False:
        shadow_element = False
    else:
        shadow_element = True
    try:
        if not shadow_element:
            if not wait_:
                wait_ = 5
            actionChains = ActionChains(driver)
            wait = WebDriverWait(driver, int(wait_))
            try:
                elementLocator = wait.until(EC.visibility_of_element_located((types[data_type], data_)))
                SetVar(result, elementLocator.text)
            except TimeoutException:
                raise Exception("The item is not available to be selected")
        else:
            try:
                texto = shadow_root.find_element(element_root, data_).text
                SetVar(result, texto)
            except:
                PrintException()
                raise Exception("The item is not available to be selected")

    except Exception as e:
        print("\x1B[" + "31;40mEXCEPTION \x1B[" + "0m")
        PrintException()
        raise e

if module == "selectPro":
    
    data_ = GetParams("data")
    wait_ = GetParams("wait")
    data_type = GetParams("data_type")
    shadow_element = GetParams("shadow_element")
    if shadow_element == None or shadow_element == False:
        shadow_element = False
    else:
        shadow_element = True

    try:
        if not shadow_element:
            if not wait_:
                wait_ = 5
            actionChains = ActionChains(driver)
            wait = WebDriverWait(driver, int(wait_))
            try:
                elementLocator = wait.until(EC.visibility_of_element_located((types[data_type], data_)))
                webdriver._object_selected = elementLocator
            except TimeoutException:
                raise Exception("The item is not available to be selected")
        else:
            try:
                webdriver._object_selected = shadow_root.find_element(element_root, data_)
            except:
                PrintException()
                raise Exception("The item is not available to be selected")

    except Exception as e:
        print("\x1B[" + "31;40mEXCEPTION \x1B[" + "0m")
        PrintException()
        raise e

if module == "changeIframePro":
    data_ = GetParams("data")
    wait_ = GetParams("wait")
    data_type = GetParams("data_type")
    index_check = GetParams("index_check")
    index = GetParams("index")
    try:
        if not wait_:
            wait_ = 5
        actionChains = ActionChains(driver)
        wait = WebDriverWait(driver, int(wait_))
        try:

            if index_check and eval(index_check):
                driver.switch_to.frame(int(index))
            else:
                elementLocator = wait.until(EC.presence_of_element_located((types[data_type], data_)))
                if sys.maxsize > 2**32:
                    driver.switch_to.frame(elementLocator)
                else:
                    driver.switch_to_frame(elementLocator)

        except TimeoutException:
            raise Exception("The item is not available to be clicked")

    except Exception as e:
        print("\x1B[" + "31;40mEXCEPTION \x1B[" + "0m")
        PrintException()
        raise e

if module == "changeMultipleIframes":
    data_list = GetParams("data_list") 
    wait_ = GetParams("wait")
    data_type = GetParams("data_type")
    var_ = GetParams("var_")
    
    try:
        if not wait_:
            wait_ = 5
        actionChains = ActionChains(driver)
        wait = WebDriverWait(driver, int(wait_))

        if data_list:
            data_list = eval(data_list)
        if isinstance(data_list, list):
            iframe_identifiers = data_list 
            for iframe in iframe_identifiers:
                try:
                    # if index_check and eval(index_check):
                    #     print(iframe)
                    #     driver.switch_to.frame(int(iframe))
                    # else:
                    elementLocator = wait.until(EC.presence_of_element_located((types[data_type], iframe)))
                    if sys.maxsize > 2**32:
                        driver.switch_to.frame(elementLocator)
                    else:
                        driver.switch_to_frame(elementLocator)

                    time.sleep(0.5)
                    SetVar(var_, True)
                except Exception as e:
                    SetVar(var_, False)
                    import traceback
                    traceback.print_exc()
                    raise e
        else:
            SetVar(var_, False)
            raise ValueError("No iframe identifiers provided")
    except Exception as e:
        SetVar(var_, False)
        print("\x1B[" + "31;40mEXCEPTION \x1B[" + "0m")
        PrintException()
        raise e

if module == "sendkeys":

    text = GetParams("text")
    special = GetParams("special")
    if special is None:
        special = ""

    try:
        web_driver = GetGlobals("web")
        driver = web_driver.driver_list[web_driver.driver_actual_id]
        actions = ActionChains(driver)
        if len(special) > 0:
            actions.send_keys(special_keys[special])
        else:
            actions.send_keys(text)
        actions.perform()
    except Exception as e:
        print("\x1B[" + "31;40mEXCEPTION \x1B[" + "0m")
        PrintException()
        raise e


if module == "printPDF":
    import json
    from selenium import webdriver as wd
    chrome_options = wd.ChromeOptions()
    landscape = GetParams("landscape")

    if landscape:
        script = """
            var style = document.createElement('style');
            style.type = 'text/css';
            style.innerHTML = '@page { size: landscape; }';
            document.head.appendChild(style);
        """

        driver.execute_script(script)


    settings = {
       "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
        }
    prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
    
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_argument('--kiosk-printing')

    driver.execute_script('window.print();')


if module == "forceDownload":
    url_file = GetParams("url_file")
    name_file = GetParams("name_file")

    try:
        from json import dumps
        web_driver = GetGlobals("web")
        driver = web_driver.driver_list[web_driver.driver_actual_id]

        driver.execute_script("""
            var url_file = arguments[0]
            var name_file = arguments[1]
            var link = document.createElement("a");
            link.download = name_file
            link.href = url_file;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            delete link;
            """, url_file, name_file)
    except Exception as e:
        PrintException()
        raise e

if module == "new_tab":
    url_ = GetParams("url_")
    # open tab
    driver.execute_script(f'''window.open("{url_}","_blank");''')
    driver.switch_to.window(driver.window_handles[-1])

if module == "open_browser":
    
    browser_ = GetParams("browser")
    timeout = GetParams("timeout")
    url_ = GetParams("url_")
    newId = GetParams("newId")
    download_path = GetParams("download_path")
    if download_path:
        download_path = download_path.replace("/", os.sep)
    force_downloads = GetParams("force_downloads")
    profile_path = GetParams("profile_path")
    
    if profile_path == None or profile_path == "":
        profile_path = ""
    
    if not browser_:
        browser_ = "chrome"
    

    custom_options = GetParams("custom_options")
    arguments = GetParams("arguments")
    
    try:
        custom_options = eval(custom_options)
    except:
        pass

    try:
        arguments = eval(arguments)
    except:
        pass

    try:    
        if browser_ == "chrome":
            platform_ = platform.system()
            if platform_.endswith('dows'):
                chrome_driver = os.path.join(base_path, os.path.normpath(r"drivers\win\chrome"), "chromedriver.exe")
            elif platform_ == "Linux" or platform_ == "Linux2":
                chrome_driver = os.path.join(base_path, "drivers", "linux", "chrome", "chromedriver")
            else:
                chrome_driver = os.path.join(base_path, os.path.normpath(r"drivers/mac/chrome"), "chromedriver")
            
            caps = selenium.webdriver.ChromeOptions()
            
            if platform_ == "Linux" or platform_ == "Linux2":
                caps.add_argument("start-maximized")
                caps.add_argument("disable-infobars")
                caps.add_argument("--disable-extensions")
                caps.add_argument('log-level=3')
                settings = {
                        "recentDestinations": [{
                                "id": "Save as PDF",
                                "origin": "local",
                                "account": "",
                            }],
                            "selectedDestinationId": "Save as PDF",
                            "version": 2
                        }
                prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
                caps.add_experimental_option('prefs', prefs)
                caps.add_argument('--kiosk-printing')
            else:
                caps.add_argument("--safebrowsing-disable-download-protection")
            
            prefs = {"download.default_directory": download_path}

            if force_downloads == "True":
                force_download_params = {
                'download.prompt_for_download': False,
                'safebrowsing.enabled': False,
                'plugins.always_open_pdf_externally': True
                }
                prefs.update(force_download_params)
            if custom_options:
                prefs.update(custom_options)
                
            settings = {"recentDestinations": [{
                    "id": "Save as PDF",
                    "origin": "local",
                    "account": "",
                }],
                "selectedDestinationId": "Save as PDF",
                "version": 2
            }
            
            prefs.update({'printing.print_preview_sticky_settings.appState': json.dumps(settings)})

            caps.add_experimental_option("prefs", prefs)
            caps.add_argument('--kiosk-printing')
            
            if profile_path == "":
                pass
            else:
                caps.add_argument("--user-data-dir=" + profile_path)
            
            if arguments:
                for arg in arguments:
                    caps.add_argument(arg)
            
            browser_driver = Chrome(executable_path=chrome_driver, chrome_options=caps)

        elif browser_ == "firefox":
            platform_ = platform.system()
            if platform_.endswith('dows'):
                firefox_driver = os.path.join(base_path, os.path.normpath(r"drivers\win\firefox\x64"), "geckodriver.exe")
            elif platform_ == "Linux" or platform_ == "Linux2":
                firefox_driver = os.path.join(base_path, os.path.normpath(r"drivers/linux/firefox"), "geckodriver")
            else:
                firefox_driver = os.path.join(base_path, os.path.normpath(r"drivers/mac/chrome"), "geckodriver")
                
                
            firefox_options = FirefoxOptions()

            if platform_ == "Linux" or platform_ == "Linux2":
                firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
                firefox_capabilities['marionette'] = True
                firefox_options.binary_location = r'/usr/bin/firefox'

            if profile_path != "":
                profile = FirefoxProfile(profile_path)
                #firefox_options.add_argument("-profile")
                #firefox_options.add_argument(profile_path)
                
            else:
                from time import sleep
                new_path = os.path.join(base_path, "firefox_temp_profile")
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                sleep(2)
                profile = FirefoxProfile(new_path)
                profile.set_preference("profile_dir", new_path)

            if download_path:
                firefox_options.set_preference("browser.download.folderList", 2)
                firefox_options.set_preference("browser.download.dir", download_path)
                profile.set_preference("browser.download.manager.showWhenStarting", False)  
                profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "*")

            if force_downloads == "True":
                firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "*")
            
            if custom_options:
                for key, value in custom_options.items():
                    firefox_options.set_preference(key, value)
            
            try:
                browser_driver = Firefox(executable_path=firefox_driver, firefox_options=firefox_options)
            except:
                try:
                    browser_driver = Firefox(executable_path=firefox_driver, options=firefox_options, firefox_profile=profile)
                except:
                    browser_driver = Firefox(executable_path=firefox_driver, options=firefox_options)

        if not timeout:
            timeout = 100

        if not (newId):
            newId = "default"
        webdriver.driver_actual_id = newId
        webdriver.driver_list[webdriver.driver_actual_id] = browser_driver
        
        webdriver.driver_list[webdriver.driver_actual_id].set_page_load_timeout(int(timeout))
        webdriver.driver_list[webdriver.driver_actual_id].get(url_)        
    except Exception as e:
        PrintException()
        raise e
try:
    if module == "drag_and_drop":
        source = GetParams("source")
        target = GetParams("target")
        tipo = GetParams("tipo")
    
        script_js = """
            path1="{path1}",path2="{path2}",option="{tipo}","xpath"==option&&(source=document.evaluate(path1,document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue,target=document.evaluate(path2,document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue),"id"==option&&(source=document.querySelector("#"+path1),target=document.querySelector("#"+path2)),"class"==option&&(source=document.querySelector("."+path1),target=document.querySelector("."+path2)),"tag"==option&&(source=document.querySelector(path1),target=document.querySelector(path2)),target.appendChild(source);
        """.format(path1=source, path2=target, tipo=tipo)
        driver.execute_script(script_js)

    if module == "uploadFiles":
        data_ = GetParams("data")
        data_type = GetParams("data_type")
        files = GetParams("files")
        single_file = GetParams("single_file")
        
        if single_file == "":
            single_file = None
        
        element = driver.find_element(data_type, data_)
        print('path:', single_file)
        if single_file != None:
            element.send_keys(single_file)
        else:
            files = files.replace("\\", "/")
            
            if files.startswith("["):
                files = eval(files)
                files = " \n ".join(files)
                element.send_keys(files)

    if module == "sendKeyCombination":
        first_special_key = GetParams("first_special_key")    
        text = GetParams("text")
        second_special_key = GetParams("second_special_key")    
        try:
            web_driver = GetGlobals("web")
            driver = web_driver.driver_list[web_driver.driver_actual_id]
            from selenium.webdriver import ActionChains
            actions = ActionChains(driver)
            if not text:
                actions.key_down(special_keys[first_special_key]).send_keys(special_keys[second_special_key]).key_up(special_keys[first_special_key]).perform()
            if text:
                actions.key_down(special_keys[first_special_key]).send_keys(text).key_up(special_keys[first_special_key]).perform()
        except Exception as e:
            print("\x1B[" + "31;40mEXCEPTION \x1B[" + "0m")
            PrintException()
            raise e
      
    if module == "shadow_dom":
        data = GetParams("data")
        
        shadow_root = Shadow(driver)
        element_root = shadow_root.find_element(data)

    if module == "RightClick":
        data = GetParams("data")
        data_type = GetParams("data_type")

        actionChains = ActionChains(driver)
        elementLocator = driver.find_element(data_type, data)
        actionChains.context_click(elementLocator).perform()

    if module == "getImage":
        data = GetParams("data")
        data_type = GetParams("data_type")
        img_path = GetParams("img_path")
        img_path = img_path.replace("/", os.sep)
        img_name = GetParams("img_name")

        try:
            import urllib.request

            element = driver.find_element(data_type, data)
            src = element.get_attribute("src")

            if os.path.isdir(img_path):
                if not img_name:
                    filename = os.path.basename(src)
                    print(filename)

                    if not "." in filename:
                        filename = filename + ".jpg"

                    img_path = os.path.join(img_path, filename)

                else:
                    if not "." in img_name:
                        img_name = img_name + ".jpg"
                        
                    img_path = os.path.join(img_path, img_name)
            
            if not img_name:
                filename = os.path.basename(src)
                print(filename)

                if not "." in filename:
                    filename = filename + ".jpg"


            if src.startswith("data:image"):
                src = src.split(",")[1]
                src = base64.b64decode(src)
                with open(img_path, "wb") as fh:
                    fh.write(src)
            else:
                urllib.request.urlretrieve(src, img_path)

        except Exception as e:
            PrintException()
            raise e
        
    if module == "multiple_select":
        data_type = GetParams("data_type")
        data = GetParams("data")
        selection_type = GetParams("selection_type")
        options = GetParams("options")

        try:
            element = driver.find_element(data_type, data)
            select = Select(element)
            options = options.split(",")

            if selection_type == "select_all":
                options = [x for x in range(len(select.options))]
                for option in options:
                    select.select_by_index(int(option))
            elif selection_type == "deselect_all":
                select.deselect_all()
            elif selection_type == "index":
                for option in options:
                    select.select_by_index(int(option))
            elif selection_type == "value":
                for option in options:
                    select.select_by_value(option)
            elif selection_type == "text":
                for option in options:
                    select.select_by_visible_text(option)
            else:
                raise Exception("Invalid selection type")

        except Exception as e:
            PrintException()
            raise e
        
    if module == "get_cookies":
        var_ = GetParams("var_")
        cookies = driver.get_cookies()
        SetVar(var_, str(cookies))
        
    if module == "delete_cookies":
        driver.delete_all_cookies()

    if module == "zoom":
        selection = GetParams("selection_zoom")
        try:
            current_zoom = driver.execute_script("return document.body.style.zoom || '1'")
            step=0.1
            if selection == "in":
                current_zoom = float(current_zoom)
                new_zoom = current_zoom + step
                driver.execute_script(f"document.body.style.zoom='{new_zoom}'")
            elif selection == "out":
                current_zoom = float(current_zoom)
                new_zoom = current_zoom - step
                driver.execute_script(f"document.body.style.zoom='{new_zoom}'")
            elif selection == "reset":
                driver.execute_script(f"document.body.style.zoom='1'")
        except Exception as e:
            traceback.print_exc()
            PrintException()
            raise e

except Exception as e:
    traceback.print_exc()
    PrintException()
    raise e
