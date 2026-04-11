.PHONY: run test clean

run:
	python main.py

test:
	pytest -q

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
	find . -type f -name "*.pyc" -delete
