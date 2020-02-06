DCMP = docker-compose

clean:
		find . -name "*.pyc" -exec rm -rf {} \;
		find . -type d -empty -delete;
		rm -rf htmlcov/
		rm -rf .coverage
		rm -rf *.log

build:
		${DCMP} build

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
		${MAKE} startd