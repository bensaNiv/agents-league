---
# Smart Librarian Export (v2.0)
- Page Number: 59
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/guides/integration/coiled
- Page Title: Using uv with Coiled | uv
- Semantic Filename: using_uv_with_coiled_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 6,693 characters
---

# Using uv with Coiled | uv

[ Skip to content ](https://docs.astral.sh/uv/guides/integration/coiled/#using-uv-with-coiled)
# [Using uv with Coiled](https://docs.astral.sh/uv/guides/integration/coiled/#using-uv-with-coiled)
This guide shows how to run Python scripts on the cloud using uv for dependency management and Coiled for cloud deployment.
## [Managing script dependencies with uv](https://docs.astral.sh/uv/guides/integration/coiled/#managing-script-dependencies-with-uv)
Note
We'll use this concrete example throughout this guide, but any Python script can be used with uv and Coiled.
We'll use the following script as an example:
process.py```
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-0-1)# /// script
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-0-2)# requires-python = ">=3.12"
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-0-3)# dependencies = [
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-0-4)#   "pandas",
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-0-5)#   "pyarrow",
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-0-6)#   "s3fs",
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-0-7)# ]
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-0-8)# ///
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-0-9)
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-0-10)import pandas as pd
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-0-11)
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-0-12)df = pd.read_parquet(
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-0-13)    "s3://coiled-data/uber/part.0.parquet",
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-0-14)    storage_options={"anon": True},
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-0-15))
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-0-16)print(df.head())

```

The script uses 
When running this script locally, e.g., with:
```
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-1-1)$
```

uv will automatically create a virtual environment and installs its dependencies.
To learn more about using inline script metadata with uv, see the [script guide](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies).
## [Running scripts on the cloud with Coiled](https://docs.astral.sh/uv/guides/integration/coiled/#running-scripts-on-the-cloud-with-coiled)
Using inline script metadata makes the script fully self-contained: it includes the information that is needed to run it. This makes it easier to run on other machines, like a machine in the cloud.
There are many use cases where resources beyond what's available on a local workstation are needed, e.g.:
  * Processing large amounts of cloud-hosted data
  * Needing accelerated hardware like GPUs or a big machine with more memory
  * Running the same script with hundreds or thousands of different inputs, in parallel


Coiled makes it simple to run code on cloud hardware.
First, authenticate with Coiled using 
```
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-2-1)$
```

You'll be prompted to create a Coiled account if you don't already have one — it's free to start using Coiled.
To instruct Coiled to run the script on a virtual machine on AWS, add two comments to the top:
process.py```
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-1)# COILED container ghcr.io/astral-sh/uv:debian-slim
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-2)# COILED region us-east-2
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-3)
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-4)# /// script
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-5)# requires-python = ">=3.12"
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-6)# dependencies = [
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-7)#   "pandas",
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-8)#   "pyarrow",
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-9)#   "s3fs",
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-10)# ]
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-11)# ///
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-12)
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-13)import pandas as pd
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-14)
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-15)df = pd.read_parquet(
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-16)    "s3://coiled-data/uber/part.0.parquet",
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-17)    storage_options={"anon": True},
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-18))
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-3-19)print(df.head())

```

Tip
While Coiled supports AWS, GCP, and Azure, this example assumes AWS is being used (see the `region` option above). If you're new to Coiled, you'll automatically have access to a free account running on AWS. If you're not running on AWS, you can either use a valid `region` for your cloud provider or remove the `region` line above.
The comments tell Coiled to use the official [uv Docker image](https://docs.astral.sh/uv/guides/integration/docker/) when running the script (ensuring uv is available) and to run in the `us-east-2` region on AWS (where this example data file happens to live) to avoid any data egress.
To submit a batch job for Coiled to run, use `uv run` command in the cloud:
```
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-4-1)$\
[](https://docs.astral.sh/uv/guides/integration/coiled/#__codelineno-4-2)
```

The same process that previously ran locally is now running on a remote cloud VM on AWS.
You can monitor the progress of the batch job in the UI at `coiled batch status`, `coiled batch wait`, and `coiled batch logs` commands.
![Coiled UI](https://docs.coiled.io/_images/uv-coiled.png)
Note there's additional configuration we could have specified, e.g., the instance type (the default is a 4-core virtual machine with 16 GiB of memory), disk size, whether to use spot instance, and more. See the 
For more details on Coiled, and how it can help with other use cases, see the 
September 12, 2025
