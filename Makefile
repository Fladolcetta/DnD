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