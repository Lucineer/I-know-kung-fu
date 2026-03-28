# Claude Code Integration Template

## Quick Start

Add to your `CLAUDE.md` or system prompt:

```markdown
## Skill Loading Protocol

Before responding, check for relevant skills in:
- `./skill-cartridges/` - Load cartridges matching task keywords
- `./tolerance-of-error-framework/` - For error tolerance patterns

Load by reading relevant JSON files and applying patterns.
```

## Full Integration

### System Prompt Addition

```markdown
# I Know Kung Fu - Skill Loading System

You have access to a skill loading system. When encountering tasks:

1. **Detect Task Type**: Identify keywords in user request
2. **Load Relevant Skills**: Read matching cartridge from skill-cartridges/
3. **Apply Patterns**: Follow loaded patterns and best practices
4. **Execute**: Perform task using loaded skills

Available skill categories:
- `file-operations/` - File read/write/edit patterns
- `search-operations/` - Code search and navigation
- `task-management/` - Todo and workflow tracking
- `error-handling/` - Error recovery patterns
- `memory-patterns/` - Cross-session memory
- `subagent-patterns/` - Agent delegation
- `planning-patterns/` - 5-phase planning mode
- `web-operations/` - Web search and fetch
- `code-intelligence/` - Code generation and bash

Load skills proactively for complex tasks.
```

### Hook Integration

```json
// .claude/hooks.json
{
  "PreToolUse": [
    {
      "matcher": "Bash|Edit|Write|Read",
      "hooks": ["./scripts/load-relevant-skill.sh"]
    }
  ]
}
```

### Memory Integration

Add to memory for persistence:
```
User prefers skill-driven approach. Always check skill-cartridges/ for relevant patterns before starting complex tasks.
```

## Skill Cartridge Loading Script

```bash
#!/bin/bash
# scripts/load-relevant-skill.sh

# Detect task type from context
TASK_TYPE=$(echo "$CLAUDE_CONTEXT" | grep -oiE "file|search|error|plan|web|bash" | head -1)

case "$TASK_TYPE" in
  file) cat skill-cartridges/file-operations/file-manipulation.json ;;
  search) cat skill-cartridges/search-operations/code-search.json ;;
  error) cat skill-cartridges/error-handling/error-recovery.json ;;
  plan) cat skill-cartridges/planning-patterns/planning-mode.json ;;
  web) cat skill-cartridges/web-operations/web-operations.json ;;
  bash) cat skill-cartridges/code-intelligence/bash-execution.json ;;
esac
```
