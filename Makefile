PYTHON=python3
REQUIREMENTS=requirements.txt

.PHONY: all clean test install run

all:
	echo "To start the bot run: make run"

run:
	$(PYTHON) -m main

clear:
	find . -name '__pycache__' -exec rm -rf {} +

install:
	$(PYTHON) -m pip install -r $(REQUIREMENTS)
