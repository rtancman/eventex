setup:
	python -m venv .wttd && \
	source .wttd/bin/activate

install:
	pip install -r requirements.txt

starteventex:
	django-admin startproject eventex .

aliasmanagepy:
	alias manage='python $VIRTUAL_ENV/../manage.py'

startprojet:
	manage runserver

startappcore:
	manage startapp core

createenv:
    echo -e  "SECRET_KEY=ap)$co*gr*3bfy1rp2b$+yl%tywu&8zg9p57+mlju+p5olnh7- \n\
    DEBUG=True" >> ./.env ;

herokuaddsendgrid:
    heroku addons:create sendgrid:starter

testnomigrations:
    manage test --nomigrations

djangomakemigration:
    manage makemigrations

djangoapplymigration:
    manage migration

djangodumpdbapp:
    manage dumpdata --indent 4 subscriptions

herokurunmigration:
    heroku run python manage.py migrate

criarfixturespeaker:
    manage dumpdata --indent 4 core.Speaker >> keynotes.json


migrandodadosdebancousando_abc_to_mti:
    manage makemigrations --empty -n course_abc_to_mti core