installs:
	npm install &&\
	cd src && pip install -r requirements.txt
build:
	npm run build:css

run:
	cd src && python manage.py runserver

push:
	git add . && git commit -m "update" && git push origin main
