---
# Smart Librarian Export (v2.0)
- Page Number: 61
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://pydantic.dev/enterprise
- Page Title: Pydantic Enterprise Solutions
- Semantic Filename: pydantic_enterprise_solutions.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 2,889 characters
---

# Pydantic Enterprise Solutions

/enterprise
# Pydantic Logfire Enterprise Plans
Last updated: 2025/08/05
/contents
Enterprise Cloud Enterprise Self-Hosted A Look Under the Hood Get Started
  *   *   *   * 

Pydantic Logfire has two enterprise options, depending on how much control you want: 
  * **Enterprise Cloud** – Fully managed. SLA-backed. No infrastructure work.
  * **Enterprise Self-Hosted** – Run it yourself, in your own Kubernetes cluster. Same product, but with full data control.


* * *
## Enterprise Cloud
**For teams who want managed infra, advanced compliance, guaranteed uptime, and top-tier support**
### Good for:
  * Longer retention than the standard 30 days
  * SLA requirements
  * Custom DPAs, HIPAA BAAs
  * Invoice billing
  * Custom SSO (Okta, Azure Entra ID, etc.)


### Features
Feature | Description  
---|---  
Fully Hosted | We run everything in our cloud. Upgrading from SaaS Pro takes 5 mins, no migration required.  
24/7 Support | You get priority access and support  
Compliance & Billing | DPAs, BAAs, invoices, whatever your legal team needs.  
Custom Retention | Store data for longer. You choose how long.  
Custom SSO | Plug in your identity provider, Dex makes it work with almost anything.  
**SSO Note:**
We use 
* * *
## Enterprise Self-Hosted
**For teams who want full control over their data.**
### Good for:
  * Adhering to strict compliance or data residency requirements
  * Teams with Kubernetes know-how


### Features
Feature | Description  
---|---  
All Enterprise Features | Custom data retention & SSO are configurable, 24/7 support.  
Open-Source Helm Chart | You are free to explore the   
Uncomplicated Infrastructure | The only stateful services are Postgres and Object Storage. Use any S3-compatible backend. Managed Postgres (e.g. RDS) is fine.  
Scalability | The system is designed to autoscale.  
### Support Includes
  * Help getting set up
  * Advice for production best practices
  * Real engineers for troubleshooting
  * Optional health checks and performance tuning


* * *
## A Look Under the Hood
In addition to the open-source Helm chart, our [self-hosted documentation](https://logfire.pydantic.dev/docs/reference/self-hosted/overview/) contains recommended configurations, how-tos for running locally with Tilt and troubleshooting guides.
**Performance Bonus:**
We use Apache DataFusion, which is the 
**AI-Ready:**
You can query your data with SQL, no new query language to learn. This also means that your LLMs can easily help you (AI is very good at SQL), for example via our [Logfire MCP server.](https://logfire.pydantic.dev/docs/how-to-guides/mcp-server/#logfire-mcp-server)
**Open Standards:**
Everything's built on open standards (OTel, SQL, Parquet). Easy to extend, integrate, or migrate. No lock-in.
* * *
## Get Started
For more information contact: 
### Explore Logfire.
[Get started Get started](https://pydantic.dev/contact)
