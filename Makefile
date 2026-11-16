.PHONY: help doctor check serve-prototype
help:
	@echo 'Milestone 0 helpers: make doctor | make check | make serve-prototype'
	@echo 'NOT YET IMPLEMENTED: make up/seed/scenario/evidence/reset/down'
doctor:
	@python --version
	@python -c 'import fastapi, uvicorn, httpx; print("prototype Python dependencies present")'
check:
	@cd apps/prototype && python -m unittest discover -s tests -v
serve-prototype:
	@cd apps/prototype && python -m uvicorn app.main:app --host 127.0.0.1 --port 8765
