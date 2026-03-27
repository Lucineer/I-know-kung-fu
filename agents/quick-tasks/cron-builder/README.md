# Cron Expression Builder

> **Quick Task Agent - Instant Results**

## Overview
Build, explain, and validate cron expressions. Never struggle with cron syntax again.

## Capabilities
- Natural language → cron expression
- Cron expression → human readable
- Validate cron syntax
- Next run times preview
- Timezone conversion
- Common patterns library

## Input
```json
{
  "action": "build|explain|validate|preview",
  "description": "every weekday at 9am",
  "cron": "0 9 * * 1-5",
  "timezone": "America/New_York"
}
```

## Output
```json
{
  "cron": "0 9 * * 1-5",
  "human": "At 9:00 AM, Monday through Friday",
  "next_runs": ["2024-03-04 09:00", "2024-03-05 09:00", ...],
  "valid": true
}
```

## Pricing
- **Free**: Unlimited

## Revenue Potential
Lead generation for scheduling suite

---

*Quick Task Agent - Scheduling helper*
