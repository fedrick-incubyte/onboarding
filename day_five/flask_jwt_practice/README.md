# Flask JWT Auth

## Setup

```bash
# 1. Activate the virtual environment
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create both databases (using your local Postgres user)
createdb flask_jwt_dev
createdb flask_jwt_test

# 4. Copy the environment template and fill in your values
cp .env.example .env

# 5. Apply migrations to the dev database
alembic upgrade head
```

## Running the API

```bash
flask --app app run --debug
```

## Running the Tests

```bash
cd flask_jwt_practice
pytest -v
```

Tests use Alembic to downgrade and re-apply migrations before each test function.
This guarantees a clean schema state regardless of prior test failures.

## Project Structure

```
flask_jwt_practice/
├── app.py              # Application factory
├── config.py           # Config loaded from environment
├── constants.py        # All magic strings and numbers
├── database.py         # SQLAlchemy engine and session context manager
├── exceptions.py       # Domain exceptions — services raise, routes catch
├── migrations/         # Alembic versioned migrations
├── models/user.py      # SQLAlchemy User model
├── schemas/auth.py     # Pydantic request schemas
├── services/
│   ├── auth_service.py # hash_password, verify_password, create/decode_access_token
│   └── user_service.py # register_user, login_user, find_user_by_email/id
├── middleware/
│   └── jwt_middleware.py  # jwt_required decorator
├── routes/
│   ├── auth_routes.py  # POST /register, POST /login
│   └── user_routes.py  # GET /public, GET /me
└── tests/
    ├── conftest.py     # Fixtures and shared helpers
    └── test_auth.py    # 25 tests in TDD order
```

## Design Decisions

**Services raise, routes catch.** Services never import Flask. Domain exceptions
(`EmailAlreadyRegisteredError`, `InvalidCredentialsError`, etc.) flow up to routes,
which translate them to HTTP responses. This keeps business logic testable in isolation.

**Alembic for all schema changes.** Tests run `alembic downgrade base → upgrade head`
on every test, not `metadata.create_all`. This keeps the test schema in sync with the
production migration history and catches migration errors before they hit production.

**Identical error for wrong password and missing user.** `login_user` raises the same
`InvalidCredentialsError` whether the email doesn't exist or the password is wrong.
This prevents user enumeration — an attacker learns nothing from the response.

**`g.current_user` set by middleware.** The `jwt_required` decorator validates the token
and sets `flask.g.current_user = user` before calling the route function. The route
reads from `g` — it never re-queries the database.

**bcrypt used directly** (not via passlib) because passlib 1.7.4 is incompatible with
bcrypt 5.x. Using `bcrypt.hashpw` and `bcrypt.checkpw` directly avoids the dependency
friction without losing constant-time comparison guarantees.
