# Advent of Code 2024
These are my submissions for the Advent of Code (AoC).

Useful links:
- [Advent of code](https://adventofcode.com)
- [My LinkedIn profile](https://linkedin.com/in/dennisbakhuis)

## Useful tools
Create a new puzzle file in python:
```bash
make 2024 1
```

This will create a new file from the template in the `python` folder:
src/2024/python/day_01.py

## Install (Python)
Requirements:
- [Conda (I use micromamba)](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html)
- [Poetry](https://python-poetry.org/)

Then:
```bash
conda env create -f environment.yml
conda activate aoc

poetry install
```

## Install (Rust)
Requirements:
- [Rust](https://rust-lang.org)

Then:
```bash
brew install rustup
rustup-init

cargo build
```
