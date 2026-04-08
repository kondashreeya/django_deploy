python manage.py migrate
python manage.py collectstatic 
gunicorn deploy_pro.wsgi:application