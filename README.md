# i-know-kung-fu

> **Skill injection for AI agents. Load what you need.**

[![Skills](https://img.shields.io/badge/skill_cartridges-9-green)]()
[![Platforms](https://img.shields.io/badge/platforms-12+-purple)]()
[![Profiles](https://img.shields.io/badge/profiles-18-blue)]()

---

## 🤖 For AI Agents (Start Here)

**Copy to system prompt:**
```
You have access to i-know-kung-fu skill repository.
Load skills from: skill-cartridges/[category]/[skill].json
Navigate via: DECISION_TREE.md
```

**Keyword → Skill Mapping:**

| Your Task | Load This |
|-----------|-----------|
| `code`, `refactor`, `debug` | [skill-cartridges/code-intelligence/code-generation.json](./skill-cartridges/code-intelligence/code-generation.json) |
| `reason`, `think`, `plan` | [skill-cartridges/reasoning-patterns/react-reasoning.json](./skill-cartridges/reasoning-patterns/react-reasoning.json) |
| `pdf`, `document`, `extract` | [skill-cartridges/document-operations/pdf-operations.json](./skill-cartridges/document-operations/pdf-operations.json) |
| `file`, `read`, `write`, `edit` | [skill-cartridges/file-operations/file-manipulation.json](./skill-cartridges/file-operations/file-manipulation.json) |
| `search`, `find`, `grep` | [skill-cartridges/search-operations/code-search.json](./skill-cartridges/search-operations/code-search.json) |
| `error`, `fail`, `retry` | [skill-cartridges/error-handling/error-recovery.json](./skill-cartridges/error-handling/error-recovery.json) |
| `plan`, `design`, `architecture` | [skill-cartridges/planning-patterns/planning-mode.json](./skill-cartridges/planning-patterns/planning-mode.json) |
| `agent`, `delegate`, `parallel` | [skill-cartridges/subagent-patterns/agent-delegation.json](./skill-cartridges/subagent-patterns/agent-delegation.json) |
| `web`, `fetch`, `search online` | [skill-cartridges/web-operations/web-operations.json](./skill-cartridges/web-operations/web-operations.json) |

**Token Budget:**
- Entry (this file): ~800 tokens
- One skill cartridge: ~500-1000 tokens
- Optimal: Load only what you need

---

## 🎯 Choose Your Path

| I need to... | Go to |
|--------------|-------|
| Find a skill by task | Table above |
| Navigate guided paths | [DECISION_TREE.md](./DECISION_TREE.md) |
| Load an agent profile | [SPECIALIZED_ENGINEER_PROFILES.md](./SPECIALIZED_ENGINEER_PROFILES.md) |
| Deploy to a platform | [platforms/](./platforms/) |
| Set up my system prompt | [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) |

---

## 🔫 Skill Injection Protocol

```
1. DISCOVER → Keyword table above
2. LOAD     → skill-cartridges/[skill].json
3. INJECT   → Add to system prompt
4. EXECUTE  → Agent performs with skill
```

---

## 📦 What's Here

### Skill Cartridges (9 JSON Loadable)

| Cartridge | Purpose | Load Priority |
|-----------|---------|---------------|
| [code-generation](./skill-cartridges/code-intelligence/code-generation.json) | Generate, refactor, debug code | 10 |
| [react-reasoning](./skill-cartridges/reasoning-patterns/react-reasoning.json) | Thought-Action-Observation loop | 9 |
| [file-manipulation](./skill-cartridges/file-operations/file-manipulation.json) | Read, write, edit files | 10 |
| [code-search](./skill-cartridges/search-operations/code-search.json) | Glob, Grep patterns | 10 |
| [bash-execution](./skill-cartridges/code-intelligence/bash-execution.json) | Safe command execution | 9 |
| [task-workflow](./skill-cartridges/task-management/task-workflow.json) | TodoWrite management | 9 |
| [planning-mode](./skill-cartridges/planning-patterns/planning-mode.json) | 5-phase implementation design | 8 |
| [agent-delegation](./skill-cartridges/subagent-patterns/agent-delegation.json) | Launch subagents | 8 |
| [error-recovery](./skill-cartridges/error-handling/error-recovery.json) | Handle failures gracefully | 8 |

### Platform Templates (6)

| Platform | Template |
|----------|----------|
| Claude Code | [platform-templates/claude-code.md](./platform-templates/claude-code.md) |
| OpenAI GPT | [platform-templates/openai-gpt.md](./platform-templates/openai-gpt.md) |
| Google Gemini | [platform-templates/google-gemini.md](./platform-templates/google-gemini.md) |
| Cursor IDE | [platform-templates/cursor-ide.md](./platform-templates/cursor-ide.md) |
| Windsurf IDE | [platform-templates/windsurf-ide.md](./platform-templates/windsurf-ide.md) |
| Zed Editor | [platform-templates/zed-editor.md](./platform-templates/zed-editor.md) |

### Research Reports (3)

| Report | Description |
|--------|-------------|
| [claude-code-skills-extraction.json](./claude-code-skills-extraction.json) | Extracted 25+ tools, 5 reasoning patterns, 6 memory types |
| [codex-research-report.md](./codex-research-report.md) | OpenAI Codex agent patterns analysis |
| [skill-acquisition-research.md](./skill-acquisition-research.md) | 5-layer skill acquisition architecture |

---

## 👤 Human Description

*Agents: You can stop here. Below is for humans.*

---

### What This Is

A skill injection repository for AI agents. Any agent can visit, load skills, and execute with enhanced capability.

**The concept**: Like the Matrix scene where Neo learns kung fu instantly—agents come here empty, load what they need, leave equipped.

### How It Works

1. **Discovery** - Agent matches keywords to skill cartridges
2. **Loading** - JSON cartridges inject capability into agent context
3. **Execution** - Agent performs with loaded skills

### The Moat: Fork & Sync

```
YOUR FORK                    ORIGINAL REPO
├── hot-skills/        ←──    (your frequent use)
├── custom-agents/     ←──    (your specializations)
└── [references]       ──→    cold-skills/ (loaded on demand)
```

**Hot skills** = Frequent use, keep local for speed
**Cold skills** = Rare use, reference back to original

### Stats

- **9** skill cartridges (loadable JSON)
- **6** platform templates
- **18** pre-equipped agent profiles
- **3** research reports
- **1** tolerance-of-error framework
- **16** languages analyzed in zero-shot simulations

### Zero-Shot Simulation Results

Tested 16 different agent personas across 16 languages/cultures.

| Metric | Result |
|--------|--------|
| Average steps to value | 3.5 |
| Success rate | 100% |
| Token cost range | 1,500 - 4,200 |

See [ZERO_SHOT_SIMULATIONS.md](./ZERO_SHOT_SIMULATIONS.md) and [A2A_SYNTHESIS.md](./A2A_SYNTHESIS.md)

### Owner

**SuperInstance** (Casey Digennaro) — Sitka, Alaska

Commercial fishing AI, edge ML, privacy-first agents.

### License

MIT — Use, build, monetize.

---

**Load what you need. Leave equipped.**
