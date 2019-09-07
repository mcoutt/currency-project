
# make environmental
`python3 -m venv venv`

# activate it
source venv/bin/activate

# install requirements
pip install -r requirements.txt

# make integration with db in project root directory
`python manage.py makemigration`
`python manage.py migrate`

# run Celery service
`celery -A currency worker -l info`


# for run project from root project dir
`python manage.py runserver`


