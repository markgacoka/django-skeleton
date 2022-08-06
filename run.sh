git pull origin main
pip install -r requirements.txt
python manage.py makemigrations app
python manage.py migrate app
python manage.py collectstatic --noinput --clear
python manage.py test
find . -type d -name __pycache__ -exec rm -rf {} \+
