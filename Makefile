compile-deps:
	pip install pip-tools
	pip-compile requirements/base.in
	pip-compile requirements/dev.in

install-deps:
	pip install -r requirements/base.txt

install-dev-deps:
	pip install -r requirements/dev.txt

start:
	uvicorn porta.main:app --reload
