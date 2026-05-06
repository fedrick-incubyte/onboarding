# Cycle Examples Reference

Concrete examples of well-formed and poorly-formed TDD cycles.
Read this when uncertain about how to structure a cycle.

---

## Well-Formed Cycles

---

### Example A — Simple Happy Path Cycle

```
### Cycle 3 — Registration returns 201 with user_id

RED
  Test:     should_return_201_with_user_id_when_registering_with_valid_data
  File:     tests/test_auth.py
  Why:      Forces the route, DB model, schema, and password hashing
            into existence simultaneously — the minimum vertical slice.

GREEN
  Write:
    - routes/auth_routes.py  → POST /register route (orchestrator only)
    - models/user.py         → User SQLAlchemy model (id, email, hashed_password, created_at)
    - schemas/auth.py        → RegisterRequest Pydantic model (email: EmailStr, password: str)
    - services/auth_service.py → hash_password(plain_password: str) -> str
    - database.py            → SQLAlchemy engine, session, Base
  Rule:     No login route. No JWT. No duplicate-email check. Not yet.

COMMIT
  Message:  feat: return 201 with user_id on successful registration

REFACTOR
  Do:       Move RegisterRequest into schemas/auth.py if not already there.
            Add type hints and docstring to hash_password.
            Add BCRYPT_ROUNDS to constants.py.

COMMIT
  Message:  refactor: extract hash_password into auth_service with type hints
```

**Why this is well-formed:**
- One test, one behaviour
- GREEN lists exact files and functions — no ambiguity
- REFACTOR is justified — extracting a service is significant
- Both commits have clear, imperative messages

---

### Example B — Error Case Cycle (after happy path)

```
### Cycle 5 — Registration rejects duplicate email

RED
  Test:     should_return_400_when_email_is_already_registered
  File:     tests/test_auth.py
  Why:      Forces a DB lookup before insert and introduces the first
            typed domain exception.

GREEN
  Write:
    - exceptions.py          → EmailAlreadyRegisteredError(Exception)
    - services/user_service.py → register_user() queries DB, raises
                                  EmailAlreadyRegisteredError if email found
    - routes/auth_routes.py  → catch EmailAlreadyRegisteredError → 400
    - constants.py           → ErrorMessages.EMAIL_ALREADY_REGISTERED

  Rule:     The route catches the exception — it does not contain the query.
            The service raises — it does not return an HTTP response.

COMMIT
  Message:  feat: return 400 when attempting to register a duplicate email

REFACTOR
  Do:       Confirm find_user_by_email is extracted to user_service.py
            and not duplicated inside register_user body.

COMMIT
  Message:  refactor: extract find_user_by_email into user_service
```

---

### Example C — Middleware Cycle (stub first, logic incrementally)

```
### Cycle 8 — Protected route returns 401 with no token (stub)

RED
  Test:     should_return_401_when_no_authorization_header_is_sent
  File:     tests/test_auth.py
  Why:      Forces the creation of GET /me and the jwt_required decorator.
            The decorator starts as a stub — it always returns 401.
            No JWT logic yet.

GREEN
  Write:
    - routes/user_routes.py    → GET /me with @jwt_required decorator
    - middleware/jwt_middleware.py → jwt_required decorator that
                                    immediately returns 401

  Rule:     The decorator does nothing except return 401.
            JWT decoding comes in the next cycle.

COMMIT
  Message:  feat: protect /me route, return 401 when no authorization header sent

(no REFACTOR — the stub is intentionally minimal)
```

```
### Cycle 9 — Middleware rejects tampered tokens

RED
  Test:     should_return_401_when_token_signature_has_been_tampered_with
  File:     tests/test_auth.py
  Why:      Forces the actual jwt.decode call inside the decorator.
            The stub from Cycle 8 becomes real.

GREEN
  Write:
    - middleware/jwt_middleware.py → add jwt.decode using SECRET_KEY,
                                    catch InvalidTokenError → 401
    - services/auth_service.py    → decode_access_token(token: str) -> dict
                                    raises InvalidTokenError on bad signature

  Rule:     Expiry handling is the next cycle — do not add it here.

COMMIT
  Message:  feat: return 401 when JWT signature is invalid

REFACTOR
  Do:       Move decode logic to auth_service.decode_access_token.
            Add typed raises to docstring.

COMMIT
  Message:  refactor: extract decode_access_token into auth_service
```

