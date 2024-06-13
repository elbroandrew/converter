#! /bin/sh

set -e

# until cd /app/api
# do
#     echo "Waiting for server volume..."
# done

echo "Starting server on port: 5000"

python3 app.py