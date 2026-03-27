# Skill Pattern Abstractions

> **Meta-Guide: The Patterns Behind All Agent Skills**

## Overview

After creating 200+ agent specifications, clear patterns emerge. This document captures the higher-level abstractions that can be used to create any agent skill.

---

## The Universal Skill Anatomy

Every agent skill consists of these core components:

```
skill/
├── README.md          # Purpose, features, pricing
├── schema.json        # Input/output definitions
├── config.json        # Platform-specific config
├── examples.md        # Usage examples
├── monetization.md    # Pricing & revenue strategy
└── templates/         # Optional: reusable templates
```

---

## Pattern 1: Input-Process-Output (IPO)

Every skill follows this fundamental pattern:

```json
{
  "inputs": {
    "trigger": "what initiates the skill",
    "context": "additional information needed",
    "parameters": "configurable options"
  },
  "process": {
    "steps": "ordered operations",
    "fallback": "error handling",
    "optimization": "performance tuning"
  },
  "outputs": {
    "primary": "main result",
    "metadata": "supplementary info",
    "artifacts": "generated files"
  }
}
```

### Example Instantiations

| Skill Type | Input | Process | Output |
|------------|-------|---------|--------|
| **Quick Task** | Single datum | Transform | Single result |
| **Analysis** | Dataset/Stream | Analyze | Insights + Report |
| **Creative** | Prompt + Constraints | Generate | Content + Variations |
| **Orchestration** | Goal + Resources | Coordinate | Results + Status |
| **Validation** | Artifact + Rules | Check | Pass/Fail + Issues |

---

## Pattern 2: Capability Dimensions

Every skill can be measured across these dimensions:

### 1. Complexity Spectrum
```
Simple ───────────────────────────────────── Complex
|          |          |          |          |
Quick      Utility    Workflow   System    Platform
Task       Skill      Skill      Skill     Skill
(1 step)   (2-3 steps) (5+ steps) (multi-skill) (multi-system)
```

### 2. Autonomy Level
```
Passive ←─────────────────────────────────→ Autonomous
|           |           |           |           |
Prompt-     Tool-      Advisor    Agent      Autonomous
Based       Assisted   Mode       Mode       Agent
(user-led)  (helpful)  (guides)   (executes) (self-directed)
```

### 3. Domain Specificity
```
Horizontal ←─────────────────────────────────→ Vertical
|              |              |              |
Universal      Industry-      Domain-       Specialized
Skill          Agnostic       Specific      Expert
(any context)  (any company)  (any user)    (expert user)
```

### 4. Revenue Model Mapping
```
| Complexity | Autonomy | Domain   | Pricing Model    | Price Range    |
|------------|----------|----------|------------------|-----------------|
| Simple     | Passive  | Horizontal| Freemium         | Free-$9/mo      |
| Utility    | Tool     | Industry | Subscription     | $9-29/mo        |
| Workflow   | Advisor  | Domain   | Tiered           | $29-99/mo       |
| System     | Agent    | Specialized| Enterprise      | $99-499/mo      |
| Platform   | Auto     | Expert   | Custom/Usage     | $499+/mo        |
```

---

## Pattern 3: Skill Composition

Skills can be composed to create higher-order capabilities:

### Composition Rules

1. **Sequential**: Skill A → Skill B → Skill C
   - Example: Document Reader → Summarizer → Email Sender

2. **Parallel**: Skill A + Skill B → Combined Output
   - Example: Web Search + PDF Reader → Research Report

3. **Conditional**: If X then Skill A, else Skill B
   - Example: Language Detection → Translator (appropriate language)

4. **Iterative**: Skill A applied repeatedly
   - Example: Page Scraper applied to URL list

5. **Hierarchical**: Meta-skill managing other skills
   - Example: Workflow Orchestrator → [Skill 1, Skill 2, Skill 3]

### Composition Templates

```json
{
  "composite_skill": {
    "name": "Research Pipeline",
    "components": [
      {"skill": "web-search", "role": "gather"},
      {"skill": "content-extractor", "role": "process"},
      {"skill": "summarizer", "role": "synthesize"},
      {"skill": "report-generator", "role": "output"}
    ],
    "flow": "sequential",
    "error_handling": "fallback_to_alternative"
  }
}
```

---

