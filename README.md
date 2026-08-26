# Python Practice

## What I've Learned

### Python Fundamentals
- Functions, return values, raising exceptions

### Object-Oriented Programming
- Classes, inheritance, polymorphism
- Dunder methods (`__init__`, `__eq__`)
- `super()` calls
- Abstract base classes
- Custom exceptions (`TooManyStudents`)

### pytest
- Basic assertions
- `pytest.raises` for exception testing
- Fixtures (`@pytest.fixture`) and `conftest.py`
- Fixture composition
- Class-based tests (`setup_method` / `teardown_method`)
- `@pytest.mark.parametrize` — data-driven tests
- `@pytest.mark.skip` / `@pytest.mark.xfail`
- Custom marks (`slow`, `hogwarts`, `students`, `teachers`)

### Mocking
- `unittest.mock.patch` and `Mock` objects
- Mocking external APIs (`requests`)

### FastAPI
- Pydantic models
- GET/POST route handlers
- Request body validation

## Running Tests
- Run all: `pytest`
- By mark: `pytest -m hogwarts`
- Skip slow: `pytest -m "not slow"`
