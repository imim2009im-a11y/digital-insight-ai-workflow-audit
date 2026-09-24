# Technical Guardrails

These guardrails apply to any future implementation.

## Access
- least privilege,
- time-bounded credentials,
- no shared personal accounts,
- no credential storage in Git,
- explicit production authorization.

## Data
- minimum necessary data,
- synthetic/test data where possible,
- no raw customer export by default,
- retention must be defined,
- deletion path must exist.

## AI
- human approval for material actions,
- no autonomous financial/payment actions,
- no hallucinated customer facts,
- no silent model changes in production,
- evaluation before scale.

## Operations
- logs without secrets,
- rollback plan,
- owner for each automation,
- failure notification,
- manual fallback for critical workflows.

## Claims
No marketing claim may exceed what measured evidence supports.
