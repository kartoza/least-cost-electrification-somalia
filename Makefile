PROJECT_ID := gep-benin

SHELL := /bin/bash
COMPOSE := -f docker-osm-compose.yml -f docker-compose.yml

up:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose $(COMPOSE) -p $(PROJECT_ID) up -d

geonode-up:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building in production mode"
	@echo "------------------------------------------------------------------"
	@cd geonode/scripts/spcgeonode; docker-compose up --build -d django geoserver postgres nginx

prepare-dev-db:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "prepare database"
	@echo "------------------------------------------------------------------"
	@docker exec -it $(PROJECT_ID)_backend_1 npm run prepare-dev-db

kill:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Killing in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose $(COMPOSE) -p $(PROJECT_ID) kill

rm: kill
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Removing production instance!!! "
	@echo "------------------------------------------------------------------"
	@docker-compose $(COMPOSE) -p $(PROJECT_ID) rm

rm-volumes:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Removing all volumes!!!! "
	@echo "------------------------------------------------------------------"
	@docker volume rm $(PROJECT_ID)_osm-postgis-data $(PROJECT_ID)_import_queue $(PROJECT_ID)_import_done $(PROJECT_ID)_cache