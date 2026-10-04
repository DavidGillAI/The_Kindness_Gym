# The Kindness Gym: Preliminary GDPR Assessment

Assessment updated: 4 October 2026
Status: Round 2 academic assessment, implementation and provider verification incomplete.

## 1. Current Scope

The current MVP is a FastAPI web app. A user submits an everyday dilemma, which is sent to an OpenAI model. The app displays AI guidance and, where relevant, a separately selected research card.

The MVP does not include accounts, conversation history, course progress, payments or the proposed 21-day programme.

The n8n proof of concept remains a separate project artefact. Its provider settings require separate review if it is used again.

LangSmith is used to evaluate fictional scenarios. Live user submissions are not intentionally included in that evaluation workflow.

This assessment describes the development setup. It does not establish readiness for a public pilot.

## 2. Data Flow and Minimisation

| Data | Current use | Privacy consideration |
| --- | --- | --- |
| Dilemma text | Sent to OpenAI to generate guidance | May contain personal data about the user or other people |
| Generated guidance | Returned to the browser | May repeat personal information from the submission |
| Request metadata | Local server access logs | May include IP addresses and request details |
| Timing and token metrics | Printed in the terminal | Used for technical evaluation |
| Fictional evaluation inputs and outputs | Stored in LangSmith and project files | Must remain fictional and free of real identifying details |
| API credentials | Loaded from a local environment file | Must remain private and excluded from Git |

The interface asks users to leave out names and identifying details. That reminder reduces risk but does not prevent sensitive disclosures.

The app has no implemented conversation-history database. This does not mean that browsers, providers or development tools retain nothing.

Before a pilot, verify every location where submissions, responses or metadata could be recorded, including exception logs and any enabled tracing.

## 3. Sensitive Information and Lawful Basis

Free-text dilemmas may disclose health information, religious or philosophical beliefs, sexual orientation, or information about other identifiable people.

Not every personal disclosure is special-category data. Where Article 9 applies, processing needs both an Article 6 lawful basis and an applicable Article 9 condition.

Neither basis has been finalised for real-user operation. Explicit consent is a possible condition, not an automatic solution.

Avoiding sensitive questions and displaying a disclaimer do not remove obligations when sensitive information is actually processed. Safety response instructions are not a privacy consent mechanism.

Before real-user testing, document the processing purposes, lawful bases and approach to unexpected sensitive disclosures. Establish any necessary consent and withdrawal arrangements.

## 4. Providers and Account Responsibilities

### OpenAI

The app uses an API key supplied through the Ironhack instance account. The relevant account owner, contractual arrangements and project-level data controls must be identified.

Requests use `store=False`. This setting must not be described as Zero Data Retention. OpenAI documents separate abuse-monitoring and caching arrangements, with behaviour dependent on the endpoint and account configuration.

Do not assume that the developer can change organisation-level controls or delete all provider-held data.

### LangSmith

The evaluation uses the EU LangSmith endpoint and stores fictional inputs, rendered outputs and experiment information.

Using an EU endpoint does not establish all contractual, subprocessor, retention or transfer arrangements. These remain to be verified.

Keep evaluation uploads restricted to fictional cases. Do not enable live-user tracing without a documented purpose, privacy review and appropriate controls.

### Other services

The research and support links open external websites. Their privacy arrangements are separate. Do not add user dilemma text or identifiers to those links.

Any future hosting, analytics or monitoring service must be added to this assessment before use.

## 5. Retention, Deletion and User Rights

No complete retention schedule or user-rights procedure has been implemented.

Before a pilot:

- Define justified retention periods for logs, evaluation records and any stored user data.
- Provide a contact route for applicable access, correction, deletion and other rights requests.
- Verify identity only to the extent necessary.
- Coordinate provider-held data requests with the relevant account owner.
- Document provider retention, backup and deletion limitations.

The absence of accounts does not remove these obligations where personal data is processed.

## 6. Security and Deployment

Current development measures include keeping credentials outside source control, escaping user and model text before HTML display, and limiting input length.

These measures do not constitute a complete security assessment.

The app currently runs locally. WiFi testing used HTTP rather than HTTPS. The temporary firewall allowance was removed after testing.

Before external testing, review HTTPS, access restrictions, abuse controls, credential management, logging and breach-response procedures. Confirm that support and research links contain no submission data.

Provider agreements, roles, subprocessors, processing locations and any required international-transfer safeguards remain unverified.

## 7. DPIA Screening

A formal DPIA screening has not been completed.

Assess the intended processing against GDPR Article 35 and the Portuguese CNPD mandatory DPIA list, including Regulation 798/2018. AI use alone does not settle whether a DPIA is required.

Consider sensitive disclosures, vulnerable users, third-party information, scale and the consequences of inappropriate guidance. Complete a DPIA before relevant processing if required, and assess whether prior supervisory consultation is necessary.

## 8. Current Status and Next Actions

| Area | Status |
| --- | --- |
| Current data flow | Described at development level |
| Data minimisation | Partly implemented |
| Lawful basis and Article 9 condition | Not finalised |
| Privacy notice and contact route | Not implemented |
| Retention and user-rights procedures | Not implemented |
| Provider agreements and account responsibilities | Not verified |
| Processing locations and transfers | Not verified |
| Security review for external testing | Incomplete |
| DPIA screening | Pending |
| LangSmith evaluation | Fictional cases only |

Next actions:

1. Verify provider controls and responsibilities with the Ironhack account owner.
2. Finalise the intended pilot audience, hosting and processing purposes.
3. Complete lawful-basis and DPIA screening work.
4. Prepare an accurate privacy notice and rights contact route.
5. Implement and test the required retention, access and security controls.

The current evidence does not establish GDPR compliance. Continue development evaluation using fictional scenarios while the real-user arrangements remain unresolved.

## Sources

- [GDPR, Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)
- [CNPD: Data Protection Impact Assessment](https://www.cnpd.pt/organizacoes/outras-obrigacoes/avaliacao-de-impacto/)
- [OpenAI API data controls](https://developers.openai.com/api/docs/guides/your-data)

Provider documentation must be checked against the actual account configuration.