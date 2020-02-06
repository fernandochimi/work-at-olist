DCMP = docker-compose

clean:
		find . -name "*.pyc" -exec rm -rf {} \;
		find . -type d -empty -delete;
		rm -rf htmlcov/
		rm -rf .coverage
		rm -rf *.log

build:
		${DCMP} build

makemigrations:
	 	${DCMP} run authors python src/manage.py makemigrations --settings=settings.dev

migrate:
	 	${DCMP} run authors python src/manage.py migrate --settings=settings.dev

import_authors:
	 	${DCMP} run authors python src/manage.py runscript import_authors --settings=settings.dev

test:
		${DCMP} run authors coverage run --source='./src/' src/manage.py test --settings=settings.dev

start:
		${DCMP} up

startd:
		${DCMP} up -d

prune:
		docker container prune -f

stoppsql:
		sudo service postgresql stop

stop:
		${DCMP} stop

execute:
		${MAKE} clean
		${MAKE} build
		${MAKE} makemigrations
		${MAKE} migrate
		${MAKE} import_authors
		${MAKE} test
		${MAKE} startd
		${MAKE} prune