# Flask Multithreading Demo

Demo Flask Application to demonstrate multithreading behavior with Gunicorn


# Activate Virtual Env
pyenv activate flask


# Run With Flask
cd src 
flask run

- only app.py needed
- "WARNING: This is a development server. Do not use it in a production deployment"


# Flask Debugger mode

FLASK_ENV=development flask run


# Run with Main

- View Threads in Debugger in Intellij
- View Threads in System Monitor


# Run without Threads but Processes 

- See MainThreads in Debugger
- See Processes in htop
-- Ctrl S to freeze the View
-- F2 -> Tree View
-- Search for Flask


# Run with Gunicorn

gunicorn --bind 0.0.0.0:5000 app:application


# Only 1 worker = process
gunicorn --workers 1 --bind 0.0.0.0:5000 app:application

- 1 process
- no parallel execution (/sleep)


# Multiple threads
gunicorn --threads 2 --bind 0.0.0.0:5000 app:application

- not threadsafe /not_threadsafe
- 2 threads generate -> 2 random numbers

gunicorn --threads 3 --bind 0.0.0.0:5000 app:application
- etc


# 2 workers = processes
gunicorn --workers 2 --bind 0.0.0.0:5000 app:application

- 2 processes
- no multithreading problem /not_threadsafe


# Thread local variable

- allows to store values in a threadsafe variable


# Summary

- Flask has a build-in webserver which is used for development mode
- Flask the build-in webserver supports multithreading
- In production, we don't use flask as a webserver but Gunicorn on top of (Elastic Beanstalk)
- Gunicorn can run with multiple workers (=processes) and multiple threads / worker (=threads)
- OS sees and manages the threads of the python process (no "green threads")
- Processes have their own space of memory, threads share the memory
- Threads can access shared global variables, Processes can not
- We can use threadlocal variables to store values in a threadsafe way