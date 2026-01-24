1. init.py -> empty folder
2. settings.py -> 
3. wsgi.py -> used for deployment
4. asgi.py -> used for deployment , used for storing database username, password 


---------------------------------Templates--------------------------------------
-Template literals/Template tag

------------------------------------Cookies-----------------------------------------
can be implemented using session-API or Cookies

setting data into cookie object:
response.set_cookie(key,value)

How to read data from cookie object:
value = request.COOKIES['key']
or 
'key' in request.COOKIES:




