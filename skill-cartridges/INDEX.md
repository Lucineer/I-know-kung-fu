# Skill Cartridge Index

Quick reference for loading skill cartridges. Agents should use this to find relevant skills.

## By Task Type

| Task | Cartridge Path | Load Priority |
|------|----------------|---------------|
| Read/write/edit files | `file-operations/file-manipulation.json` | 10 |
| Search code/find files | `search-operations/code-search.json` | 10 |
| Run bash commands | `code-intelligence/bash-execution.json` | 9 |
| Track tasks/todos | `task-management/task-workflow.json` | 9 |
| Plan implementation | `planning-patterns/planning-mode.json` | 8 |
| Delegate to subagents | `subagent-patterns/agent-delegation.json` | 8 |
| Handle errors | `error-handling/error-recovery.json` | 8 |
| Cross-session memory | `memory-patterns/agent-memory.json` | 7 |
| Web search/fetch | `web-operations/web-operations.json` | 7 |

## By Keyword

```
file, read, write, edit → file-operations/file-manipulation.json
find, search, grep, locate → search-operations/code-search.json
bash, command, execute, run → code-intelligence/bash-execution.json
todo, task, track, manage → task-management/task-workflow.json
plan, design, architecture → planning-patterns/planning-mode.json
agent, delegate, parallel → subagent-patterns/agent-delegation.json
error, fail, retry, recover → error-handling/error-recovery.json
memory, remember, persist → memory-patterns/agent-memory.json
web, fetch, search online → web-operations/web-operations.json
```

## Load Order for Complex Tasks

For multi-faceted tasks, load in this order:
1. `task-workflow.json` - Establish task tracking
2. `planning-mode.json` - Plan approach
3. `file-manipulation.json` - File operations
4. `code-search.json` - Navigation
5. `error-recovery.json` - Error handling

## Cartridge Summary

### file-manipulation.json
- **Tools**: Read, Write, Edit, MultiEdit, NotebookEdit
- **Key Pattern**: Always read before editing
- **Anti-pattern**: Never use cat/head/tail

### code-search.json
- **Tools**: Glob, Grep
- **Key Pattern**: Use tools, not bash equivalents
- **Anti-pattern**: Never use find/grep commands

### bash-execution.json
- **Tool**: Bash
- **Key Pattern**: Quote paths, use absolute paths
- **Anti-pattern**: Don't use find/grep/cat in bash

### task-workflow.json
- **Tool**: TodoWrite
- **Key Pattern**: One in_progress at a time
- **Anti-pattern**: Never batch completion updates

### planning-mode.json
- **Tools**: EnterPlanMode, ExitPlanMode
- **Key Pattern**: 5-phase workflow
- **Anti-pattern**: Never skip phases

### agent-delegation.json
- **Tool**: Agent (subagent launcher)
- **Key Pattern**: Launch in parallel
- **Anti-pattern**: Never sequential when parallel possible

### error-recovery.json
- **Pattern**: Don't retry same failing operation
- **Recovery**: Fallback, escalate, or abort

### agent-memory.json
- **Types**: Session, Agent, Nested, Team
- **Pattern**: Update on learning

### web-operations.json
- **Tools**: WebFetch, WebSearch
- **Pattern**: Search then fetch
