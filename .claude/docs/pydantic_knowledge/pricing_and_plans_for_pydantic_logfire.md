---
# Smart Librarian Export (v2.0)
- Page Number: 29
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://pydantic.dev/pricing
- Page Title: Pricing and Plans for Pydantic Logfire
- Semantic Filename: pricing_and_plans_for_pydantic_logfire.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 4,437 characters
---

# Pricing and Plans for Pydantic Logfire

# Simple, scalable pricing
## Free
$0
  * 10 million free spans/metrics per month
  * Free indefinitely
  * Upgrade any time


## Pro
$2/million
  * 10 million free spans/metrics per month
  * $2 USD per million after that
  * Downgrade any time
  * Scale to zero


## Cloud Enterprise
contact sales
  * 100 million spans/metrics per month included
  * $1 per million spans/metrics thereafter
  * Extended retention available
  * Dedicated Slack channel
  * Invoiced billing
  * SSO (e.g. Okta)
  * SLA & custom BAA
  * Unlimited orgs, projects, users, seats


## Self-hosted Enterprise
contact sales
  * 100 million spans/metrics per month included
  * $1 per million spans/metrics thereafter
  * Discounts available for high volume
  * Retention configurable
  * Dedicated Slack channel
  * Invoiced billing, SLA, BAA
  * 1 year contract required
  * Unlimited orgs, projects, users, seats


[Get Started](https://pydantic.dev/contact)
## Enterprise & self-hosting
[Get in touch for pricing](https://pydantic.dev/contact)
### Account details
![icon](https://pydantic.dev/cdn-cgi/image/width=128,quality=75,format=auto/https://pydantic.dev/assets/pricing/check.svg)
**Unlimited Organisations, Projects and Seats.** Within reason — please don't spam our APIs.
![icon](https://pydantic.dev/cdn-cgi/image/width=128,quality=75,format=auto/https://pydantic.dev/assets/pricing/check.svg)
**One month data retention.** We offer extended retention options for [enterprise customers](https://logfire.pydantic.dev/docs/enterprise/).
![icon](https://pydantic.dev/cdn-cgi/image/width=128,quality=75,format=auto/https://pydantic.dev/assets/pricing/check.svg)
**Generous 5KB allocation.** Logfire allocates 5KB (5120 bytes) per span or metric, averaged across your use over time. We will contact you if frequently exceeded. (Spans/metrics are normally <1KB).
![icon](https://pydantic.dev/cdn-cgi/image/width=128,quality=75,format=auto/https://pydantic.dev/assets/pricing/check.svg)
**No card required to get started.** Sign up and start logging your data — it's up to you to upgrade when you're ready.
![icon](https://pydantic.dev/cdn-cgi/image/width=128,quality=75,format=auto/https://pydantic.dev/assets/pricing/check.svg)
**No hidden fees.** Don't get stung with unexpected charges, like a fee-per-host. We only meter based on how much data you send to us.
## Cost calculator
Spans sent to Logfire
M
Metrics sent to Logfire
M
Price
$2/M
Total
30M
Free allowance
- 10M
Payable
= 20M
Total you will pay:
$2/M x 20M
$40
[Get Started Get Started](https://pydantic.dev/contact)
### FAQ
### What is a Span?
A span is the building block of a trace — a single row in our live view. To give an example of how you might conceive of a span, image you were measuring how many birds cross a specific river. If you instrumented one border of the river with a counter, you would receive one span back for every time this sensor was triggered.
### What is a Metric?
A metric is a single data point, sometimes called a "sample" or "metric recording". To complete the analogy from above, in order to measure a metric related to birds crossing a river, imagine this time you measured bird altitude using a gauge metric. In this version, your gauge metric would tell you the number of birds at different altitudes in proximity to the river, and from here you could extrapolate crossings.
### What happens if I use more than the free allowance?
On the Free plan, we'll send you emails and in-app alerts on your level of use. If you go well over the free allowance, we'll eventually stop storing new data, your application won't be affected. You might see warnings in stdout/stderr about 4XX responses from the Logfire API.
### Can I use the free tier in production?
Yes! The free tier is designed for you to test Logfire or use it with side projects. You can safely use it in production if you don't mind losing data when you exceed the free allowance.
### How long is my data stored in Logfire?
One month data retention. We offer extended retention options for [enterprise customers](https://logfire.pydantic.dev/docs/enterprise/).
### Will Pydantic remain free?
The Pydantic Library is (always has been, always will be) completely free and permissively licensed under the MIT license. Prices displayed on this page apply to Pydantic Logfire, only.
### Understand your code like never before
[Get started Get started](https://pydantic.dev/contact)pip install logfire
