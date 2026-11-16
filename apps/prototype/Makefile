.PHONY: serve test help
help:
	@echo "Kivaryx synthetic local prototype: make serve | make test"
serve:
	python -m uvicorn app.main:app --host 127.0.0.1 --port 8765
test:
	python -m unittest discover -s tests -v
