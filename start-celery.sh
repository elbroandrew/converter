#! /bin/sh

set -e

celery -A celeryapp.celery_worker worker --loglevel=info