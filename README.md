# Django News

## What is project about?
This is simple news site that has a premoderation of posts - before publishing, the administrator can approve (approve) the post or decline (decline). An approved post is published.

## How is project implemented?
Short description of main functionality:

1. Singup form use email and password, has email verification mechanism. This handled by [allauth](https://django-allauth.readthedocs.io/en/latest/overview.html) library.
2. Allauth works via [sendgrid](https://sendgrid.com/) and uses [celery](http://www.celeryproject.org/) for sending emails asynchronously.
3. Post creation form implemented with [markdownx](https://neutronx.github.io/django-markdownx/). It support markdown and media files. extra_markdown tampletag was created for correct displaying.
4. Administration can approve selected posts. For this admin actions was implemented. After approve posts will be shown on the main page.


### Steps to install:
Clone project:

    https://github.com/dev-yaroslav-b/django-news.git

Create env file for dev:

    touch .env.dev

And fill according to the `.env.template`

Build compose:

    docker-compose up --build
    
    
### What should be added?
Short TODO list:

1. Unittests
2. Comments/post details/ author notifications
3. Stable docker compose and deployment pipeline 