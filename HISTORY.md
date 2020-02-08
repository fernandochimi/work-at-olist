# History Application

This document describes the tools used in this application.

## Libraries, Frameworks and Programming Language

* [Python 3](https://www.python.org): The main programming language of the application. Provides excelent native libraries that makes the programming easy.
* [Django](https://www.djangoproject.com/): The Python framework. Provides a lot of classes that help on appplication development.
* [Django Extensions](https://django-extensions.readthedocs.io/en/latest/): This library provides a lot of custom extensions. In this project, Django Extensions are used when the list of authors are imported to database
* [Django Rest Framework](https://www.django-rest-framework.org/): The Django Rest library. This library provides a lot of classes to help develop the API writing with less code blocks
* [Coverage](https://coverage.readthedocs.io/en/coverage-5.0.3/): A library to cover and show a complete report of code covered in tests
* [Factory Boy](https://factoryboy.readthedocs.io/en/latest/): This library provides some classes to make tests more easy to write
* [PsycoPg](https://www.psycopg.org/): This is the library to run PostgreSQL in this application

## Infrastructure
* [Docker Engine](https://docs.docker.com/engine/installation/) and [Docker Compose](https://docs.docker.com/compose/install/): My favorite! This tool is very important to virtualize and build applications.
* [Git](https://git-scm.com/downloads): This tool are essential to versioning the code
* [Sublime](https://www.sublimetext.com/): A lightweight text editor that support a lot of programming languages and files
* `Mac Terminal`
* [PostgreSQL](https://www.postgresql.org): A free database to persist the data application

## Swagger and Heroku
This project does not provides this two application. Here is the reasons:
* [Swagger](https://www.swagger.io): The libraries that support django rest framework does not work in this scenarios and the most important Swagger Django libraries ([Django Rest Swagger](https://django-rest-swagger.readthedocs.io/en/latest/) and [drf-yasg](https://github.com/axnsan12/drf-yasg)) have some errors
* [Heroku](https://www.heroku.com): It's present some erros on install in Mac.
Thanks to understand