# FastAPI

It is a modern, fast, and high-performance web framework for building APIs with Python.

* [project example script](https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/APIs%20%26%20Web%20Scraping/FastAPI/fastAPI.py)

<br>

* [Fast API with Python - codewithtomi via FreeCodeCamp](https://www.youtube.com/watch?v=tLKKmouUams&ab_channel=freeCodeCamp.org)

* [Fast API Cheat Sheet - by codewithtomi.com](https://www.dropbox.com/s/bw4lektx9x9467i/FastAPI%20Cheat%20Sheet.pdf?dl=0)


## Installation & Doc

* Install fastapi: 

        python -m pip install fastapi

* Install uvicorn for running the web server: 
    
        pip install uvicorn

* Activate the web server: via the terminal, navigate to the path that hosts the fastAPI python script, and run: 

        uvicorn script_filename:app --reload

*Note: the script filename should be written without the .py suffix*      

* After the above step, copy and navigate to the uvivorn URL adress given in the terminal
        
  * `URL/docs` for displaying the current documentation of your FastAPI script

  * `URL/<path parameter>/<value>` to get a specific value from a method (path parameter)

<br>

| Error Code| Error Message| Error Description|
|-------|----------------|------------|
| 500 |Internal Server Error| Data does not exist|
|422|Unprocessable Entity|Data is out of boundaries that we have previously set|

--- 

## Resources

* https://fastapi.tiangolo.com/

* https://www.youtube.com/watch?v=tLKKmouUams&ab_channel=freeCodeCamp.org