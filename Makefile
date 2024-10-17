.PHONY: build up down test docs

setup:
	brew install python3
	pip3 install -r requirements.txt --break-system-packages
	brew install --cask docker
	brew install write-good
	brew install flake8
	brew install djlint
	brew install mysql
	brew install hadolint
	brew install minikube
	brew services start mysql

build:
	sudo docker build . -t dnd-python:latest -f ./Dockerfile

upk8s:
	minikube start
	kubectl config use-context docker-desktop
	kubectl apply -f kubernetes
	minikube service python

up: build
	sudo docker compose up -d
	open http://localhost:8080

down:
	sudo docker compose down

test:
	pylint ./src ./main.py ./tests --rcfile ./.pylintrc
	djlint ./templates
	flake8 --ignore E501
	write-good README.md
	pytest --cov=src tests
	hadolint Dockerfile
	docker compose config --quiet

docs:
	pydoc-markdown -I src --render-toc > ./docs/code.md