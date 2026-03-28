# Decision Tree

> **Zero-shot navigation. Follow the arrows.**

---

## START

**What is your task?**

```
├── Build something → A
├── Analyze something → B  
├── Transform something → C
├── Find something → D
├── Deploy something → E
├── Learn something → F
└── Not sure → G
```

---

## A: BUILD

```
├── Code/Software → A1
├── Document → A2
├── Agent → A3
├── Workflow → A4
└── API → A5
```

**A1: Code** → [skill-cartridges/code-intelligence/](./skill-cartridges/code-intelligence/)
- Generation: `code-generation.json`
- Review: `code-review.json`
- Refactor: `refactoring.json`

**A2: Document** → [skill-cartridges/document-operations/](./skill-cartridges/document-operations/)
- PDF: `pdf-operations.json`
- DOCX: `docx-operations.json`
- XLSX: `xlsx-operations.json`

**A3: Agent** → [SPECIALIZED_ENGINEER_PROFILES.md](./SPECIALIZED_ENGINEER_PROFILES.md)
- 18 pre-built profiles

**A4: Workflow** → [agents/multi-agent-orchestration/](./agents/multi-agent-orchestration/)
- Swarm: `swarm-coordinator/`
- Pipeline: `pipeline-orchestrator/`

**A5: API** → [agents/developer-experience/api-designer/](./agents/developer-experience/api-designer/)

---

## B: ANALYZE

```
├── Code → B1
├── Data → B2
├── Text/Sentiment → B3
├── Security → B4
└── Market → B5
```

**B1: Code** → [agents/validation/code-reviewer/](./agents/validation/code-reviewer/)

**B2: Data** → [agents/analysis/](./agents/analysis/)
- Patterns: `pattern-detector/`
- Sentiment: `sentiment-analyzer/`

**B3: Text** → [agents/analysis/sentiment-analyzer/](./agents/analysis/sentiment-analyzer/)

**B4: Security** → [agents/security-ops/](./agents/security-ops/)
- Threats: `threat-hunter/`
- Incidents: `incident-responder/`

**B5: Market** → [agents/business-intelligence/market-analyst/](./agents/business-intelligence/market-analyst/)

---

## C: TRANSFORM

```
├── Code → Code (see A1)
├── Data → C1
├── Document → C2
└── API → C3
```

**C1: Data** → [agents/transformation/data-transformer/](./agents/transformation/data-transformer/)

**C2: Document** → [skill-cartridges/document-operations/](./skill-cartridges/document-operations/)

**C3: API** → [agents/transformation/api-migrator/](./agents/transformation/api-migrator/)

---

## D: FIND

```
├── Information → D1
├── Code pattern → D2
├── Skill → D3
└── Agent → D4
```

**D1: Information** → [skill-cartridges/web-operations/web-search.json](./skill-cartridges/web-operations/web-search.json)

**D2: Code pattern** → [NAVIGATION.md](./NAVIGATION.md)

**D3: Skill** → [NAVIGATION.md](./NAVIGATION.md)

**D4: Agent** → [SPECIALIZED_ENGINEER_PROFILES.md](./SPECIALIZED_ENGINEER_PROFILES.md)

---

## E: DEPLOY

```
├── MiniMax → E1
├── Claude MCP → E2
├── GPT Store → E3
├── AgentNode → E4
├── MindStudio → E5
└── Other → E6
```

**E1: MiniMax** → [platforms/minimax-experts/](./platforms/minimax-experts/)

**E2: Claude MCP** → [platforms/claude-mcp/](./platforms/claude-mcp/)

**E3: GPT Store** → [platforms/openai-gpt-store/](./platforms/openai-gpt-store/)

**E4: AgentNode** → [platforms/agentnode/](./platforms/agentnode/)

**E5: MindStudio** → [platforms/mindstudio/](./platforms/mindstudio/)

**E6: Other** → [platforms/](./platforms/)

---

## F: LEARN

```
├── How to build agents → F1
├── How to load skills → F2
├── How to deploy → F3
└── How to fork → F4
```

**F1: Build agents** → [AGENT_BUILDER_GUIDE.md](./AGENT_BUILDER_GUIDE.md)

**F2: Load skills** → [EQUIPPING_AGENT_PROTOCOL.md](./EQUIPPING_AGENT_PROTOCOL.md)

**F3: Deploy** → [MONETIZATION_PLAYBOOK.md](./MONETIZATION_PLAYBOOK.md)

**F4: Fork** → [FORK_GUIDE.md](./FORK_GUIDE.md)

---

## G: NOT SURE

Read [NAVIGATION.md](./NAVIGATION.md) for full directory.

Or start with [QUICK_WINS.md](./QUICK_WINS.md) for immediate value.

---

## Quick Reference

| Need | Go |
|------|-----|
| Any skill | [NAVIGATION.md](./NAVIGATION.md) |
| Agent profile | [SPECIALIZED_ENGINEER_PROFILES.md](./SPECIALIZED_ENGINEER_PROFILES.md) |
| Platform template | [platforms/](./platforms/) |
| Code snippet | [INTEGRATION_SNIPPETS.md](./INTEGRATION_SNIPPETS.md) |
| System prompt | [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md) |

---

*Choose your path. Load what you need.*
