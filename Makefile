# pip-tools ftw light alternative to pipenv, poetry
install-pip-tools:
	pip install pip-tools

# Builds the dependency trees
compile-deps: install-pip-tools
	pip-compile requirements/base.in
	pip-compile requirements/dev.in

# Simple pip install from requirements
install-deps:
	pip install -r requirements/base.txt

# Simple pip install from requirements
install-dev-deps:
	pip install -r requirements/dev.txt

# Sync deps from requirements, everything else will be removed
sync-deps: install-pip-tools
	pip-sync requirements/base.txt

# Sync deps from requirements, everything else will be removed
sync-dev-deps: install-pip-tools
	pip-sync requirements/dev.txt

# Start server with reload mode
start:
	uvicorn porta.main:app --host=0.0.0.0 --port 8002 --reload
