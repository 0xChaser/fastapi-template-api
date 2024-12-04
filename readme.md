# FastAPI Template

## Contains : 

 - SRC Layout
 - Basic dependencies
 - DockerCompose (PostgreSQL, PgAdmin, API)
 - DockerFile for API Container
 - Alembic (Versioning database)
 - SQLAlchemy (ORM)
 - FastAPI ( Framework python for API)
 - Pydantic (Type of data)
 - Base files / Folders
 - One basic endpoint (Test)
 - .env organisation on settings file


## For running an api using this project : 

#### Make sure git and docker are installed on your system
1) Clone the project :

```
git clone git@github.com:0xChaser/fastapi-template-api.git
```

2) Configure .env file base on indication in src/project_template/settings.py and the docker-compose.yaml

3) Once the .env is configured, launch docker using : 

```
docker compose up
```
4) Once it's done, just go on :
- http://localhost:8000/docs to see the documentation of your API


#### In this template, You wil only see one example endpoint named **Test**, each CRUD operations are available !
