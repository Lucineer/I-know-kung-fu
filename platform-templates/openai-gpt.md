# OpenAI GPT Integration Template

## System Prompt Addition

Add to your GPT's system instructions:

```
You have access to skill cartridges that enhance your capabilities. 

## Skill Loading Protocol

When you encounter a task, first determine which skills apply:

| Task Keywords | Load This Cartridge |
|--------------|---------------------|
| file, read, write, edit | file-operations/file-manipulation.json |
| search, find, grep, locate | search-operations/code-search.json |
| todo, task, track, manage | task-management/task-workflow.json |
| error, fail, retry, recover | error-handling/error-recovery.json |
| plan, design, architecture | planning-patterns/planning-mode.json |
| web, fetch, search online | web-operations/web-operations.json |
| bash, command, execute, run | code-intelligence/bash-execution.json |

After identifying relevant skills, apply their patterns before proceeding.

## Key Patterns

### File Operations
- Always read before editing
- Use Edit over Write for existing files
- Use absolute paths

### Search Operations  
- Use Glob for file finding (never bash find)
- Use Grep for content search (never bash grep)
- Start with files_with_matches mode

### Task Management
- Create TodoWrite for 3+ step tasks
- Only one task in_progress at a time
- Mark completed immediately after finishing

### Error Handling
- Don't retry exact same failing operation
- Think about root cause
- Consider alternatives before escalating
```

## Function Calling Integration

For GPTs with function calling, define skill loading:

```json
{
  "name": "load_skill_cartridge",
  "description": "Load a skill cartridge for enhanced task execution",
  "parameters": {
    "type": "object",
    "properties": {
      "cartridge_path": {
        "type": "string",
        "description": "Path to skill cartridge JSON file"
      }
    },
    "required": ["cartridge_path"]
  }
}
```

## Assistants API Integration

```python
from openai import OpenAI

client = OpenAI()

assistant = client.beta.assistants.create(
    name="Skilled Assistant",
    instructions="""You have access to skill cartridges. 
    Load relevant skills from skill-cartridges/ directory before complex tasks.
    
    Available skills:
    - file-manipulation: File operations
    - code-search: Search and navigation
    - task-workflow: Task management
    - error-recovery: Error handling
    - planning-mode: Implementation planning
    """,
    model="gpt-4-turbo-preview"
)
```
