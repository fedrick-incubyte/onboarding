---
name: craft-planner
description: >
  Takes a PRD, requirements document, or feature description and produces a
  detailed, incremental implementation plan following Software Craftsmanship
  principles and strict TDD (Red → Green → Refactor). Use this skill whenever
  the user provides a PRD, spec, requirements document, or says anything like
  "plan this out", "create an implementation plan", "how should I build this",
  "break this down into steps", "give me a TDD plan", or "I want to start
  implementing this". Also triggers when the user shares a feature description
  and asks where to begin. Always use this skill before writing any
  implementation code — the plan comes first.
---

# Craft Planner

Produces a detailed, ordered, incremental implementation plan from a PRD or
requirements document. Every plan it produces enforces:

- **Strict TDD** — no production code before a failing test
- **Red → Green → Refactor** cycle for every single behaviour
- **Software Craftsmanship standards** — naming, SRP, no magic values,
  type hints, docstrings, typed exceptions, thin routes, structured logging
- **Commit discipline** — commit on GREEN, refactor commit only if significant

---

## Step 1 — Read, Extract, and Interview

**Read the entire PRD before doing anything else.** Do not skim.
Do not start planning. Read it completely, then work through this step.

### 1a — Extract What Is Clear

Pull out everything the PRD states explicitly and organise it into these
categories. Write this out internally as a working checklist — you will need
it in the interview step:

```
CLEAR (stated explicitly in PRD):
  Stack:           [ ]
  Endpoints:       [ ]
  Data model:      [ ]
  Error contracts: [ ]
  Craft standards: [ ]
  Test naming:     [ ]
  DB/infra:        [ ]
  Auth mechanism:  [ ]
  Env config:      [ ]

AMBIGUOUS (implied but not confirmed):
  ...

MISSING (needed to plan but not mentioned):
  ...
```

### 1b — Identify Every Gap

A gap is anything that would force you to make an assumption during planning.
Assumptions in plans are silent bugs — the developer codes to the wrong thing
and only discovers it when the tests fail for the wrong reason.

Common gaps to look for:

| Category | Examples of gaps |
|---|---|
| Stack | Library versions not pinned — does it matter? |
| DB | Connection pooling? Test DB separate from dev DB? |
| Auth | Token storage location? Refresh token needed? |
| Errors | Same error shape for all endpoints? |
| Validation | Which fields require validation beyond types? |
| Ordering | Any endpoints that depend on each other? |
| Testing | Test DB seeded or always empty? Fixtures shared or per-test? |
| Deployment | Any env-specific behaviour needed in the plan? |
| Stretch goals | Should stretch goals be planned now or separately? |

### 1c — Ask First, Plan Never

**Never assume. Never fill gaps silently. Always ask.**

If you identified any gaps in 1b, stop here and ask the developer before
producing a single line of the plan.

Group your questions by category. Ask only what you genuinely cannot infer.
Do not ask about things the PRD already answers — that wastes the developer's
time and signals you did not read carefully.

**Format for asking questions:**

```
Before I produce the plan, I have a few questions — I want to make sure
the plan reflects exactly what you intend, not what I assumed.

**Stack / Dependencies**
- [ question ]

**Database**
- [ question ]

**Error Handling**
- [ question ]

**Testing**
- [ question ]

Once you answer these, I will produce the full plan.
```

**Rules for questions:**
- One question per bullet — no multi-part questions disguised as one
- If a question has a sensible default that most developers would expect,
  state the default and ask the developer to confirm or override:
  `"I'll use one test DB separate from dev — is that right, or do you
  want a shared DB with transaction rollback between tests?"`
- If the answer to one question makes another question irrelevant,
  ask the dependent questions only if needed
- Do not ask stylistic preferences — apply the craft standards
- Do not ask questions the developer would find obvious — use judgment

### 1d — Confirm Understanding Before Planning

Once all gaps are resolved, write a brief **"Here is what I understood"**
summary — no more than 10 bullet points — and ask the developer to confirm
before you produce the plan:

```
Got it. Here is what I am planning against — please confirm or correct
anything before I produce the full plan:

- Stack: Python + Flask + PostgreSQL + PyJWT + Passlib
- 4 endpoints: POST /register, POST /login, GET /public, GET /me
- JWT: HS256, 30-minute access token, no refresh token in scope
- Errors: uniform { "error": "..." } shape, HTTP status carries classification
- Tests: should_ prefix, pytest, separate test DB, clean slate per test
- Craft standards: from the PRD (typed exceptions, thin routes, constants, etc.)
- Stretch goals: planned separately at the end, clearly marked

Ready to produce the plan?
```

Only proceed to Step 2 once the developer confirms.

---

## Step 2 — Wait for Confirmation

Do not produce the plan until the developer explicitly confirms the summary
from Step 1d.

If they correct something, update your understanding and re-summarise only
the corrected points. Confirm again.

