# The Kindness Gym MVP

A FastAPI app that offers AI guidance for everyday dilemmas and small, realistic ways to practise kindness. Personal development, not therapy, medical advice or an emergency service.

## Status

The app was deployed on 8 October 2026:

- [Hosted app](https://the-kindness-gym.onrender.com/)
- [Round 2 presentation](https://docs.google.com/presentation/d/13qKwBTc_Ezx4IsB0cpECYZm9SLOteHz_u2CO7xDgFqM/edit)

Hosted guidance, invalid-code rejection, the individual daily limit and tester record removal have passed manual checks. The wider pilot has not started. Provider/privacy arrangements and further evaluation remain open; this is not a production-ready or validated product.

## Current behaviour

Users enter a private access code and a dilemma of 1–4,000 characters. Before calling OpenAI, the app validates the code and reserves a daily submission in PostgreSQL.

The model is `gpt-5.6-luna`, with reasoning effort `none`, a 3,000-token output limit, a 30-second client timeout and no automatic client retries. The prompt requests acknowledgement, a balanced perspective, practical kindness actions and grounded Radical gratitude observations in British English. Detected crisis situations are intended to receive a different response without gratitude; prompt instructions do not guarantee detection or safe advice in every case.

Code handles research separately. Keyword matching selects at most one card from three curated studies, using fixed summaries and source links. The selected study is not passed to the model as retrieved context. The interface includes a loading state, error messages, optional research/support sections and a Google Forms feedback link.

There are no conventional user accounts, saved conversation history, payments, progress tracking or implemented 21-day programme.

## Local setup

Python is pinned to `3.14.2` in the root `.python-version`. From the repository root, create and activate a virtual environment if one is not already active:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r mvp/requirements.txt
```

Create `mvp/.env` with your own credentials:

```dotenv
OPENAI_API_KEY="your-api-key"
DATABASE_URL="your-full-postgresql-connection-url"
```

Use a full `postgresql://` URL, not a `psql` shell command. Keep the `.env` file out of Git. Do not commit or publish API keys, database passwords, access codes or tester lists.

The app loads `.env` locally; Render supplies the same two variables through its Environment settings. The database helper requires TLS and disables prepared statements for compatibility with transaction pooling.

### Database schema

The existing Neon project already has these tables. For a new database, run the following once in its SQL editor:

```sql
CREATE TABLE beta_testers (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    code_hash TEXT UNIQUE NOT NULL,
    active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE beta_daily_usage (
    tester_id BIGINT NOT NULL REFERENCES beta_testers(id),
    usage_date DATE NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (tester_id, usage_date)
);
```

Test the connection, then start the app:

```powershell
python -m mvp.beta_access
python -m uvicorn mvp.main:app --port 8001
```

The first command should print `Database connection OK`. Open `http://127.0.0.1:8001/` after starting the server. Stop it with Ctrl+C.

`/health` returns `{"status":"ok"}`. This checks the app process only, not database or OpenAI availability. A valid registered code is required to submit, including locally.

## Hosted configuration

Render runs the app on its Free web service plan in Frankfurt. Neon PostgreSQL is also in Frankfurt.

```text
Language: Python 3
Branch: main
Root directory: leave blank
Build command: pip install -r mvp/requirements.txt
Start command: python -m uvicorn mvp.main:app --host 0.0.0.0 --port $PORT
Health check path: /health
```

Set `OPENAI_API_KEY` and `DATABASE_URL` as separate Render environment variables. Their hosted values contain only the credential or URL, without shell commands, variable-name prefixes or surrounding quotes. Save the environment change and deploy it for the app to receive the new values.

GitHub pushes trigger the configured automatic deployment. Verify the service shows Live before checking the hosted page. Free Render can sleep when idle; load the page ahead of a presentation to allow it to wake. Its local filesystem is ephemeral, so usage records live in Neon rather than local files.

The teacher explicitly approved using the Ironhack API key for the hosted beta. Available allowance still limits operation. Permission to use the key does not establish provider data-processing terms or privacy compliance.

## Access and quota rules

- Each code permits one submission per Lisbon calendar day.
- The limit resets at midnight in `Europe/Lisbon` time.
- Invalid codes and invalid dilemmas do not reserve usage.
- Usage is reserved before the AI request, so failed AI requests count too.
- Local and hosted requests share usage when configured with the same database.
- A database transaction lock serialises quota reservations. An overall 20-submissions-per-day cap is implemented but has not been specifically tested, including under concurrent requests.
- If access checking fails, the app returns an unavailable message and does not call AI.

Codes are random bearer credentials, not verified identities. Anyone given the code shares its access and allowance. The database stores a SHA-256 hash of each code; it cannot recover the original secret. A tester reference is the database record ID, not an access credential.

## Tester administration

Run these commands from the repository root with the virtual environment active. Keep the printed codes private and outside the Git repository.

### Create one tester

```powershell
python -c "from mvp.beta_access import create_tester_with_reference; ref, code = create_tester_with_reference(); print('Tester reference:', ref); print('Access code:', code)"
```

The command creates a database record. Save the two printed values together; the command itself is not the access code. Give each invited tester their own reference and code.

### Create a batch

This example creates eight additional tester records. Do not rerun it merely to display existing codes: every run creates new ones.

```powershell
@'
from mvp.beta_access import create_tester_with_reference

for number in range(1, 9):
    ref, code = create_tester_with_reference()
    print(f"Tester {number}")
    print(f"Reference: {ref}")
    print(f"Access code: {code}")
    print()
'@ | python
```

The display labels are batch positions; use the printed database references for administration. Maintain any private mapping between references and invitations separately and minimise the identifying details recorded.

### Remove a tester

Verify the requester against the original invitation before acting; a reference number alone is not proof of ownership. Do not ask them to email their dilemma or secret code.

Replace `123` below with the verified tester reference. This deletes that tester's usage records and access record, permanently invalidating the code:

```powershell
python -c "from mvp.beta_access import remove_tester; print('Removed:', remove_tester(123))"
```

`True` means an access record was removed. `False` means no matching access record was found. This does not delete emails, feedback responses, provider logs or backups.

### End-of-beta cleanup

The live notice commits to deletion of access and usage records within 30 days after the beta ends. The operator must schedule and perform this cleanup; it is not an automatic expiry job.

After the beta ends, notify testers and confirm the correct database. Only then run this transaction in the Neon SQL editor. It removes **all** beta access and usage records, including demo codes:

```sql
BEGIN;
SELECT pg_advisory_xact_lock(746201);
DELETE FROM beta_daily_usage;
DELETE FROM beta_testers;
COMMIT;
```

Verify both tables contain zero rows, and remove the separate private code/invitation list when no longer needed. Deal with feedback, email and provider-held data under their applicable retention and rights arrangements. Do not run the cleanup during an active beta or merely as a connection test.

## Data handling and privacy

The dilemma is processed by the Render-hosted FastAPI app and sent to OpenAI; the response returns to the browser. Neon stores reference IDs, code hashes, active status, dates and timestamps, not dilemmas or replies. Technical logs and provider processing remain separate data flows.

OpenAI calls set `store=False`; this is not a guarantee of zero provider retention. Frankfurt hosting does not establish EU-only processing throughout the full data flow.

The on-page privacy summary includes `davidstevengill+beta_testers@gmail.com` for questions and record-related requests. The optional feedback form uses Google Forms. Users are asked to omit identifying and sensitive details.

See [the GDPR assessment](../research/gdpr_assessment_round2.md), [EU AI Act assessment](../research/eu_ai_act_assessment_round2.md) and [pilot plan](../deployment/round2_pilot_plan.md). Lawful basis, sensitive-data handling, provider/account responsibilities, applicable terms, transfers, security review and DPIA screening remain open before wider invitations. No compliance certification is claimed.

## Checks completed and limitations

On 8 October 2026, manual checks verified local/hosted health responses, invalid-code rejection, a successful hosted AI response, repeated-submission rejection, persistence of local usage in the hosted app, temporary tester removal, and display of the privacy summary/contact. The reference-generation helper also printed a reference/code pair successfully.

The 6 October evaluation used 14 fictional cases. All 14 passed each automated guidance, research-display and gratitude-display check. Two assisted content reviews identified advice weaknesses; twelve replies remain to review. Display checks and deployment checks are not advice-quality or overall safety pass rates.

Remaining work includes the overall quota/concurrency tests, broader outage/error checks, advice review and regression testing, provider/privacy arrangements, and documentation consistency. Keyword research matching can miss context, and prompt instructions cannot guarantee appropriate guidance.

For demonstrations, prepare a private dedicated code, leave it unused on the presentation day until the demo, warm up hosting, and keep a clearly labelled prerecorded fictional example as a backup. API access depends on the remaining allowance.

Updated 9 October 2026 from the implementation and checks completed on 8 October.
