# Dockerized Django with Postgres

## Use this project as new django project cascade

### Steps to install:
Clone project:

    git clone https://github.com/dev-yaroslav-b/django-docker-cascade.git

Rename folder:
    
    mv django-docker-cascade <your-project-name>

Create env file for dev:

    touch .env.dev

And fill according to the `.env.template`

Build compose:

    docker-compose up --build

## TODO:
1. Add prod setup