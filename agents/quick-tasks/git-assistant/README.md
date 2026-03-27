# Git Command Helper

> **Quick Task Agent - Instant Results**

## Overview
Natural language git commands. Never forget git syntax.

## Capabilities
- Natural language → git command
- Explain git errors
- Interactive rebase helper
- Merge conflict resolution
- Branch management
- Commit message generation

## Input
```json
{
  "action": "command|explain|resolve",
  "description": "undo last commit but keep changes",
  "error": "optional error message to explain"
}
```

## Output
```json
{
  "command": "git reset --soft HEAD~1",
  "explanation": "This undoes the last commit but stages...",
  "alternatives": ["git reset --mixed HEAD~1", "git reset --hard HEAD~1"],
  "warning": "Be careful if you've already pushed"
}
```

## Pricing
- **Free**: Unlimited

## Revenue Potential
Lead generation for developer tools

---

*Quick Task Agent - Git made easy*
