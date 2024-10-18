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
	brew install kube-linter
	docker image pull mysql:9.1.0
	sudo chmod -R g+rw "$HOME/.docker"
	brew services start mysql
	minikube start
	kubectl config use-context docker-desktop

build:
	@eval $$(minikube -p minikube docker-env);\
	docker build . -t dnd-python:1.0 -f ./Dockerfile

refresh: k8sDelete build k8sApply k8sup

up: build k8sApply k8sup

down: k8sDelete

k8sApply:
	kubectl apply -f kubernetes

k8sDelete:
	kubectl delete -f kubernetes

k8sup:
	minikube service python

dockerup:	build
	sudo docker compose up -d
	open http://localhost:8080

dockerdown:
	sudo docker compose down

test:
	pylint ./src ./main.py ./tests --rcfile ./.pylintrc
	djlint ./templates
	flake8 --ignore E501
	write-good README.md
	pytest --cov=src tests
	hadolint Dockerfile
	docker compose config --quiet
	kube-linter lint ./kubernetes

docs:
	pydoc-markdown -I src --render-toc > ./docs/code.md