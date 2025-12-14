# Claude Configuration Component Types Reference

A comprehensive guide to understanding the different types of `.claude` configuration components and their specific characteristics for copying and management.

## Overview

Claude Code supports multiple configuration component types, each with distinct purposes, structures, and copying requirements. This reference helps you understand what each component type does and how to handle them properly.

## Component Type Categories

### Shareable Components (High Reusability)

These components are designed for sharing across projects and typically provide universal functionality.

#### Skills (`skills/`)

**Purpose**: Reusable capabilities and workflows with comprehensive documentation

**Structure**:
```
skills/skill-name/
├── SKILL.md (or skill.md)     # Main skill documentation
├── references/                # Optional supporting documentation
│   ├── patterns.md
│   ├── examples.md
│   └── troubleshooting.md
└── scripts/                   # Optional implementation scripts
    └── helper.py
```

**Frontmatter Format**:
```yaml
---
name: skill-name
description: Brief description of what this skill does
tags: [optional, categorization, tags]
---
```

**Copying Considerations**:
- Always copy complete directory structure including `references/`
- Validate frontmatter integrity in main SKILL.md file
- Check for internal references between files in references/
- High priority for sharing due to universal applicability

**Examples from Exploration**:
- `debug-unit-test-pass` (275 lines) - Systematic test debugging
- `run-tests` (700+ lines) - Reliable pytest execution
- `code-quality-check` (490 lines) - Comprehensive quality analysis
- `create-project-readme` (758 lines) - Structured README generation

#### Agents (`agents/`)

**Purpose**: Specialized AI assistants with specific expertise and tool access

**Structure**:
```
agents/
├── agent-name.md              # Single file agent definition
└── another-agent.md
```

**Frontmatter Format**:
```yaml
---
name: agent-name
description: Agent description and expertise area
tools: Bash, Read, Grep, Glob, Edit
model: inherit
color: red
---
```

**Copying Considerations**:
- Single file components (easier to copy)
- May reference knowledge bases - check for `knowledge/` dependencies
- Tool permissions are important for functionality
- Color coding helps with visual identification

**Examples from Exploration**:
- `tester.md` (126 lines) - QA automation specialist
- `code-reviewer.md` (247 lines) - Pre-commit review specialist
- `debugger.md` - Debugging specialist with red color coding
- `writer.md` - Documentation and writing specialist

#### Commands (`commands/`)

**Purpose**: Slash commands that expand to full prompts for specific workflows

**Structure**:
```
commands/
├── command-name.md            # Single file command definition
├── complex-command/           # Or directory for complex commands
│   ├── command.md
│   └── templates/
└── simple-command.md
```

**Frontmatter Format**:
```yaml
---
allowed-tools: Bash, Read, Glob, AskUserQuestion, Task
description: Command description and purpose
---
```

**Copying Considerations**:
- Most are single files (simple to copy)
- Some may have associated directories with templates
- Tool permissions are critical for command execution
- Project-specific commands should be filtered out

**Examples from Exploration**:
- `prime.md` - Context loading for new sessions
- `question.md` - Project structure queries
- `create-feature-prompt.md` - Interactive feature specification
- `git_status.md` - Repository status display

#### Hooks (`hooks/`)

**Purpose**: Python scripts that execute at specific lifecycle events

**Structure**:
```
hooks/
├── session_start.py           # Lifecycle event scripts
├── pre_tool_use.py
├── post_tool_use.py
├── notification.py
└── utils/                     # Supporting utilities
    ├── llm/
    └── tts/
```

**Script Header Format**:
```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# dependencies = ["requests", "aiohttp"]
# ///
```

**Copying Considerations**:
- Python scripts with specific dependency requirements
- May have supporting utility modules in `utils/`
- Execution permissions important
- Some may be project-specific (logging paths, etc.)

**Examples from Exploration**:
- `pre_tool_use.py` - Pre-execution logic and validation
- `notification.py` - Alert and notification system
- `stop.py` - Session cleanup with chat summaries
- `user_prompt_submit.py` - Prompt logging and session naming

#### Knowledge Bases (`knowledge/`)

**Purpose**: Organized information repositories for agent expertise

**Structure**:
```
knowledge/agent-name/
├── 00_INDEX.md                # Navigation and overview
├── 01_category.md             # Organized by topic
├── 02_another-topic.md
└── 08_advanced-topics.md
```

**Copying Considerations**:
- Complete directory structures must be preserved
- Numbered files indicate intended reading order
- Often referenced by specific agents
- High value for code review and quality standards

**Examples from Exploration**:
- `code-reviewer/` (234 lines total, 8 files) - Multi-language code standards
- Includes: Python/TypeScript/Go/Java/C++ standards
- OWASP Top 10, technical debt economics, quantitative metrics

#### Output Styles (`output-styles/`)

**Purpose**: Response formatting templates and display preferences

**Structure**:
```
output-styles/
├── style-name.md              # Single file style definitions
└── another-style.md
```

**Frontmatter Format**:
```yaml
---
name: Style Name
description: Style description and use cases
---
```

**Copying Considerations**:
- Single file components
- Personal preference items (lower priority)
- Can enhance user experience consistency
- Usually safe to copy without conflicts

