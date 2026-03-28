# Cursor IDE Integration Template

## .cursorrules Configuration

Create or update `.cursorrules` in your project:

```cursorrules
# I Know Kung Fu - Skill Loading System

## File Operations
- Always read files before modifying them
- Use Edit over Write for existing files
- Use absolute paths for all file operations

## Search Operations
- Use Glob tool for file finding (never bash find)
- Use Grep tool for content search (never bash grep)
- Start with files_with_matches mode

## Task Management
- Create todo list for tasks with 3+ steps
- Only one task in_progress at a time
- Mark tasks completed immediately after finishing

## Error Handling
- Don't retry the same failing operation
- Think about root cause before retrying
- Consider alternatives before escalating

## Planning
- Use planning mode for non-trivial implementations
- Consider multiple approaches for complex tasks
- Get user approval before major changes
```

## VS Code Settings

Add to `.vscode/settings.json`:

```json
{
  "cursor.ai.systemPrompt": "You have access to skill cartridges. Load patterns from skill-cartridges/ for enhanced task execution. Key patterns: read before edit, use Glob/Grep tools, create todos for 3+ steps.",
  
  "cursor.ai.customPrompts": {
    "refactor": "Load skill-cartridges/code-intelligence/code-generation.json. Apply refactoring patterns with full context awareness.",
    "debug": "Load skill-cartridges/error-handling/error-recovery.json. Apply error recovery patterns systematically.",
    "implement": "Load skill-cartridges/planning-patterns/planning-mode.json. Plan before implementing complex features."
  }
}
```

## Command Palette Integration

Add custom commands:

```json
// .vscode/commands.json
{
  "cursor.loadSkill": {
    "title": "Load Skill Cartridge",
    "category": "I Know Kung Fu"
  },
  "cursor.planMode": {
    "title": "Enter Planning Mode",
    "category": "I Know Kung Fu"
  },
  "cursor.verifyCode": {
    "title": "Verify Implementation",
    "category": "I Know Kung Fu"
  }
}
```

## Workspace Configuration

Create `i-know-kung-fu.code-workspace`:

```json
{
  "folders": [
    {
      "path": "."
    }
  ],
  "settings": {
    "cursor.ai.contextFiles": [
      "skill-cartridges/**/*.json",
      "NAVIGATION.md",
      "DECISION_TREE.md"
    ],
    "cursor.ai.maxContextFiles": 50
  },
  "extensions": {
    "recommendations": [
      "cursor.cursor"
    ]
  }
}
```

## Inline Chat Enhancement

For inline chat (Cmd+K), use:

```
@skill file-manipulation - Apply file operation patterns
@skill code-search - Apply search patterns
@skill planning-mode - Apply planning patterns
@skill error-recovery - Apply error handling patterns
```
