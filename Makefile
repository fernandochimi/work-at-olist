DCMP = docker-compose

clean:
		find . -name "*.pyc" -exec rm -rf {} \;
		find . -type d -empty -delete;
		rm -rf htmlcov/
		rm -rf .coverage
		rm -rf *.log

build:
		${DCMP} build

migrate:
	 	${DCMP} run authors python src/manage.py migrate --settings=settings.dev

import_authors:
	 	${DCMP} run authors python src/manage.py runscript import_authors --script-args 'config/authors.csv' --settings=settings.dev

test:
		${DCMP} run authors coverage run --omit="**migrations**,**tests**" --source='./src/authors,./src/books' src/manage.py test --settings=settings.dev

report:
		${DCMP} run authors coverage report -m

start:
		${DCMP} up

startd:
		${DCMP} up -d

createsuperuser:
		${DCMP} run authors python src/manage.py createsuperuser --username user --email user@example.com --no-input --settings=settings.dev

token:
		${DCMP} run authors python src/manage.py drf_create_token user --settings=settings.dev

prune:
		docker container prune -f

stoppsql:
		sudo service postgresql stop

stop:
		${DCMP} stop

execute:
		${MAKE} clean
		${MAKE} build
		${MAKE} migrate
		${MAKE} import_authors
		${MAKE} test
		${MAKE} report
		${MAKE} startd
		${MAKE} createsuperuser
		${MAKE} token
		${MAKE} prune