---
applyTo: "src/**/dags/**/*.py,src/**/phases/phase2*"
---

# Data Pipelines — CareerDEX Specifics

## Architecture
- Medallion pattern: Bronze (raw) → Silver (cleaned) → Gold (aggregated)
- Pipelines must be idempotent — log processing counts/IDs

## Connectors
- LinkedIn, Indeed, Glassdoor (API stubs)
- JSON and CSV file connectors (implemented)
- All connectors inherit from `JobSourceConnector` ABC

## Quality
- `SchemaValidator` for job postings and user profiles
- `QualityScorer` for scoring record completeness
- `DeduplicationEngine` for hash-based dedup
- `DataHash` for deterministic record hashing
