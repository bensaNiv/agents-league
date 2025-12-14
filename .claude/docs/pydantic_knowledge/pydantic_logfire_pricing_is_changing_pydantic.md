---
# Smart Librarian Export (v2.0)
- Page Number: 21
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://pydantic.dev/articles/logfire-pricing-change
- Page Title: Pydantic Logfire Pricing is Changing | Pydantic
- Semantic Filename: pydantic_logfire_pricing_is_changing_pydantic.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 8,319 characters
---

# Pydantic Logfire Pricing is Changing | Pydantic

/Logfire
# Pydantic Logfire Pricing is Changing
![Samuel Colvin avatar](https://pydantic.dev/cdn-cgi/image/width=96,quality=75,format=auto/https://avatars.githubusercontent.com/u/4039449)
Samuel Colvin
5 mins
2025/12/08
_Mea culpa:_ Logfire has been ludicrously cheap, we're putting our pricing up for some customers.
**We're changing Logfire's pricing structure, starting January 1, 2026.**
We're seeing teams use Logfire to run large-scale production workloads entirely on the free tier. While we love the fact people are finding it useful, that's a sign our pricing hasn't kept up with changes in how people use the platform.
We want to build a long-term business that can keep improving Logfire (as well as our open source: [Pydantic](https://pydantic.dev/), [Pydantic AI](https://ai.pydantic.dev/), 
##  [#](https://pydantic.dev/articles/logfire-pricing-change#the-good-news)The Good News
Our existing $2/million spans price is not changing.
The Personal plan remains free, and it's still extremely generous:
  * **10 million logs/spans/metrics per month included**
  * 1 seat, 3 projects, 2 guests (read-only)
  * 30 days retention


If you're building a side project or an early stage company, you won't pay a dime.
To put the included records in perspective: 10 million spans would represent ~$100,000 of LLM spend at $0.01 per request. Most individual developers will never hit this cap. If you do hit the limit on the Personal plan, we'll continue to store your data in case you want to upgrade.
Existing [enterprise cloud and enterprise self-hosted](https://pydantic.dev/enterprise) customers are also unaffected by this price change.
##  [#](https://pydantic.dev/articles/logfire-pricing-change#the-new-structure)The New Structure
For teams and growing companies, we are standardizing on three main tiers. Here is the breakdown:
Feature | Personal | Team | Growth  
---|---|---|---  
**Base Cost** | **$0/mo** | **$49/mo** | **$249/mo**  
**Included Usage** | 10M records/metrics* | 10M records/metrics* | 10M records/metrics*  
**Overage Rate** | NA | $2 / million records/metrics | $2 / million records/metrics  
**Seats** | 1 | 5 | Unlimited  
**Projects** | 3 | 5 | Unlimited  
**Guests (read-only)** | 2 | 10 | Unlimited  
*Records include spans, logs, and metrics. Learn more in [our docs](https://logfire.pydantic.dev/docs/concepts/#concepts).
###  [#](https://pydantic.dev/articles/logfire-pricing-change#key-details)Key Details
  * **Team Plan ($49/mo):** Designed for startups and small teams shipping to production. It includes **5 seats** and **5 projects** , plus **up to 10 project guests**.
  * **Growth Plan ($249/mo):** For scaling teams who need room to move. It removes the caps, offering **unlimited seats** and **unlimited projects** , plus priority support and self-service data deletion.
  * **Overage:** On paid plans (Team and Growth), if you exceed the included 10 million records, you pay **$2 per million additional records**. You can set a **price cap** to ensure you never go over budget.
  * **Enterprise:** If you need self-hosted options, SSO, custom retention, SLA, or are interested in high volume discounts, [get in touch](https://pydantic.dev/contact) and 


Every paid plan includes a price cap, so you can set a ceiling on your spend and never be surprised.
##  [#](https://pydantic.dev/articles/logfire-pricing-change#why)Why
We built Logfire because existing observability tools were painful, slow, didn't follow open standards, and didn't understand Python or AI. We believe we've built something significantly better: the only platform that properly combines general-purpose monitoring with LLM observability.
We treat pricing changes with gravity. This is the first adjustment we have made since Logfire went General Availability (GA) in October 2024. Since then, adoption has grown - in the last month alone, close to 5000 organizations sent data to Logfire. However, as the platform has matured, the way teams extract value from it has evolved.
Specifically, AI workloads have fundamentally changed the "volume equals value" equation. A traditional high-traffic web server might emit millions of logs to help you catch a single bug. In contrast, an AI application might emit far fewer spans, but each trace carries a lot of value, capturing complex prompt flows, offline evaluation results, and direct cost tracking.
Because of this efficiency, we are seeing sophisticated production AI systems running entirely on our free tier. While we are proud to offer a generous entry point, this creates a misalignment. When a platform delivers enterprise-grade infrastructure but is priced like a hobbyist tool, it sends a confusing signal to organizations looking for a long-term partner.
We are updating our structure to reflect the reality of what Logfire is today: a critical component of the production stack. This change ensures we are building a commercially viable business that can continue to support your future growth.
##  [#](https://pydantic.dev/articles/logfire-pricing-change#if-youre-on-the-current-free-plan)If you're on the current Free plan
If your usage fits within the new Personal limits: 1 seat, 3 projects, nothing changes. You're already set.
If you're over those limits, you have until February 1, 2026 to decide: consolidate down to fit within the Personal plan, or upgrade to either the Team or Growth plan.
##  [#](https://pydantic.dev/articles/logfire-pricing-change#if-youre-on-the-current-pro-plan)If you're on the current Pro plan
First: thank you. You took a bet on us early, and that trust means a lot.
We'll email you in January with an estimate of what you will pay and ask you to choose a plan. On February 1st, users sending us data on a paid plan who haven't selected a plan will be upgraded to Team or Growth based on their usage (we will send plenty of email notifications about this).
Although the new pricing goes live on January 1, 2026, you have a grace period until February 1, 2026 to adjust. If the new pricing doesn't work for you, [reach out](https://pydantic.dev/contact). We want to find a solution and are receptive to feedback.
##  [#](https://pydantic.dev/articles/logfire-pricing-change#still-generous-just-not-absurd)Still generous, just not absurd
We're not trying to extract maximum revenue from our users. We're trying to build a viable business that can keep improving Logfire for the years ahead.
Our free tier is still more comprehensive than most competitors. $2/million spans is still **orders of magnitude better value** than any other AI observability company on the market. We don't want to name and shame here, but if you do the math it is clear. Our paid tiers are still competitively priced. We're just moving from "ludicrously cheap" to "very good value."
If you're a student, work at a non-profit, or maintain open source software, we offer discounts, just ask. Same goes for early-stage startups who need a bit more runway. [Get in touch](https://pydantic.dev/contact) and we'll sort something out.
##  [#](https://pydantic.dev/articles/logfire-pricing-change#questions)Questions?
The new pricing takes effect January 1, 2026. The grace period for existing users runs until February 1, 2026.
If you have questions or concerns email us at 
— Samuel
P.S. We've got a packed roadmap for 2026, especially for LLM observability: annotations, annotation queues, prompt management, and some things we're not ready to talk about yet. Watch this space. Follow us on [social media](https://pydantic.dev/links?utm_source=blog) and join our [Slack community](https://logfire.pydantic.dev/docs/join-slack/) to stay in the loop.
## Related content
[View all articles](https://pydantic.dev/articles)
[ /Open Source Pydantic joins the Agentic AI Foundation ![Laís Carvalho](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://avatars.githubusercontent.com/u/42092770)Laís Carvalho 2025/12/09 ](https://pydantic.dev/articles/pydantic_agentic_ai)[ /PydanticAI Announcement: Pydantic AI Gateway Open Beta ![Samuel Colvin](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://avatars.githubusercontent.com/u/4039449)Samuel Colvin 2025/11/13 ](https://pydantic.dev/articles/gateway-open-beta)
### Explore Logfire
[Get started Get started](https://pydantic.dev/contact)
