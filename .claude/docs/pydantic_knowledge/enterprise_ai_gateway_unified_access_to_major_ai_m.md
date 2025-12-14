---
# Smart Librarian Export (v2.0)
- Page Number: 67
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://pydantic.dev/ai-gateway
- Page Title: Enterprise AI Gateway: Unified Access to Major AI Models
- Semantic Filename: enterprise_ai_gateway_unified_access_to_major_ai_m.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 8,433 characters
---

# Enterprise AI Gateway: Unified Access to Major AI Models

# Pydantic AI Gateway
![Pydantic AI Gateway](https://pydantic.dev/cdn-cgi/image/width=828,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/ai-gateway.svg)BETA
## Introducing enterprise-ready AI model routing (that developers love)
One key for all your models with real-time monitoring and budget control that works.
[Try it now Try it now](https://gateway.pydantic.dev)
[Visit docs](https://ai.pydantic.dev/gateway)
No credit card required
![AI Gateway Diagram](https://pydantic.dev/cdn-cgi/image/width=3840,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/diagram.svg)![AI Gateway Diagram](https://pydantic.dev/cdn-cgi/image/width=828,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/diagram-mobile.svg)
## Intelligent AI Workflows without the middleware bloat
Start with a few lines of code
```
from pydantic_ai import Agent

agent = Agent(
    'gateway/openai:gpt-5',
    instructions='Be concise, reply with one sentence.'
)

result = agent.run_sync('Hello World')
print(result.output)

```

You can access multiple models with the same API key.
To use different models, change the model string `gateway/<api_format>:<model_name>` to other models offered by the supported providers.
## Available Providers
Provider | Available? | Built-in? |  BYOK?Bring Your Own Key | Model families provided  
---|---|---|---|---  
![Anthropic](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/anthropic.svg)Anthropic | Yes | Yes | Yes | Claude  
![AWS Bedrock](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/bedrock.svg)AWS Bedrock | Yes | Yes | Yes | Nova, Claude, etc...  
![Google Vertex](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/vertex.svg)Google Vertex | Yes | Yes | Yes | Gemini, Claude  
![Groq](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/groq.svg)Groq | Yes | Yes | Yes | Open Source models  
![OpenAI](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/openai.svg)OpenAI | Yes | Yes | Yes | GPT  
![Chat & Responses](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/chat.svg)Chat & Responses | Yes | No | Yes | Any compatible provider  
![Azure](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/azure.svg)Azure | Soon... | No | Yes | GPT  
Provider
Model families
![Anthropic](https://pydantic.dev/cdn-cgi/image/width=48,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/anthropic.svg)Anthropic
Available: Yes
Build-in: Yes
BYOK: Yes
Claude
![AWS Bedrock](https://pydantic.dev/cdn-cgi/image/width=48,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/bedrock.svg)AWS Bedrock
Available: Yes
Build-in: Yes
BYOK: Yes
Nova, Claude, etc...
![Google Vertex](https://pydantic.dev/cdn-cgi/image/width=48,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/vertex.svg)Google Vertex
Available: Yes
Build-in: Yes
BYOK: Yes
Gemini, Claude
![Groq](https://pydantic.dev/cdn-cgi/image/width=48,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/groq.svg)Groq
Available: Yes
Build-in: Yes
BYOK: Yes
Open Source models
![OpenAI](https://pydantic.dev/cdn-cgi/image/width=48,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/openai.svg)OpenAI
Available: Yes
Build-in: Yes
BYOK: Yes
GPT
![Chat & Responses](https://pydantic.dev/cdn-cgi/image/width=48,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/chat.svg)Chat & Responses
Available: Yes
Build-in: No
BYOK: Yes
Any compatible provider
![Azure](https://pydantic.dev/cdn-cgi/image/width=48,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/azure.svg)Azure
Available: Soon...
Build-in: No
BYOK: Yes
GPT
Cost control for AI Models, Native APIs underneath
## What is the Pydantic AI Gateway?
Pydantic AI Gateway gives you cost control and intelligent routing without the abstraction overhead. Unlike traditional AI gateways that wrap providers in a universal schema, PAIG passes requests through in their native format. When providers like OpenAI, Anthropic, or Google ship new features, you can use them immediately.
The core is open source (AGPL-3.0) with a cloud dashboard (SaaS), or self-host for enterprise. Start with BYOK or use our built-in providers for single-key access to all models. PAIG comes with smart routing defaults you can fully customize. Use with Pydantic AI for one-line integration or point any existing provider SDK at the gateway, your code stays the same.
![Pydantic AI Gateway](https://pydantic.dev/cdn-cgi/image/width=384,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/ai-gateway.svg)
  * [Dashboard](https://gateway.pydantic.dev/admin)
  * [Users](https://gateway.pydantic.dev/admin/users)
  * [Keys](https://pydantic.dev/admin/keys)
  * [Providers](https://gateway.pydantic.dev/admin/providers)
  * [Projects](https://gateway.pydantic.dev/admin/projects)
  * [Settings](https://gateway.pydantic.dev/admin/settings)


U
UserUser's Org
## Users
[View all](https://gateway.pydantic.dev/admin/users)
1 user
U
## Projects
[View all](https://gateway.pydantic.dev/admin/projects)
3 projects
### Default Project
1 member
+ 2 more projects
![AI Gateway](https://pydantic.dev/cdn-cgi/image/width=384,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/ai-gateway.svg)
Unified access to LLM providers
OpenAI
Anthropic
Google Vertex
AWS Bedrock
Groq
### One key for every model
One API key to access multiple providers - OpenAI, Anthropic, Google, etc
### Enterprise Ready
SSO, granular permissions, and self-hosting options
### Cost Control
Set spending limits per user, project, or API key
### Pydantic Integration
Built-in Pydantic AI support with Logfire observability
## API Keys
[View all](https://gateway.pydantic.dev/admin/keys)
5 keys
Top keys by usage
key_vuc...4E
key_Gnk...03
key_Q1Q...Mr
## Providers
[View all](https://gateway.pydantic.dev/admin/providers)
8 providers
OpenAIAnthropicGoogle AI
[+ 5 more providers](https://gateway.pydantic.dev/admin/providers)
## Why use Pydantic AI Gateway?
![One API, every model](https://pydantic.dev/cdn-cgi/image/width=96,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/one-api.svg)
### One key, multiple models
Connect to models on OpenAI, Anthropic, Google, Groq, and AWS Bedrock with one API key. Access multiple providers instantly without swapping credentials.
![Spend control that actually works](https://pydantic.dev/cdn-cgi/image/width=96,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/spend-control.svg)
### Flexible spend control
Set limits on your terms. Choose your level of control: project, user, or API key. Pick your timeframe: daily, weekly, monthly, or total.
![Zero translation, full speed requests](https://pydantic.dev/cdn-cgi/image/width=96,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/zero-translation.svg)
### No schema translation
Requests flow in each provider's native format. New model features are accessible as soon as they are released by providers.
![Complete visibility](https://pydantic.dev/cdn-cgi/image/width=96,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/complete-visibility.svg)
### Send OpenTelemetry traces for full visibility
Log every request through [Pydantic Logfire](https://pydantic.dev/logfire) or any OTel backend. Create a centralized audit trail where no API usage can hide.
![Your deployment, your choice ](https://pydantic.dev/cdn-cgi/image/width=96,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/self-hosting.svg)
### Self-hosting available immediately
Deploy to your Cloudflare account, or run on-premises with our
![Enterprise without the wait](https://pydantic.dev/cdn-cgi/image/width=96,quality=75,format=auto/https://pydantic.dev/assets/ai-gateway/enterprise.svg)
### Enterprise without the wait
SSO with OIDC, granular permissions, and flexible deployment—ready now (not a roadmap promise).
[Try it now Try it now](https://gateway.pydantic.dev)
[Visit docs](https://ai.pydantic.dev/gateway)
No credit card required
## Free while in Beta
Zero margin on built-in provider inference (we’ll eat the card fee for now)
Full pricing coming soon
