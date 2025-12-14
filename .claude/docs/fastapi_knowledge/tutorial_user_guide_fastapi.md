---
# Smart Librarian Export (v2.0)
- Page Number: 4
- Timestamp: 2025-12-14T14:53:15.917822+02:00
- Source URL: https://fastapi.tiangolo.com/tutorial
- Page Title: Tutorial - User Guide - FastAPI
- Semantic Filename: tutorial_user_guide_fastapi.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 2,529 characters
---

# Tutorial - User Guide - FastAPI

[ Skip to content ](https://fastapi.tiangolo.com/tutorial/#tutorial-user-guide)
[ **FastAPI and friends** newsletter 🎉 ](https://fastapi.tiangolo.com/newsletter/)
# Tutorial - User Guide[¶](https://fastapi.tiangolo.com/tutorial/#tutorial-user-guide)
This tutorial shows you how to use **FastAPI** with most of its features, step by step.
Each section gradually builds on the previous ones, but it's structured to separate topics, so that you can go directly to any specific one to solve your specific API needs.
It is also built to work as a future reference so you can come back and see exactly what you need.
## Run the code[¶](https://fastapi.tiangolo.com/tutorial/#run-the-code)
All the code blocks can be copied and used directly (they are actually tested Python files).
To run any of the examples, copy the code to a file `main.py`, and start `fastapi dev` with:
```

fastapi dev main.p

```

It is **HIGHLY encouraged** that you write or copy the code, edit it and run it locally.
Using it in your editor is what really shows you the benefits of FastAPI, seeing how little code you have to write, all the type checks, autocompletion, etc.
* * *
## Install FastAPI[¶](https://fastapi.tiangolo.com/tutorial/#install-fastapi)
The first step is to install FastAPI.
Make sure you create a [virtual environment](https://fastapi.tiangolo.com/virtual-environments/), activate it, and then **install FastAPI** :
```


pip install "fastapi[standard]"  
  



```

Note
When you install with `pip install "fastapi[standard]"` it comes with some default optional standard dependencies, including `fastapi-cloud-cli`, which allows you to deploy to 
If you don't want to have those optional dependencies, you can instead install `pip install fastapi`.
If you want to install the standard dependencies but without the `fastapi-cloud-cli`, you can install with `pip install "fastapi[standard-no-fastapi-cloud-cli]"`.
## Advanced User Guide[¶](https://fastapi.tiangolo.com/tutorial/#advanced-user-guide)
There is also an **Advanced User Guide** that you can read later after this **Tutorial - User guide**.
The **Advanced User Guide** builds on this one, uses the same concepts, and teaches you some extra features.
But you should first read the **Tutorial - User Guide** (what you are reading right now).
It's designed so that you can build a complete application with just the **Tutorial - User Guide** , and then extend it in different ways, depending on your needs, using some of the additional ideas from the **Advanced User Guide**.
