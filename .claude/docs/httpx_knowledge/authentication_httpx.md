---
# Smart Librarian Export (v2.0)
- Page Number: 10
- Timestamp: 2025-12-14T15:04:40.282509+02:00
- Source URL: https://www.python-httpx.org/advanced/authentication
- Page Title: Authentication - HTTPX
- Semantic Filename: authentication_httpx.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 8,281 characters
---

# Authentication - HTTPX

[ Skip to content ](https://www.python-httpx.org/advanced/authentication/#basic-authentication)
# Authentication
Authentication can either be included on a per-request basis...
```
>>> auth = httpx.BasicAuth(username="username", password="secret")
>>> client = httpx.Client()
>>> response = client.get("https://www.example.com/", auth=auth)

```

Or configured on the client instance, ensuring that all outgoing requests will include authentication credentials...
```
>>> auth = httpx.BasicAuth(username="username", password="secret")
>>> client = httpx.Client(auth=auth)
>>> response = client.get("https://www.example.com/")

```

## Basic authentication
HTTP basic authentication is an unencrypted authentication scheme that uses a simple encoding of the username and password in the request `Authorization` header. Since it is unencrypted it should typically only be used over `https`, although this is not strictly enforced.
```
>>> auth = httpx.BasicAuth(username="finley", password="secret")
>>> client = httpx.Client(auth=auth)
>>> response = client.get("https://httpbin.org/basic-auth/finley/secret")
>>> response
<Response [200 OK]>

```

## Digest authentication
HTTP digest authentication is a challenge-response authentication scheme. Unlike basic authentication it provides encryption, and can be used over unencrypted `http` connections. It requires an additional round-trip in order to negotiate the authentication. 
```
>>> auth = httpx.DigestAuth(username="olivia", password="secret")
>>> client = httpx.Client(auth=auth)
>>> response = client.get("https://httpbin.org/digest-auth/auth/olivia/secret")
>>> response
<Response [200 OK]>
>>> response.history
[<Response [401 UNAUTHORIZED]>]

```

## NetRC authentication
HTTPX can be configured to use 
The `.netrc` config file allows authentication credentials to be associated with specified hosts. When a request is made to a host that is found in the netrc file, the username and password will be included using HTTP basic authentication.
Example `.netrc` file:
```
machine example.org
login example-username
password example-password

machine python-httpx.org
login other-username
password other-password

```

Some examples of configuring `.netrc` authentication with `httpx`.
Use the default `.netrc` file in the users home directory:
```
>>> auth = httpx.NetRCAuth()
>>> client = httpx.Client(auth=auth)

```

Use an explicit path to a `.netrc` file:
```
>>> auth = httpx.NetRCAuth(file="/path/to/.netrc")
>>> client = httpx.Client(auth=auth)

```

Use the `NETRC` environment variable to configure a path to the `.netrc` file, or fallback to the default.
```
>>> auth = httpx.NetRCAuth(file=os.environ.get("NETRC"))
>>> client = httpx.Client(auth=auth)

```

The `NetRCAuth()` class uses `.netrc` file is not found, or cannot be parsed.
## Custom authentication schemes
When issuing requests or instantiating a client, the `auth` argument can be used to pass an authentication scheme to use. The `auth` argument may be one of the following...
  * A two-tuple of `username`/`password`, to be used with basic authentication.
  * An instance of `httpx.BasicAuth()`, `httpx.DigestAuth()`, or `httpx.NetRCAuth()`.
  * A callable, accepting a request and returning an authenticated request instance.
  * An instance of subclasses of `httpx.Auth`.


The most involved of these is the last, which allows you to create authentication flows involving one or more requests. A subclass of `httpx.Auth` should implement `def auth_flow(request)`, and yield any requests that need to be made...
```
classMyCustomAuth(httpx.Auth):
    def__init__(self, token):
        self.token = token

    defauth_flow(self, request):
        # Send the request, with a custom `X-Authentication` header.
        request.headers['X-Authentication'] = self.token
        yield request

```

If the auth flow requires more than one request, you can issue multiple yields, and obtain the response in each case...
```
classMyCustomAuth(httpx.Auth):
    def__init__(self, token):
        self.token = token

    defauth_flow(self, request):
      response = yield request
      if response.status_code == 401:
          # If the server issues a 401 response then resend the request,
          # with a custom `X-Authentication` header.
          request.headers['X-Authentication'] = self.token
          yield request

```

Custom authentication classes are designed to not perform any I/O, so that they may be used with both sync and async client instances. If you are implementing an authentication scheme that requires the request body, then you need to indicate this on the class using a `requires_request_body` property.
You will then be able to access `request.content` inside the `.auth_flow()` method.
```
classMyCustomAuth(httpx.Auth):
    requires_request_body = True

    def__init__(self, token):
        self.token = token

    defauth_flow(self, request):
      response = yield request
      if response.status_code == 401:
          # If the server issues a 401 response then resend the request,
          # with a custom `X-Authentication` header.
          request.headers['X-Authentication'] = self.sign_request(...)
          yield request

    defsign_request(self, request):
        # Create a request signature, based on `request.method`, `request.url`,
        # `request.headers`, and `request.content`.
        ...

```

Similarly, if you are implementing a scheme that requires access to the response body, then use the `requires_response_body` property. You will then be able to access response body properties and methods such as `response.content`, `response.text`, `response.json()`, etc.
```
classMyCustomAuth(httpx.Auth):
    requires_response_body = True

    def__init__(self, access_token, refresh_token, refresh_url):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.refresh_url = refresh_url

    defauth_flow(self, request):
        request.headers["X-Authentication"] = self.access_token
        response = yield request

        if response.status_code == 401:
            # If the server issues a 401 response, then issue a request to
            # refresh tokens, and resend the request.
            refresh_response = yield self.build_refresh_request()
            self.update_tokens(refresh_response)

            request.headers["X-Authentication"] = self.access_token
            yield request

    defbuild_refresh_request(self):
        # Return an `httpx.Request` for refreshing tokens.
        ...

    defupdate_tokens(self, response):
        # Update the `.access_token` and `.refresh_token` tokens
        # based on a refresh response.
        data = response.json()
        ...

```

If you _do_ need to perform I/O other than HTTP requests, such as accessing a disk-based cache, or you need to use concurrency primitives, such as locks, then you should override `.sync_auth_flow()` and `.async_auth_flow()` (instead of `.auth_flow()`). The former will be used by `httpx.Client`, while the latter will be used by `httpx.AsyncClient`.
```
importasyncio
importthreading
importhttpx


classMyCustomAuth(httpx.Auth):
    def__init__(self):
        self._sync_lock = threading.RLock()
        self._async_lock = asyncio.Lock()

    defsync_get_token(self):
        with self._sync_lock:
            ...

    defsync_auth_flow(self, request):
        token = self.sync_get_token()
        request.headers["Authorization"] = f"Token {token}"
        yield request

    async defasync_get_token(self):
        async with self._async_lock:
            ...

    async defasync_auth_flow(self, request):
        token = await self.async_get_token()
        request.headers["Authorization"] = f"Token {token}"
        yield request

```

If you only want to support one of the two methods, then you should still override it, but raise an explicit `RuntimeError`.
```
importhttpx
importsync_only_library


classMyCustomAuth(httpx.Auth):
    defsync_auth_flow(self, request):
        token = sync_only_library.get_token(...)
        request.headers["Authorization"] = f"Token {token}"
        yield request

    async defasync_auth_flow(self, request):
        raise RuntimeError("Cannot use a sync authentication class with httpx.AsyncClient")

```

