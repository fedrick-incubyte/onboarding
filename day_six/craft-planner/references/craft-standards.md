# Craft Standards Reference

These are the default Software Craftsmanship standards applied to every plan
when the PRD does not define its own, or used to supplement a partial PRD.

---

## 1. Naming

Names are the most important thing in a codebase.
A good name makes a comment unnecessary. A bad name silently misleads.

**Functions** — name after what they return or what they do, not how:
```
✅ find_user_by_email     ❌ get_user
✅ hash_password          ❌ do_password
✅ decode_access_token    ❌ handle_jwt
```

**Variables** — name after what they represent in the domain, not their type:
```
✅ hashed_password        ❌ pw, pwd, password_hash
✅ access_token           ❌ token, t, result
✅ registered_user        ❌ user_obj, u, data
```

**Tests** — must read as a plain English sentence:
```
✅ should_return_401_when_token_is_expired
❌ test_jwt, test_401, testLoginFails
```

### How to embed in cycles

If a cycle introduces a function or variable with a bad name, the REFACTOR
step must fix it. Name it right from GREEN if possible — but never let a bad
name survive past its own cycle's REFACTOR.

---

## 2. Single Responsibility

Every function does one thing. Every module owns one concept.
If you need "and" to describe what a function does, it does too much.

```
✅ hash_password()           — hashes. that's it.
✅ find_user_by_email()      — queries by email. that's it.
✅ create_access_token()     — builds and signs. that's it.
❌ login_and_generate_token_and_log_audit()
```

Routes are orchestrators only. They call services. They do not contain
SQL queries, hashing calls, or JWT logic directly.

### How to embed in cycles

Any cycle where a route handler risks gaining business logic must include a
REFACTOR step that extracts the logic to a service. Flag this proactively.

---

## 3. No Magic Values

Every string literal or number that carries meaning lives in one place.
If a value appears in two places, it is in the wrong place.

```python
# ❌ Wrong — scattered
return jsonify({"error": "Invalid credentials"}), 401
jwt.encode(payload, "my-secret", algorithm="HS256")

# ✅ Right — defined once
from constants import ErrorMessages, HttpStatus, JWT_ALGORITHM
return jsonify({"error": ErrorMessages.INVALID_CREDENTIALS}), HttpStatus.UNAUTHORIZED
```

### How to embed in cycles

The cycle that first introduces a magic value should have a REFACTOR step
that moves it to `constants.py`. The second cycle that would use the same
value should use the constant from the start — not introduce a duplicate.

---

## 4. Type Hints Everywhere

Every function signature has complete type hints — parameters and return type.
No exceptions. This is documentation that the runtime can verify.

```python
# ❌ Wrong
def hash_password(password):
    ...

# ✅ Right
def hash_password(plain_password: str) -> str:
    ...

def find_user_by_email(email: str, db: Session) -> User | None:
    ...
```

### How to embed in cycles

The GREEN step for every service function must include type hints in the
function signature listed. If the developer skips them, the REFACTOR step
must add them before the commit.

---

## 5. Docstrings on Every Public Function

The docstring explains *why* the function exists and any non-obvious
behaviour. It must not repeat what the name already says.

```python
# ❌ Wrong — repeats the name
def verify_password(plain: str, hashed: str) -> bool:
    """Verifies a password."""

# ✅ Right — adds what the name cannot say
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Compares a plain password against a bcrypt hash using constant-time
    comparison to prevent timing attacks.
    Returns True if matched, False for any mismatch or error. Never raises.
    """
```

### How to embed in cycles

Every service function introduced in GREEN must have its docstring written
in the same step. Not in REFACTOR — in GREEN. The docstring is part of the
minimum viable implementation, not a cleanup.

---

## 6. Typed Domain Exceptions

Business rule violations are expressed as typed exceptions.
Services raise them. Routes catch them and translate to HTTP responses.
Services must never know about HTTP status codes.

