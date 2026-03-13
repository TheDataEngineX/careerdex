---
applyTo: "src/**/ml/**/*.py,src/**/phases/phase4*"
---

# ML — CareerDEX Specifics

## Models
- Resume-Job Matcher: cosine similarity + skill overlap + location + salary
- Salary Predictor: XGBoost-style with percentile ranges (p25/p50/p75)
- Skill Gap Analyzer: TF-IDF based skill demand scoring
- Career Path Recommender: Graph-based traversal with transition probabilities
- Churn Predictor: Logistic regression for user engagement risk

## Conventions
- Use `from loguru import logger` (not structlog) in all ML modules
- Model lifecycle: development → staging → production → archived
- All predictions return confidence scores
