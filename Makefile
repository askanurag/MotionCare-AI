install:
	python -m pip install -e ".[notebooks]"
test:
	python -m unittest discover -s tests -v
train:
	python -m healthcare_ai.cli train --csv data/demo.csv
notebooks:
	python scripts/execute_notebooks.py
