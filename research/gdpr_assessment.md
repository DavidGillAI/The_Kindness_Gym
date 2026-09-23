# The Kindness Gym: Preliminary GDPR Assessment

Assessment date: 23 September 2026
Status: Preliminary Ironhack Round 1 assessment

## 1. Personal Data and Data Minimisation

### Purpose

Identify what personal data the proposed application
needs, what information it might receive and how
unnecessary collection can be avoided.

### Proposed Data Categories

| Data | Purpose | Initial Approach |
|---|---|---|
| Account identifier | Maintain an optional user account | Use a pseudonymous identifier where possible |
| Course progress | Track completed exercises | Store only necessary progress data |
| User preferences | Personalise exercises | Make optional and minimise collection |
| Conversation text | Generate contextual AI guidance | Process only what is needed for the response |
| Technical logs | Security and troubleshooting | Minimise content and limit retention |

These are proposed categories, not evidence that
the existing POC already implements them.

### Potentially Sensitive Information

Users might voluntarily disclose information about:

- Physical or mental health.
- Religious or philosophical beliefs.
- Sexual orientation or relationships.
- Financial difficulties.
- Family circumstances.
- Other identifiable individuals.

Not all personal disclosures are special-category
data under GDPR.

However, disclosures involving health, religion,
sexual orientation or other Article 9 categories
may trigger additional legal requirements.

### Data Minimisation Measures

The proposed pilot should:

1. Avoid requesting real names where unnecessary.
2. Avoid requesting medical histories or diagnoses.
3. Allow users to describe situations without
   identifying the people involved.
4. Avoid storing conversation histories by default
   unless a justified purpose requires retention.
5. Store minimal course-progress information.
6. Define retention periods for each data category.
7. Avoid collecting information merely because
   it might become useful in the future.

### Important Design Decision

The 21-day course should not require users to
disclose sensitive personal experiences.

Users should be able to complete exercises
without submitting identifiable reflections
to an AI system.

### Current POC Status

The current n8n POC processes messages entered
through its chat interface and sends them to
an OpenAI model.

Its exported workflow does not establish the
complete retention arrangements of n8n,
OpenAI or the hosting environment.

The POC has been tested using fictional scenarios.

Production data storage, retention and
deletion procedures have not been implemented
or verified.

### Preliminary Conclusion

A data-minimisation approach could substantially
reduce the amount of personal information
required by the application.

However, free-text AI conversations create
a foreseeable risk of receiving sensitive
information even when it is not requested.

The pilot therefore requires additional
technical and organisational safeguards.

## 2. Lawful Basis for Processing

### Relevant Legislation

GDPR Articles 6, 7 and 9.

### Proposed Processing Activities

| Processing Activity | Potential Lawful Basis |
|---|---|
| Creating an optional account | Performance of a contract |
| Storing essential course progress | Performance of a contract |
| Processing messages to generate AI guidance | To be determined based on the final service design |
| Optional personalisation | Consent or another justified lawful basis |
| Optional marketing communications | Consent, subject to applicable rules |
| Essential security logging | Potentially legitimate interests |

These are preliminary possibilities, not final legal determinations.

Each processing purpose must have an identified and documented lawful basis before deployment.

### Consent Requirements

Where consent is used, it must be:

- Freely given.
- Specific to the processing purpose.
- Informed.
- Unambiguous.
- Demonstrable and easy to withdraw.

Consent should not be bundled with unrelated processing activities.

Users must not be required to accept unnecessary data processing merely to access the core service.

### Special-Category Data

Users may voluntarily disclose health information,
religious beliefs or other special-category data
during conversations.

Processing such information requires both an
Article 6 lawful basis and an applicable Article 9
condition.

Explicit consent under Article 9(2)(a) is one possible
condition, but it must not automatically be assumed
to be appropriate or sufficient.

The preferred initial design is to avoid requesting
special-category data and minimise opportunities
for unnecessary collection.

Before the pilot, the project must determine how
unexpected sensitive disclosures will be handled,
including whether they will be processed, rejected,
redacted or deleted.

### Proposed Implementation

Before public deployment:

1. Identify the purpose of each processing activity.
2. Document an appropriate Article 6 lawful basis.
3. Determine whether any activity involves
   special-category data.
4. Identify an applicable Article 9 condition
   wherever required.
5. Implement appropriate consent and withdrawal
   mechanisms where consent is relied upon.
6. Explain the processing clearly in the privacy notice.

### Current Status

The n8n POC processes fictional test scenarios.

It does not implement a documented lawful-basis
register, consent-management system or procedures
for handling unexpected sensitive disclosures.

