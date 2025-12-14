---
allowed-tools: Write, AskUserQuestion, Read, Glob
description: Create a feature specification document through interactive questions
argument-hint: [feature_name]
---

# Create Feature Prompt

Interactively gather feature requirements and generate a high-level feature specification document (WHAT the feature does, not HOW to implement it). The specification will be saved to `.claude/feature_prompts/{feature_name}.md`.

**Purpose**: This command creates feature specifications focused on requirements, behavior, and expected outcomes - NOT implementation details or code snippets. Use this to document feature requests before handing them to design/implementation agents.

## Execute

### Step 1: Determine Feature Name
- If `$ARGUMENTS` is provided, use it as the feature name
- If not provided, ask the user for a feature name
- Convert feature name to snake_case for the filename
- Validate: no special characters, max 50 characters
- Set output path: `.claude/feature_prompts/{feature_name_snake_case}.md`

### Step 2: Check File Existence
- Check if `.claude/feature_prompts/{feature_name}.md` already exists
- If exists: Exit with error message: "❌ Feature prompt already exists at {path}. Use a different name or delete the existing file."
- Ensure `.claude/feature_prompts/` directory exists (create if needed)

### Step 3: Gather Feature Requirements (Interactive Questions)

Use the `AskUserQuestion` tool to gather requirements in 4 batches:

**Batch 1 - Core Feature**
Ask these questions:
1. "What is the primary purpose of this feature?" (header: "Purpose", multiSelect: false)
   - Options: New functionality, Enhancement to existing feature, Bug fix, Refactoring, Performance optimization
2. "Which parts of the system will be affected?" (header: "Scope", multiSelect: true)
   - Options: CLI interface, Core logic/crawler, Data models, Configuration, Documentation
3. "Should this feature be required or optional?" (header: "Requirement", multiSelect: false)
   - Options: Required (always active), Optional with flag, Optional in config, Conditional based on context

**Batch 2 - Behavior & User Experience**
Ask these questions:
1. "What format should the feature output/results be in?" (header: "Output Format", multiSelect: false)
   - Options: Plain text, JSON, Markdown, Files on disk, No output (side effect only)
2. "How should errors be handled?" (header: "Error Handling", multiSelect: false)
   - Options: Exit with error code, Log warning and continue, Fallback to default behavior, Prompt user for action
3. "What should be displayed to the user during/after execution?" (header: "Console Output", multiSelect: false)
   - Options: Success message only, Detailed progress, Summary statistics, Quiet mode (no output)

**Batch 3 - Technical Approach**
Ask these questions:
1. "What external libraries or packages should be considered?" (header: "Libraries", multiSelect: false)
   - Options: Standard library only, Existing project dependencies, New package needed, Framework-specific tools
2. "What validation should happen before execution?" (header: "Validation", multiSelect: true)
   - Options: Input validation, File/path validation, Permission checks, Network/resource availability, Configuration validation
3. "What metadata/context should be tracked?" (header: "Metadata", multiSelect: true)
   - Options: Timestamps, User information, Configuration used, Statistics/metrics, Source/origin data

**Batch 4 - Quality & Edge Cases**
Ask these questions:
1. "Which edge cases must be explicitly handled?" (header: "Edge Cases", multiSelect: true)
   - Options: Empty/null inputs, File already exists, Permission denied, Network failure, Invalid data format, Resource limits exceeded
2. "What testing scenarios are most critical?" (header: "Testing", multiSelect: true)
   - Options: Happy path, Error conditions, Edge cases, Integration with other features, Performance/load testing

### Step 4: Generate Feature Specification File

Using all answers from Step 3, create a markdown file with this structure:

```markdown
# Feature: {Feature Name}

## Overview
{Generate 2-3 sentences describing the feature purpose based on Batch 1 answers}

## Feature Requirements

### 1. {Category Based on Scope}
{List specific requirements from user answers - focus on WHAT not HOW}
- Observable behaviors
- Expected inputs and outputs
- User interaction patterns

### 2. {Another Category if multiple scopes}
{Continue with requirements}

### 3. Error Handling
{Based on Batch 2 error handling answer}
- What errors should be caught
- Expected error messages format
- Exit codes or continuation logic

### 4. User Experience
{Based on Batch 2 console output answer}
- What user sees during execution
- Success/failure indicators
- Verbosity options

## Development Approach

**Recommended Flow**:
- Test-Driven Development: Write tests first to define expected behavior
- Modular Design: Separate concerns (e.g., validation, core logic, output)
- Integration: Connect components cleanly

**Technology Suggestions**:
{Based on Batch 3 libraries answer - mention packages/frameworks, NO code snippets}

**Quality Standards**:
- Follow existing project code style
- Comprehensive type hints and docstrings
- Clear, actionable error messages

## Edge Cases to Handle

{List from Batch 4, bullet points}

## Testing Requirements

{Based on Batch 4 testing answer}
Test coverage should include:
- {Testing scenarios selected}

## Validation

{Based on Batch 3 validation answer}
Before execution, validate:
- {List validation requirements}

## Metadata

{Based on Batch 3 metadata answer}
Track the following information:
- {List metadata fields}

## Success Criteria

{Generate 5-10 measurable success criteria based on all answers}
1. {Specific observable outcome}
2. {Another measurable result}
...

## Example Usage After Implementation

```bash
# {Generate 3-5 realistic usage examples based on feature purpose}
```
```

Save this content to `.claude/feature_prompts/{feature_name}.md`

### Step 5: Report Success

Display to user:
```
✅ Feature specification created successfully!
📄 File: .claude/feature_prompts/{feature_name}.md

💡 Important: This is a FEATURE SPECIFICATION (WHAT), not an implementation guide (HOW)
   - Focuses on requirements, behavior, and expected outcomes
   - No implementation details or code snippets
   - High-level technology suggestions only

🎯 Next Steps:
   - Review the specification for completeness
   - Share with design/planning agent to create implementation plan
   - Or share with implementation agent to build the feature
```

## Read

If needed during question formulation, read:
- Existing feature prompts in `.claude/feature_prompts/` for examples
- Project structure to understand scope options
