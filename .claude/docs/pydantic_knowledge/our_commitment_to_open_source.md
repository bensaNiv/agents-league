---
# Smart Librarian Export (v2.0)
- Page Number: 66
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://pydantic.dev/opensource
- Page Title: Our Commitment to Open Source
- Semantic Filename: our_commitment_to_open_source.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 2,005 characters
---

# Our Commitment to Open Source

# /opensource
##  Powering the Python community
Our open source packages are built for the Python and Rust community and MIT licensed — and will remain so, forever.
[](https://logfire.pydantic.dev/docs/join-slack/)
pydantic
### The default data validation library for Python
```
from datetime import datetime
from typing import Tuple

from pydantic import BaseModel

class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]

m = Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '20'])
print(repr(m.timestamp))
#> datetime.datetime(2020, 1, 2, 3, 4, 5, tzinfo=TzInfo(UTC))
print(m.dimensions)
#> (10, 20)
```

**Pydantic is the most widely used data validation library,** downloaded millions of times a day by thousands of developers all over the world.
**Pydantic's success stems from its great developer experience. **It's simple to use, even when doing complex things.
[ /Open Source Pydantic joins the Agentic AI Foundation ![Laís Carvalho](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://avatars.githubusercontent.com/u/42092770)Laís Carvalho 2025/12/09 ](https://pydantic.dev/articles/pydantic_agentic_ai)[ /Logfire Pydantic Logfire Pricing is Changing ![Samuel Colvin](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://avatars.githubusercontent.com/u/4039449)Samuel Colvin 2025/12/08 ](https://pydantic.dev/articles/logfire-pricing-change)[ /PydanticAI Announcement: Pydantic AI Gateway Open Beta ![Samuel Colvin](https://pydantic.dev/cdn-cgi/image/width=64,quality=75,format=auto/https://avatars.githubusercontent.com/u/4039449)Samuel Colvin 2025/11/13 ](https://pydantic.dev/articles/gateway-open-beta)
## The Pydantic Open Source Fund
For too long the open source ecosystem has been taken for granted. We're proud to be part of the movement to change that. More about the Pydantic [Open Source fund initiative.](https://pydantic.dev/articles/pydantic-oss-fund-2025)
Pydantic is proud to be a member of the
