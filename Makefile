api:
	python3 serve.py
.PHONY: api

scaffold:
	graphscale scaffold graphscale_todo.graphql
.PHONY: scaffold
