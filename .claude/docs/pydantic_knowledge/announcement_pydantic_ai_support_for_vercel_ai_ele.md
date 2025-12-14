---
# Smart Librarian Export (v2.0)
- Page Number: 68
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://pydantic.dev/articles/pydantic-ai-ui-vercel-ai
- Page Title: Announcement: Pydantic AI support for Vercel AI Elements | Pydantic
- Semantic Filename: announcement_pydantic_ai_support_for_vercel_ai_ele.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 6,266 characters
---

# Announcement: Pydantic AI support for Vercel AI Elements | Pydantic

/Pydantic AI
# Announcement: Pydantic AI support for Vercel AI Elements
![Laís Carvalho avatar](https://pydantic.dev/cdn-cgi/image/width=96,quality=75,format=auto/https://avatars.githubusercontent.com/u/42092770?v=4)
Laís Carvalho
4 mins
2025/11/05
Pydantic AI now supports Vercel AI frontends natively via the `VercelAIAdapter` class.
[Pydantic AI](https://ai.pydantic.dev/) and 
Before, you needed to write translation code in your agent logic:
```
@app.post('/chat')
async def chat(request: Request):
    # 100 lines of translation code...

```

Now, because Pydantic AI supports the [Vercel AI Data Stream Protocol](https://ai.pydantic.dev/ui/vercel-ai/), you can use the `dispatch_request()` method to handle the event translation:
```
@app.post('/chat')
async def chat(request: Request) -> Response:
    return await VercelAIAdapter.dispatch_request(request, agent=agent)

```

##  [#](https://pydantic.dev/articles/pydantic-ai-ui-vercel-ai#use-with-starlette-based-web-frameworks)Use with Starlette-based web frameworks
If your app uses FastAPI or another Starlette-based web framework, the `VercelAIAdapter.dispatch_request(request, agent=agent)` class method parses the request body, runs the agent with streaming, and encodes the response as server-sent events (SSE), as detailed on the code snippet below.
```
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from pydantic_ai import Agent
from pydantic_ai.ui.vercel_ai import VercelAIAdapter


agent = Agent('openai:gpt-5')
app = FastAPI()


@app.post('/chat')
async def chat(request: Request) -> Response:
    return await VercelAIAdapter.dispatch_request(request, agent=agent)

```

Reference docs available at: [ai.pydantic.dev/ui/vercel-ai](https://ai.pydantic.dev/ui/vercel-ai/).
##  [#](https://pydantic.dev/articles/pydantic-ai-ui-vercel-ai#use-vercelaiadapter-methods-directly)Use `VercelAIAdapter` methods directly
For backends that use non-Starlette-based frameworks such as `VercelAIAdapter` instance and use its individual methods to build a custom adapter.
Check out the [official docs](https://ai.pydantic.dev/ui/vercel-ai/#advanced-usage) for details on individual method's usage.
##  [#](https://pydantic.dev/articles/pydantic-ai-ui-vercel-ai#why-we-built-the-vercelaiadapter-interface)Why we built the `VercelAIAdapter` interface
When building a chat app or other interactive frontend for an AI agent, your backend will need to receive agent run input (like a chat message or complete [message history](https://ai.pydantic.dev/message-history/)) from the frontend. You will also need to stream the [agent's events](https://ai.pydantic.dev/agents/#streaming-all-events) (like text, thinking, and tool calls) to the frontend in real time. While your frontend could use Pydantic AI's [ModelRequest](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.ModelRequest) and [AgentStreamEvent](https://ai.pydantic.dev/api/messages/#pydantic_ai.messages.AgentStreamEvent) directly, you will typically want to use a UI event stream protocol that is natively supported by your frontend framework. That's why we built the [Vercel AI Data Stream Protocol](https://ai.pydantic.dev/ui/vercel-ai/) integration, to help you bridge the two frameworks seamlessly.
Give it a try and [let us know](https://logfire.pydantic.dev/docs/join-slack/) what you think.
##  [#](https://pydantic.dev/articles/pydantic-ai-ui-vercel-ai#faq)FAQ
###  [#](https://pydantic.dev/articles/pydantic-ai-ui-vercel-ai#does-this-work-with-django-or-flask)Does this work with Django or Flask?
Yes, but you'll need to use the adapter's individual methods instead of the `dispatch_request()` convenience one, which only works with Starlette-based frameworks like FastAPI. The [docs](https://ai.pydantic.dev/ui/vercel-ai/) show how to use `build_run_input()`, `run_stream()`, and `encode_stream()` methods directly. This way, you can modify events before they reach the frontend.
###  [#](https://pydantic.dev/articles/pydantic-ai-ui-vercel-ai#what-events-get-streamed-to-the-frontend)What events get streamed to the frontend?
Everything your agent does: text chunks as they are generated, tool calls with their arguments, thinking steps, errors, and completion events. The adapter transforms each Pydantic AI event type into its Vercel AI equivalent.
###  [#](https://pydantic.dev/articles/pydantic-ai-ui-vercel-ai#whats-the-on_complete-callback-for)What's the `on_complete` callback for?
It lets you access the agent output and message history, and inject additional events after the agent finishes. Pass a callback function to `dispatch_request()` or `run_stream()` that receives the completed `AgentRunResult` and optionally yields more Vercel AI events. Useful for logging, analytics, storing conversations, or triggering follow-up actions.
###  [#](https://pydantic.dev/articles/pydantic-ai-ui-vercel-ai#is-there-performance-overhead)Is there performance overhead?
Minimal. Events are transformed as they stream through, with no buffering. The overhead is just the event transformation itself.
###  [#](https://pydantic.dev/articles/pydantic-ai-ui-vercel-ai#does-this-work-with-pydantic-logfire)Does this work with Pydantic Logfire?
Yes. [Logfire](https://pydantic.dev/logfire) supports cross-language observability through OpenTelemetry, which means you can trace requests across your entire application stack. Logfire gives you end-to-end visibility for debugging streaming issues, monitoring performance, and understanding how users interact with your application's AI features.
## Related content
[View all articles](https://pydantic.dev/articles)
[ /Pydantic AI Pydantic AI v1: A Predictable & Robust GenAI Framework ![Samuel Colvin](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://avatars.githubusercontent.com/u/4039449)Samuel Colvin 2025/09/04 ](https://pydantic.dev/articles/pydantic-ai-v1)[ /Company Introducing Pydantic’s New Brand Identity ![Laura Summers](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://avatars.githubusercontent.com/u/6570564)Laura Summers 2025/08/29 ](https://pydantic.dev/articles/pydantic-rebranding)
### Explore Logfire
[Get started Get started](https://pydantic.dev/contact)
