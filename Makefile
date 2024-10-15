.PHONY: build up down test docs

build:
	sudo docker build . -t dnd_app -f ./docker/dnd/Dockerfile
	sudo docker build . -t dnd_sql -f ./docker/mysql/Dockerfile

up:
	docker run --rm \
				-d \
				-it \
				-p 8080:5000 \
				-v .:/dnd \
				--name dnd-container \
				dnd
	open http://localhost:8080

down:
	docker stop dnd-container

test:
	pylint ./src ./main.py ./tests --rcfile ./.pylintrc
	djlint ./templates
	flake8 --ignore E501
	write-good README.md
	pytest --cov=src tests

docs:
	pydoc-markdown -I src --render-toc > ./docs/code.md