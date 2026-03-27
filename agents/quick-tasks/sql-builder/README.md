# SQL Query Builder

> **Quick Task Agent - Instant Results**

## Overview
Natural language to SQL and SQL optimization. For developers and analysts who work with databases.

## Capabilities
- Natural language → SQL query
- SQL → Natural language explanation
- Query optimization suggestions
- Index recommendations
- Schema exploration
- Join optimization
- Query debugging

## Input
```json
{
  "action": "build|explain|optimize|debug",
  "natural_language": "show me users who signed up last week",
  "schema": "optional table definitions",
  "dialect": "postgres|mysql|sqlite|bigquery"
}
```

## Output
```json
{
  "sql": "SELECT * FROM users WHERE created_at >= NOW() - INTERVAL '7 days'",
  "explanation": "Selects all columns from users table...",
  "optimization": "Consider adding index on created_at",
  "estimated_cost": "Low"
}
```

## Pricing
- **Free**: 30 queries/day
- **Pro**: $4.99/mo unlimited

## Revenue Potential
$300-1,500/month

---

*Quick Task Agent - Database assistant*
