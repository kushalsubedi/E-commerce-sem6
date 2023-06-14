ifeq ($(OS),Windows_NT)
dev-init:
	virtualenv venv &&\
	venv\Scripts\activate &&\
	npm install -D tailwindcss &&\
	cd src && pip install -r requirements.txt 
else
dev-init:
	virtualenv venv &&\
	/bin/bash -c "source venv/bin/activate" &&\
	npm install -D tailwindcss &&\
	cd src && pip install -r requirements.txt 
endif

installs:
	npm install &&\
	cd src && pip install -r requirements.txt
build-css:
	npm run build:css
collectstatic:
	cd src && python manage.py collectstatic

run:
	@echo "!!!!! running Python server ... !!!!!"
	cd src && python manage.py runserver

initial-push:

	@echo "Enter your branch name: ";\
	read branch_name ;\
	git branch $$branch_name && git checkout $$branch_name &&\
	git add . && git commit -m "initial-commit" && git push --set-upstream origin $$branch_name
push:
	@echo "Enter your commit message seperated by _ ";\
	read commit ;\
	git add . && git commit -m $$commit && git push 


