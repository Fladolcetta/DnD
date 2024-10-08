build:
	sudo docker build -t dnd .
up:
	docker run --rm -d -it -p 8080:5000 -v ./.env:/dnd/.env --name dnd-container dnd
	open http://localhost:8080

down:
	docker stop dnd-container