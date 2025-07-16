# Lance le projet localement depuis l'image Docker
make run:
	docker pull dockerpython603/oc-lettings-site:latest
	docker run -p 8000:8000 dockerpython603/oc-lettings-site:latest
