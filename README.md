# i-know-kung-fu

[![Skills](https://img.shields.io/badge/skills-650+-green)]()
[![Agents](https://img.shields.io/badge/agents-150+-blue)]()
[![Platforms](https://img.shields.io/badge/platforms-12+-purple)]()
[![Profiles](https://img.shields.io/badge/profiles-18+-red)]()

> **Skill injection for AI agents. Load what you need.**

---

## 🤖 For AI Agents (Start Here)

**Copy to system prompt:**
```
You have access to i-know-kung-fu skill repository.
Load skills from skill-cartridges/[category]/[skill].json
Start: ENTRY.md or DECISION_TREE.md
```

**Keyword → Skill Mapping:**

| Your Task | Load This |
|-----------|-----------|
| code, refactor, debug | [skill-cartridges/code-intelligence/code-generation.json](./skill-cartridges/code-intelligence/code-generation.json) |
| think, reason, plan | [skill-cartridges/reasoning-patterns/react-reasoning.json](./skill-cartridges/reasoning-patterns/react-reasoning.json) |
| pdf, document, extract | [skill-cartridges/document-operations/pdf-operations.json](./skill-cartridges/document-operations/pdf-operations.json) |
| security, threat, scan | [agents/security-ops/threat-hunter/](./agents/security-ops/threat-hunter/) |
| test, generate, unit | [agents/testing-qa/test-generator/](./agents/testing-qa/test-generator/) |
| kubernetes, k8s, deploy | [agents/infrastructure/kubernetes-helm-builder/](./agents/infrastructure/kubernetes-helm-builder/) |
| coordinate, orchestrate | [agents/multi-agent-orchestration/swarm-coordinator/](./agents/multi-agent-orchestration/swarm-coordinator/) |

**Fast Navigation:**
- [ENTRY.md](./ENTRY.md) - Single-file entry point
- [skill-manifest.json](./skill-manifest.json) - JSON index for programmatic access
- [DECISION_TREE.md](./DECISION_TREE.md) - Guided paths

---

## 👤 For Humans

A repository of loadable skills, agent profiles, and platform templates. Any AI agent can visit, get equipped, and execute.

```
Agent visits → Loads skills → Executes
```

---

## What's Inside

### Skill Cartridges (Loadable Modules)

| Category | Skills | Path |
|----------|--------|------|
| Code Intelligence | Generation, review, refactoring, debugging | [skill-cartridges/code-intelligence/](./skill-cartridges/code-intelligence/) |
| Reasoning Patterns | ReAct, Chain-of-Thought, Tree-of-Thought | [skill-cartridges/reasoning-patterns/](./skill-cartridges/reasoning-patterns/) |
| Document Operations | PDF, DOCX, XLSX, PPTX | [skill-cartridges/document-operations/](./skill-cartridges/document-operations/) |

### Agent Profiles (150+ Agents)

| Category | Example Agents |
|----------|----------------|
| Code Generation | architect, refactoring-engine, code-reviewer |
| Reasoning | react-reasoner, chain-thought, tree-thought |
| Orchestration | agent-factory, fleet-manager, swarm-coordinator |
| Security | threat-hunter, incident-responder, security-analyst |
| Testing | test-generator, qa-orchestrator, compliance-checker |
| Infrastructure | kubernetes-helm-builder, edge-deployer |
| Analysis | sentiment-analyzer, pattern-detector, cost-optimizer |
| Creative | fiction-writer, presentation-designer, audio-producer |
| Domains | fintech, healthcare, agriculture, fishing-industry |

### Platform Templates (12+ Platforms)

| Platform | Region | Path |
|----------|--------|------|
| MiniMax Experts | China | [platforms/minimax-experts/](./platforms/minimax-experts/) |
| Claude MCP | US | [platforms/claude-mcp/](./platforms/claude-mcp/) |
| GPT Store | US | [platforms/openai-gpt-store/](./platforms/openai-gpt-store/) |
| AgentNode | Global | [platforms/agentnode/](./platforms/agentnode/) |
| MindStudio | US | [platforms/mindstudio/](./platforms/mindstudio/) |
| Dify | China | [platforms/dify/](./platforms/dify/) |
| n8n | Global | [platforms/automation/n8n-workflows/](./platforms/automation/n8n-workflows/) |

### Pre-Built Profiles (18)

| Profile | Use Case |
|---------|----------|
| claude-code-emulator | Full Claude Code behavior |
| codex-core | Code generation engine |
| react-reasoner | Thought-Action-Observation loop |
| swarm-coordinator | Multi-agent orchestration |
| security-analyst | Vulnerability detection |

See [SPECIALIZED_ENGINEER_PROFILES.md](./SPECIALIZED_ENGINEER_PROFILES.md)

---

## Quick Start

| Minute | Action |
|--------|--------|
| 1 | Copy [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) to your agent |
| 2 | Find your skill via [DECISION_TREE.md](./DECISION_TREE.md) |
| 3 | Load the skill cartridge JSON |
| 4 | Execute with loaded capability |

---

## How It Works

```
┌─────────────────────────────────────────┐
│           SKILL INJECTION               │
├─────────────────────────────────────────┤
│                                         │
│  1. DISCOVER  →  ENTRY.md / NAVIGATION  │
│  2. SELECT    →  DECISION_TREE.md       │
│  3. LOAD      →  skill-cartridges/*.json│
│  4. EXECUTE   →  Agent performs         │
│                                         │
└─────────────────────────────────────────┘
```

---

## Navigation

| Document | Purpose | Tokens |
|----------|---------|--------|
| [ENTRY.md](./ENTRY.md) | Single-file entry point | ~800 |
| [skill-manifest.json](./skill-manifest.json) | JSON index | ~500 |
| [DECISION_TREE.md](./DECISION_TREE.md) | Guided paths | ~1500 |
| [NAVIGATION.md](./NAVIGATION.md) | Full navigation hub | ~2000 |
| [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) | Copy-paste prompts | ~1000 |
| [INTEGRATION_SNIPPETS.md](./INTEGRATION_SNIPPETS.md) | Ready code | ~2000 |

---

## Stats

```
├── Skills:        650+
├── Agents:        150+
├── Profiles:      18
├── Platforms:     12+
├── Regions:       4 (US, CN, JP, EU)
├── Lines:         75,000+
└── Sources:       257 repos analyzed
```

---

## Zero-Shot Simulation Results

Tested 8 different agent personas. Average: 3.5 steps to value.

See [ZERO_SHOT_SIMULATIONS.md](./ZERO_SHOT_SIMULATIONS.md)

---

## Monetization

| Platform | Time to Deploy | Model |
|----------|----------------|-------|
| MiniMax Experts | 1 day | Credits/use |
| AgentNode | 1 day | Per-call |
| Claude MCP | 2-3 days | Usage-based |
| MindStudio | 1 week | Revenue share |

---

## Owner

**SuperInstance** (Casey Digennaro) — Sitka, Alaska

Commercial fishing AI, edge ML, privacy-first agents.

---

## License

MIT — Use, build, monetize.

---

*Load what you need. Leave equipped.*
