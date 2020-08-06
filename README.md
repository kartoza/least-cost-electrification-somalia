# Benin Electrification Platform
Electrification Platform for Benin

## Preparation
1. `git submodule init`
2. `git submodule update`

## Development
To deploy the GEP stuff:
1. Go back to deployment folder, and do `make up`
2. Go to backend/data-service/fixtures and put the the scenario in there. 
3. After everything done, do `make prepare-dev-db`
4. The server will be ready in http://localhost:9000/

To deploy geonode:
1. `make geonode-up`
2. and can be opened in http://localhost/


## To create new project 
This project setup for benin. You can fork this project and change the configuration for specific country. To do it:
1. Fork this project
2. Go to deployment/Makefile and change `PROJECT_ID`
3. Go to deployment/.env
4. Change `COMPOSE_PROJECT_NAME=gep-benin` to `COMPOSE_PROJECT_NAME=gep-country name` without space (change space with dash) 
5. Open `docker-compose.yml`. On line 49-51, change 3 configurations into the country name 
6. Go to frontend/app/assets/scripts/config/defaults.js, change `COUNTRY` into the country name
7. On the `docker-osm-setting`, put `clip.geojson` file with geojson on the country.