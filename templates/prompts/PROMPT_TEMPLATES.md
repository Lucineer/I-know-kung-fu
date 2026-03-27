# Prompt Templates

> **Ready-to-use prompt templates for common agent scenarios.**

---

## 🚀 Quick Start Prompts

### Tool Discovery Prompt

```markdown
I need to accomplish the following task: [DESCRIBE TASK]

Please help me find the right agent or tool by:

1. Checking DECISION_TREE.md for guided discovery
2. Looking at TOOL_CARDS.md for quick reference
3. Identifying the complexity level (simple/moderate/complex/enterprise)
4. Recommending the best agent with reasoning

After finding the right tool, provide:
- Agent name and location
- Key configuration needed
- Expected outcome
```

### Multi-Tool Orchestration Prompt

```markdown
I have a complex task that might need multiple tools: [DESCRIBE TASK]

Please:
1. Break down the task into sub-tasks
2. Identify which agents/tools are needed for each
3. Determine the execution order
4. Show how outputs flow between tools
5. Suggest any optimization opportunities

Format the orchestration as:
Step 1: [Agent] → [Output]
Step 2: [Agent] → [Output]
...
```

### Cost Optimization Prompt

```markdown
My current LLM costs are too high. Current situation:
- Queries per day: [NUMBER]
- Average tokens per query: [NUMBER]
- Current cost per day: [$AMOUNT]

Please recommend:
1. Which cost optimization agents would help most
2. Expected savings percentage
3. Implementation complexity
4. Any trade-offs to consider

Priority: [cost/quality/speed]
```

---

## 🧠 Reasoning Prompts

### ReAct Reasoning Prompt

```markdown
Using the ReAct (Reasoning and Acting) pattern, solve this problem:

PROBLEM: [DESCRIBE PROBLEM]

Available tools: [LIST TOOLS]

For each step:
1. Thought: [Your reasoning about the current state]
2. Action: [Tool to use or action to take]
3. Observation: [What you learned]

Continue until you reach a final answer.
```

### Chain-of-Thought Prompt

```markdown
Analyze this step-by-step using Chain-of-Thought reasoning:

QUESTION: [YOUR QUESTION]

Show your work:
Step 1: [First reasoning step]
Step 2: [Second reasoning step]
...
Conclusion: [Final answer with confidence level]

Verify: Check each step for logical consistency.
```

### Tree-of-Thought Prompt

```markdown
Explore multiple solution paths for this problem:

PROBLEM: [DESCRIBE PROBLEM]

For each potential approach:
1. Describe the approach
2. Evaluate pros/cons (score 1-10)
3. Identify potential issues
4. Estimate likelihood of success

After exploring 3-5 paths:
- Recommend the best approach
- Explain why it's optimal
- Note any risks or considerations
```

---

## 💬 Conversation Prompts

### Customer Support Prompt

```markdown
You are a customer support agent with access to:
- Knowledge base (via RAG Pipeline)
- Customer history (via Hierarchical Memory)
- Escalation rules (via Escalation Router)

Customer message: [MESSAGE]
Customer tier: [TIER]
Previous interactions: [COUNT]

Guidelines:
1. Detect emotional state (use Emotion Detector patterns)
2. Retrieve relevant knowledge
3. Provide helpful, empathetic response
4. Determine if escalation needed

Response format:
- Acknowledgment of issue
- Solution or information
- Next steps (if any)
- Escalation status (if applicable)
```

### Persona Adaptation Prompt

```markdown
Adapt the following response to match these persona requirements:

ORIGINAL RESPONSE:
[ORIGINAL TEXT]

TARGET PERSONA:
- Tone: [formal/friendly/casual/technical]
- Audience: [executive/developer/consumer/expert]
- Brand voice: [description]

Constraints:
- Maximum length: [WORDS]
- Include: [SPECIFIC ELEMENTS]
- Avoid: [SPECIFIC ELEMENTS]

Output the adapted response.
```

---

## 💻 Code Prompts

### Architecture Design Prompt

```markdown
Design a system architecture for:

REQUIREMENTS:
- Functionality: [DESCRIBE]
- Scale: [USERS/REQUESTS PER DAY]
- Performance: [LATENCY REQUIREMENTS]
- Budget: [CONSTRAINTS]

Please provide:
1. High-level architecture diagram (ASCII or description)
2. Technology recommendations with rationale
3. Scalability considerations
4. Security considerations
5. Estimated costs
6. Implementation phases

Reference any relevant patterns from the agents/code-architect/ specifications.
```

### Test Generation Prompt

```markdown
Generate comprehensive tests for this code:

```[LANGUAGE]
[CODE TO TEST]
```

Requirements:
- Test framework: [JEST/PYTEST/JUNIT/ETC]
- Coverage target: [PERCENTAGE]
- Test types needed: [UNIT/INTEGRATION/EDGE CASES]

Generate:
1. Happy path tests
2. Error case tests
3. Edge case tests
4. Boundary tests
5. Mock setup (if needed)
```

### Refactoring Prompt