Status: Assessment in progress; implementation pending.S

## 3. Data Retention, Deletion and User Rights

### Relevant Legislation

GDPR Articles 5, 12–20.

### Proposed Retention Approach

The Kindness Gym should avoid retaining personal
information beyond what is necessary to provide
the service.

Proposed arrangements:

- Account data: Retain while the account is active,
  subject to applicable legal requirements.
- Course progress: Retain only while needed to
  provide the chosen course experience.
- AI conversations: Avoid permanent storage
  by default.
- Technical logs: Establish a short, justified
  retention period.
- Optional research participation: Store separately
  where appropriate and apply documented
  retention rules.

Specific retention periods must be established
and justified before public deployment.

### User Rights

The pilot should provide procedures that allow
users to exercise applicable GDPR rights, including:

- Accessing their personal data.
- Correcting inaccurate personal data.
- Requesting deletion of their information.
- Requesting restriction of processing.
- Objecting to processing where applicable.
- Requesting data portability where applicable.
- Withdrawing consent where consent is used.

Requests must be handled within the applicable
GDPR deadlines.

### Proposed Implementation

Before deployment:

1. Create a documented retention schedule.
2. Establish account and data deletion procedures.
3. Provide an accessible method for submitting
   data protection requests.
4. Define procedures for responding to requests
   and verifying identity where necessary.
5. Determine how deletion requests will be
   handled across n8n, OpenAI and other providers.
6. Document any legally justified exceptions
   to deletion.

### Important Technical Consideration

Deleting information from The Kindness Gym's
own database does not automatically establish
that copies held by external service providers
have also been deleted.

Provider retention, backup and deletion
arrangements must be verified.

### Current POC Status

The exported n8n workflow establishes that
user messages are passed to an OpenAI model.

It does not establish the complete retention
and deletion arrangements of the services
involved.

No production retention schedule or user
rights procedures have been implemented.

Status: Planned; provider arrangements
and technical implementation require review.

## 4. Security, Third-Party Processors and International Transfers

### Relevant Legislation

GDPR Articles 28, 32 and 44–49.

### Controller and Processor Responsibilities

For the proposed pilot, The Kindness Gym would
need to identify the organisation responsible
for determining the purposes and means of
personal-data processing.

This organisation would generally act as the
data controller.

External services processing personal data
on its behalf may act as data processors.

The precise roles of each provider must be
verified before deployment.

### Third-Party Services

The current proof of concept uses:

- n8n for workflow automation.
- OpenAI for AI-generated responses.

The proposed pilot may also require hosting,
authentication, database and analytics services.

Before deployment, the project must:

1. Identify all providers processing personal data.
2. Review their data processing agreements.
3. Identify relevant subprocessors.
4. Verify applicable security and retention arrangements.
5. Establish the geographical locations of processing.

The current assessment does not establish
that any particular hosting or API configuration
is GDPR-compliant.

### Security Measures

The pilot should implement appropriate
technical and organisational safeguards,
including:

- Encryption in transit and, where appropriate,
  encryption of stored personal data.
- Restricted access to user information.
- Secure storage of API keys and credentials.
- Appropriate authentication for administrative access.
- Minimised logging of conversation content.
- Regular review of system access and permissions.
- Procedures for identifying and responding
  to personal-data breaches.
- Testing and periodic review of security controls.

Specific controls must be selected according
to the actual risks and system architecture.

### International Data Transfers

Before public deployment, the project must
establish whether personal data will be
transferred outside the European Economic Area.

Where such transfers occur, the project must
identify an applicable GDPR transfer mechanism.

Depending on the destination and circumstances,
this may involve:

- A European Commission adequacy decision.
- Appropriate safeguards, such as Standard
  Contractual Clauses.
- Additional assessments or supplementary
  measures where required.

Using a European hosting location does not,
by itself, establish that all processing and
subsequent transfers remain within the EEA.

### Current POC Status

The exported n8n workflow confirms that
chat messages are sent to an OpenAI model.

However, the export does not establish:

- The location of all data processing.
- Applicable data processing agreements.
- Complete subprocessor arrangements.
- Actual data retention settings.
- International transfer mechanisms.
- The security configuration of the hosting
  environment.

These matters require verification using
the actual provider agreements and
deployment configuration.

### Preliminary Conclusion

Third-party processing and international
transfers require additional investigation
before The Kindness Gym can be publicly deployed.

Status: Not yet verified.

## 5. Data Protection Impact Assessment (DPIA)

### Relevant Legislation

