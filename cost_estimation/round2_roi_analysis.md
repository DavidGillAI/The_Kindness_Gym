# The Kindness Gym: Round 2 Cost and ROI Analysis

Date: 4 October 2026
Status: Preliminary scenarios, not a sales forecast.

## Purpose

Estimate costs, returns and break-even over 12 and 36 months for a founder-built app with unpaid founder work and volunteer beta testers.

The Round 1 estimate in `cost_analysis.md` remains unchanged.

Supplier prices are researched. Customer numbers, operating budgets and founder hours are assumptions. No paid demand has been established.

## Proposed Business Model

Start with a six-week free pilot, allowing approximately two months for testing and review before a possible paid launch.

| Plan | Daily allowance | Monthly consumer price |
|---|---:|---:|
| Free | One dilemma | €0 |
| Plus | Up to three dilemmas | €0.99 |
| Premium | Up to ten dilemmas | €1.99 |

Prices and limits are proposals to test. Allowances are ceilings, not usage targets.

Accounts, payments and enforced limits are not implemented in the current MVP. The founder intends to build these without paid development support.

Survey participants may be invited separately to volunteer as beta testers. Survey participation does not itself mean agreement to testing.

Advertising revenue is €0 in all scenarios. Charity advertising may be considered later, with review for emotional pressure. It would be separate from guidance and would not use dilemma text for targeting.

## AI Costs

The provisional model is `gpt-5.6-luna`, with reasoning effort `none`.

Recent evaluation requests used approximately 1,350 input tokens and 250 output tokens.

Published prices per million tokens:

| Token type | USD price |
|---|---:|
| Input | $0.20 |
| Cached input | $0.02 |
| Cache writes | $0.25 |
| Output | $1.20 |

Treating all input as a fresh cache write:

(1,350 × $0.25 + 250 × $1.20) / 1,000,000
= $0.0006375 per dilemma.

| Usage over 30 days | Estimated AI cost |
|---|---:|
| One dilemma daily | $0.019 |
| Three daily | $0.057 |
| Ten daily | $0.191 |

Monthly euro allowances used in the forecast:

- Free user: €0.02.
- Plus subscriber: €0.06.
- Premium subscriber: €0.20.

These are planning allowances, not confirmed currency conversions or Ironhack charges.

Longer inputs, longer answers, reasoning, retries and price changes can increase costs. Actual usage and invoices must replace these estimates before launch.

## Payments and VAT

Stripe is the example payment provider, not an implemented integration.

Published Portuguese fees assumed:

- Standard EEA cards: 1.5% plus €0.25 per payment.
- Stripe Billing: an additional 0.7% of billing volume.

Other cards and services may cost more.

For modelling, consumer prices include 23% VAT, using mainland Portugal's standard rate. Actual tax treatment, exemptions and cross-border obligations require confirmation before selling.

| Plan | Consumer price | Revenue excluding assumed VAT | Payment fees | AI allowance | Contribution |
|---|---:|---:|---:|---:|---:|
| Plus | €0.99 | €0.805 | €0.272 | €0.06 | €0.473 |
| Premium | €1.99 | €1.618 | €0.294 | €0.20 | €1.124 |

Contribution is the amount available for shared running costs and recovery of initial spending.

Calculations use unrounded values.

## Initial Cash Budget

| Item | Assumed cash cost |
|---|---:|
| Founder development and deployment | €0 |
| Volunteer tester recruitment and incentives | €0 |
| External privacy and security review | €600 |
| Contingency reserve | €300 |
| Total cash budget | €900 |

The €600 review allowance is a placeholder, not a quote or confirmation that this amount will cover the necessary work.

Contingency is not an automatic expense. For prudence, the scenarios assume the entire €300 is spent. If unused, cash results improve by €300.

The founder does development work unpaid. No paid specialist development is assumed. If external help becomes necessary, the budget must increase.

The pilot also incurs hosting and AI costs from the start.

## Monthly Running Costs