```markdown
Analyze and refactor this code for improvement:

```[LANGUAGE]
[CODE TO REFACTOR]
```

Focus areas:
- [ ] Readability
- [ ] Performance
- [ ] Maintainability
- [ ] Test coverage

Provide:
1. List of code smells detected
2. Specific refactoring recommendations
3. Refactored code with changes highlighted
4. Summary of improvements
5. Any trade-offs introduced
```

---

## 📊 Data Prompts

### Data Quality Assessment Prompt

```markdown
Assess the quality of this dataset:

DATASET DESCRIPTION:
- Source: [SOURCE]
- Size: [ROWS x COLUMNS]
- Purpose: [USE CASE]

Sample data:
[PROVIDE SAMPLE OR SCHEMA]

Evaluate:
1. Completeness (missing values)
2. Accuracy (valid values)
3. Consistency (format uniformity)
4. Timeliness (data freshness)
5. Uniqueness (duplicates)

Output:
- Quality score (0-100)
- Issues found (prioritized)
- Recommendations for improvement
```

### RAG Query Prompt

```markdown
Answer this question using the provided context:

QUESTION: [QUESTION]

CONTEXT:
[RETRIEVED DOCUMENTS]

Instructions:
1. Answer ONLY using the provided context
2. If answer is not in context, say so
3. Cite specific sources for each claim
4. Format citations as [Source: Document Name]

Answer:
[YOUR ANSWER]

Sources used:
- [Document 1]: [Relevant excerpt]
- [Document 2]: [Relevant excerpt]
```

---

## 🎯 Decision Prompts

### A/B Test Analysis Prompt

```markdown
Analyze this A/B test result:

TEST: [TEST NAME]
Duration: [DAYS]
Control: [A DESCRIPTION]
Treatment: [B DESCRIPTION]

DATA:
- Control: [N] users, [conversion]% conversion
- Treatment: [N] users, [conversion]% conversion

Analyze:
1. Statistical significance (p-value)
2. Effect size
3. Confidence interval
4. Practical significance
5. Segment breakdown (if available)

Recommendation:
- [ ] Implement treatment
- [ ] Continue testing
- [ ] Discard treatment
- [ ] Investigate further

Rationale: [EXPLANATION]
```

### Escalation Decision Prompt

```markdown
Determine if this query should be escalated:

QUERY: [USER QUERY]
CONTEXT: [ADDITIONAL CONTEXT]

Escalation criteria:
- Complex legal/regulatory issues
- High-value customer complaints
- Technical issues beyond AI capability
- Safety concerns
- Explicit human request

Analysis:
- Complexity score: [1-10]
- Risk level: [LOW/MEDIUM/HIGH]
- Confidence in AI response: [0-100%]

Decision: [ESCALATE/HANDLE AI]
Reasoning: [EXPLANATION]
Recommended action: [SPECIFIC NEXT STEP]
```

---

## 🌐 Platform-Specific Prompts

### MiniMax Expert Prompt

```markdown
Create a MiniMax Expert configuration for:

EXPERT NAME: [NAME]
PURPOSE: [DESCRIPTION]

Define:
1. Expert description (2-3 sentences)
2. Input parameters with types
3. Output format
4. Example interactions (3-5)
5. Pricing tier recommendation

Output in MiniMax schema format.
```

### Claude MCP Server Prompt

```markdown
Design an MCP server for:

SERVER NAME: [NAME]
PURPOSE: [DESCRIPTION]

Define:
1. Tools provided (with schemas)
2. Resources exposed
3. Prompts included
4. Configuration options
5. Installation instructions

Output as MCP server implementation guide.
```

### Skills.sh Skill Prompt

```markdown
Create a Skills.sh skill for:

SKILL NAME: [NAME]
DESCRIPTION: [ONE-LINER]

Include:
1. Skill purpose (when to use)
2. Step-by-step instructions
3. 3-5 examples with inputs/outputs
4. Configuration options
5. Dependencies

Format for Skills.sh directory submission.
```

---

## 🔧 Integration Prompts

### Agent Stack Building Prompt

```markdown
Build an agent stack for this use case:

USE CASE: [DESCRIPTION]
SCALE: [VOLUME/USERS]
BUDGET: [CONSTRAINTS]
QUALITY REQUIREMENT: [LEVEL]

Design a stack by:
1. Identifying necessary capabilities
2. Selecting primary agents
3. Adding enhancement agents
4. Defining data flow between agents
5. Estimating costs and performance

Output as:
- Architecture diagram
- Agent list with configuration
- Flow description
- Cost estimate
```

### System Prompt Generation Prompt

```markdown
Generate a system prompt for an AI that:

ROLE: [DESCRIPTION]
CAPABILITIES: [LIST]
CONSTRAINTS: [LIST]
TONE: [DESCRIPTION]

The system prompt should:
1. Define the agent's role clearly
2. List available tools/agents
3. Specify decision protocols
4. Include quality guidelines
5. Add fallback behaviors

Output as copy-paste ready system prompt.
```

---

*Templates: 20+ prompts | Last Updated: March 2026*
