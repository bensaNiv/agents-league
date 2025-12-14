---
name: create-expert-agent
description: Create specialized expert Claude Code sub-agents from Smart Librarian knowledge bases. This skill should be used when users want to create domain-specific expert agents (e.g., claude-code-expert, radar-expert, numpy-expert) that can efficiently answer questions using structured documentation with INDEX.md files.
---

# Create Expert Agent

## Overview

Generate specialized expert Claude Code sub-agents from Smart Librarian knowledge bases. This skill creates intelligent agents that know how to efficiently navigate documentation using INDEX.md files and can be consulted for domain-specific expertise.

## When to Use This Skill

Use this skill when users request:
- "Create a [domain] expert agent from this knowledge base"
- "Generate an expert agent for [technology/system] documentation"
- "I have documentation, make an expert agent that can answer questions about it"
- Creating domain specialists like claude-code-expert, radar-expert, api-expert, numpy-expert, etc.

## Workflow

### 1. Validate Requirements

First, ensure the knowledge base follows Smart Librarian format:
- Contains an `INDEX.md` file at the root
- Has properly structured documentation files
- Uses the consultation rules format ("Consult when: ...")

Use the validation script:
```bash
python scripts/validate_smart_librarian.py <knowledge-base-path>
```

### 2. Create the Expert Agent

Run the main creation script with the required parameters:
```bash
python scripts/create_expert_agent.py \
  --knowledge-base <path-to-knowledge-base> \
  --expert-name <expert-name> \
  --expert-description "<description of expertise>"
```

**Parameters:**
- `--knowledge-base`: Path to the Smart Librarian knowledge base directory
- `--expert-name`: Name for the expert (e.g., "claude-code", "radar-api", "numpy-math")
- `--expert-description`: What the expert specializes in (e.g., "Claude Code and Agent SDK expert")

### 3. Conflict Resolution

If an expert agent with the same name already exists, the script will:
- Display the existing agent's expertise
- Ask for user confirmation to overwrite
- Offer to create a versioned copy instead

### 4. Agent Capabilities

The created expert agent will:
- Have access to the knowledge base at `.claude/docs/<expert-name>_knowledge/`
- Know to consult the INDEX.md file first for efficient information retrieval
- Understand consultation rules to find relevant documentation quickly
- Be automatically discoverable by the main Claude Code session

## Expert Agent Usage

Once created, users can interact with the expert agent in two ways:

**Automatic consultation:** Main Claude session will understand when to call the expert based on the expertise description.

**Direct consultation:** Users can explicitly ask:
- "Ask [expert-name] expert about..."
- "Consult the [domain] expert for..."

## Knowledge Base Structure

The skill expects Smart Librarian knowledge bases with:
```
knowledge-base/
├── INDEX.md                    # Master index with consultation rules
├── document1.md               # Documentation files
├── document2.md
└── ...
```

The INDEX.md should contain:
- Document catalog with "Consult when" rules
- Quick reference for efficient navigation
- Metadata about the knowledge base

## Bundled Resources

### Scripts
- `create_expert_agent.py` - Main agent creation script
- `validate_smart_librarian.py` - Knowledge base format validation

### References
- `index_optimization_guide.md` - Best practices for INDEX.md usage
- `expert_agent_patterns.md` - Guidelines for effective expert agents

### Assets
- `expert_agent_template.md` - Template for generating expert agent files

## Examples

**Create a Claude Code expert:**
```bash
python scripts/create_expert_agent.py \
  --knowledge-base ./claude-docs \
  --expert-name claude-code \
  --expert-description "Claude Code and Agent SDK expert who can answer questions about Claude Code features, SDK usage, and development practices"
```

**Create a Radar expert:**
```bash
python scripts/create_expert_agent.py \
  --knowledge-base ./radar-docs \
  --expert-name radar-api \
  --expert-description "Radar system expert specializing in API usage, test cases, and bug tracking workflows"
```

The created agents will efficiently use the INDEX.md files to provide accurate, contextual answers about their domain of expertise.