| Item | Cash allowance |
|---|---:|
| Initial hosting | €10 |
| Database, email and monitoring reserve | €10 |
| Paid marketing and recruitment | €0 |
| Founder maintenance and support | €0 |
| Total before AI and payment fees | €20 |

Render is the proposed hosting option. A small paid web server starts at $7 monthly. It supports FastAPI, GitHub deployment and a Frankfurt hosting region.

The €10 hosting allowance is a rounded euro budget, not a supplier quotation.

The additional €10 is a provisional allowance for commercial features. Services may not be needed during the initial pilot, or may cost more later.

Render's free server sleeps after 15 minutes without traffic and takes approximately one minute to restart. Paid hosting is assumed.

These small operating allowances are starting assumptions. They are not verified capacity or cost estimates for thousands of users.

## Recording Founder Time

Founder work has no cash charge in the forecast.

A separate view values:

- Initial work: 100 hours × €20 = €2,000.
- Maintenance and support: four hours monthly × €20 = €80 monthly.

These are illustrative estimates of time value, not wages owed or amounts paid.

Initial investment including time: €2,900.

Monthly shared costs including time: €100, before AI and payment fees.

Earlier course work is excluded. Additional unpaid recruitment, support or development time must be recorded if it exceeds these allowances.

## Customer Scenarios

All customer numbers are illustrative and unvalidated.

The paying audience is assumed to comprise 60% Plus and 40% Premium subscribers.

Average monthly contribution per paying subscriber:

(60% × €0.473098) + (40% × €1.124106)
= approximately €0.734.

| Scenario | Year 1 free / paid | Year 2 free / paid | Year 3 free / paid |
|---|---:|---:|---:|
| Conservative | 200 / 10 | 500 / 25 | 1,000 / 50 |
| Middle | 500 / 50 | 1,500 / 150 | 3,000 / 300 |
| Optimistic | 1,000 / 150 | 3,000 / 450 | 6,000 / 900 |

These are average monthly active users, not year-end totals. Free users are additional to subscribers.

Year 1 has ten paid months after the pilot and review. Free-user costs and shared expenses run for twelve months.

Years 2 and 3 each have twelve paid months.

Unpaid recruitment is assumed. There is no evidence that the founder can acquire or retain these audiences without advertising expenditure.

## Calculations

Monthly subscription revenue excluding assumed VAT:

Paid subscribers ×
[(60% × €0.99 + 40% × €1.99) / 1.23].

Cash result:

Revenue excluding VAT
− payment fees
− all users' AI costs
− shared cash expenses
− initial cash budget.

Result including founder time:

Cash result − estimated value of founder work.

Cost-based ROI:

Result / total corresponding costs × 100.

Cash ROI excludes founder time from both result and costs.

ROI including time includes its estimated value in both.

These are simple, undiscounted measures before income tax.

## 12 and 36 Month Results

| Scenario | Period | Revenue excluding VAT | Cash result | Cash ROI | Result including time | ROI including time |
|---|---:|---:|---:|---:|---:|---:|
| Conservative | 12 months | €113 | −€1,115 | −90.8% | −€4,075 | −97.3% |
| Conservative | 36 months | €1,130 | −€1,294 | −53.4% | −€6,174 | −84.5% |
| Middle | 12 months | €565 | −€893 | −61.3% | −€3,853 | −87.2% |
| Middle | 36 months | €6,667 | €1,508 | 29.2% | −€3,372 | −33.6% |
| Optimistic | 12 months | €1,695 | −€280 | −14.2% | −€3,240 | −65.7% |
| Optimistic | 36 months | €20,002 | €8,963 | 81.2% | €4,083 | 25.6% |

Euro results are rounded.

The middle scenario recovers cash spending within three years, but does not cover the estimated value of founder time.

Only the optimistic scenario covers both within three years.

Cash surplus is not take-home income. Applicable income taxes and unmodelled expenses may reduce the amount available to the founder.

## Break-even

At 1,500 active free users:

- Free-user AI costs: €30 monthly.
- Shared cash expenses: €20 monthly.
- Estimated founder time: €80 monthly.

