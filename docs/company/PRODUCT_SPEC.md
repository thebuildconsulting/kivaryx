# Kivaryx — realistic synthetic product specification

## User journeys and screen map

| Surface | Audience | Required experience | Initially supported |
|---|---|---|---|
| `/` | Prospective merchants | Fictional marketing landing page; product/value, CTA into demo | Yes |
| `/app` | Merchant operator | KPI cards, transaction history, status/risk badges, new synthetic payment, trace IDs, transaction drill-down | Yes |
| `/ops` | Internal support/risk analyst | Cross-merchant synthetic transaction view, risk state and events, read-only incident evidence | Yes |
| Future merchant onboarding | Merchant admin | Demo API credentials, client config, webhook simulator | Planned |
| Future risk workspace | Risk analysts | Model versions, drift signals, rules and review queue | Planned |
| Future AI assistant | Approved operator | Retrieval grounded in synthetic runbooks and read-only tool access | Planned |

## Data model

- Merchant: `merchant_id`, `display_name`, `sector`, `status`.
- Transaction: `transaction_id`, `merchant_id`, `amount_minor`, `currency`, `status`, `risk_score`, `risk_reason`, `model_version`, `provider_reference`, `request_id`, `idempotency_key`, `created_at`.
- Transaction event: `event_id`, `transaction_id`, `stage`, `details`, `created_at`.
- Mock payment request: merchant, amount in minor units, currency, idempotency key, fake payment-method token (`pm_demo_...` if shown). No PAN/CVV/bank account details, no real person IDs.

## Product invariants

1. Any output is stamped **fictional / synthetic** in the application.
2. Same merchant + same idempotency key + identical payload yields the same transaction, not a duplicate.
3. Same merchant + key + different payload is rejected as conflict.
4. Every transaction gets an immutable-looking ID, request ID and chronological event trail.
5. Scoring result includes **simulated** model version, reason and numeric score; no claim of trained ML until a genuine model is introduced and evaluated.
6. Processor outcomes `approved`, `declined` and `requires_review` are synthetic deterministic test scenarios.
7. The UI works locally with backend APIs, not screenshots of invented data. Risk/approval figures are aggregate queries over seeded SQLite rows.
8. Cross-merchant role and login in v3 are **simulation only**. Do not expose prototype publicly; real authenticated access, authorisation and isolation are later Codex requirements.

## Later quality bar

- Responsive React/Next or equivalent UI selected via ADR after Codex reviews constraints.
- Independent APIs and workers, Postgres persistence, queue/outbox decision, schema migrations, trace propagation, synthetic seeding, deterministic load tests and multiple environment configurations.
- Browser E2E tests and API schema contract tests.
- Clearly labelled incident injection and post-change measurements. No uncontrolled failures leaking into baseline.
