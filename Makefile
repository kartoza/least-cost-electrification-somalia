PROJECT_ID := gep-benin

SHELL := /bin/bash

up:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) up -d

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