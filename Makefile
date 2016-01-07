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

appcore:
	manage startapp core