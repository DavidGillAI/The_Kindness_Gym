# The Kindness Gym: Preliminary GDPR Assessment

Assessment updated: 9 October 2026
Status: Hosted beta controls partly implemented and tested. Lawful-basis, provider and other privacy work remains incomplete; this assessment does not establish GDPR compliance.

## 1. Current Scope

The current MVP is a FastAPI web app. A user submits an everyday dilemma, which is sent to an OpenAI model. The app displays AI guidance and, where relevant, a separately selected research card.

The MVP does not include accounts, conversation history, course progress, payments or the proposed 21-day programme.

The n8n proof of concept remains a separate project artefact. Its provider settings require separate review if it is used again.

LangSmith is used to evaluate fictional scenarios. Live user submissions are not intentionally included in that evaluation workflow.

This assessment covers the hosted Render app, Neon beta-access database and optional Google Forms feedback route, as well as fictional evaluation. Deployment occurred on 8 October. The planned six-week pilot is not recorded as started. Technical deployment does not establish readiness for unrestricted public use.

## 2. Data Flow and Minimisation

| Data | Current use | Privacy consideration |
| --- | --- | --- |
| Dilemma text | Sent to OpenAI to generate guidance | May contain personal data about the user or other people |
| Generated guidance | Returned to the browser | May repeat personal information from the submission |
| Request metadata | Local and hosted server/provider logs | May include IP addresses and request details; actual retention requires verification |
| Beta access and usage records | Neon stores tester reference, code hash, active status, submission date and reservation timestamp | Pseudonymous access and quota records; not anonymous if linked to invitations |
| Private invitation records | Founder retains codes and tester references outside the repository | Keep private; define access, retention and deletion separately |
| Optional feedback | Submitted directly to Google Forms | May contain personal information even without email collection |
| Timing and token metrics | Printed in the terminal | Used for technical evaluation |
| Fictional evaluation inputs and outputs | Stored in LangSmith and project files | Must remain fictional and free of real identifying details |
| API and database credentials | Local environment file and separately configured Render environment variables | Must remain private and excluded from Git, documentation and slides |

The interface asks users to leave out names and identifying details. That reminder reduces risk but does not prevent sensitive disclosures.

The app has no implemented conversation-history database. Neon stores access and usage records, not dilemma text or generated guidance. The access code is submitted to the app for validation; only its hash is retained in the database. This does not mean that browsers, providers or development tools retain nothing.

Before a pilot, verify every location where submissions, responses or metadata could be recorded, including exception logs and any enabled tracing.

## 3. Sensitive Information and Lawful Basis

Free-text dilemmas may disclose health information, religious or philosophical beliefs, sexual orientation, or information about other identifiable people.

Not every personal disclosure is special-category data. Where Article 9 applies, processing needs both an Article 6 lawful basis and an applicable Article 9 condition.

Neither basis has been finalised for real-user operation. Explicit consent is a possible condition, not an automatic solution.

Avoiding sensitive questions and displaying a disclaimer do not remove obligations when sensitive information is actually processed. Safety response instructions are not a privacy consent mechanism.

Before real-user testing, document the processing purposes, lawful bases and approach to unexpected sensitive disclosures. Establish any necessary consent and withdrawal arrangements.

## 4. Providers and Account Responsibilities

### OpenAI

The app uses an API key supplied through the Ironhack instance account. The teacher has explicitly authorised its use for external beta testing. This permission does not settle controller/processor roles, contractual arrangements or project-level data controls, which still require verification.

Requests use `store=False`. This setting must not be described as Zero Data Retention. OpenAI documents separate abuse-monitoring and caching arrangements, with behaviour dependent on the endpoint and account configuration.

Do not assume that the developer can change organisation-level controls or delete all provider-held data.

### LangSmith

The evaluation uses the EU LangSmith endpoint and stores fictional inputs, rendered outputs and experiment information.

Using an EU endpoint does not establish all contractual, subprocessor, retention or transfer arrangements. These remain to be verified.

Keep evaluation uploads restricted to fictional cases. Do not enable live-user tracing without a documented purpose, privacy review and appropriate controls.

### Render and Neon

The app uses Render Free hosting in Frankfurt and Neon Free Postgres in AWS Frankfurt. Selected regions do not establish that all provider processing remains in the EU. Verify the actual account agreements, subprocessors, technical logs, backups, access controls and international-transfer arrangements.

Neon records are used to validate access codes and enforce quotas. Treat them as pseudonymous records where they can be linked to an invitation, rather than anonymous data. A code identifies an allowance, not a verified person.

### Other services

The research and support links open external websites. Their privacy arrangements are separate. Do not add user dilemma text or identifiers to those links.

Google Forms is covered in section 9. Any additional analytics or monitoring service must be reviewed before use.

## 5. Retention, Deletion and User Rights

A beta privacy notice and contact route are live: davidstevengill+beta_testers@gmail.com. The notice describes Render, OpenAI, Neon, optional feedback and the limits of application storage controls. It is an initial notice, not a completed Article 13 assessment.

The stated retention commitment is to delete beta access and usage records within 30 days after the beta ends. The MVP README documents a manual cleanup procedure. No automatic deletion job exists, and end-of-beta cleanup has not yet been run. Record the beta end date, deletion deadline and completion evidence.

The `remove_tester(tester_id)` function deletes a tester and its usage records. A temporary-record test confirmed that both were removed and the code then became invalid. This covers active application records, not all provider backups, logs or optional feedback. Verify requests against the original invitation before acting; a numeric reference alone is not proof of identity. Do not ask people to email their dilemma or access code.

A complete retention schedule and rights procedure remains unfinished, including feedback, private invitation mappings and provider-held records.

