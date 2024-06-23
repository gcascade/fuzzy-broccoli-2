# fuzzy-broccoli-2

## Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package installer)

### Steps
1. **Clone the repository**:
    ```bash
    git clone https://github.com/gcascade/fuzzy-broccoli-2.git
    cd fuzzy-broccoli-2
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install pip-tools**:
    ```bash
    pip install pip-tools
    ```

4. **Compile dependencies**:
    ```bash
    pip-compile requirements.in
    pip install -r requirements.txt
    ```

5. **Install Tox**:
    ```bash
    pip install tox
    ```

6. **Install pre-commit hooks**:
    ```bash
    pre-commit install
    ```

## Usage

1. **Run the game**:
    ```bash
    python main.py
    ```

2. **Run Tox to check the code**:
    ```bash
    tox
    ```

## Testing

### Run Tests
We use PyTest for testing. To run tests, use:
```bash
pytest
```

## Run Linting and Type Checking
We use Flake8 for linting and Mypy for type checking. To run these checks, use:
```bash
flake8 .
mypy scripts tests
```

## Run Code Formatting Checks
We use Black for code formatting and isort for sorting imports. To run these checks, use:
```bash
black --check .
isort --check-only .
```

## Compile Requirements
To compile the requirements.txt file from requirements.in using pip-tools, run:
```bash
tox -e requirements
```
