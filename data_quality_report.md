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

