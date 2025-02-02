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

instead of the code above just run `./sql_init.sh`

give it permissions: `sudo chmod u+x sql_init.sh` 

upd 2:

no need in using sql_init.sh script, just remove the records from the `alembic_version` table in MySQL:

`docker exec -ti <mysql container> mysql DELETE FROM alembic_version`

and remove everything from `mysql/data` folder




Run Dockerfile:

Go to parent dir `converter`:

`docker build -f auth/Dockerfile  -t auth_image . `

then run the container:

`docker run -d --name auth  -p 5005:5005 auth_service`

then go into the browser on the host machine and put:

`http://127.0.0.1:5005` -- do not forget to change `127.0.0.1` to `0.0.0.0` in the `auth.py` file.