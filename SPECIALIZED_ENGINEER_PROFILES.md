# Specialized Engineer Profiles

> **18 pre-equipped agent profiles. Load one.**

---

## Quick Select

| Need | Profile |
|------|---------|
| Full Claude Code behavior | `claude-code-emulator` |
| Code generation | `codex-core` |
| System design | `codex-architect` |
| Debugging | `codex-debugger` |
| Safe refactoring | `codex-refactorer` |
| Step-by-step reasoning | `react-reasoner` |
| Logical problems | `chain-of-thought` |
| Creative exploration | `tree-of-thought` |
| Self-improvement | `reflection-agent` |
| Strategic planning | `plan-execute` |
| Parallel agents | `swarm-coordinator` |
| Top-down control | `hierarchy-manager` |
| Multi-perspective | `debate-moderator` |
| Agreement seeking | `consensus-builder` |
| Security analysis | `security-analyst` |
| Financial analysis | `financial-analyst` |
| Research | `research-specialist` |
| Creative content | `creative-writer` |

---

## Profile Format

Each profile loads as:

```json
{
  "profile_id": "profile-name",
  "skills_equipped": ["skill-1", "skill-2"],
  "reasoning_pattern": "react|cot|tot|reflection",
  "tolerance_level": "exact|close|approximate|behavioral",
  "system_prompt_base": "..."
}
```

---

## Code Intelligence

### claude-code-emulator
Full Claude Code behavior with adversarial verification.
- Skills: file-ops, code-exec, task-mgmt, react, reflection
- Tolerance: close
- Use: General development tasks

### codex-core
Code generation with context optimization.
- Skills: generation, completion, context-mgmt
- Tolerance: close
- Use: Write code from scratch

### codex-architect
System design and multi-file reasoning.
- Skills: architecture, dependencies, planning
- Tolerance: approximate
- Use: Design systems

### codex-debugger
Error resolution with hypothesis testing.
- Skills: trace-analysis, root-cause, fix-suggest
- Tolerance: close
- Use: Debug issues

### codex-refactorer
Safe transformation with behavior preservation.
- Skills: ast-transform, verify, rollback
- Tolerance: close
- Use: Refactor safely

---

## Reasoning Patterns

### react-reasoner
Thought-Action-Observation loops.
- Pattern: ReAct
- Max iterations: 10
- Use: Iterative problem solving

### chain-of-thought
Step-by-step logical reasoning.
- Pattern: CoT
- Use: Math, logic, sequential problems

### tree-of-thought
Multi-path exploration.
- Pattern: ToT
- Branching: 3
- Use: Creative, strategic problems

### reflection-agent
Self-evaluating with iterative improvement.
- Pattern: Reflection
- Max refinement: 3
- Use: Quality-critical tasks

### plan-execute
Strategic planning with adaptive execution.
- Pattern: Plan-Execute
- Use: Long-horizon tasks

---

## Orchestration

### swarm-coordinator
Parallel multi-agent execution.
- Distribution: broadcast, partition
- Aggregation: merge, vote, rank
- Use: Parallel workloads

### hierarchy-manager
Top-down chain of command.
- Levels: 3 (orchestrator, manager, worker)
- Use: Enterprise workflows

### debate-moderator
Multi-perspective synthesis.
- Participants: 2-4
- Turns: 3
- Use: Complex decisions

### consensus-builder
Agreement-seeking coordination.
- Voting: majority, unanimous, weighted
- Use: Team decisions

---

## Domain Specialists

### security-analyst
Vulnerability detection and audit.
- Tolerance: exact
- Use: Security reviews

### financial-analyst
Market analysis and modeling.
- Tolerance: exact (calcs)
- Use: Financial tasks

### research-specialist
Information synthesis.
- Tolerance: approximate
- Use: Research tasks

### creative-writer
Content generation.
- Tolerance: behavioral
- Use: Creative tasks

---

## How to Load

```
1. Read profile JSON
2. Inject system_prompt_base
3. Load skills_equipped
4. Activate reasoning_pattern
5. Set tolerance_level
```

---

*Load one profile. Become that agent.*
