# notes

**Please read this entire README before you begin**

Some proficiency with Git, Python, Django, and your terminal is assumed. No proficiency with Docker is assumed but it is suggested that you read [this](https://docs.docker.com/engine/docker-overview/) to get familiar with the vocabulary.

### Overview

This repository is an example of what a typical SportsHi backend application codebase would look like, although production related files and folders have been omitted to keep things simple. The notable items are...
- `local`: shell script that provides a number of useful commands for local development. In your terminal run `./local` to see the full list of commands; you will at least need to use the `up`, `down`, `python`, and `lint` commands.
- `docker/local/`: directory containing files used by Docker for local development.
- `components/`: directory containing some number of isolated source code directories, each of which would run in a distinct Docker container; in this example there is only one component, but multiple components are common for real world applications, such as a server combined with a reverse proxy.
- `components/server/`: directory containing the source code for a server, in this example a [Django](https://www.djangoproject.com/) server using Python 3; **you should only edit the files in this folder**.

### About the Django server

The Django server has been created for you in the `components/server/` directory. It includes a Django app called `notes` in `server/apps/notes/` that was generated using the Django CLI and has not been modified. The Django project files are in  `server/project/`. The server is already setup to connect with a PostgreSQL database, which is automatically created for you when you start the server using the command `./local up`. You can kill the server using `./local down`, which will also bring down the database and save its data. If you need to use the Django CLI, you can run commands using `./local django-admin ...` or `./local python ...`. For example, to update the database with your latest models you would run `./local python manage.py migrate`. Note that these commands will be running **inside** a Docker container where the working directory is `server/`, so there is no need to change your terminal's working directory - it is suggested that you keep the top level directory of this repository as your terminal's working directory. To lint your Python code against the PEP 8 style guide run `./local lint`.

### Your task

Your task is to use the Django `notes` app to implement a simple REST API that allows clients to read from a global list of notes and add new notes. There is no notion of authentication or authorization - any client can use this API. The API is defined in [this OAS3 API specification](https://app.swaggerhub.com/apis/sportshi-team/notes/1.0). Most of your work should be confined to the `server/apps/notes/` directory, but you will at least need to update the `server/project/urls.py` file to make the API available for use. The [Django REST Framework](https://www.django-rest-framework.org/) app has been included in the project and you should use it for your API implementation. You should not install any additional Django apps.

While developing you will need to interact with your API to test it. Run `./local up` to start the server - it will be available on `http://0.0.0.0:8000/`. How you make requests to your API is up to you, but some options are your terminal, web browser, or an API development tool like Postman.

Roughly, the steps you need to follow to complete your task are...

1. Clone the repository onto your machine
2. [Download and install](https://www.docker.com/products/docker-desktop) Docker Desktop for your operating system; aside from Docker you don't need any other special software installed on on your machine, not even Python.
3. Start Docker Desktop on your machine
4. Open your terminal and cd into the repository
5. Run `./local python manage.py migrate` so that Django can initialize the database
6. Run `./local up` to start the server and database
7. Visit `http://0.0.0.0:8000/` in your browser to verify that the django server is running
8. Edit the files in `components/server/...` to implement the API defined [here](https://app.swaggerhub.com/apis/sportshi-team/notes/1.0)

Additionally, your code should conform to the PEP 8 style guide. You check how you're doing by running `./local lint`.

### When you are done

 Once you have finished your task you should push this repository to your own GitHub account under public settings so that it can be cloned by a SportsHi team member for testing. Let a SportsHi team member know when it is ready. They will test your API to see if it implements the specification. The quality of the code that you write will also be considered.
