
.PHONY: sort-imports
sort-imports:
	isort .


.PHONY: reformat
reformat:
	black .


.PHONY: lint
lint: reformat sort-imports
