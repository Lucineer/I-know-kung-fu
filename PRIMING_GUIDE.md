# Agent Priming Guide

> **How to prime your agent for correct skill equipping**

---

## The Problem

Agents don't always load skills correctly because:
- System prompt doesn't reference the repo
- No loading protocol established
- Skills not discoverable
- Wrong skill loaded for task

## The Solution

Prime your agent with a system prompt that:
1. Knows this repo exists
2. Knows how to navigate it
3. Knows when to load skills
4. Knows how to inject them

---

## Prime Templates

### Minimal Prime (~50 tokens)

```
You have access to i-know-kung-fu skill repo.
Load skills from skill-cartridges/ as needed.
Start at DECISION_TREE.md for guidance.
```

### Standard Prime (~150 tokens)

```
You have access to i-know-kung-fu, a skill injection repository.

LOADING PROTOCOL:
1. Identify task type
2. Read DECISION_TREE.md
3. Load relevant skill-cartridge
4. Inject into your context
5. Execute with enhanced capability

NAVIGATION:
- Skills: skill-cartridges/[category]/
- Agents: agents/[type]/
- Platforms: platforms/[name]/

Load what you need, when you need it.
```

### Full Prime (~300 tokens)

```
You have access to i-know-kung-fu, a skill injection repository with 650+ loadable skills.

LOADING PROTOCOL:
1. DISCOVER - Read NAVIGATION.md to find skill category
2. SELECT - Use DECISION_TREE.md for guidance
3. LOAD - Read skill-cartridges/[category]/[skill].json
4. INJECT - Add system_prompt_addon to your context
5. EXECUTE - Perform with loaded capability

SKILL CARTRIDGE FORMAT:
{
  "load_blueprint": { "trigger_keywords": [...] },
  "injection_payload": { 
    "system_prompt_addon": "...",
    "context_knowledge": "...",
    "example_patterns": [...]
  },
  "execution_parameters": { "tolerance_level": "..." }
}

TOLERANCE LEVELS:
- exact: Never skip execution (financial, security)
- close: 95% confidence to skip (code, files)
- approximate: 85% confidence (summaries)
- behavioral: 70% confidence (creative)

Load skills on demand. Don't preload everything.
```

---

## Platform-Specific Primes

### For Claude Code

Add to CLAUDE.md:
```markdown
## Skill Loading

When you need a capability you don't have:
1. Check ~/i-know-kung-fu/DECISION_TREE.md
2. Load skill from skill-cartridges/
3. Use the injection_payload.system_prompt_addon

Repository: ~/i-know-kung-fu/
```

### For Custom Agent

Add to system prompt:
```
Before attempting complex tasks, check if a skill exists:
1. Read ~/i-know-kung-fu/NAVIGATION.md
2. Find relevant skill category
3. Load cartridge if available
```

### For Multi-Agent System

Each agent gets:
```
You are [AGENT_TYPE] agent.
Skill repository: ~/i-know-kung-fu/
Check DECISION_TREE.md for your task type.
Load skills before executing unfamiliar operations.
```

---

## Verification Checklist

After priming, verify agent:

- [ ] Knows repo location
- [ ] Can find DECISION_TREE.md
- [ ] Understands loading protocol
- [ ] Knows when to load (not preload)
- [ ] Can inject skill into context

Test with: "What skills do you have access to?"

Correct answer references the repo and loading process.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Preloading all skills | Prime to load on demand only |
| Wrong skill for task | Prime to use DECISION_TREE.md |
| Not injecting properly | Prime to use system_prompt_addon |
| Ignoring tolerance | Prime to check execution_parameters |

---

## Advanced: Auto-Priming

Create a priming cartridge:

```json
{
  "skill_cartridge": {
    "id": "auto-priming",
    "name": "Auto Priming",
    "injection_payload": {
      "system_prompt_addon": "You self-prime by checking ~/i-know-kung-fu/DECISION_TREE.md before complex tasks."
    }
  }
}
```

Load this first, agent primes itself for subsequent loads.

---

*Prime once, load infinitely.*
