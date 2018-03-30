test:
	@pytest tests

docs:
	@sphinx-apidoc -f -o docs oriole_test
	@sphinx-build docs docs/build/html

.PHONY: test docs
