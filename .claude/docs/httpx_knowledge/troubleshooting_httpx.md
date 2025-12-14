---
# Smart Librarian Export (v2.0)
- Page Number: 16
- Timestamp: 2025-12-14T15:04:40.282509+02:00
- Source URL: https://www.python-httpx.org/troubleshooting
- Page Title: Troubleshooting - HTTPX
- Semantic Filename: troubleshooting_httpx.md
- Ollama Model: llama3.2:3b
- Export Mode: Smart Deep Crawl
- Statistics:
  - Status: Success
  - Content Length: 1,959 characters
---

# Troubleshooting - HTTPX

[ Skip to content ](https://www.python-httpx.org/troubleshooting/#troubleshooting)
# Troubleshooting
This page lists some common problems or issues you could encounter while developing with HTTPX, as well as possible solutions.
## Proxies
* * *
### "`The handshake operation timed out`" on HTTPS requests when using a proxy
**Description** : When using a proxy and making an HTTPS request, you see an exception looking like this:
```
httpx.ProxyError: _ssl.c:1091: The handshake operation timed out

```

**Similar issues** : 
**Resolution** : it is likely that you've set up your proxies like this...
```
mounts = {
  "http://": httpx.HTTPTransport(proxy="http://myproxy.org"),
  "https://": httpx.HTTPTransport(proxy="https://myproxy.org"),
}

```

Using this setup, you're telling HTTPX to connect to the proxy using HTTP for HTTP requests, and using HTTPS for HTTPS requests.
But if you get the error above, it is likely that your proxy doesn't support connecting via HTTPS. Don't worry: that's a [common gotcha](https://www.python-httpx.org/advanced/proxies/#http-proxies).
Change the scheme of your HTTPS proxy to `http://...` instead of `https://...`:
```
mounts = {
  "http://": httpx.HTTPTransport(proxy="http://myproxy.org"),
  "https://": httpx.HTTPTransport(proxy="http://myproxy.org"),
}

```

This can be simplified to:
```
proxy = "http://myproxy.org"
with httpx.Client(proxy=proxy) as client:
  ...

```

For more information, see [Proxies: FORWARD vs TUNNEL](https://www.python-httpx.org/advanced/proxies/#forward-vs-tunnel).
* * *
### Error when making requests to an HTTPS proxy
**Description** : your proxy _does_ support connecting via HTTPS, but you are seeing errors along the lines of...
```
httpx.ProxyError: [SSL: PRE_MAC_LENGTH_TOO_LONG] invalid alert (_ssl.c:1091)

```

**Similar issues** : 
**Resolution** : HTTPX does not properly support HTTPS proxies at this time. If that's something you're interested in having, please see 
