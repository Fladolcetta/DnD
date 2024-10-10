.PHONY: build up down test docs

build:
	sudo docker build -t dnd .
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
	pylint ./src ./main.py --rcfile ./.pylintrc
	djlint ./templates
	flake8 --ignore E501
	write-good README.md

docs:
	pydoc-markdown -I src --render-toc > ./docs/code.md