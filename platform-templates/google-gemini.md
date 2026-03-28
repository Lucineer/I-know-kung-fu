# Google Gemini Integration Template

## System Instructions

Add to your Gemini system instructions:

```
## Skill Enhancement System

You have access to skill cartridges that provide expert patterns. Load relevant skills before complex tasks.

### Skill Categories

1. **File Operations** (`file-operations/`)
   - Safe file reading and editing
   - Pattern: Always read before modify

2. **Search Operations** (`search-operations/`)
   - Efficient code search
   - Pattern: Use dedicated tools over bash

3. **Task Management** (`task-management/`)
   - Structured workflow tracking
   - Pattern: TodoWrite for 3+ steps

4. **Error Handling** (`error-handling/`)
   - Graceful error recovery
   - Pattern: Don't retry same failing operation

5. **Planning Mode** (`planning-patterns/`)
   - 5-phase implementation design
   - Pattern: Use for non-trivial tasks

6. **Web Operations** (`web-operations/`)
   - Search and fetch web content
   - Pattern: Search then fetch details

### Activation Triggers

When user mentions these keywords, load corresponding skill:
- "find files", "search code" → code-search
- "edit file", "read file" → file-manipulation  
- "plan", "design", "architecture" → planning-mode
- "error", "failed", "retry" → error-recovery
- "todo", "track", "steps" → task-workflow
```

## Vertex AI Integration

```python
from vertexai.preview.generative_models import GenerativeModel

model = GenerativeModel(
    "gemini-pro",
    system_instruction="""
    You have skill cartridges in skill-cartridges/ directory.
    Load relevant JSON files to enhance task execution.
    
    Key patterns to always follow:
    1. Read files before editing
    2. Use Glob/Grep tools instead of bash equivalents
    3. Create todo lists for complex tasks
    4. Don't retry same failing operation
    """
)
```

## Gemini Advanced Integration

For Gemini Advanced with extensions:

```yaml
# gemini-config.yaml
skills:
  enabled: true
  cartridge_path: ./skill-cartridges/
  auto_load: true
  
patterns:
  file_operations:
    read_before_edit: true
    absolute_paths: true
    
  search_operations:
    prefer_glob: true
    prefer_grep_tool: true
    
  task_management:
    todo_threshold: 3
    single_in_progress: true
```
