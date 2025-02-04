## The auth service to let users to get authorized with JWT

linux:
```
export FLASK_APP=app.py

init DB (before that delete any existing DB and migrations folder):

flask db init

flask db migrate -m "some message here"

flask db upgrade
```
upd 1:

Instead of the code above just run `./sql_init.sh`

give it permissions: `sudo chmod u+x sql_init.sh` 

upd 2:

No need in using `sql_init.sh script`, just remove the records from the `alembic_version` table in MySQL:

`docker exec -ti <mysql container> mysql DELETE FROM alembic_version`

and remove everything from `mysql/data` folder

upd 3:

First start of the MySQL container takes too long, so that the auth `sql_init.sh` script is not able to run successfully.

So, do not run this script and do not remove `mysql/data` folder, just go inside the DB and:

`DELETE FROM users;`

`ALTER TABLE users AUTO_INCREMENT = 1;`  (to start new IDs from 1 again) if you want to remove all the users,

then restart the containers and you can add users again.

In future -- do not run a database inside a container.

## Run Makefile

make up

make down