## Pattern 4: Monetization Patterns

### Pattern 4.1: The Value Ladder

```
Free Tier (Lead Generation)
    ↓
Basic Tier ($9-29/mo) - Single use case
    ↓
Pro Tier ($29-99/mo) - Multiple use cases
    ↓
Business Tier ($99-299/mo) - Team features
    ↓
Enterprise Tier ($299+/mo) - Advanced features
    ↓
Custom/White-label (Negotiated) - Full ownership
```

### Pattern 4.2: Pricing by Outcome

| Outcome Type | Pricing Model | Example |
|--------------|---------------|---------|
| Time Saved | Per-hour saved | $10/hour recovered |
| Money Saved | % of savings | 10% of costs cut |
| Revenue Generated | % of revenue | 5% of attributed sales |
| Risk Mitigated | Per-incident avoided | $100/incident prevented |
| Quality Improved | Per-point increase | $50/NPS point |

### Pattern 4.3: Platform-Specific Pricing

| Platform | Best Model | Price Range |
|----------|------------|--------------|
| MiniMax Experts | Credit-based | 1-5 credits/use |
| MCP Servers | Subscription | $29-299/mo |
| MindStudio | Revenue share | Platform split |
| AgentNode | Per-use | $0.05-1.00/action |
| GPT Store | Free (brand building) | Lead gen value |

---

## Pattern 5: Skill Discovery Framework

To discover new skill opportunities:

### 5.1 Problem → Skill Mapping

```
User Pain Point → Skill Opportunity

"I waste time on..." → Automation Skill
"I don't understand..." → Explanation Skill
"I can't find..." → Search/Discovery Skill
"I'm not sure if..." → Validation Skill
"I need to create..." → Generation Skill
"I want to improve..." → Optimization Skill
```

### 5.2 Repo → Skill Extraction

```
Existing Code → Skill Opportunity

Infrastructure code → Utility Skill
Business logic → Domain Skill
Integration code → Connector Skill
Analysis code → Intelligence Skill
Automation code → Workflow Skill
```

### 5.3 Trend → Skill Prediction

```
Market Trend → Emerging Skill

AI coding assistants → Code review skills
Remote work → Collaboration skills
Privacy regulations → Compliance skills
Climate focus → Sustainability skills
Voice interfaces → Voice UX skills
```

---

## Pattern 6: Skill Quality Dimensions

Every skill should be evaluated on:

1. **Accuracy**: How often does it produce correct results?
2. **Speed**: How fast does it complete?
3. **Reliability**: How often does it fail?
4. **Flexibility**: How many use cases does it support?
5. **Integrability**: How easily does it connect to other skills?
6. **Discoverability**: How easily can users find it?
7. **Learnability**: How quickly can users become proficient?
8. **Monetizability**: How readily can it generate revenue?

---

## Pattern 7: Skill Naming Conventions

### Verb-Noun Pattern (Most Common)
- `document-processor`
- `data-analyzer`
- `code-reviewer`
- `sentiment-analyzer`

### Role-Based Pattern
- `devops-engineer`
- `security-analyst`
- `product-manager`

### Domain-Expert Pattern
- `fishing-industry`
- `healthcare-compliance`
- `climate-tech`

### Outcome Pattern
- `cost-optimizer`
- `risk-mitigator`
- `time-saver`

---

## The Skill Builder's Checklist

Before creating any skill, verify:

- [ ] Clear problem statement
- [ ] Defined input/output schema
- [ ] At least 3 use cases
- [ ] Error handling strategy
- [ ] Performance expectations
- [ ] Pricing strategy
- [ ] Platform targets
- [ ] Revenue potential estimate
- [ ] Differentiation from existing skills
- [ ] Source repository mapping (for your repos)

---

## Application: Creating Any Skill

1. **Identify the problem** - What pain does this solve?
2. **Determine the pattern** - Which IPO structure fits?
3. **Position on dimensions** - Complexity, autonomy, domain
4. **Choose composition** - Standalone or composite?
5. **Set monetization** - Which pricing model?
6. **Build the schema** - Define inputs/outputs
7. **Write documentation** - README, examples
8. **Test against quality dimensions**
9. **Publish to platforms**
10. **Iterate based on usage**

---

*This living document evolves with every new skill discovered and built.*
