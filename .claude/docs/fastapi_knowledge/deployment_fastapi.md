---
# Smart Librarian Export (v2.0)
- Page Number: 11
- Timestamp: 2025-12-14T14:53:15.917822+02:00
- Source URL: https://fastapi.tiangolo.com/deployment
- Page Title: Deployment - FastAPI
- Semantic Filename: deployment_fastapi.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 1,607 characters
---

# Deployment - FastAPI

[ Skip to content ](https://fastapi.tiangolo.com/deployment/#deployment)
[ **FastAPI and friends** newsletter 🎉 ](https://fastapi.tiangolo.com/newsletter/)
# Deployment[¶](https://fastapi.tiangolo.com/deployment/#deployment)
Deploying a **FastAPI** application is relatively easy.
## What Does Deployment Mean[¶](https://fastapi.tiangolo.com/deployment/#what-does-deployment-mean)
To **deploy** an application means to perform the necessary steps to make it **available to the users**.
For a **web API** , it normally involves putting it in a **remote machine** , with a **server program** that provides good performance, stability, etc, so that your **users** can **access** the application efficiently and without interruptions or problems.
This is in contrast to the **development** stages, where you are constantly changing the code, breaking it and fixing it, stopping and restarting the development server, etc.
## Deployment Strategies[¶](https://fastapi.tiangolo.com/deployment/#deployment-strategies)
There are several ways to do it depending on your specific use case and the tools that you use.
You could **deploy a server** yourself using a combination of tools, you could use a **cloud service** that does part of the work for you, or other possible options.
For example, we, the team behind FastAPI, built 
I will show you some of the main concepts you should probably keep in mind when deploying a **FastAPI** application (although most of it applies to any other type of web application).
You will see more details to keep in mind and some of the techniques to do it in the next sections. ✨
