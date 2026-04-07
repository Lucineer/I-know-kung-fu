# i-know-kung-fu

Skill injection for AI agents. Load what you need.

Agents can fail on trivial tasks not from model limits, but from missing specific capabilities. You don't need to fine-tune or rewrite your runtime—just load the required skill for the job.

This is a shared library of standard agent behaviors packaged as plain JSON cartridges. Inject them directly into your agent's system context when needed. Fork and modify any skill without permission.

## Why this exists

Every team rebuilds the same base capabilities: error recovery, file safety rules, PDF extraction. This library provides tested, forkable implementations of these common skills to reduce duplication.

## How it works

These are auditable JSON behavior cartridges. You load them into your agent's system prompt only for relevant tasks. Start with zero skills and pay only the token cost for what you use.

**Copy to system prompt:**
```
You have access to i-know-kung-fu skill repository.
Load skills from: skill-cartridges/[category]/[skill].json
Navigate via: DECISION_TREE.md
```

## Skill reference

| Task keywords | Load this skill |
|---------------|-----------------|
| `code`, `refactor`, `debug` | [skill-cartridges/code-intelligence/code-generation.json](./skill-cartridges/code-intelligence/code-generation.json) |
| `reason`, `think`, `plan` | [skill-cartridges/reasoning-patterns/react-reasoning.json](./skill-cartridges/reasoning-patterns/react-reasoning.json) |
| `pdf`, `document`, `extract` | [skill-cartridges/document-operations/pdf-operations.json](./skill-cartridges/document-operations/pdf-operations.json) |
| `file`, `read`, `write`, `edit` | [skill-cartridges/file-operations/file-manipulation.json](./skill-cartridges/file-operations/file-manipulation.json) |
| `search`, `find`, `grep` | [skill-cartridges/search-operations/code-search.json](./skill-cartridges/search-operations/code-search.json) |
| `error`, `fail`, `retry` | [skill-cartridges/error-handling/error-recovery.json](./skill-cartridges/error-handling/error-recovery.json) |
| `plan`, `design`, `architecture` | [skill-cartridges/planning-patterns/planning-mode.json](./skill-cartridges/planning-patterns/planning-mode.json) |
| `agent`, `delegate`, `parallel` | [skill-cartridges/subagent-patterns/agent-delegation.json](./skill-cartridges/subagent-patterns/agent-delegation.json) |
| `web`, `fetch`, `search online` | [skill-cartridges/web-operations/web-operations.json](./skill-cartridges/web-operations/web-operations.json) |

For guided navigation, see [DECISION_TREE.md](./DECISION_TREE.md). For pre-configured agent roles, see [SPECIALIZED_ENGINEER_PROFILES.md](./SPECIALIZED_ENGINEER_PROFILES.md).

## Token budget

- This README: ~800 tokens
- One skill cartridge: 500-1000 tokens
- Load only what you need

## Limitation

Skills are static JSON definitions that describe behavior patterns but don't include actual code execution. You must implement the underlying tool calls referenced in the skills.

## License

MIT © Superinstance & Lucineer (DiGennaro et al.)

---

<div>
  <a href="https://the-fleet.casey-digennaro.workers.dev">The Fleet</a> •
  <a href="https://cocapn.ai">Cocapn</a>
</div>