```python
# exceptions.py — defined once, imported everywhere
class EmailAlreadyRegisteredError(Exception):
    """Raised when attempting to register an email that already exists."""

class InvalidCredentialsError(Exception):
    """Raised when login fails due to wrong email or wrong password."""

# ❌ Wrong — service knows about HTTP
def register_user(...):
    if user_exists:
        return jsonify({"error": "..."}), 400

# ✅ Right — service raises, route translates
def register_user(...):
    if user_exists:
        raise EmailAlreadyRegisteredError("Email already registered")

@app.post("/register")
def register():
    try:
        user_service.register_user(...)
    except EmailAlreadyRegisteredError as e:
        return jsonify({"error": str(e)}), HttpStatus.BAD_REQUEST
```

### How to embed in cycles

The first cycle that needs to signal a business rule failure must include
creating `exceptions.py` in its GREEN step. Every subsequent cycle that raises
a new exception type must add it to `exceptions.py` in its GREEN step.

---

## 7. Consistent Error Response Shape

Every error response across every endpoint looks identical:

```json
{ "error": "A single, human-readable sentence." }
```

No nested error objects. No error codes inside the body. No stack traces.
The HTTP status code carries the machine-readable classification.

### How to embed in cycles

The first cycle that introduces an error response must also add the shape
to `constants.py` or a shared response helper. All subsequent error
responses must use the same helper — never hand-roll a new shape.

---

## 8. No print() — Structured Logging Only

`print()` is never acceptable in production code. Every meaningful event
is logged using the standard logging module.

```python
import logging
logger = logging.getLogger(__name__)

# ✅ Right
logger.info("User registered", extra={"user_id": user.id})
logger.warning("Failed login attempt", extra={"email": email})
logger.error("Token decode failed", extra={"error": str(e)})

# ❌ Wrong
print(f"User {user.id} registered")
```

### How to embed in cycles

The first cycle that introduces a meaningful server-side event (user created,
login failed, token rejected) must include adding a logger call in its GREEN
or REFACTOR step. Tests may use print freely.

---

## 9. Thin Routes, Rich Services

Routes are 5–10 lines. They parse the request, call a service, handle
exceptions, and return a response. All logic lives in services.

```python
# ✅ Right — route is an orchestrator
@auth_blueprint.post("/register")
def register() -> tuple[Response, int]:
    body = parse_request_body(RegisterRequest)
    user = user_service.register_user(body.email, body.password)
    return jsonify({"user_id": user.id}), HttpStatus.CREATED
```

### How to embed in cycles

If a route's GREEN step risks growing beyond orchestration, flag it. Include
a REFACTOR step to extract the logic to a service before committing.

---

## 10. Git Discipline

- **Commit on GREEN** — the tests prove the behaviour works; that is the
  safe checkpoint
- **Refactor commit only if significant** — a rename or docstring amendment
  goes in the GREEN commit; extracting a whole service layer earns its own
- **Never commit on RED** — broken code in history makes debugging harder
- **Message format** — imperative mood, describes behaviour not code:

```
✅ feat: return 401 when JWT has expired
✅ refactor: extract verify_password into auth_service
❌ fix stuff
❌ update auth
❌ wip
```

### How to embed in cycles

Every cycle block includes an explicit COMMIT line with the exact message
to use. The developer does not have to compose it — they copy it from the plan.

---

## 11. Environment Variables — Never Hardcode Secrets

Secrets and environment-specific config live in `.env` loaded via
`python-dotenv` (or equivalent). The application raises at startup if a
required variable is missing — fail loud, fail early.

```python
# ✅ Right
SECRET_KEY: str = os.environ["SECRET_KEY"]   # raises KeyError immediately if absent

# ❌ Wrong
SECRET_KEY = "my-secret"                      # hardcoded, in version control
SECRET_KEY = os.environ.get("SECRET_KEY", "") # silently uses an empty string
```

`.env` is always in `.gitignore`. `.env.example` is always committed with
all required keys but no values.

### How to embed in cycles

The project setup section must include creating `.env.example` and
`.gitignore`. The first cycle that needs a secret must reference the
env var, not hardcode a value.
