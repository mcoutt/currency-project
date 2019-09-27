
# make environmental
`python3 -m venv venv`

# activate it
`source venv/bin/activate`

# install requirements
`pip install -r requirements.txt`

# make integration with db in project root directory
`python manage.py makemigration`

`python manage.py migrate`

# run Redis server
# - if you use debian like os
`sudo service redis start`

# and for check status run next command
`sudo systemctl status redis.service`

# - if you use os X like os
`redis-server &`

# run Celery service
`celery -A currency worker -n c_worker -B -l info -E -Q set_schedule`

celery -A currency worker -l info

`celery -A currency flower --port=6379`

# for run project from root project dir
`python manage.py runserver`


