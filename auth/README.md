## The auth service to let users to get authorized with JWT

linux:
```
export FLASK_APP=app.py

init DB (before that delete any existing DB and migrations folder):

flask db init

flask db migrate -m "some message here"

flask db upgrade
```
instead of the code above just run `./sqlite_init.sh`

give it permissions: `sudo chmod u+x sqlite_init.sh` 
