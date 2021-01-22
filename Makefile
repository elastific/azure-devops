hello:
	echo "this is my first make comand"
install:
	echo "This will later be a pip install command"
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,E1120 hello.py

test:
	python -m pytest -vv test_hello.py