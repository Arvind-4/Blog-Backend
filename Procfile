release: python manage.py makemigrations && python manage.py migrate
web: gunicorn blog.wsgi --log-file -