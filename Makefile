SHELL := /bin/sh

.PHONY: check html preview clean

check:
	python scripts/check_project_state.py
	python scripts/check_quarto_source.py

html: check
	quarto render --to html

preview: check
	quarto preview

clean:
	rm -rf _book .quarto
