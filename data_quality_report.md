# Data Quality Report

## Missing Values Audit

The healthcare operations dataset was audited for missing values in key operational and financial fields

| Field          | Missing Records |
| -------------- | --------------- |
| Doctor         | 1,771           |
| Hospital       | 1,193           |
| Billing Amount | 1,168           |

### Observations

- Missing Doctor values may indicate incomplete provider assignment.
- Missing Hospital values may result from multi-site export aggregation issues.
- Missing Billing Amount values may indicate pending or failed charge exports.

## Duplicate Record Audit

The dataset was reviewed for duplicate records that may have resulted from repeated exports or append operational files.

| Audit Type               | Duplicate Records Identified |
| ------------------------ | ---------------------------- |
| Full Row Duplicate Audit | 3,796                        |

## Observations

- Duplicate healthcare records can artificially inflate operational metrics such as admissions, billing totals, and provider utilization.
- Duplicate records should be resolved before reporting or dashboard development.