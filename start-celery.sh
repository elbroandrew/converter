#! /bin/sh

set -e

# until cd /app/api
# do
#     echo "Waiting for server volume..."
# done

celery -A celeryapp.celery_worker worker --loglevel=info