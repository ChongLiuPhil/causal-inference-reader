SHELL := /bin/sh

.PHONY: check stack-check html preview clean

check:
	python scripts/check_project_state.py
	python scripts/check_stack_consistency.py
	python scripts/check_quarto_source.py

stack-check:
	python scripts/check_stack_consistency.py

html: check
	quarto render --to html

preview: check
	quarto preview

clean:
	rm -rf _book .quarto
