## CSI 2132 Project
https://github.com/m9p909/CSI2132-Class-Project


By:
Jack Clarke     300080674

Amine Baba      300145121

Victor Babineau 300010115

Carson Boyne    300207779

Jathushan Karthigesar 300060617


## Important Files for Part 2

Main.sql: The sql file to generate the database

drop_main_tables.sql : deletes the database

./dentistapp :  django project

./dentistapp/gen_fake_data.sql : generate fake data in database


## Installation Instructions:

### Part A: setup database
1. setup a postgres server somewhere
2. create a database
3. run ./Main.sql on the schema, to create the database (if something goes wrong, you can use ./drop_main_tables.sql
4. run ./dentistapp/gen_fake_data.sql
5. get the connection string for the database (must start with postgresql://)

### Part B: setup app
1. cd ./dentistapp, from here onwards dentistapp is the root folder
2. create a venv `python3 -m venv ./.venv`
3. launch the venv `source ./.venv/bin/activate`
4. install dependencies: `pip install -r ./requirements.txt`
5. clone dentistapp/.env.example to dentistapp/.env
6. change the string in dentistapp/.env to the database url
7. run `gunicorn dentistapp.wsgi` for prod or `python3 manage.py runserver` for dev
8. Ip should display, and a message "connected to database" should display

### .env example
```
DATABASE_URL=postgresql://postgres:Yipyapyop1@localhost:5432
```





