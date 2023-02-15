# WEB Pro
  
Module with extended functionalities for the browser that works as a complement to the commands of the web section

*Read this in other languages: [English](README.md), [Portugues](README.pr.md), [Español](README.es.md).*

## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  


## How to use this module
This module complements the native Web modules and commands that come by default in Rocketbot. In order to use the module you must have a browser opened from Rocketbot with the "Open Browser" command. After that, you will be able to use the commands.
In order to use Edge in Internet Explorer mode, the following settings must be made:
1. Configure the browser based on the following documentation: https://docs.rocketbot.com/?p=169
2. Download the Internet Explorer driver from the link below: https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.3.0/IEDriverServer_Win32_4.3.0.zip and place it in Rocketbot/drivers/win/ie/x86/
3. To be able to access the developer tools, IEChooser.exe must be opened. To do so, press the Windows key + R and type the following: %systemroot%\system32\f12\IEChooser.exe and then press accept. Select the window of your browser, and you will be able to explore the elements of the page.


## Overview


1. List of items  
Gets a list of all elements and their children from a class or name in order to iterate over it.

2. Clean input and send text  
Deletes the contents of an input object and sends the text

3. Save Cookies  
Saves the cookies of a page so that it can be loaded in another instance

4. Load Cookies  
Loads a file with cookies

5. Reload Page  
Reload Page

6. Back  
Back to previous page

7. Double Click  
Double click on a selected object

8. Scroll  
Scroll to a specific position

9. Count Elements  
Delivers the total number of elements

10. Select Object by Index  
Select an object by passing it the index

11. Click Object by Index  
Click an object by passing it the index

12. Export page to PDF  
Export the page to a PDF file. If the page contains sticky elements, they can be removed with Javascript to get a proper export.

13. Open Chrome headless  
Open Chrome in headless mode

14. Take screenshot from coordinates  
Take a screenshot to a section of the page by coordinates

15. Get bounding rectangle  
Obtains x and y coordinates and dimensions of an object

16. Get location of an object  
Get x and y coordinates of an object

17. Get size of an object  
Get size of an object

18. Open Chrome developer mode  
Open Google Chrome with unsafe mode or debugger mode

19. See Console  
Get info from console

20. WebPage to PNG  
It takes multiple snapshots of the web page and concatenates them into one. If the page contains fixed elements, they can be removed with Javascript to obtain a correct export.

21. Hover Element  
Move mouse over the element

22. Open Edge (Chromium)  
Open the new Edge based on Chromium

23. Access Shadow DOM  
Access an element within a Shadow DOM. The data must belong to the parent element of the shadow-root.

24. Click Pro  
Click on a selected object waiting that it's clickeable

25. Extract text Pro  
Get a text object waiting that it's present

26. Select object Pro  
Select an object waiting that it's present

27. Change to iframe Pro  
Change to iframe waiting that it's present

28. Send Keys  
Similar to Send keys web, but low level

29. Print to PDF (Chrome)  
Print the page as a PDF in Chrome. The PDF is generated based on the available content of the page. It does not represent a true copy of the site.

30. Force Download  
Force Download

31. Open New Tab  
Open new tab with the URL

32. Open Browser  
Open a browser the URL

33. Drag and drop  
Do a drag and drop

34. Upload files  
Command to upload one or more files to an input of type file. Just complete a single value depending on how many files you want to upload.

35. Send key combination  
Command to send key combination

36. Right Click  
Right click on a selected object  



### Changes
Tue Sep 13 19:15:44 2022  Merge branch qa of https://github.com/rocketbot-cl/webpro
Thu Aug 4 13:00:30 2022  [Merge] added Open browser with or without profile by jmsiro
Mon May 2 16:53:22 2022  Merge from QA - Merge pull request from rocketbot-cl
Thu Aug 19 13:24:01 2021  Merge branch master of github.com:rocketbot-cl/webpro
Fri Apr 24 16:28:55 2020  Merge branch master of https://github.com/rocketbot-cl/webpro
Wed Mar 11 14:24:59 2020  Merge branch master of https://github.com/rocketbot-cl/webpro

----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**beautifulsoup4**](https://pypi.org/project/beautifulsoup4/)- [**requests**](https://pypi.org/project/requests/)- [**pyshadow**](https://pypi.org/project/pyshadow/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)