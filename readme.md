# FastAPI Template

## Contains : 

 - Base on Repository Pattern
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
 - Commons HTTP Requests (GET, POST, PATCH, DELETE)


## For running an api using this project : 

#### Make sure git and docker are installed on your system
1) Clone the project :

```
git clone git@github.com:0xChaser/fastapi-template-api.git
```

2) Configure .env file base on indication in src/project_template/settings.py and the docker-compose.yaml

Here's an example : 

```
database_uri="postgresql+asyncpg://project_template_admin:test@project_template_db:5432/project_template"
POSTGRES_USER='project_template_admin'
POSTGRES_PASSWORD='test'
POSTGRES_DB='project_template'
PGADMIN_EMAIL="test@gmail.com"
PGADMIN_PASSWORD="test"
host="0.0.0.0"
```
3) Once the .env is configured, launch docker using : 

```
docker compose up
```
4) When container  __project_template_back__ is ready, go on and run this command :

```
alembic upgrade head
```

It will update your postgreSQL with the last version file in ./alembic/versions/


5) Once it's done, just go on :
- http://localhost:8000/docs to see the documentation of your API


#### In this template, You wil only see one example endpoint named **Test**, each CRUD operations are available !
