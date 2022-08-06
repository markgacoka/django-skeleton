git pull origin main
pip install -r requirements.txt
python manage.py makemigrations app
python manage.py migrate app
python manage.py collectstatic --noinput --clear
python manage.py test

clear
sudo python3 manage.py runserver 0.0.0.0:80
