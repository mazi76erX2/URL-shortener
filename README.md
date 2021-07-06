ShortLink
=============

**URL shortening service using Python and Django.**

Endpoints
---------

-   /encode - Encodes a URL to a shortened URL
-   /decode - Decodes a shortened URL to its original URL.

Installation
------------

```bash
virtualenv venv

###For Linux and Mac
$ source venv/bin/activate

###For Windows
$ source venv/Scripts/activate

$ pip install -r requirements.txt

$ pip install httpie

$ python manage.py runserver
```

Usage
-----
In a separate terminal

```bash
$ http GET 127.0.0.1:8000/generate_csrf/

HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Content-Length: 66
Content-Type: application/json
Date: Tue, 06 Jul 2021 12:22:19 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.9.2
Set-Cookie: csrftoken=wKxwnGZPMLRmuWQPSDrwPOMQSQ33R7uVQhLQQ6ORq90ugCLjnpgb6XKGNQdWmB7l; 
...

"oPW0skyOzNARAMKYHBvfjdnAFk0ylMbrImakVKnQdbJZmsFscnkUAmlqAkarQgOR"
```

For Encode

```bash
$ http POST 127.0.0.1:8002/encode/ orignal_url="https://thischarmingninja.me" X-CSRFToken:"oPW0skyOzNARAMKYHBvfjdnAFk0ylMbrImakVKnQdbJZmsFscnkUAmlqAkarQgOR"
```

For Decode

```bash
http GET 127.0.0.1:8002/decode/ shortened_url="short.url/Tr2e21" X-CSRFToken:"oPW0skyOzNARAMKYHBvfjdnAFk0ylMbrImakVKnQdbJZmsFscnkUAmlqAkarQgOR"
```

Tests (Incomplete)
------------------

```bash
$ pip install -r requirements-dev.txt

$ coverage run manage.py test

$ coverage html

.....
-------------------------------------------------------------------
Ran 7 tests in 0.005s

OK

$ open html/index.html
```