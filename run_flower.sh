#!/bin/sh

until gtimeout 3 celery -A currency inspect ping; do
    >&2 echo "Celery workers not available"
done

echo 'Starting flower'
celery -A currency flower
