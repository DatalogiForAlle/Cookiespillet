## ----------------------------------------------------------------------------------
## Makefile for "CookieSpillet"
##
## Used for both development and production. Command "make" shows all make-commands. 
## See targets below.
## ----------------------------------------------------------------------------------

help: # Show this help.
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

up: ## docker-compose up -d --build
	docker-compose up -d --build

down: ## docker-compose down
	docker-compose down

createsuperuser: ## docker-compose exec web python manage.py createsuperuser
	docker-compose exec web python manage.py createsuperuser

test: ## docker-compose exec web python manage.py test
	docker-compose exec web python manage.py test

migrate: ## docker-compose exec web python manage.py migrate
	docker-compose exec web python manage.py migrate

logs: ## docker-compose logs
	docker-compose logs

collectstatic: ## docker-compose exec web python manage.py collectstatic
	docker-compose exec web python manage.py collectstatic