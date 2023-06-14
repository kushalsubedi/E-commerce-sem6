installs:
	npm install &&\
	cd src && pip install -r requirements.txt
build:
	npm run build:css

run:
	cd src && python manage.py runserver

push:
	git config --global user.email "kushalsubedi55@gmail.com" &&\
	git config --global user.name "kushalsubedi" &&\
	git add . && git commit -m "update${+1}" && git push origin master
