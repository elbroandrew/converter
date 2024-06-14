#! /bin/sh

set -e

# until cd /app/api
# do
#     echo "Waiting for server volume..."
# done

echo "Starting server at: http://$(hostname -i):5000"

python3 app.py