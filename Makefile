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
	brew install eslint
	brew install pydoc-markdown
	brew install prettier
	brew install ruff
	docker image pull mysql:9.1.0
	sudo chmod -R g+rw "$HOME/.docker"
	brew services start mysql
	sudo minikube delete
	minikube start
	kubectl config use-context docker-desktop

build:
	@eval $$(minikube -p minikube docker-env);\
	docker build . -t dnd-python:1.0 -f ./Dockerfile

refresh: k8sDelete minikubeRefresh build k8sApply k8sup

up: build k8sApply k8sup

down: k8sDelete

mount:
	minikube mount .:/dnd

k8sApply:
	kubectl apply -f kubernetes

k8sDelete:
	kubectl delete -f kubernetes

k8sup:
	minikube service python

minikubeRefresh:
	sudo minikube delete
	minikube start

dockerup:	build
	sudo docker compose up -d
	open http://localhost:8080

dockerdown:
	sudo docker compose down

test: docs lint
	pytest --cov=src tests

coverage:
	pytest --cov=src tests --cov-report=html

docs:
	pydoc-markdown -I src --render-toc > ./docs/code.md

lint:
	prettier ./ -w
	docker compose config --quiet
	kube-linter lint ./kubernetes
	pylint ./src ./main.py ./tests --rcfile ./.pylintrc
	djlint ./templates
	flake8 --ignore E501
	write-good README.md
	eslint --no-config-lookup static
	hadolint Dockerfile
	ruff check --select ALL ./src main.py --ignore E501
	ruff check --select ALL ./tests --ignore E501,S101,ANN001,PLR2004
