install:

git clone https://github.com/OS-SiGNas/django-correct-answer.git

cd django-correct-answer/

virtualenv venv -p python3

source venv/bin/activate

pip3 install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver


join

http://localhost:8000

and

http://localhost:8000/admin/
