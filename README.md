# djangoPastebin
A Pastebin web app built using django
# Overview
This is a Pastebin Web App written in Python using Django.
# Installation
 - Begin by cloning this repo `git clone https://github.com/vishalbala-nps/djangoPastebin`
 - Create a Virtual environment by running: `virtualenv -p python3 env`
 - Activate the environment by running `source env/bin/activate`
 - Install the required modules by running: `pip3 install -r requirements.txt`
 - Run the following commands to set up the database: `python3 manage.py makemigrations` and `python3 manage.py migrate`
 - Start the server by running: `python3 manage.py runserver`
 - You can open a browser and access the app at `http://127.0.0.1:8000/`
# Frontend
This project includes a frontend as well. You can access it at `http://127.0.0.1:8000/`
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
# Deployment on Heroku
The production-heroku branch of this repo consists of a Heroku Procfile and Necesary changes to settings.py to use PostgreSQL as the DB Backend. You can visit the deployed app [here](http://djangopastebin.herokuapp.com)



