.PHONY: test docs servedocs

test:
	@py.test

docs:
	@rm -f docs/oriole_test.rst
	@rm -f docs/modules.rst
	@sphinx-apidoc -o docs/ oriole_test
	@$(MAKE) -C docs clean
	@$(MAKE) -C docs html

servedocs: docs
	@watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .
