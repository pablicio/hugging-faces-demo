install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	# python -m pytest -vvv --cov=hello --cov=greeting \
	# 	--cov=smath --cov=web tests
	# python -m pytest --nbval notebook.ipynb	#tests our jupyter notebook
	# python -m pytest -v app.py #if you just want to test web

debug:
	python -m pytest -vv --pdb	#Debugger is invoked

one-test:
	python -m pytest -vv app.py



format:
	black *.py

lint:
	pylint --disable=R,C *.py

all: install lint test format