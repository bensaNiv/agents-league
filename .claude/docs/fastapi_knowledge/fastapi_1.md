---
# Smart Librarian Export (v2.0)
- Page Number: 2
- Timestamp: 2025-12-14T14:53:15.917822+02:00
- Source URL: https://fastapi.tiangolo.com
- Page Title: FastAPI
- Semantic Filename: fastapi.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 16,913 characters
---

# FastAPI

[ Skip to content ](https://fastapi.tiangolo.com/#fastapi)
[ **FastAPI and friends** newsletter 🎉 ](https://fastapi.tiangolo.com/newsletter/)
# FastAPI[¶](https://fastapi.tiangolo.com/#fastapi)
[![FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)](https://fastapi.tiangolo.com)
_FastAPI framework, high performance, easy to learn, fast to code, ready for production_
* * *
**Documentation** : <https://fastapi.tiangolo.com>
**Source Code** : 
* * *
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.
The key features are:
  * **Fast** : Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic). [One of the fastest Python frameworks available](https://fastapi.tiangolo.com/#performance).
  * **Fast to code** : Increase the speed to develop features by about 200% to 300%. *
  * **Fewer bugs** : Reduce about 40% of human (developer) induced errors. *
  * **Intuitive** : Great editor support. Completion everywhere. Less time debugging.
  * **Easy** : Designed to be easy to use and learn. Less time reading docs.
  * **Short** : Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
  * **Robust** : Get production-ready code. With automatic interactive documentation.
  * **Standards-based** : Based on (and fully compatible with) the open standards for APIs: 


* estimation based on tests conducted by an internal development team, building production applications.
## Sponsors[¶](https://fastapi.tiangolo.com/#sponsors)
### Keystone Sponsor[¶](https://fastapi.tiangolo.com/#keystone-sponsor)
### Gold and Silver Sponsors[¶](https://fastapi.tiangolo.com/#gold-and-silver-sponsors)
[Other sponsors](https://fastapi.tiangolo.com/fastapi-people/#sponsors)
## Opinions[¶](https://fastapi.tiangolo.com/#opinions)
"_[...] I'm using**FastAPI** a ton these days. [...] I'm actually planning to use it for all of my team's **ML services at Microsoft**. Some of them are getting integrated into the core **Windows** product and some **Office** products._"
Kabir Khan - **Microsoft**
* * *
"_We adopted the**FastAPI** library to spawn a **REST** server that can be queried to obtain **predictions**. [for Ludwig]_"
Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - **Uber**
* * *
"_**Netflix** is pleased to announce the open-source release of our **crisis management** orchestration framework: **Dispatch**! [built with **FastAPI**]_"
Kevin Glisson, Marc Vilanova, Forest Monsen - **Netflix**
* * *
"_I’m over the moon excited about**FastAPI**. It’s so fun!_"
Brian Okken - 
* * *
"_Honestly, what you've built looks super solid and polished. In many ways, it's what I wanted**Hug** to be - it's really inspiring to see someone build that._"
Timothy Crosley - 
* * *
"_If you're looking to learn one**modern framework** for building REST APIs, check out **FastAPI** [...] It's fast, easy to use and easy to learn [...]_"
"_We've switched over to**FastAPI** for our **APIs** [...] I think you'll like it [...]_"
Ines Montani - Matthew Honnibal - 
* * *
"_If anyone is looking to build a production Python API, I would highly recommend**FastAPI**. It is **beautifully designed** , **simple to use** and **highly scalable** , it has become a **key component** in our API first development strategy and is driving many automations and services such as our Virtual TAC Engineer._"
Deon Pillsbury - **Cisco**
* * *
##  **Typer** , the FastAPI of CLIs[¶](https://fastapi.tiangolo.com/#typer-the-fastapi-of-clis)
[![](https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg)](https://typer.tiangolo.com)
If you are building a CLI app to be used in the terminal instead of a web API, check out [**Typer**](https://typer.tiangolo.com/).
**Typer** is FastAPI's little sibling. And it's intended to be the **FastAPI of CLIs**. ⌨️ 🚀
## Requirements[¶](https://fastapi.tiangolo.com/#requirements)
FastAPI stands on the shoulders of giants:
## Installation[¶](https://fastapi.tiangolo.com/#installation)
Create and activate a [virtual environment](https://fastapi.tiangolo.com/virtual-environments/) and then install FastAPI:
```


pip install "fastapi[standard]"  
  



```

**Note** : Make sure you put `"fastapi[standard]"` in quotes to ensure it works in all terminals.
## Example[¶](https://fastapi.tiangolo.com/#example)
### Create it[¶](https://fastapi.tiangolo.com/#create-it)
Create a file `main.py` with:
```
fromtypingimport Union
fromfastapiimport FastAPI
app = FastAPI()
@app.get("/")
defread_root():
    return {"Hello": "World"}
@app.get("/items/{item_id}")
defread_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

```

Or use `async def`...
If your code uses `async` / `await`, use `async def`:
```
fromtypingimport Union
fromfastapiimport FastAPI
app = FastAPI()
@app.get("/")
async defread_root():
    return {"Hello": "World"}
@app.get("/items/{item_id}")
async defread_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

```

**Note** :
If you don't know, check the _"In a hurry?"_ section about [`async` and `await` in the docs](https://fastapi.tiangolo.com/async/#in-a-hurry).
### Run it[¶](https://fastapi.tiangolo.com/#run-it)
Run the server with:
```


fastapi dev main.py  
 ╭────────── FastAPI CLI - Development mode ───────────╮  
 │                                                     │  
 │  Serving at: http://127.0.0.1:8000                  │  
 │                                                     │  
 │  API docs: http://127.0.0.1:8000/docs               │  
 │                                                     │  
 │  Running in development mode, for production use:   │  
 │                                                     │  
 │  fastapi run                                        │  
 │                                                     │  
 ╰─────────────────────────────────────────────────────╯  
  
INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']  
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)  
INFO:     Started reloader process [2248755] using WatchFiles  
INFO:     Started server process [2248757]  
INFO:     Waiting for application startup.  
INFO:     Application startup complete.  
  



```

About the command `fastapi dev main.py`...
The command `fastapi dev` reads your `main.py` file, detects the **FastAPI** app in it, and starts a server using 
By default, `fastapi dev` will start with auto-reload enabled for local development.
You can read more about it in the [FastAPI CLI docs](https://fastapi.tiangolo.com/fastapi-cli/).
### Check it[¶](https://fastapi.tiangolo.com/#check-it)
Open your browser at 
You will see the JSON response as:
```
{"item_id":5,"q":"somequery"}

```

You already created an API that:
  * Receives HTTP requests in the _paths_ `/` and `/items/{item_id}`.
  * Both _paths_ take `GET` _operations_ (also known as HTTP _methods_).
  * The _path_ `/items/{item_id}` has a _path parameter_ `item_id` that should be an `int`.
  * The _path_ `/items/{item_id}` has an optional `str` _query parameter_ `q`.


### Interactive API docs[¶](https://fastapi.tiangolo.com/#interactive-api-docs)
Now go to 
You will see the automatic interactive API documentation (provided by 
![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)
### Alternative API docs[¶](https://fastapi.tiangolo.com/#alternative-api-docs)
And now, go to 
You will see the alternative automatic documentation (provided by 
![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)
## Example upgrade[¶](https://fastapi.tiangolo.com/#example-upgrade)
Now modify the file `main.py` to receive a body from a `PUT` request.
Declare the body using standard Python types, thanks to Pydantic.
```
fromtypingimport Union
fromfastapiimport FastAPI
frompydanticimport BaseModel
app = FastAPI()
classItem(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
@app.get("/")
defread_root():
    return {"Hello": "World"}
@app.get("/items/{item_id}")
defread_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
@app.put("/items/{item_id}")
defupdate_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

```

The `fastapi dev` server should reload automatically.
### Interactive API docs upgrade[¶](https://fastapi.tiangolo.com/#interactive-api-docs-upgrade)
Now go to 
  * The interactive API documentation will be automatically updated, including the new body:


![Swagger UI](https://fastapi.tiangolo.com/img/index/index-03-swagger-02.png)
  * Click on the button "Try it out", it allows you to fill the parameters and directly interact with the API:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-04-swagger-03.png)
  * Then click on the "Execute" button, the user interface will communicate with your API, send the parameters, get the results and show them on the screen:


![Swagger UI interaction](https://fastapi.tiangolo.com/img/index/index-05-swagger-04.png)
### Alternative API docs upgrade[¶](https://fastapi.tiangolo.com/#alternative-api-docs-upgrade)
And now, go to 
  * The alternative documentation will also reflect the new query parameter and body:


![ReDoc](https://fastapi.tiangolo.com/img/index/index-06-redoc-02.png)
### Recap[¶](https://fastapi.tiangolo.com/#recap)
In summary, you declare **once** the types of parameters, body, etc. as function parameters.
You do that with standard modern Python types.
You don't have to learn a new syntax, the methods or classes of a specific library, etc.
Just standard **Python**.
For example, for an `int`:
```
item_id: int

```

or for a more complex `Item` model:
```
item: Item

```

...and with that single declaration you get:
  * Editor support, including:
    * Completion.
    * Type checks.
  * Validation of data:
    * Automatic and clear errors when the data is invalid.
    * Validation even for deeply nested JSON objects.
  * Conversion of input data: coming from the network to Python data and types. Reading from:
    * JSON.
    * Path parameters.
    * Query parameters.
    * Cookies.
    * Headers.
    * Forms.
    * Files.
  * Conversion of output data: converting from Python data and types to network data (as JSON):
    * Convert Python types (`str`, `int`, `float`, `bool`, `list`, etc).
    * `datetime` objects.
    * `UUID` objects.
    * Database models.
    * ...and many more.
  * Automatic interactive API documentation, including 2 alternative user interfaces:
    * Swagger UI.
    * ReDoc.


* * *
Coming back to the previous code example, **FastAPI** will:
  * Validate that there is an `item_id` in the path for `GET` and `PUT` requests.
  * Validate that the `item_id` is of type `int` for `GET` and `PUT` requests.
    * If it is not, the client will see a useful, clear error.
  * Check if there is an optional query parameter named `q` (as in `http://127.0.0.1:8000/items/foo?q=somequery`) for `GET` requests.
    * As the `q` parameter is declared with `= None`, it is optional.
    * Without the `None` it would be required (as is the body in the case with `PUT`).
  * For `PUT` requests to `/items/{item_id}`, read the body as JSON:
    * Check that it has a required attribute `name` that should be a `str`.
    * Check that it has a required attribute `price` that has to be a `float`.
    * Check that it has an optional attribute `is_offer`, that should be a `bool`, if present.
    * All this would also work for deeply nested JSON objects.
  * Convert from and to JSON automatically.
  * Document everything with OpenAPI, that can be used by:
    * Interactive documentation systems.
    * Automatic client code generation systems, for many languages.
  * Provide 2 interactive documentation web interfaces directly.


* * *
We just scratched the surface, but you already get the idea of how it all works.
Try changing the line with:
```
    return {"item_name": item.name, "item_id": item_id}

```

...from:
```
        ... "item_name": item.name ...

```

...to:
```
        ... "item_price": item.price ...

```

...and see how your editor will auto-complete the attributes and know their types:
![editor support](https://fastapi.tiangolo.com/img/vscode-completion.png)
For a more complete example including more features, see the [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/).
**Spoiler alert** : the tutorial - user guide includes:
  * Declaration of **parameters** from other different places as: **headers** , **cookies** , **form fields** and **files**.
  * How to set **validation constraints** as `maximum_length` or `regex`.
  * A very powerful and easy to use **Dependency Injection** system.
  * Security and authentication, including support for **OAuth2** with **JWT tokens** and **HTTP Basic** auth.
  * More advanced (but equally easy) techniques for declaring **deeply nested JSON models** (thanks to Pydantic).
  * **GraphQL** integration with 
  * Many extra features (thanks to Starlette) as:
    * **WebSockets**
    * extremely easy tests based on HTTPX and `pytest`
    * **CORS**
    * **Cookie Sessions**
    * ...and more.


### Deploy your app (optional)[¶](https://fastapi.tiangolo.com/#deploy-your-app-optional)
You can optionally deploy your FastAPI app to 
If you already have a **FastAPI Cloud** account (we invited you from the waiting list 😉), you can deploy your application with one command.
Before deploying, make sure you are logged in:
```


fastapi login  
You are logged in to FastAPI Cloud 🚀  
  



```

Then deploy your app:
```


fastapi deploy  
Deploying to FastAPI Cloud...  
  
✅ Deployment successful!  
  
🐔 Ready the chicken! Your app is ready at https://myapp.fastapicloud.dev  
  



```

That's it! Now you can access your app at that URL. ✨
#### About FastAPI Cloud[¶](https://fastapi.tiangolo.com/#about-fastapi-cloud)
**FastAPI**.
It streamlines the process of **building** , **deploying** , and **accessing** an API with minimal effort.
It brings the same **developer experience** of building apps with FastAPI to **deploying** them to the cloud. 🎉
FastAPI Cloud is the primary sponsor and funding provider for the _FastAPI and friends_ open source projects. ✨
#### Deploy to other cloud providers[¶](https://fastapi.tiangolo.com/#deploy-to-other-cloud-providers)
FastAPI is open source and based on standards. You can deploy FastAPI apps to any cloud provider you choose.
Follow your cloud provider's guides to deploy FastAPI apps with them. 🤓
## Performance[¶](https://fastapi.tiangolo.com/#performance)
Independent TechEmpower benchmarks show **FastAPI** applications running under Uvicorn as 
To understand more about it, see the section [Benchmarks](https://fastapi.tiangolo.com/benchmarks/).
## Dependencies[¶](https://fastapi.tiangolo.com/#dependencies)
FastAPI depends on Pydantic and Starlette.
###  `standard` Dependencies[¶](https://fastapi.tiangolo.com/#standard-dependencies)
When you install FastAPI with `pip install "fastapi[standard]"` it comes with the `standard` group of optional dependencies:
Used by Pydantic:
Used by Starlette:
  * `TestClient`.
  * "parsing", with `request.form()`.


Used by FastAPI:
  * `uvicorn[standard]`, which includes some dependencies (e.g. `uvloop`) needed for high performance serving.
  * `fastapi-cli[standard]` - to provide the `fastapi` command.
    * This includes `fastapi-cloud-cli`, which allows you to deploy your FastAPI application to 


### Without `standard` Dependencies[¶](https://fastapi.tiangolo.com/#without-standard-dependencies)
If you don't want to include the `standard` optional dependencies, you can install with `pip install fastapi` instead of `pip install "fastapi[standard]"`.
### Without `fastapi-cloud-cli`[¶](https://fastapi.tiangolo.com/#without-fastapi-cloud-cli)
If you want to install FastAPI with the standard dependencies but without the `fastapi-cloud-cli`, you can install with `pip install "fastapi[standard-no-fastapi-cloud-cli]"`.
### Additional Optional Dependencies[¶](https://fastapi.tiangolo.com/#additional-optional-dependencies)
There are some additional dependencies you might want to install.
Additional optional Pydantic dependencies:
Additional optional FastAPI dependencies:
  * `ORJSONResponse`.
  * `UJSONResponse`.


## License[¶](https://fastapi.tiangolo.com/#license)
This project is licensed under the terms of the MIT license.
  *[Completion]: also known as auto-complete, autocompletion, IntelliSense
  *[CLI]: Command Line Interface
  *[Conversion]: also known as: serialization, parsing, marshalling
  *[Dependency Injection]: also known as components, resources, providers, services, injectables
  *["parsing"]: converting the string that comes from an HTTP request into Python data
