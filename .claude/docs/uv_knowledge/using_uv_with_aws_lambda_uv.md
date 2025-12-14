---
# Smart Librarian Export (v2.0)
- Page Number: 46
- Timestamp: 2025-12-11T15:43:20.114410+02:00
- Source URL: https://docs.astral.sh/uv/guides/integration/aws-lambda
- Page Title: Using uv with AWS Lambda | uv
- Semantic Filename: using_uv_with_aws_lambda_uv.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 39,104 characters
---

# Using uv with AWS Lambda | uv

[ Skip to content ](https://docs.astral.sh/uv/guides/integration/aws-lambda/#using-uv-with-aws-lambda)
# [Using uv with AWS Lambda](https://docs.astral.sh/uv/guides/integration/aws-lambda/#using-uv-with-aws-lambda)
You can use uv with AWS Lambda to manage your Python dependencies, build your deployment package, and deploy your Lambda functions.
Tip
Check out the 
## [Getting started](https://docs.astral.sh/uv/guides/integration/aws-lambda/#getting-started)
To start, assume we have a minimal FastAPI application with the following structure:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-0-1)project
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-0-2)├── pyproject.toml
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-0-3)└── app
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-0-4)    ├── __init__.py
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-0-5)    └── main.py

```

Where the `pyproject.toml` contains:
pyproject.toml```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-1-1)[project]
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-1-2)name="uv-aws-lambda-example"
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-1-3)version="0.1.0"
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-1-4)requires-python=">=3.13"
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-1-5)dependencies=[
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-1-6)# FastAPI is a modern web framework for building APIs with Python.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-1-7)"fastapi",
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-1-8)# Mangum is a library that adapts ASGI applications to AWS Lambda and API Gateway.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-1-9)"mangum",
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-1-10)]
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-1-11)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-1-12)[dependency-groups]
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-1-13)dev=[
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-1-14)# In development mode, include the FastAPI development server.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-1-15)"fastapi[standard]>=0.115",
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-1-16)]

```

And the `main.py` file contains:
app/main.py```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-2-1)import logging
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-2-2)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-2-3)from fastapi import FastAPI
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-2-4)from mangum import Mangum
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-2-5)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-2-6)logger = logging.getLogger()
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-2-7)logger.setLevel(logging.INFO)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-2-8)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-2-9)app = FastAPI()
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-2-10)handler = Mangum(app)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-2-11)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-2-12)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-2-13)@app.get("/")
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-2-14)async def root() -> str:
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-2-15)    return "Hello, world!"

```

We can run this application locally with:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-3-1)$ uv
```

From there, opening 
## [Deploying a Docker image](https://docs.astral.sh/uv/guides/integration/aws-lambda/#deploying-a-docker-image)
To deploy to AWS Lambda, we need to build a container image that includes the application code and dependencies in a single output directory.
We'll follow the principles outlined in the [Docker guide](https://docs.astral.sh/uv/guides/integration/docker/) (in particular, a multi-stage build) to ensure that the final image is as small and cache-friendly as possible.
In the first stage, we'll populate a single directory with all application code and dependencies. In the second stage, we'll copy this directory over to the final image, omitting the build tools and other unnecessary files.
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-1)FROMghcr.io/astral-sh/uv:0.9.17ASuv
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-2)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-3)# First, bundle the dependencies into the task root.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-4)FROMpublic.ecr.aws/lambda/python:3.13ASbuilder
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-5)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-6)# Enable bytecode compilation, to improve cold-start performance.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-7)ENVUV_COMPILE_BYTECODE=1
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-8)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-9)# Disable installer metadata, to create a deterministic layer.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-10)ENVUV_NO_INSTALLER_METADATA=1
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-11)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-12)# Enable copy mode to support bind mount caching.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-13)ENVUV_LINK_MODE=copy
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-14)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-15)# Bundle the dependencies into the Lambda task root via `uv pip install --target`.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-16)#
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-17)# Omit any local packages (`--no-emit-workspace`) and development dependencies (`--no-dev`).
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-18)# This ensures that the Docker layer cache is only invalidated when the `pyproject.toml` or `uv.lock`
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-19)# files change, but remains robust to changes in the application code.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-20)RUN=from=uv,source=/uv,target=/bin/uv\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-21)=type=cache,target=/root/.cache/uv\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-22)=type=bind,source=uv.lock,target=uv.lock\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-23)=type=bind,source=pyproject.toml,target=pyproject.toml\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-24)export&&\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-25)"${LAMBDA_TASK_ROOT}"
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-26)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-27)FROMpublic.ecr.aws/lambda/python:3.13
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-28)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-29)# Copy the runtime dependencies from the builder stage.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-30)COPY=builder${LAMBDA_TASK_ROOT}${LAMBDA_TASK_ROOT}
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-31)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-32)# Copy the application code.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-33)COPY${LAMBDA_TASK_ROOT}/app
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-34)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-35)# Set the AWS Lambda handler.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-4-36)CMD["app.main.handler"]