Before a pilot:

- Define justified retention periods for logs, evaluation records and any stored user data.
- Complete the procedure behind the implemented contact route for applicable access, correction, deletion and other rights requests.
- Verify identity only to the extent necessary.
- Coordinate provider-held data requests with the relevant account owner.
- Document provider retention, backup and deletion limitations.

The absence of accounts does not remove these obligations where personal data is processed.

## 6. Security and Deployment

Current development measures include keeping credentials outside source control, escaping user and model text before HTML display, and limiting input length.

These measures do not constitute a complete security assessment.

The app now runs on Render over HTTPS and uses TLS for Neon database connections. Credentials are configured separately in Render and locally. Earlier local WiFi testing used HTTP; its temporary firewall allowance was removed.

Private codes enforce one submission daily per code and an overall 20 daily, with resets based on Europe/Lisbon. Invalid-code and repeat-use rejection have been observed. The overall-cap boundary and concurrent-request behaviour still need explicit tests. Quotas reduce API use but do not replace broader abuse prevention or an account-level spending threshold.

Before external testing, review HTTPS, access restrictions, abuse controls, credential management, logging and breach-response procedures. Confirm that support and research links contain no submission data.

Provider agreements, roles, subprocessors, processing locations and any required international-transfer safeguards remain unverified.

## 7. DPIA Screening

A formal DPIA screening has not been completed.

Assess the intended processing against GDPR Article 35 and the Portuguese CNPD mandatory DPIA list, including Regulation 798/2018. AI use alone does not settle whether a DPIA is required.

Consider sensitive disclosures, vulnerable users, third-party information, scale and the consequences of inappropriate guidance. Complete a DPIA before relevant processing if required, and assess whether prior supervisory consultation is necessary.

## 8. Current Status and Next Actions

| Area | Status |
| --- | --- |
| Current data flow | Updated for Render, OpenAI, Neon and optional feedback; provider verification incomplete |
| Data minimisation | Partly implemented |
| Lawful basis and Article 9 condition | Not finalised |
| Privacy notice and contact route | Initial beta notice and contact live; full notice review incomplete |
| Retention and user-rights procedures | Tester removal tested; manual end-of-beta database cleanup documented; broader procedure incomplete |
| Provider agreements and account responsibilities | Not verified |
| Processing locations and transfers | Not verified |
| Security review for external testing | Incomplete |
| DPIA screening | Pending |
| LangSmith evaluation | Fictional cases only |

Next actions:

1. Verify provider controls and responsibilities with the Ironhack account owner.
2. Confirm the intended adult pilot audience and processing purposes; hosting is selected and deployed.
3. Complete lawful-basis and DPIA screening work.
4. Complete the existing notice and rights procedure, including lawful basis, feedback retention and provider limitations.
5. Implement and test the required retention, access and security controls.

The current evidence does not establish GDPR compliance. Continue development evaluation using fictional scenarios while the real-user arrangements remain unresolved.

## 9. Round 2 Update: Optional Feedback Form

Update recorded: 6 October 2026.

The results page now links to a Google Form for voluntary feedback. This is separate from the initial research survey.

### Purpose and Data Flow

The form asks whether the response was helpful and whether anything felt inaccurate, pressuring or inappropriate. It also includes optional text boxes for general feedback and feature suggestions.

Only the helpfulness question is required. Using the feedback form itself is optional.

Feedback is submitted directly to Google Forms and stored separately from the app. The feedback link does not automatically include the dilemma, generated response or a user identifier.

Users could still manually paste personal or sensitive information into the optional text boxes.

### Implemented Measures

- Email collection is disabled.
- Google sign-in is not required.
- Respondents cannot view other people's response summaries.
- The form asks users to omit names, identifying details and private information.
- The form explains that feedback is not monitored for urgent help.
- The confirmation message states that feedback is reviewed periodically and is not an emergency support channel.

These settings reduce deliberate personal-data collection. They do not establish that responses are anonymous or that Google processes no personal data. Google may process technical information under its own privacy arrangements.

### Actions Required Before the Pilot

- Include Google Forms and its actual account arrangements in the provider review.
- Establish the applicable contractual roles, processing locations and any required transfer safeguards. Do not assume that a personal Google account has the same arrangements as a managed Google Workspace account.
- Expand the existing beta notice: it mentions optional Google Forms feedback and a rights contact, but the complete feedback purpose, data, recipients and justified retention period still need review.
- Document the lawful basis for feedback processing and how unexpected sensitive disclosures will be handled.
- Set a justified retention period and a review and deletion procedure.
- Check access permissions for the form and any linked spreadsheet or exported copies.
- Keep raw feedback out of GitHub, presentation materials and LangSmith evaluation uploads.
- Use aggregated findings or carefully de-identified summaries when reporting results.

The absence of email collection may make a particular response difficult to locate for a rights request. Do not collect additional identifying information solely to make responses identifiable.

### Status

The feedback link and reported minimisation settings are implemented. The initial beta notice now mentions Google Forms and a contact route. Feedback-specific retention, a complete notice and provider verification remain incomplete. The form settings were reported during development and should be rechecked before recruitment.

Adding this section does not establish GDPR compliance or readiness for real-user testing.

## Sources

- [GDPR, Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)
- [CNPD: Data Protection Impact Assessment](https://www.cnpd.pt/organizacoes/outras-obrigacoes/avaliacao-de-impacto/)
- [OpenAI API data controls](https://developers.openai.com/api/docs/guides/your-data)

- [Google Forms: View and manage responses](https://support.google.com/docs/answer/139706?hl=en)
- [Google Privacy Policy](https://policies.google.com/privacy)


Provider documentation must be checked against the actual account configuration.