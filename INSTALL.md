# Authors API

This is an API that provider some informations about authors and books.

## Install Guide

### Prerequisites
Check if you have the follow tools:
1. [Docker Engine](https://docs.docker.com/engine/installation/)
2. [Docker Compose](https://docs.docker.com/compose/install/).
3. [Git](https://git-scm.com/downloads)

### Run application
1. First, clone this repository into your local machine using the follow command:
`git clone git@github.com:fernandochimi/work-at-olist.git`
2. Run `make execute` to build and run the application
3. Go! :rocket:

PS: The file `config/api.env` is for environment values from the application. The default values corresponds to host/port of application and the database pre defined values.

### Test API
You can test the API by [Swagger Documentation](http://localhost:8000/docs/). This link will works when you run application.

## `Makefile` tips
The `Makefile` provides some commands to run the application automatically in the Docker container.

* `make execute` - This command will execute the following commands:
	* `clean` - Clean useless files in the application structure before you up the container.
	* `build` - This command will be build the application in container.
	* `migrate` - This command will run the database migrations.
	* `import_authors` - This command will run the script to import the `config/authors.csv` to the database.
	* `test` - This command will run the django tests before start the application
	* `report` - This command will show the coverage test report in terminal.
	* `startd` - This command will execute the container in background.
	* `createsuperuser` - This command will create a super user to provide an access to Admin Site and to associate the `token`.
	* `token` - This command will generate an access token to consult the API endpoints.
	* `prune` - This command will clean all unused containers and images.
* `start` - This command will execute the container and exhibit logs.
* `stop` - This command will stop the container.