GDPR Articles 35 and 36.

Portuguese CNPD Regulation 798/2018.

### Purpose

Determine whether the proposed processing of
personal data requires a formal Data Protection
Impact Assessment before public deployment.

### Preliminary Risk Screening

The following characteristics require examination:

1. AI-generated guidance based on personal
   descriptions of everyday situations.

2. Potential processing of highly personal
   information, including unexpected disclosures
   of special-category data.

3. Possible future personalisation using previous
   conversations and behavioural information.

4. The use of external AI and automation providers.

5. The possibility of collecting information
   about vulnerable individuals.

The presence of AI does not automatically make
a DPIA mandatory. The nature, scope, context
and purposes of the processing must be assessed.

### Preliminary Assessment

The currently proposed pilot is small in scale
and is not intended to make automated decisions
with legal or similarly significant effects.

However, its free-text conversational interface
may receive sensitive or highly personal data.

Its use of AI and proposed personalisation
features also warrant closer examination.

At this stage, insufficient information is
available to make a final determination
about whether a DPIA is legally mandatory.

### Required Actions

Before public deployment:

1. Complete a documented DPIA screening
   using the final processing architecture.

2. Review GDPR Article 35 and the applicable
   Portuguese CNPD mandatory DPIA list.

3. Identify the categories and expected
   volume of personal data processed.

4. Assess the likelihood and severity of
   potential harm to individuals.

5. Document measures designed to reduce
   identified risks.

6. Complete a formal DPIA before processing
   begins if the screening establishes that
   one is required.

7. Consult the CNPD before processing if
   a required DPIA identifies residual
   high risks that cannot be sufficiently
   mitigated.

### Current Status

The project has identified preliminary
privacy risks and proposed safeguards.

A formal DPIA screening has not yet
been completed.

A full DPIA has not been conducted.

Status: Further assessment required
before public deployment.

## 6. Preliminary Conclusion and Action Plan

### Preliminary Conclusion

The Kindness Gym could be designed to minimise
personal-data collection while providing its
core personal-development features.

However, its conversational AI interface may
receive sensitive personal information even
when the application does not request it.

The current n8n proof of concept has not been
assessed or configured as a GDPR-compliant
production system.

### Required Actions Before Public Deployment

1. Finalise the personal data collected by
   each feature and document its purpose.

2. Establish and document the appropriate
   lawful basis for every processing activity.

3. Determine how unexpected special-category
   data will be handled.

4. Prepare a clear, accessible privacy notice.

5. Implement justified retention periods,
   deletion procedures and user rights processes.

6. Verify provider agreements, security controls,
   processing locations and international transfers.

7. Complete a documented DPIA screening and
   conduct a full DPIA if required.

8. Implement appropriate privacy and security
   safeguards before processing real user data.

9. Test these safeguards before inviting
   participants to a public pilot.

### Current Assessment Status

| Assessment Area | Status |
|---|---|
| Data categories and minimisation | Preliminary assessment completed |
| Lawful bases | Not finalised |
| Special-category data handling | Not implemented |
| Retention and user rights | Not implemented |
| Provider and transfer arrangements | Not verified |
| Security controls | Not fully assessed |
| DPIA screening | Pending |
| Privacy notice | Not prepared |

### Overall Status

Preliminary academic GDPR assessment completed.

The assessment identifies the principal privacy
risks and the work required before a public pilot.

It does not establish that The Kindness Gym
currently complies with the GDPR.

The final system architecture, processing
arrangements and safeguards must be reviewed
before deployment.

### Regulatory Considerations

**EU AI Act**
- Preliminary assessment: non-high-risk AI system,
  based on the currently proposed functionality.
- Implement clear user-facing AI disclosure.
- Document AI literacy and operational safeguards.
- Test for harmful or manipulative guidance.

**GDPR**
- Minimise personal data collection.
- Establish lawful bases and procedures for
  handling sensitive disclosures.
- Verify third-party processing, retention,
  deletion and international transfers.
- Complete a DPIA screening before deployment.

**Current status:**
Preliminary assessments completed.
Production compliance has not been established.

## Regulatory Assessments

Preliminary regulatory assessments have been completed:

- `research/eu_ai_act_assessment.md`
- `research/gdpr_assessment.md`

The EU AI Act assessment considers intended purpose,
risk classification, transparency, AI literacy and
prohibited AI practices.

The GDPR assessment covers data minimisation,
lawful bases, user rights, retention, third-party
processing, international transfers and DPIA screening.

Both assessments identify actions required before
public deployment. They do not establish that the
current proof of concept is legally compliant.