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

test:
		${DCMP} run authors coverage run --source='./src/' src/manage.py test --settings=settings.dev

start:
		${DCMP} up

startd:
		${DCMP} up -d

stoppsql:
		sudo service postgresql stop

stop:
		${DCMP} stop

execute:
# 		sudo chown -R $(USER):$(USER) .
		# ${MAKE} stoppsql
		${MAKE} clean
		${MAKE} build
		${MAKE} makemigrations
		${MAKE} migrate
		${MAKE} test
		${MAKE} startd