**Examples from Exploration**:
- `ultra-concise.md` - Minimal words, maximum speed
- `bullet-points.md` - Structured bullet formatting
- `yaml-structured.md` - YAML-based response format
- `table-based.md` - Tabular data presentation

### Project-Specific Components (Default Exclude)

These components are typically specific to individual projects and should not be shared.

#### Runtime Data (`logs/`, `data/`)

**Purpose**: Session logs, execution data, cached information

**Structure**:
```
logs/
├── session-20241207-143022.json
├── pre-tool-use.log
└── notifications.json

data/
├── session-cache/
└── temporary-files/
```

**Copying Considerations**:
- **Always exclude** - contains project-specific runtime data
- May contain sensitive information or large files
- Not useful in other project contexts
- Can be regenerated by Claude Code during execution

#### Configuration Files (`settings.json`, `settings.local.json`)

**Purpose**: Project-specific permissions, hooks, and overrides

**Structure**:
```json
{
  "permissions": {
    "allow": ["mkdir", "uv", "python3"],
    "deny": ["rm", "sudo"]
  },
  "hooks": [...],
  "statusLine": "python3 .claude/status_lines/status_line_v4.py"
}
```

**Copying Considerations**:
- **Always exclude** - highly project-specific
- Contains local paths and project permissions
- Hooks configuration may reference project-specific scripts
- Merging would be complex and error-prone

#### Context and Prompts (`context/`, `feature_prompts/`, `design_prompts/`)

**Purpose**: Project-specific documentation and prompt libraries

**Structure**:
```
context/
├── project-context.md
└── domain-knowledge.md

feature_prompts/
├── auth-system.md
└── payment-flow.md
```

**Copying Considerations**:
- **Usually exclude** - domain/project specific
- May contain proprietary information
- Not applicable to other projects
- Can be large and unwieldy in shared configurations

#### Status Lines (`status_lines/`)

**Purpose**: Custom status display generators (Python scripts)

**Structure**:
```
status_lines/
├── status_line_v1.py
├── status_line_v2.py
├── status_line_v3.py
└── status_line_v4.py
```

**Copying Considerations**:
- **Mixed priority** - some are highly customized, others generic
- Version iterations show evolution (v1 → v4)
- May contain project-specific paths or logic
- Consider copying only if truly generic

## Component Detection Strategies

### Automatic Classification

Use file patterns and directory structures to automatically classify components:

```bash
# Shareable components
find .claude -type d -name "skills" -o -name "agents" -o -name "commands" -o -name "hooks" -o -name "knowledge" -o -name "output-styles"

# Project-specific (exclude)
find .claude -type d -name "logs" -o -name "data" -o -name "context" -o -name "*_prompts" -o -name "project_*"

# Configuration files (exclude)
find .claude -name "settings*.json" -o -name "*.local.*"
```

### Content-Based Analysis

Analyze file contents for project-specific indicators:

```bash
# Check for project-specific paths
grep -r "/Users/.*/" .claude/ --include="*.md" --include="*.py"

# Check for project names in content
grep -r "index_mcp\|specific-project-name" .claude/ --include="*.md"

# Check for local dependencies
grep -r "localhost\|127.0.0.1" .claude/ --include="*.py" --include="*.md"
```

### Frontmatter Analysis

Extract metadata from frontmatter to determine shareability:

```bash
# Extract names and descriptions
find .claude -name "*.md" -exec grep -l "^---$" {} \; | while read file; do
    echo "File: $file"
    sed -n '/^---$/,/^---$/p' "$file" | grep -E "^(name|description):"
    echo ""
done
```

## Conflict Resolution by Component Type

### Skills
- **High Impact**: Usually large, complex, with references
- **Strategy**: Backup + Replace recommended for newer versions
- **Validation**: Check references/ directory integrity

### Agents
- **Medium Impact**: Single files, but may affect knowledge bases
- **Strategy**: Review differences, especially tool permissions
- **Validation**: Verify knowledge base references still work

### Commands
- **Low-Medium Impact**: Usually single files
- **Strategy**: Overwrite safe for generic commands
- **Validation**: Check tool permissions compatibility

### Hooks
- **High Impact**: Affects system behavior
- **Strategy**: Backup + Replace, careful review recommended
- **Validation**: Test execution, check dependencies

### Knowledge Bases
- **High Impact**: Complex directory structures
- **Strategy**: Backup + Replace for complete directories
- **Validation**: Verify agent references, check file numbering

### Output Styles
- **Low Impact**: Personal preferences
- **Strategy**: Overwrite generally safe
- **Validation**: Basic frontmatter check sufficient

## Best Practices

### Pre-Copy Analysis
1. Scan all component types present in source
2. Classify each component as shareable vs project-specific
3. Identify potential conflicts with target directory
4. Estimate disk space requirements

### Copy Strategy Selection
1. **New Components**: Direct copy with validation
2. **Identical Components**: Skip to save time
3. **Conflicted Components**: Interactive resolution based on type
4. **Directory Structures**: Preserve complete hierarchy

### Post-Copy Validation
1. Verify frontmatter integrity in all .md files
2. Check directory structure completeness for skills
3. Validate references between components (agents → knowledge)
4. Test basic functionality where possible

This reference provides the foundation for intelligent component handling in the update-prime-claude-directory skill.