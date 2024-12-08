YEAR=$(shell printf "%04d" $(firstword $(MAKECMDGOALS)))
DAY=$(shell printf "%d" $(word 2, $(MAKECMDGOALS)))
DAY_PADDED=$(shell printf "%02d" $(DAY))
GENERATE_SCRIPT=src/templates/generate_template.py
TEMPLATE=src/templates/python_template.py
OUTPUT=src/$(YEAR)/python/day_$(DAY_PADDED).py

# Default target: show help if no arguments are provided
help:
	@echo "Usage: make YEAR DAY"
	@echo "Example: make 2024 1"
	@echo "This will generate a file src/2024/python/day_01.py from the template."

# If no valid year/day provided, show help
ifeq ($(YEAR),0000)
ifeq ($(DAY),0)
.DEFAULT_GOAL := help
endif
endif

%:
	@:

$(YEAR): $(DAY)
	mkdir -p $(dir $(OUTPUT))
	python3 $(GENERATE_SCRIPT) $(TEMPLATE) $(OUTPUT) $(YEAR) $(DAY)
