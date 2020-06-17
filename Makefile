PROJECT_ID := gep-benin

SHELL := /bin/bash

up:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "Building in production mode"
	@echo "------------------------------------------------------------------"
	@docker-compose -p $(PROJECT_ID) up -d

prepare-dev-db:
	@echo
	@echo "------------------------------------------------------------------"
	@echo "prepare database"
	@echo "------------------------------------------------------------------"
	@docker exec -it $(PROJECT_ID)_backend_1 npm run prepare-dev-db