```

Tip
To deploy to ARM-based AWS Lambda runtimes, replace `public.ecr.aws/lambda/python:3.13` with `public.ecr.aws/lambda/python:3.13-arm64`.
We can build the image with, e.g.:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-5-1)$ uv[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-5-2)$ docker
```

The core benefits of this Dockerfile structure are as follows:
  1. **Minimal image size.** By using a multi-stage build, we can ensure that the final image only includes the application code and dependencies. For example, the uv binary itself is not included in the final image.
  2. **Maximal cache reuse.** By installing application dependencies separately from the application code, we can ensure that the Docker layer cache is only invalidated when the dependencies change.


Concretely, rebuilding the image after modifying the application source code can reuse the cached layers, resulting in millisecond builds:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-6-1) => [internal] load build definition from Dockerfile                                                                 0.0s
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-6-2) => => transferring dockerfile: 1.31kB                                                                               0.0s
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-6-3) => [internal] load metadata for public.ecr.aws/lambda/python:3.13                                                   0.3s
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-6-4) => [internal] load metadata for ghcr.io/astral-sh/uv:latest                                                         0.3s
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-6-5) => [internal] load .dockerignore                                                                                    0.0s
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-6-6) => => transferring context: 106B                                                                                    0.0s
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-6-7) => [uv 1/1] FROM ghcr.io/astral-sh/uv:latest@sha256:ea61e006cfec0e8d81fae901ad703e09d2c6cf1aa58abcb6507d124b50286f  0.0s
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-6-8) => [builder 1/2] FROM public.ecr.aws/lambda/python:3.13@sha256:f5b51b377b80bd303fe8055084e2763336ea8920d12955b23ef  0.0s
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-6-9) => [internal] load build context                                                                                    0.0s
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-6-10) => => transferring context: 185B                                                                                    0.0s
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-6-11) => CACHED [builder 2/2] RUN --mount=from=uv,source=/uv,target=/bin/uv     --mount=type=cache,target=/root/.cache/u  0.0s
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-6-12) => CACHED [stage-2 2/3] COPY --from=builder /var/task /var/task                                                     0.0s
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-6-13) => CACHED [stage-2 3/3] COPY ./app /var/task                                                                        0.0s
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-6-14) => exporting to image                                                                                               0.0s
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-6-15) => => exporting layers                                                                                              0.0s
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-6-16) => => writing image sha256:6f8f9ef715a7cda466b677a9df4046ebbb90c8e88595242ade3b4771f547652d                         0.0

```

After building, we can push the image to 
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-7-1)$ aws|[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-7-2)$ docker[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-7-3)$ docker
```

Finally, we can deploy the image to AWS Lambda using the AWS Management Console or the AWS CLI, e.g.:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-8-1)$ aws\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-8-2)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-8-3)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-8-4)ImageUri=aws_account_id.dkr.ecr.region.amazonaws.com/fastapi-app:latest\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-8-5)
```

Where the 
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-9-1)$ aws\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-9-2)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-9-3)'{"Version": "2012-10-17", "Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'

```

Or, update an existing function with:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-10-1)$ aws\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-10-2)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-10-3)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-10-4)
```

To test the Lambda, we can invoke it via the AWS Management Console or the AWS CLI, e.g.:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-11-1)$ aws\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-11-2)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-11-3)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-11-4)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-11-5)[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-11-6){
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-11-7)  "StatusCode": 200,
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-11-8)  "ExecutedVersion": "$LATEST"
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-11-9)}

```

Where `event.json` contains the event payload to pass to the Lambda function:
event.json```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-12-1){
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-12-2)"httpMethod":"GET",
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-12-3)"path":"/",
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-12-4)"requestContext":{},
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-12-5)"version":"1.0"
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-12-6)}

```

And `response.json` contains the response from the Lambda function:
response.json```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-13-1){
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-13-2)"statusCode":200,
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-13-3)"headers":{
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-13-4)"content-length":"14",
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-13-5)"content-type":"application/json"
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-13-6)},
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-13-7)"multiValueHeaders":{},
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-13-8)"body":"\"Hello, world!\"",
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-13-9)"isBase64Encoded":false
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-13-10)}

```

