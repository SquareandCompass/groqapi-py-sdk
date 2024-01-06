# GroqAPI Python SDK

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![coverage](https://git.groq.io/cloud/groqapi-py/badges/%{default_branch}/coverage.svg)

## Devlopment

### Setup
first install `poetry` via `pipx`:
```bash
sudo apt install pipx

pipx install poetry
```
Then install the project:
```bash
poetry install
```
### Testing
Make sure to export an appropriate key for the end-to-end tests:
```bash
export GROQ_SECRET_ACCESS_KEY="<key>"
```
To run the tests in `/tests`, run
```bash
poetry run pytest
```
To generate a coverage report as well, run
```bash
poetry run pytest --cov=groq
```

### Linting & Formatting

To black everything, run
```bash
poetry run black .
```
To lint with prospector, run
```bash
poetry run prospector
```

### Building
To build .whl files and such, run 
```bash
poetry build
```

### Publishing
> Note, not tested or implemented yet, I need to add the keys and show for test repo as well
```bash
poetry publish
```

## Run Examples
To run the example code, you can use `poetry run python` like so:
```bash
poetry run python examples/examples.py
```
