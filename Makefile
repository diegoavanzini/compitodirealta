.PHONY: run test clean

run:
	python app.py

test:
	pytest -q

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
	find . -type f -name "*.pyc" -delete

translate:
	msgfmt locale/es/LC_MESSAGES/messages.po -o locale/es/LC_MESSAGES/messages.mo
	msgfmt locale/en/LC_MESSAGES/messages.po -o locale/en/LC_MESSAGES/messages.mo
	msgfmt locale/it/LC_MESSAGES/messages.po -o locale/it/LC_MESSAGES/messages.mo
