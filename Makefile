docker-up:
	docker compose up --build -d
	docker exec -it python-matplotlib-kata python userInterface.py

docker-down:
	docker compose down