# Fork & Customize Guide

> **Build your own skill library while staying connected to the ecosystem**

---

## The Fork Strategy

```
ORIGINAL (i-know-kung-fu)
├── skill-cartridges/     ← Cold skills (reference on demand)
├── agents/
├── platforms/
└── ...

YOUR FORK
├── hot-skills/          ← Skills you use constantly
├── custom-agents/       ← Your specialized agents
├── custom-platforms/    ← Your platform configs
└── references/          → Point back to original for cold skills
```

---

## Hot vs Cold Skills

### Hot Skills (Keep Local)

Skills you use constantly. Keep in your fork for:
- Zero latency
- Custom modifications
- Always available

### Cold Skills (Reference Original)

Skills you rarely use. Don't duplicate:
- Reference original repo
- Load on demand
- Stay synced with updates

---

## Setting Up Your Fork

### Step 1: Fork on GitHub

1. Go to https://github.com/SuperInstance/I-know-kung-fu
2. Click "Fork"
3. Name it (e.g., `my-agent-skills`)

### Step 2: Clone and Structure

```bash
git clone https://github.com/YOUR-USERNAME/my-agent-skills.git
cd my-agent-skills

# Create your structure
mkdir -p hot-skills custom-agents references
```

### Step 3: Configure Upstream

```bash
git remote add upstream https://github.com/SuperInstance/I-know-kung-fu.git
```

### Step 4: Create Reference System

Create `references/skill-router.json`:

```json
{
  "hot_skills": [
    "code-generation",
    "pdf-operations",
    "react-reasoning"
  ],
  "cold_skill_source": "https://github.com/SuperInstance/I-know-kung-fu",
  "routing": {
    "hot": "./hot-skills/",
    "cold": "https://raw.githubusercontent.com/SuperInstance/I-know-kung-fu/main/skill-cartridges/"
  }
}
```

---

## The Moat: Stay Synced

### Check for Updates

```bash
git fetch upstream
git log HEAD..upstream/main --oneline
```

Shows:
```
abc1234 Add 15 new skill cartridges
def5678 Update reasoning patterns
ghi9012 Add platform templates for Mistral
```

### Merge Updates

```bash
git merge upstream/main
```

Your customizations stay, new skills flow in.

### What You Get

- New skills automatically available
- Structure improvements
- Platform additions
- Bug fixes

---

## Customization Patterns

### Pattern 1: Specialized Skill

Create `hot-skills/my-specialty.json`:

```json
{
  "skill_cartridge": {
    "id": "my-specialty",
    "name": "My Domain Specialty",
    "injection_payload": {
      "system_prompt_addon": "You are specialized in [MY DOMAIN].",
      "context_knowledge": "[DOMAIN-SPECIFIC KNOWLEDGE]"
    }
  }
}
```

### Pattern 2: Streamlined Agent

Create `custom-agents/my-agent.json`:

```json
{
  "profile": "my-agent",
  "base": "claude-code-emulator",
  "modifications": {
    "skills_equipped": [
      "hot-skills/my-specialty",
      "hot-skills/code-generation"
    ],
    "removed_skills": ["creative-writing", "marketing"],
    "custom_behavior": "Always prefer local hot-skills over cold skills"
  }
}
```

### Pattern 3: Custom Platform

Create `custom-platforms/my-deployment/`:

```
custom-platforms/
└── my-deployment/
    ├── config.json
    ├── skill-map.json
    └── README.md
```

---

## Routing Logic

Add to your agent's prime:

```
When loading skills:
1. Check hot-skills/ first
2. If not found, check references/skill-router.json
3. Load from cold source if needed
4. Cache frequently used cold skills to hot
```

---

## Contribution Back

When you create something useful:

1. **Test** - Verify it works
2. **Document** - Add clear README
3. **PR** - Submit to original repo

Benefits:
- Others benefit from your work
- You get maintenance help
- Community improvements flow back

---

## The Moat Effect

```
         Original Repo
              │
    ┌─────────┼─────────┐
    │         │         │
 Fork A    Fork B    Fork C
    │         │         │
    ▼         ▼         ▼
Custom   Custom   Custom
Skills   Skills   Skills
    │         │         │
    └────┬────┴────┬────┘
         │         │
      PRs flow    PRs flow
      back        back
         │         │
         ▼         ▼
      Original gets better
         │
      All forks benefit
```

**This is the moat:**
- Forks reference back
- Commits visible
- Improvements shared
- Network effect grows

---

## Quick Reference

| Task | Command |
|------|---------|
| Check for updates | `git fetch upstream && git log HEAD..upstream/main` |
| Merge updates | `git merge upstream/main` |
| Push your changes | `git push origin main` |
| Create PR to original | GitHub → New pull request |

---

*Fork once, customize infinitely, stay connected.*
