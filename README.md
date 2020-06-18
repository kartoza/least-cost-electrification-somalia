# Benin Electrification Platform
Electrification Platform for Benin

## Preparation
1. `git submodule init`
2. `git submodule update`

## Development
To deploy the GEP stuff:
1. Go back to root folder, and do `make up`
2. Go to backend/data-service/fixtures and put the the scenario in there. 
3. After everything done, do `make prepare-dev-db`
4. The server will be ready in http://localhost:9000/

To deploy geonode:
1. `make geonode-up`
2. and can be opened in http://localhost/