Cash operating break-even:

(€20 + €30) / €0.733501
= approximately 69 paying subscribers.

Operating break-even including time:

(€20 + €30 + €80) / €0.733501
= approximately 178 paying subscribers.

These figures cover monthly operations only, not initial investment.

Assuming even income within each modelled year:

| Scenario | Recovery of initial cash budget | Recovery including founder time |
|---|---|---|
| Conservative | Not within 36 months | Not within 36 months |
| Middle | Approximately month 26 | Not within 36 months |
| Optimistic | Approximately month 14 | Approximately month 27 |

Actual growth, cancellations and spending will change payback timing.

## Risks and Sensitivities

| Risk | Financial effect | Response |
|---|---|---|
| Users do not pay for higher limits | Low subscription revenue | Test willingness to pay |
| Subscribers cancel quickly | Recruitment must replace them | Measure retention and cancellations |
| Volunteer recruitment does not scale | Growth falls short or marketing costs rise | Track recruitment effort and results |
| Free usage grows faster than paid usage | Higher costs without matching revenue | Monitor usage and enforce appropriate limits |
| Low prices leave little contribution | Limited money for development and support | Review pricing after the pilot |
| AI usage or prices rise | Response costs exceed allowances | Monitor invoices and usage |
| Support and infrastructure need more resources | Cash costs and founder hours increase | Reforecast as usage grows |
| External review or specialist help costs more | Larger initial investment | Obtain quotes before committing |
| Tax treatment differs | Net revenue changes | Confirm obligations before selling |
| Charity adverts undermine trust | Lower engagement without reliable income | Exclude advertising from the base forecast |

Each additional 1,000 free users adds approximately €20 monthly AI costs under the current assumption.

Each additional €100 monthly expense requires approximately 137 more paying subscribers at the assumed mix.

Keeping founder work unpaid reduces cash expenditure. It does not eliminate the workload or establish that the business can eventually provide a sustainable income.

## Pilot Measures

Measure:

- Whether guidance is useful.
- Repeat use and dilemmas submitted.
- Willingness to pay at each proposed price.
- Typical and unusually high token usage.
- Founder development, recruitment and support hours.
- Unsuitable responses and safety failures.
- Hosting performance and actual expenses.

Survey participants should opt into testing separately. Recruitment must use contact details appropriately.

Interest in a free app does not establish demand for a subscription.

## Decision

A founder-built pilot with volunteer testers needs less cash than the original outsourcing scenario.

Budget provisionally for €900 upfront and €20 monthly, plus AI usage. These figures must be revised when external review needs and service requirements are clearer.

The middle scenario produces a cash surplus within three years while relying on unpaid founder work. The optimistic scenario also covers the illustrative value of that work.

Proceed with a small pilot, then revisit prices, costs and growth assumptions before commercial launch.

## Limitations

This is a planning exercise, not proof of profitability.

It excludes income tax, financing costs, inflation and discounting.

Refunds, disputes, supplier taxes, insurance, ongoing professional oversight and major incidents are not separately priced.

The model assumes unchanged supplier prices, modest infrastructure costs and limited founder hours for 36 months. Those assumptions may become unrealistic as usage grows.

The current MVP does not implement accounts, payments or daily allowances.

## Sources

Supplier prices checked on 4 October 2026:

- OpenAI model pricing:
  https://developers.openai.com/api/docs/models/gpt-5.6-luna
- OpenAI API pricing:
  https://developers.openai.com/api/docs/pricing
- Stripe Portuguese pricing:
  https://stripe.com/en-pt/pricing
- Render pricing:
  https://render.com/pricing
- Render FastAPI deployment:
  https://render.com/docs/deploy-fastapi
- Render regions:
  https://render.com/docs/regions
- Render free-service limitations:
  https://render.com/docs/free
- Portuguese VAT Code, Article 18:
  https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/civa_rep/Pages/iva18.aspx

Token measurements come from project evaluation logs.

Customer numbers, subscriber mix, euro allowances, external review budget and founder hours are assumptions.