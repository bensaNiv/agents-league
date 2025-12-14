---
# Smart Librarian Export (v2.0)
- Page Number: 2
- Timestamp: 2025-12-14T14:59:18.950805+02:00
- Source URL: https://docs.pydantic.dev/latest
- Page Title: Welcome to Pydantic - Pydantic Validation
- Semantic Filename: welcome_to_pydantic_pydantic_validation.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 12,302 characters
---

# Welcome to Pydantic - Pydantic Validation

[ Skip to content ](https://docs.pydantic.dev/latest/#pydantic-validation)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [Pydantic validations.](https://logfire.pydantic.dev/docs/integrations/pydantic/)
# Pydantic Validation[¶](https://docs.pydantic.dev/latest/#pydantic-validation)
  
  
[![llms.txt](https://img.shields.io/badge/llms.txt-green)](https://docs.pydantic.dev/latest/llms.txt)
Documentation for version: 
Pydantic is the most widely used data validation library for Python.
Fast and extensible, Pydantic plays nicely with your linters/IDE/brain. Define how data should be in pure, canonical Python 3.9+; validate it with Pydantic.
Monitor Pydantic with Pydantic Logfire ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/1f525.svg)
**[Pydantic Logfire](https://pydantic.dev/logfire)** is an application monitoring tool that is as simple to use and powerful as Pydantic itself.
Logfire integrates with many popular Python libraries including FastAPI, OpenAI and Pydantic itself, so you can use Logfire to monitor Pydantic validations and understand why some inputs fail validation:
Monitoring Pydantic with Logfire```
fromdatetimeimport datetime

importlogfire

frompydanticimport BaseModel

logfire.configure()
logfire.instrument_pydantic()  [](https://docs.pydantic.dev/latest/#__code_0_annotation_1)


classDelivery(BaseModel):
    timestamp: datetime
    dimensions: tuple[int, int]


# this will record details of a successful validation to logfire
m = Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '20'])
print(repr(m.timestamp))
#> datetime.datetime(2020, 1, 2, 3, 4, 5, tzinfo=TzInfo(UTC))
print(m.dimensions)
#> (10, 20)

Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10'])  [](https://docs.pydantic.dev/latest/#__code_0_annotation_2)

```

Would give you a view like this in the Logfire platform:
[![Logfire Pydantic Integration](https://docs.pydantic.dev/latest/img/logfire-pydantic-integration.png)](https://logfire.pydantic.dev/docs/guides/web-ui/live/)
This is just a toy example, but hopefully makes clear the potential value of instrumenting a more complex application.
**[Learn more about Pydantic Logfire](https://logfire.pydantic.dev/docs/)**
**Sign up for our newsletter,_The Pydantic Stack_ , with updates & tutorials on Pydantic, Logfire, and Pydantic AI:**
Subscribe
## Why use Pydantic?[¶](https://docs.pydantic.dev/latest/#why-use-pydantic)
  * **Powered by type hints** — with Pydantic, schema validation and serialization are controlled by type annotations; less to learn, less code to write, and integration with your IDE and static analysis tools. [Learn more…](https://docs.pydantic.dev/latest/why/#type-hints)
  * **Speed** — Pydantic's core validation logic is written in Rust. As a result, Pydantic is among the fastest data validation libraries for Python. [Learn more…](https://docs.pydantic.dev/latest/why/#performance)
  * **JSON Schema** — Pydantic models can emit JSON Schema, allowing for easy integration with other tools. [Learn more…](https://docs.pydantic.dev/latest/why/#json-schema)
  * **Strict** and **Lax** mode — Pydantic can run in either strict mode (where data is not converted) or lax mode where Pydantic tries to coerce data to the correct type where appropriate. [Learn more…](https://docs.pydantic.dev/latest/why/#strict-lax)
  * **Dataclasses** , **TypedDicts** and more — Pydantic supports validation of many standard library types including `dataclass` and `TypedDict`. [Learn more…](https://docs.pydantic.dev/latest/why/#dataclasses-typeddict-more)
  * **Customisation** — Pydantic allows custom validators and serializers to alter how data is processed in many powerful ways. [Learn more…](https://docs.pydantic.dev/latest/why/#customisation)
  * **Ecosystem** — around 8,000 packages on PyPI use Pydantic, including massively popular libraries like _FastAPI_ , _huggingface_ , _Django Ninja_ , _SQLModel_ , & _LangChain_. [Learn more…](https://docs.pydantic.dev/latest/why/#ecosystem)
  * **Battle tested** — Pydantic is downloaded over 360M times/month and is used by all FAANG companies and 20 of the 25 largest companies on NASDAQ. If you're trying to do something with Pydantic, someone else has probably already done it. [Learn more…](https://docs.pydantic.dev/latest/why/#using-pydantic)


[Installing Pydantic](https://docs.pydantic.dev/latest/install/) is as simple as: `pip install pydantic`
## Pydantic examples[¶](https://docs.pydantic.dev/latest/#pydantic-examples)
To see Pydantic at work, let's start with a simple example, creating a custom class that inherits from `BaseModel`:
Validation Successful```
fromdatetimeimport datetime

frompydanticimport BaseModel, PositiveInt


classUser(BaseModel):
    id: int  [](https://docs.pydantic.dev/latest/#__code_1_annotation_1)
    name: str = 'John Doe'  [](https://docs.pydantic.dev/latest/#__code_1_annotation_2)
    signup_ts: datetime | None  [](https://docs.pydantic.dev/latest/#__code_1_annotation_3)
    tastes: dict[str, PositiveInt]  [](https://docs.pydantic.dev/latest/#__code_1_annotation_4)


external_data = {
    'id': 123,
    'signup_ts': '2019-06-01 12:22',  [](https://docs.pydantic.dev/latest/#__code_1_annotation_5)
    'tastes': {
        'wine': 9,
        b'cheese': 7,  [](https://docs.pydantic.dev/latest/#__code_1_annotation_6)
        'cabbage': '1',  [](https://docs.pydantic.dev/latest/#__code_1_annotation_7)
    },
}

user = User(**external_data)  [](https://docs.pydantic.dev/latest/#__code_1_annotation_8)

print(user.id)  [](https://docs.pydantic.dev/latest/#__code_1_annotation_9)
#> 123
print(user.model_dump())  [](https://docs.pydantic.dev/latest/#__code_1_annotation_10)
"""
{
    'id': 123,
    'name': 'John Doe',
    'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
    'tastes': {'wine': 9, 'cheese': 7, 'cabbage': 1},
}
"""

```

If validation fails, Pydantic will raise an error with a breakdown of what was wrong:
Validation Error```
# continuing the above example...

fromdatetimeimport datetime
frompydanticimport BaseModel, PositiveInt, ValidationError


classUser(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime | None
    tastes: dict[str, PositiveInt]


external_data = {'id': 'not an int', 'tastes': {}}  [](https://docs.pydantic.dev/latest/#__code_2_annotation_1)

try:
    User(**external_data)  [](https://docs.pydantic.dev/latest/#__code_2_annotation_2)
except ValidationError as e:
    print(e.errors())
"""
    [
        {
            'type': 'int_parsing',
            'loc': ('id',),
            'msg': 'Input should be a valid integer, unable to parse string as an integer',
            'input': 'not an int',
            'url': 'https://errors.pydantic.dev/2/v/int_parsing',
        },
        {
            'type': 'missing',
            'loc': ('signup_ts',),
            'msg': 'Field required',
            'input': {'id': 'not an int', 'tastes': {}},
            'url': 'https://errors.pydantic.dev/2/v/missing',
        },
    ]
    """

```

## Who is using Pydantic?[¶](https://docs.pydantic.dev/latest/#who-is-using-pydantic)
Hundreds of organisations and packages are using Pydantic. Some of the prominent companies and organizations around the world who are using Pydantic include:
[ ![Adobe](https://docs.pydantic.dev/latest/logos/adobe_logo.png) ](https://docs.pydantic.dev/latest/why/#org-adobe)
[ ![Amazon and AWS](https://docs.pydantic.dev/latest/logos/amazon_logo.png) ](https://docs.pydantic.dev/latest/why/#org-amazon)
[ ![Anthropic](https://docs.pydantic.dev/latest/logos/anthropic_logo.png) ](https://docs.pydantic.dev/latest/why/#org-anthropic)
[ ![Apple](https://docs.pydantic.dev/latest/logos/apple_logo.png) ](https://docs.pydantic.dev/latest/why/#org-apple)
[ ![ASML](https://docs.pydantic.dev/latest/logos/asml_logo.png) ](https://docs.pydantic.dev/latest/why/#org-asml)
[ ![AstraZeneca](https://docs.pydantic.dev/latest/logos/astrazeneca_logo.png) ](https://docs.pydantic.dev/latest/why/#org-astrazeneca)
[ ![Cisco Systems](https://docs.pydantic.dev/latest/logos/cisco_logo.png) ](https://docs.pydantic.dev/latest/why/#org-cisco)
[ ![Comcast](https://docs.pydantic.dev/latest/logos/comcast_logo.png) ](https://docs.pydantic.dev/latest/why/#org-comcast)
[ ![Datadog](https://docs.pydantic.dev/latest/logos/datadog_logo.png) ](https://docs.pydantic.dev/latest/why/#org-datadog)
[ ![Facebook](https://docs.pydantic.dev/latest/logos/facebook_logo.png) ](https://docs.pydantic.dev/latest/why/#org-facebook)
[ ![GitHub](https://docs.pydantic.dev/latest/logos/github_logo.png) ](https://docs.pydantic.dev/latest/why/#org-github)
[ ![Google](https://docs.pydantic.dev/latest/logos/google_logo.png) ](https://docs.pydantic.dev/latest/why/#org-google)
[ ![HSBC](https://docs.pydantic.dev/latest/logos/hsbc_logo.png) ](https://docs.pydantic.dev/latest/why/#org-hsbc)
[ ![IBM](https://docs.pydantic.dev/latest/logos/ibm_logo.png) ](https://docs.pydantic.dev/latest/why/#org-ibm)
[ ![Intel](https://docs.pydantic.dev/latest/logos/intel_logo.png) ](https://docs.pydantic.dev/latest/why/#org-intel)
[ ![Intuit](https://docs.pydantic.dev/latest/logos/intuit_logo.png) ](https://docs.pydantic.dev/latest/why/#org-intuit)
[ ![Intergovernmental Panel on Climate Change](https://docs.pydantic.dev/latest/logos/ipcc_logo.png) ](https://docs.pydantic.dev/latest/why/#org-ipcc)
[ ![JPMorgan](https://docs.pydantic.dev/latest/logos/jpmorgan_logo.png) ](https://docs.pydantic.dev/latest/why/#org-jpmorgan)
[ ![Jupyter](https://docs.pydantic.dev/latest/logos/jupyter_logo.png) ](https://docs.pydantic.dev/latest/why/#org-jupyter)
[ ![Microsoft](https://docs.pydantic.dev/latest/logos/microsoft_logo.png) ](https://docs.pydantic.dev/latest/why/#org-microsoft)
[ ![Molecular Science Software Institute](https://docs.pydantic.dev/latest/logos/molssi_logo.png) ](https://docs.pydantic.dev/latest/why/#org-molssi)
[ ![NASA](https://docs.pydantic.dev/latest/logos/nasa_logo.png) ](https://docs.pydantic.dev/latest/why/#org-nasa)
[ ![Netflix](https://docs.pydantic.dev/latest/logos/netflix_logo.png) ](https://docs.pydantic.dev/latest/why/#org-netflix)
[ ![NSA](https://docs.pydantic.dev/latest/logos/nsa_logo.png) ](https://docs.pydantic.dev/latest/why/#org-nsa)
[ ![NVIDIA](https://docs.pydantic.dev/latest/logos/nvidia_logo.png) ](https://docs.pydantic.dev/latest/why/#org-nvidia)
[ ![OpenAI](https://docs.pydantic.dev/latest/logos/openai_logo.png) ](https://docs.pydantic.dev/latest/why/#org-openai)
[ ![Oracle](https://docs.pydantic.dev/latest/logos/oracle_logo.png) ](https://docs.pydantic.dev/latest/why/#org-oracle)
[ ![Palantir](https://docs.pydantic.dev/latest/logos/palantir_logo.png) ](https://docs.pydantic.dev/latest/why/#org-palantir)
[ ![Qualcomm](https://docs.pydantic.dev/latest/logos/qualcomm_logo.png) ](https://docs.pydantic.dev/latest/why/#org-qualcomm)
[ ![Red Hat](https://docs.pydantic.dev/latest/logos/redhat_logo.png) ](https://docs.pydantic.dev/latest/why/#org-redhat)
[ ![Revolut](https://docs.pydantic.dev/latest/logos/revolut_logo.png) ](https://docs.pydantic.dev/latest/why/#org-revolut)
[ ![Robusta](https://docs.pydantic.dev/latest/logos/robusta_logo.png) ](https://docs.pydantic.dev/latest/why/#org-robusta)
[ ![Salesforce](https://docs.pydantic.dev/latest/logos/salesforce_logo.png) ](https://docs.pydantic.dev/latest/why/#org-salesforce)
[ ![Starbucks](https://docs.pydantic.dev/latest/logos/starbucks_logo.png) ](https://docs.pydantic.dev/latest/why/#org-starbucks)
[ ![Texas Instruments](https://docs.pydantic.dev/latest/logos/ti_logo.png) ](https://docs.pydantic.dev/latest/why/#org-ti)
[ ![Twilio](https://docs.pydantic.dev/latest/logos/twilio_logo.png) ](https://docs.pydantic.dev/latest/why/#org-twilio)
[ ![Twitter](https://docs.pydantic.dev/latest/logos/twitter_logo.png) ](https://docs.pydantic.dev/latest/why/#org-twitter)
[ ![UK Home Office](https://docs.pydantic.dev/latest/logos/ukhomeoffice_logo.png) ](https://docs.pydantic.dev/latest/why/#org-ukhomeoffice)
For a more comprehensive list of open-source projects using Pydantic see the 
Was this page helpful? 
Thanks for your feedback! 
Thanks for your feedback! 
