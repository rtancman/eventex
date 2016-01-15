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