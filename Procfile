web: cd automarket && python manage.py migrate && python manage.py collectstatic
noinput && gunicorn automarket.wsgi:application --bind 0.0.0.0:$PORT