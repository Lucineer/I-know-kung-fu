# i-know-kung-fu 🥋

You load AI skills only when you need them. Each skill is a plain JSON cartridge you insert directly into your system prompt. This is an open library of those cartridges.

**Live URL:** [https://i-know-kung-fu.casey-digennaro.workers.dev](https://i-know-kung-fu.casey-digennaro.workers.dev)

## Why This Exists
Many agent systems include a large default prompt. You often pay a token cost for capabilities your current task does not require. This library lets you start with a minimal prompt and load specific skills on demand.

## Quick Start
1.  **Fork this repository.** All development happens in your own fork.
2.  Deploy to Cloudflare Workers with one click. It has zero dependencies.
3.  Modify any JSON file in `skill-cartridges/` for your use case. No API keys or configuration is needed.

When your agent needs a capability, copy the relevant skill's JSON into your system prompt. Start each agent interaction with a clean slate.

## What Makes This Different
1.  **No SDK or integration.** You use skills by copying plain text into your prompt. This works with any LLM or agent framework immediately.
2.  **Full transparency and control.** Every skill is a readable JSON file you can audit and edit. You do not inherit hidden behaviors.
3.  **Controlled token usage.** You only add the tokens for the specific skill you are using in a given conversation.

## Features
*   Fork-first public library: every skill is a standalone, human-readable JSON file.
*   Zero runtime overhead: no external API calls or services.
*   Practical patterns for code, documents, error handling, search, and delegation.
*   MIT licensed. Use for any purpose.

## A Specific Limitation
Each skill cartridge adds to your prompt's token count, which increases cost and may hit context limits. A complex skill can be over 1,000 tokens. You must manage this trade-off between capability and context space.

## Skill Reference
| For tasks like... | Load this skill |
| :--- | :--- |
| `code`, `refactor`, `debug` | [code-generation.json](./skill-cartridges/code-intelligence/code-generation.json) |
| `pdf`, `document`, `extract` | [pdf-operations.json](./skill-cartridges/document-operations/pdf-operations.json) |
| `error`, `fail`, `retry` | [error-recovery.json](./skill-cartridges/error-handling/error-recovery.json) |
| `search`, `find`, `grep` | [code-search.json](./skill-cartridges/search-operations/code-search.json) |
| `web`, `fetch`, `search online` | [web-operations.json](./skill-cartridges/web-operations/web-operations.json) |
| `plan`, `design`, `architecture` | [planning-mode.json](./skill-cartridges/planning-patterns/planning-mode.json) |
| `agent`, `delegate`, `parallel` | [agent-delegation.json](./skill-cartridges/subagent-patterns/agent-delegation.json) |

Navigate the full catalog via [DECISION_TREE.md](./DECISION_TREE.md).

<div style="text-align:center;padding:16px;color:#64748b;font-size:.8rem"><a href="https://the-fleet.casey-digennaro.workers.dev" style="color:#64748b">The Fleet</a> &middot; <a href="https://cocapn.ai" style="color:#64748b">Cocapn</a> &middot; Superinstance and Lucineer (DiGennaro et al.)</div>