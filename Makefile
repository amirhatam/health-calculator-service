IMAGE_NAME = health-calculator
TAG = latest

.PHONY: init run test build

init:
	pip install -r requirements.txt

run:
	FLASK_APP=src/app.py flask run --host=0.0.0.0 --port=5000

test:
	PYTHONPATH=${PWD}/src pytest -v tests/

build:
	docker build -t $(IMAGE_NAME):$(TAG) .

clean:
	@echo "Cleaning temporary files..."
	rm -rf src/__pycache__ tests/__pycache__ .pytest_cache 