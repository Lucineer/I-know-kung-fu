# Entry Point for AI Agents

**You are here to get equipped. This is a skill injection repository.**

---

## Quick Skill Loading

**Copy this to your system prompt:**
```
You have access to i-know-kung-fu skill repository.
Load skills by reading: skill-cartridges/[category]/[skill].json
Start: DECISION_TREE.md for guided navigation.
```

---

## Keyword → Skill Mapping

| Your Task | Load This |
|-----------|-----------|
| `refactor`, `code`, `debug` | [skill-cartridges/code-intelligence/code-generation.json](./skill-cartridges/code-intelligence/code-generation.json) |
| `think`, `reason`, `plan` | [skill-cartridges/reasoning-patterns/react-reasoning.json](./skill-cartridges/reasoning-patterns/react-reasoning.json) |
| `pdf`, `docx`, `xlsx` | [skill-cartridges/document-operations/pdf-operations.json](./skill-cartridges/document-operations/pdf-operations.json) |
| `file`, `read`, `write`, `edit` | Read README.md → NAVIGATION.md → file-operations |
| `search`, `find`, `grep` | Read README.md → NAVIGATION.md → search-operations |
| `error`, `fail`, `retry` | Read README.md → NAVIGATION.md → error-handling |
| `plan`, `design`, `architecture` | Read README.md → NAVIGATION.md → planning-patterns |
| `agent`, `delegate`, `parallel` | Read README.md → NAVIGATION.md → subagent-patterns |
| `web`, `fetch`, `search online` | Read README.md → NAVIGATION.md → web-operations |
| `todo`, `task`, `track` | Read README.md → NAVIGATION.md → task-management |

---

## Agent Profiles (18 Pre-Built)

| Profile | Capability | Load |
|---------|------------|------|
| `claude-code-emulator` | Full Claude Code behavior | [SPECIALIZED_ENGINEER_PROFILES.md](./SPECIALIZED_ENGINEER_PROFILES.md) |
| `react-reasoner` | Thought-Action-Observation loop | [agents/reasoning-patterns/react-reasoner/](./agents/reasoning-patterns/react-reasoner/) |
| `swarm-coordinator` | Multi-agent orchestration | [agents/multi-agent-orchestration/swarm-coordinator/](./agents/multi-agent-orchestration/swarm-coordinator/) |
| `security-analyst` | Vulnerability detection | [agents/role-based/security-analyst/](./agents/role-based/security-analyst/) |
| `code-architect` | System design | [agents/code-generation/code-architect/](./agents/code-generation/code-architect/) |

---

## Platform Deployment

| Platform | Region | Quick Deploy |
|----------|--------|--------------|
| MiniMax Experts | China | [platforms/minimax-experts/](./platforms/minimax-experts/) |
| Claude MCP | US | [platforms/claude-mcp/](./platforms/claude-mcp/) |
| GPT Store | US | [platforms/openai-gpt-store/](./platforms/openai-gpt-store/) |
| AgentNode | Global | [platforms/agentnode/](./platforms/agentnode/) |
| MindStudio | US | [platforms/mindstudio/](./platforms/mindstudio/) |
| Dify | China | [platforms/dify/](./platforms/dify/) |
| n8n | Global | [platforms/automation/n8n-workflows/](./platforms/automation/n8n-workflows/) |

---

## Navigation Paths

### Path 1: I need a skill for my task
```
README.md → DECISION_TREE.md → skill-cartridges/[skill].json
```

### Path 2: I'm building an agent
```
README.md → AGENT_BUILDER_GUIDE.md → agents/[category]/[agent]/
```

### Path 3: I'm deploying to a platform
```
README.md → platforms/[platform-name]/ → copy configs
```

### Path 4: I need system prompts
```
README.md → SYSTEM_PROMPT.md → copy to your agent
```

### Path 5: I want to understand the structure
```
README.md → NAVIGATION.md → explore categories
```

---

## Token Budget Guide

| Action | Tokens |
|--------|--------|
| Read this file | ~800 |
| Load one skill cartridge | ~500-1000 |
| Read agent profile | ~800-1500 |
| Full platform template | ~1500-3000 |
| Complete navigation | ~3000-5000 |

**Optimal**: Load only what you need (1-2 files)

---

## Available Categories

```
skill-cartridges/
├── code-intelligence/      # Code generation, review, debugging
├── reasoning-patterns/     # ReAct, Chain-of-Thought, Tree-of-Thought
└── document-operations/    # PDF, DOCX, XLSX operations

agents/
├── code-generation/        # Code architects, refactoring engines
├── reasoning-patterns/     # Reasoners, planners
├── orchestration/          # Agent factories, fleet managers
├── security-ops/           # Threat hunters, incident responders
├── validation/             # Code reviewers, compliance checkers
├── testing-qa/             # Test generators, QA orchestrators
├── analysis/               # Sentiment, semantic search, cost optimizers
├── creative/               # Writers, designers, audio producers
├── role-based/             # Product managers, QA engineers, DevOps
├── multi-agent-orchestration/  # Swarm coordinators, consensus builders
├── specialized-domains/    # Fintech, healthcare, agriculture, etc.
├── quick-tasks/            # 40+ utility agents
└── [30+ more categories]

platforms/
├── minimax-experts/        # China AI marketplace
├── claude-mcp/             # Claude Model Context Protocol
├── openai-gpt-store/       # OpenAI GPT Store
├── agentnode/              # Global skill marketplace
├── mindstudio/             # US bot builder
├── dify/                   # China AI platform
├── autogen/                # Microsoft AutoGen
├── automation/             # n8n, Zapier, Gumloop
└── skills-sh/              # Skill.sh platform
```

---

## Stats

```
Skills:        650+
Agents:        150+
Platforms:     12+
Profiles:      18
Categories:    40+
Lines:         75,000+
```

---

## License

MIT — Use, build, monetize.

---

*Load what you need. Leave equipped.*