**Why this is well-formed:**
- Middleware is built incrementally — stub → signature check → expiry → user lookup
- Each concern is its own cycle with its own test
- The stub is a valid, passing state — not a hack

---

## Poorly-Formed Cycles

---

### Anti-Pattern A — Two behaviours in one cycle

```
### Cycle 3 — Registration

RED
  Test:     should_return_201_on_valid_registration
            should_return_400_on_duplicate_email      ← WRONG: two tests
  ...
```

**Why this is wrong:**
You cannot be in RED for two tests simultaneously. When the first goes green,
the second is still red — and you don't know if the implementation for the
first accidentally satisfies the second, or breaks it. One cycle, one test.

**Fix:** Split into two cycles. Cycle 3 is the happy path. Cycle 5 is the
duplicate email check — after the service layer exists to support it.

---

### Anti-Pattern B — GREEN step that does too much

```
GREEN
  Write:
    - Everything in the project structure
    - All services
    - All models
    - The complete middleware
```

**Why this is wrong:**
This is not incremental development — it is writing all the code at once and
calling it TDD. The point of RED is that the test fails because the code does
not exist yet. If you write everything upfront, you never have that moment.

**Fix:** GREEN for each cycle should list only what that one test demands.
Ask: "if I deleted everything except what this test requires, what is the
minimum set of files and functions?" That is the GREEN step.

---

### Anti-Pattern C — REFACTOR that changes behaviour

```
REFACTOR
  Do:   Rewrite the login flow to use a different hashing algorithm.
        Change the JWT expiry from 30 minutes to 15 minutes.
```

**Why this is wrong:**
REFACTOR must never change behaviour. If the tests pass before REFACTOR, they
must pass identically after. Changing the hashing algorithm changes behaviour
(and will likely break tests). Changing expiry changes behaviour.

**Fix:** If you need to change behaviour, that change needs its own RED test
first — then GREEN to implement it — then REFACTOR to clean it up.

---

### Anti-Pattern D — Cycle that skips the "why"

```
### Cycle 4

RED
  Test:     should_return_422_when_email_is_invalid

GREEN
  Write:    Add validation
```

**Why this is wrong:**
"Add validation" is not actionable. The developer does not know which file,
which library, or which function. And without a WHY, they do not know what
architectural decision this cycle is making.

**Fix:**

```
### Cycle 4 — Registration validates email format

RED
  Test:     should_return_422_when_email_format_is_invalid
  File:     tests/test_auth.py
  Why:      Forces the introduction of Pydantic's EmailStr validator
            and wires Pydantic validation errors to 422 HTTP responses.

GREEN
  Write:
    - schemas/auth.py → change email field type from str to EmailStr
    - routes/auth_routes.py → catch Pydantic ValidationError → 422
```

---

### Anti-Pattern E — Middleware built in one giant cycle

```
### Cycle 8 — JWT Middleware

RED
  Test:     should_return_401_when_no_authorization_header_is_sent
            (implicitly also tests tampered tokens, expiry, and deleted users)

GREEN
  Write:    Complete jwt_required decorator with all validation logic
```

**Why this is wrong:**
Middleware has at least four distinct concerns:
1. Header presence
2. Header format (Bearer prefix)
3. Signature validity
4. Token expiry
5. User existence in DB

Each of these is a separate behaviour. Each deserves its own failing test.
Building them all at once means you never see them fail individually — and
you cannot be sure your implementation correctly handles each case.

**Fix:** One cycle per concern. Start with a stub (Cycle 8 always returns 401).
Then add header parsing (Cycle 9). Then signature check (Cycle 10). Then
expiry (Cycle 11). Then user lookup (Cycle 12). Each cycle has one test,
one GREEN step, one commit.

---

## The Acid Test for a Well-Formed Cycle

Ask these five questions about every cycle you write:

1. **Can the test fail before any GREEN code is written?**
   If no → the test is testing something that already exists → wrong cycle order.

2. **Can a developer complete GREEN without reading any other cycle?**
   If no → the GREEN step is not specific enough.

3. **Does the REFACTOR step change any observable behaviour?**
   If yes → it is not a refactor; it needs its own RED test.

4. **Is the commit message imperative and describing behaviour?**
   If it contains "update", "fix", "changes", or "wip" → rewrite it.

5. **Could this cycle be split into two?**
   If yes → split it. Smaller cycles catch more bugs and produce cleaner history.