For details, see the 
### [Workspace support](https://docs.astral.sh/uv/guides/integration/aws-lambda/#workspace-support)
If a project includes local dependencies (e.g., via [Workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/)), those too must be included in the deployment package.
We'll start by extending the above example to include a dependency on a locally-developed library named `library`.
First, we'll create the library itself:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-14-1)$ uv[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-14-2)$ uv
```

Running `uv init` within the `project` directory will automatically convert `project` to a workspace and add `library` as a workspace member:
pyproject.toml```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-1)[project]
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-2)name="uv-aws-lambda-example"
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-3)version="0.1.0"
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-4)requires-python=">=3.13"
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-5)dependencies=[
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-6)# FastAPI is a modern web framework for building APIs with Python.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-7)"fastapi",
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-8)# A local library.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-9)"library",
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-10)# Mangum is a library that adapts ASGI applications to AWS Lambda and API Gateway.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-11)"mangum",
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-12)]
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-13)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-14)[dependency-groups]
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-15)dev=[
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-16)# In development mode, include the FastAPI development server.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-17)"fastapi[standard]",
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-18)]
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-19)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-20)[tool.uv.workspace]
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-21)members=["library"]
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-22)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-23)[tool.uv.sources]
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-15-24)lib={workspace=true}

```

By default, `uv init --lib` will create a package that exports a `hello` function. We'll modify the application source code to call that function:
app/main.py```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-1)import logging
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-2)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-3)from fastapi import FastAPI
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-4)from mangum import Mangum
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-5)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-6)from library import hello
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-7)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-8)logger = logging.getLogger()
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-9)logger.setLevel(logging.INFO)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-10)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-11)app = FastAPI()
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-12)handler = Mangum(app)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-13)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-14)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-15)@app.get("/")
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-16)async def root() -> str:
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-16-17)    return hello()

```

We can run the modified application locally with:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-17-1)$ uv
```

And confirm that opening 
Finally, we'll update the Dockerfile to include the local library in the deployment package:
Dockerfile```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-1)FROMghcr.io/astral-sh/uv:0.9.17ASuv
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-2)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-3)# First, bundle the dependencies into the task root.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-4)FROMpublic.ecr.aws/lambda/python:3.13ASbuilder
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-5)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-6)# Enable bytecode compilation, to improve cold-start performance.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-7)ENVUV_COMPILE_BYTECODE=1
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-8)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-9)# Disable installer metadata, to create a deterministic layer.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-10)ENVUV_NO_INSTALLER_METADATA=1
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-11)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-12)# Enable copy mode to support bind mount caching.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-13)ENVUV_LINK_MODE=copy
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-14)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-15)# Bundle the dependencies into the Lambda task root via `uv pip install --target`.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-16)#
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-17)# Omit any local packages (`--no-emit-workspace`) and development dependencies (`--no-dev`).
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-18)# This ensures that the Docker layer cache is only invalidated when the `pyproject.toml` or `uv.lock`
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-19)# files change, but remains robust to changes in the application code.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-20)RUN=from=uv,source=/uv,target=/bin/uv\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-21)=type=cache,target=/root/.cache/uv\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-22)=type=bind,source=uv.lock,target=uv.lock\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-23)=type=bind,source=pyproject.toml,target=pyproject.toml\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-24)export&&\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-25)"${LAMBDA_TASK_ROOT}"
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-26)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-27)# If you have a workspace, copy it over and install it too.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-28)#
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-29)# By omitting `--no-emit-workspace`, `library` will be copied into the task root. Using a separate
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-30)# `RUN` command ensures that all third-party dependencies are cached separately and remain
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-31)# robust to changes in the workspace.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-32)RUN=from=uv,source=/uv,target=/bin/uv\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-33)=type=cache,target=/root/.cache/uv\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-34)=type=bind,source=uv.lock,target=uv.lock\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-35)=type=bind,source=pyproject.toml,target=pyproject.toml\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-36)=type=bind,source=library,target=library\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-37)export&&\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-38)"${LAMBDA_TASK_ROOT}"
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-39)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-40)FROMpublic.ecr.aws/lambda/python:3.13
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-41)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-42)# Copy the runtime dependencies from the builder stage.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-43)COPY=builder${LAMBDA_TASK_ROOT}${LAMBDA_TASK_ROOT}
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-44)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-45)# Copy the application code.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-46)COPY${LAMBDA_TASK_ROOT}/app
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-47)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-48)# Set the AWS Lambda handler.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-18-49)CMD["app.main.handler"]

```

