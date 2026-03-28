# Windsurf IDE Integration Template

## .windsurfrules Configuration

Create `.windsurfrules` in your project:

```
# I Know Kung Fu - Skill Enhancement

## Core Patterns

### File Operations
- ALWAYS read before editing
- Use Edit tool for modifications
- Never create new files when editing suffices
- Use absolute paths

### Search Operations
- Use Glob for file patterns
- Use Grep for content search
- NEVER use bash find/grep/cat

### Task Management
- Create TodoWrite for 3+ steps
- Only ONE in_progress at a time
- Mark completed IMMEDIATELY after finishing

### Error Handling
- Don't retry same failing operation
- Consider root cause
- Use alternatives before escalating

### Planning
- Use 5-phase planning for non-trivial work
- Get approval before major changes
```

## Cascade Integration

For Windsurf's Cascade AI:

```yaml
# .windsurf/cascade.yaml
skills:
  enabled: true
  cartridges:
    - path: skill-cartridges/file-operations
      triggers: [file, read, write, edit]
    - path: skill-cartridges/search-operations
      triggers: [search, find, grep, locate]
    - path: skill-cartridges/task-management
      triggers: [todo, task, steps, track]
    - path: skill-cartridges/error-handling
      triggers: [error, fail, retry, recover]
    - path: skill-cartridges/planning-patterns
      triggers: [plan, design, architecture]

context:
  include:
    - NAVIGATION.md
    - DECISION_TREE.md
    - skill-cartridges/**/*.json
```

## Project Settings

```json
// .windsurf/settings.json
{
  "windsurf.ai.contextDepth": "deep",
  "windsurf.ai.contextFiles": [
    "skill-cartridges/**/*.json",
    "NAVIGATION.md",
    "SYSTEM_PROMPT.md"
  ],
  "windsurf.ai.autoContext": true,
  "windsurf.ai.maxTokens": 128000
}
```

## Workflow Triggers

Configure automatic skill loading:

```json
// .windsurf/workflows.json
{
  "workflows": {
    "beforeEdit": {
      "loadSkills": ["file-manipulation"],
      "validate": ["file-exists", "has-read"]
    },
    "beforeSearch": {
      "loadSkills": ["code-search"],
      "preferTools": ["Glob", "Grep"]
    },
    "beforeComplexTask": {
      "loadSkills": ["task-workflow", "planning-mode"],
      "createTodo": true
    }
  }
}
```

## Keyboard Shortcuts

```
Cmd+Shift+K - Load skill cartridge
Cmd+Shift+P - Enter planning mode
Cmd+Shift+T - Create todo list
Cmd+Shift+E - Error recovery mode
```
