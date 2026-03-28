# Zed Editor Integration Template

## settings.json Configuration

Add to your Zed settings:

```json
{
  "assistant": {
    "default_model": {
      "provider": "anthropic",
      "model": "claude-sonnet-4"
    },
    "system_prompt": "You have access to skill cartridges in skill-cartridges/. Load relevant patterns before complex tasks. Key patterns: read before edit, use Glob/Grep tools, create todos for 3+ steps, don't retry same failing operation."
  },
  "context_servers": {
    "skill-loader": {
      "command": "cat",
      "args": ["skill-cartridges/file-operations/file-manipulation.json"]
    }
  }
}
```

## Project Context

Create `.zed/context.md`:

```markdown
# Project Context - I Know Kung Fu Integration

## Skill Cartridges Available

Load from `skill-cartridges/` directory:

| Category | Cartridge | Use When |
|----------|-----------|----------|
| File Ops | file-manipulation.json | Reading, writing, editing files |
| Search | code-search.json | Finding files, searching content |
| Tasks | task-workflow.json | Multi-step tasks (3+ steps) |
| Errors | error-recovery.json | Handling failures |
| Planning | planning-mode.json | Non-trivial implementations |
| Web | web-operations.json | Web search and fetch |
| Bash | bash-execution.json | Running commands |

## Key Patterns

1. **Files**: Always read before editing
2. **Search**: Use Glob/Grep tools, not bash
3. **Tasks**: TodoWrite for 3+ steps
4. **Errors**: Don't retry same failure
5. **Planning**: 5-phase workflow for complex work
```

## Assistant Panel Integration

For Zed's assistant panel:

```json
{
  "assistant": {
    "panel": {
      "default_width": 400,
      "default_open": true
    },
    "enable_context": true,
    "context_paths": [
      "skill-cartridges/**/*.json",
      "NAVIGATION.md",
      "DECISION_TREE.md"
    ]
  }
}
```

## Slash Commands

Create `.zed/commands.json`:

```json
{
  "commands": {
    "/skill": {
      "description": "Load a skill cartridge",
      "action": "read",
      "path_template": "skill-cartridges/{category}/{skill}.json"
    },
    "/plan": {
      "description": "Enter planning mode",
      "load": "skill-cartridges/planning-patterns/planning-mode.json"
    },
    "/todo": {
      "description": "Create task list",
      "load": "skill-cartridges/task-management/task-workflow.json"
    }
  }
}
```

## Key Bindings

```json
{
  "key_bindings": {
    "cmd-shift-s": ["assistant::LoadSkill", {"skill": "code-search"}],
    "cmd-shift-p": ["assistant::LoadSkill", {"skill": "planning-mode"}],
    "cmd-shift-t": ["assistant::LoadSkill", {"skill": "task-workflow"}]
  }
}
```

## Inline Assistant

For inline assistant (Cmd+Enter):

```json
{
  "inline_assistant": {
    "prepend_context": "Apply patterns from skill-cartridges/ for this task.",
    "default_behavior": "read_before_edit"
  }
}
```