If they say "looks good", "yes", "correct", "go ahead", or any equivalent —
proceed to Step 3.

**Never skip this gate.** A plan built on a misunderstood PRD wastes more
time than the confirmation takes.

---

## Step 3 — Produce the Project Setup Section

Before any TDD cycles, output a **Project Setup** block that covers everything
needed before the first test can be written:

```
## Project Setup

### 1. Repository
- Initialise git repo
- Create .gitignore (language/framework appropriate)
- Create .env.example with all required environment variable keys (no values)

### 2. Dependencies
- List every dependency with its purpose
- Provide the install command

### 3. Project Structure
- Show the full folder/file tree that the TDD cycles will build into
- Every file in the tree must be justified — no speculative files

### 4. Database / Infrastructure
- Local setup commands (create DB, create test DB, run migrations if needed)
- Environment variables required

### 5. Verify Setup
- Command to confirm the environment is ready before writing the first test
```

---

## Step 4 — Produce the TDD Cycle Plan

This is the core output. Produce one block per TDD cycle, in strict build order.

**The order must be architectural** — each cycle builds exactly one layer that
the next cycle depends on. A cycle must never require something that a later
cycle introduces.

### Cycle Block Format

```
### Cycle N — <short name describing the behaviour>

RED
  Test:     should_<plain English behaviour description>
  File:     tests/<test_file>.py
  Why:      <one sentence — what piece of the system this test forces into existence>

GREEN
  Write:    <bullet list of the minimum files/functions to create or change>
  Rule:     No more than this. If you find yourself writing code with no
            failing test demanding it, stop and write the test first.

COMMIT
  Message:  feat: <imperative sentence describing the behaviour now working>

REFACTOR  (skip this block entirely if there is nothing to refactor)
  Do:       <what to extract, rename, or restructure>
  Rule:     Must not change any behaviour. Re-run all tests after.

COMMIT    (only if REFACTOR block exists and the change is significant)
  Message:  refactor: <imperative sentence describing what was cleaned up>
```

### Rules for Ordering Cycles

1. **Bootstrap first** — the app must start and respond before any feature cycle
2. **Happy path before error cases** — prove the feature works before proving
   it fails correctly
3. **Validation after happy path** — schema/input validation comes after the
   route exists
4. **Domain exceptions after services exist** — you cannot raise
   `EmailAlreadyRegisteredError` before the service layer exists
5. **Middleware last among its siblings** — build the stub first, then add
   each middleware concern as its own cycle (header parsing → signature
   verification → expiry → user lookup)
6. **Integration / multi-user tests last** — tests that register two users and
   cross-check data come after all single-user flows are green

---

## Step 5 — Produce the Acceptance Criteria

After all cycles, output an **Acceptance Criteria** checklist. It must cover:

- All tests pass
- TDD process was followed (no code before its test)
- Every craft standard from the PRD is satisfied
- All commit messages follow the agreed format

---

## Step 6 — Craft Standards Enforcement

Every plan you produce must call out craft violations as explicit cycle steps,
not as afterthoughts. This means:

- If the PRD requires typed exceptions → the cycle that first raises one must
  also include creating `exceptions.py` in its GREEN step
- If the PRD requires constants → the cycle that first introduces a magic
  string must extract it to `constants.py` in its REFACTOR step
- If the PRD requires thin routes → any cycle where business logic risks
  landing in a route must include a REFACTOR step that moves it to a service
- If the PRD requires structured logging → the first cycle that adds a
  meaningful event must include a REFACTOR step adding the logger

Read `references/craft-standards.md` for the full list of standards and how
to embed them into cycles.

---

## Step 7 — Output Format Rules

- Use `###` for each cycle heading, `##` for sections (Setup, Cycles, Criteria)
- Cycle numbers must be sequential with no gaps
- Every cycle has exactly one test — never two tests in one cycle
- Never include implementation code in the plan — only file names, function
  signatures, and descriptions
- The plan must be readable as a checklist the developer works through
  top-to-bottom without needing to re-read or jump around
- If the PRD has stretch goals, plan them in a separate **Stretch Goal Cycles**
  section at the end, clearly separated

---

## What a Good Plan Looks Like

A good plan answers these questions for every single cycle, in order:

1. What is the one test I write right now?
2. Why does this specific test come before the next one?
3. What is the absolute minimum code that makes it green?
4. What do I commit when it goes green?
5. Is there anything to clean up before moving on?
6. Does the cleanup deserve its own commit?

If the developer can open the plan, work cycle by cycle without ever wondering
"what do I do next?" — the plan is good.

---

## Reference Files

Read these when producing a plan:

- `references/craft-standards.md` — Full list of craft standards with
  examples. Read when the PRD does not define its own standards, or to
  supplement a PRD that defines them partially.

- `references/cycle-examples.md` — Concrete examples of well-formed and
  poorly-formed cycles. Read when uncertain about how to structure a tricky
  cycle (middleware, validation, exception handling).
