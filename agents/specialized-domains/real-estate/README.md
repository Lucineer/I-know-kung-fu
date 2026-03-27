# Real Estate Agent

## Overview

Specialized agent for real estate operations including property valuation, market analysis, lead qualification, and transaction support.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| Property Valuation | Estimate property values |
| Market Analysis | Analyze real estate markets |
| Lead Qualification | Qualify buyer/seller leads |
| Listing Optimization | Optimize property listings |
| Transaction Support | Support transaction process |

## Skills

### Primary Skills
1. **Property Valuation** - Estimate using comparables and features
2. **Market Trend Analysis** - Identify market trends and patterns
3. **Lead Scoring** - Score and prioritize leads
4. **Listing Description** - Generate compelling listings
5. **Investment Analysis** - Analyze investment potential

### Secondary Skills
- Neighborhood analysis
- Price optimization
- Virtual staging descriptions
- Contract review
- Timeline management

## Use Cases

1. **Property Search** - Find matching properties
2. **Valuation** - Estimate property value
3. **Lead Management** - Qualify and nurture leads
4. **Listing Creation** - Generate listings
5. **Market Reports** - Generate market analysis

## Example Interactions

### Property Valuation
```
User: "What's 123 Main St worth?"

Agent Analysis:
- Location: Downtown, walk score 85
- Sq ft: 2,100
- Beds/Baths: 3/2
- Year built: 1985 (updated 2019)
- Comparable sales: 5 within 0.5mi, last 90 days

Output:
Estimated Value: $485,000 - $525,000
Median: $505,000
Confidence: High (many comparables)

Key Factors:
✓ Walkable location (+15% vs area average)
✓ Recent renovations (+$25,000)
⚠ Older building (-$10,000)

Comparable Analysis:
- 115 Oak St: $498,000 (2,000 sqft, sold 45 days ago)
- 145 Pine Ave: $520,000 (2,200 sqft, sold 30 days ago)
- 98 Elm Rd: $475,000 (1,900 sqft, sold 60 days ago)

Recommendation: List at $515,000 for quick sale, $525,000 for max value
```

### Lead Qualification
```
User: "Score this lead: looking for 3br under $500k, pre-approved"

Agent Analysis:
- Budget: $500k (realistic for 3br in target area)
- Pre-approval: Yes (serious buyer indicator)
- Timeline: Not specified (follow-up needed)
- Specificity: Moderate

Output:
Lead Score: 82/100 (Hot Lead)
Category: Ready to Buy

Strengths:
✓ Pre-approved financing
✓ Clear criteria (3br)
✓ Realistic budget

Information Needed:
- Timeline for purchase
- Preferred neighborhoods
- Must-have features

Recommended Actions:
1. Send matching listings within 24 hours
2. Schedule showing appointment
3. Ask about timeline and preferences

Priority: Respond within 4 hours
```

## Configuration

```json
{
  "agent_type": "real-estate",
  "market_focus": "residential",
  "data_sources": ["mls", "public_records", "market_data"],
  "valuation_model": "comparable_sales",
  "lead_scoring": true,
  "listing_generation": true
}
```

## Performance Characteristics

| Metric | Value |
|--------|-------|
| Valuation accuracy | ±5% of sale price |
| Lead scoring accuracy | 88% |
| Response time | <2 seconds |

## Monetization

- **Per-valuation**: $2-5
- **Per-lead-score**: $0.50
- **SaaS subscription**: $99-499/month
- **Brokerage license**: Custom

## Related Agents

- `ecommerce-retail/` - Retail
- `financial-analysis-suite/` - Investment analysis
- `legal-document-suite/` - Contract review
