# Week 2 Summary — ETL + EDA

## Key findings
- Orders processed: 100 total orders were successfully ingested and transformed.
- Users coverage: 104 user records were loaded; all users are unique on `user_id`, enabling a valid many-to-one join.
- Join integrity: Each order maps to at most one user, and the left join preserved the original order count (no join explosion).
- Outliers identified: Extreme values in the `amount` column were winsorized, and an outlier flag was added to retain visibility for analysis.
- Time-based features added: Order timestamps were parsed in UTC and enriched with month and day-of-week features to support temporal analysis.

## Definitions
- Revenue: Sum of `amount` across all orders (raw amount retained; winsorized version used for robustness).
- Refund: An order where `status_clean == "refund"` after text normalization and mapping.
- Refund rate: Number of refunded orders divided by total orders.
- Time window: Based on `created_at` timestamps parsed in UTC.
- Outlier (amount): An order amount outside the IQR-based bounds (k = 1.5), flagged after winsorization.

## Data quality caveats
- Missingness: Missing values in numeric fields (`amount`, `quantity`) are explicitly flagged rather than dropped.
- Timestamps: Some records may have missing `created_at` values, which are tracked in run metadata.
- Join coverage: Orders without a matching user retain null user attributes (expected behavior for a left join).
- Outliers: Winsorization limits extreme values for analysis but preserves the original amount for reference.

## Next questions
- How do revenue and refund rates vary by country or signup cohort?
- Are outliers concentrated in specific time periods or user segments?
- Do order volumes or average amounts differ by day of week or month?
