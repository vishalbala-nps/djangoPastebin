# djangoPastebin
A Pastebin web app built using django
# Overview
This is a Pastebin Web App written in Python using Django. Right now, only the backend is implemented
# API Documentation (Backend)
 - api/snips
	 - GET - Lists all the snips available.
		 - Request: `curl -X GET 127.0.0.1:8000/api/snips/`
		 - Response: `[ { "id": 1, "title": "Hello World!!!!", "publishedOn": "2020-01-12T06:23:50Z" }, { "id": 2, "title": "Hi!", "publishedOn": "2020-01-12T06:24:04Z" } ]`
	 - POST - Posts a new snip. It returns the snip id
		 - Request: `curl -X POST http://127.0.0.1:8000/api/snips/ -H 'Content-Type: application/json' -d '{"title": "Test msg","text": "Hello World"}'`
		 - Response: `{"message":"9"}`
 - /api/snip/[ID]
	 - GET - Returns the snip associated with the id
		 - Request: `curl -X GET 127.0.0.1:8000/api/snip/9`
		 - Response: `{"title":"Test msg","text":"Hello World","pubDate":"2020-01-12T00:00:00Z"}`