Tip
To deploy to ARM-based AWS Lambda runtimes, replace `public.ecr.aws/lambda/python:3.13` with `public.ecr.aws/lambda/python:3.13-arm64`.
From there, we can build and deploy the updated image as before.
## [Deploying a zip archive](https://docs.astral.sh/uv/guides/integration/aws-lambda/#deploying-a-zip-archive)
AWS Lambda also supports deployment via zip archives. For simple applications, zip archives can be a more straightforward and efficient deployment method than Docker images; however, zip archives are limited to 
Returning to the FastAPI example, we can bundle the application dependencies into a local directory for AWS Lambda via:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-19-1)$ uvexport[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-19-2)$ uv\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-19-3)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-19-4)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-19-5)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-19-6)3.13\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-19-7)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-19-8)
```

Tip
To deploy to ARM-based AWS Lambda runtimes, replace `x86_64-manylinux2014` with `aarch64-manylinux2014`.
Following the 
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-20-1)$ cd[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-20-2)$ zip[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-20-3)$ cd
```

Finally, we can add the application code to the zip archive:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-21-1)$ zip
```

We can then deploy the zip archive to AWS Lambda via the AWS Management Console or the AWS CLI, e.g.:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-22-1)$ aws\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-22-2)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-22-3)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-22-4)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-22-5)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-22-6)
```

Where the 
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-23-1)$ aws\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-23-2)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-23-3)'{"Version": "2012-10-17", "Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'

```

Or, update an existing function with:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-24-1)$ aws\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-24-2)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-24-3)
```

Note
By default, the AWS Management Console assumes a Lambda entrypoint of `lambda_function.lambda_handler`. If your application uses a different entrypoint, you'll need to modify it in the AWS Management Console. For example, the above FastAPI application uses `app.main.handler`.
To test the Lambda, we can invoke it via the AWS Management Console or the AWS CLI, e.g.:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-25-1)$ aws\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-25-2)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-25-3)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-25-4)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-25-5)[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-25-6){
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-25-7)  "StatusCode": 200,
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-25-8)  "ExecutedVersion": "$LATEST"
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-25-9)}

```

Where `event.json` contains the event payload to pass to the Lambda function:
event.json```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-26-1){
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-26-2)"httpMethod":"GET",
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-26-3)"path":"/",
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-26-4)"requestContext":{},
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-26-5)"version":"1.0"
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-26-6)}

```

And `response.json` contains the response from the Lambda function:
response.json```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-27-1){
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-27-2)"statusCode":200,
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-27-3)"headers":{
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-27-4)"content-length":"14",
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-27-5)"content-type":"application/json"
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-27-6)},
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-27-7)"multiValueHeaders":{},
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-27-8)"body":"\"Hello, world!\"",
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-27-9)"isBase64Encoded":false
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-27-10)}

```

### [Using a Lambda layer](https://docs.astral.sh/uv/guides/integration/aws-lambda/#using-a-lambda-layer)
AWS Lambda also supports the deployment of multiple composed 
In particular, we can create a lambda layer for application dependencies and attach it to the Lambda function, separate from the application code itself. This setup can improve cold-start performance for application updates, as the dependencies layer can be reused across deployments.
To create a Lambda layer, we'll follow similar steps, but create two separate zip archives: one for the application code and one for the application dependencies.
First, we'll create the dependency layer. Lambda layers are expected to follow a slightly different structure, so we'll use `--prefix` rather than `--target`:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-28-1)$ uvexport[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-28-2)$ uv\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-28-3)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-28-4)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-28-5)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-28-6)3.13\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-28-7)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-28-8)
```

We'll then zip the dependencies in adherence with the expected layout for Lambda layers:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-29-1)$ mkdir[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-29-2)$ cp[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-29-3)$ zip
```

Tip
To generate deterministic zip archives, consider passing the `-X` flag to `zip` to exclude extended attributes and file system metadata.
And publish the Lambda layer:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-30-1)$ aws\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-30-2)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-30-3)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-30-4)"x86_64"

```

We can then create the Lambda function as in the previous example, omitting the dependencies:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-31-1)$ # Zip the application code.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-31-2)$ zip[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-31-3)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-31-4)$ # Create the Lambda function.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-31-5)$ aws\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-31-6)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-31-7)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-31-8)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-31-9)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-31-10)
```

Finally, we can attach the dependencies layer to the Lambda function, using the ARN returned by the `publish-layer-version` step:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-32-1)$ aws\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-32-2)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-32-3)"arn:aws:lambda:region:111122223333:layer:dependencies-layer:1"

```

When the application dependencies change, the layer can be updated independently of the application by republishing the layer and updating the Lambda function configuration:
```
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-33-1)$ # Update the dependencies in the layer.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-33-2)$ aws\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-33-3)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-33-4)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-33-5)"x86_64"
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-33-6)
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-33-7)$ # Update the Lambda function configuration.
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-33-8)$ aws\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-33-9)\
[](https://docs.astral.sh/uv/guides/integration/aws-lambda/#__codelineno-33-10)"arn:aws:lambda:region:111122223333:layer:dependencies-layer:2"

```

December 9, 2025
