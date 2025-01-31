#! /bin/sh

set -e

export FLASK_APP=auth.py

dirname="migrations"

if [ -f "data.sqlite" ] ; then
    rm "data.sqlite"
    echo "Deleted SQlite DB data.sqlite"
fi

if [ -d "$dirname" ]; then
    if ! rm -rf "$dirname"; then
        echo "Failed to delete $dirname"
        exit 1
    else
        echo "Successfully deleted $dirname"
    fi
fi

if flask db init ; then
    echo "$dirname directory has been created."
    if flask db migrate -m "init db" ; then
        echo "Make SQlite migrations and create Database"
        if flask db upgrade ; then
            echo "DB upgrade: successful."
        else
            echo "Failed to upgrade DB."
            exit 1
        fi
    else
        echo "Failed to make migrations."
        exit 1
    fi
else
    echo "Failed to create DB."
    exit 1
fi




