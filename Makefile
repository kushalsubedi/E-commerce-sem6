dev-init-windows:
	virtualenv venv &&\
	venv\Scripts\activate &&\
	npm install -D tailwindcss &&\
	cd src && pip install -r requirements.txt 

dev-init:
	virtualenv venv &&\
	source venv/bin/activate &&\
	npm install -D tailwindcss &&\
	cd src && pip install -r requirements.txt 
	

installs:
	npm install &&\
	cd src && pip install -r requirements.txt
build:
	npm run build:css

run:
	@echo "!!!!! running Python server ... !!!!!"
	cd src && python manage.py runserver

initial-push:

	@echo "Enter your branch name: ";\
	read branch_name ;\
	git branch $$branch_name && git checkout $$branch_name &&\
	git add . && git commit -m "update" && git push --set-upstream origin $$branch_name
push:
	git add . && git commit -m "update" && git push 


do:
	@echo "What is your age?: "; \
    read AGE; \
    echo "Your age is $$AGE"