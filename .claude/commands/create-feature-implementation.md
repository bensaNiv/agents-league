---
description: Generate comprehensive implementation design document from a feature prompt with interactive design decisions
allowed-tools: Read, Write, Glob, AskUserQuestion, Task
---

You are tasked with creating a comprehensive implementation design document for a new feature. You will gather design decisions through interactive questions and generate a detailed guide for another developer or AI agent to implement the feature.

## Your Mission

Transform a feature requirements document into a complete implementation guide by:
1. Understanding the feature requirements
2. Analyzing the current codebase architecture
3. Gathering design decisions through interactive questions
4. Generating a comprehensive design document with code examples

## Step 1: Read the Feature Prompt

The user has provided a path to the feature prompt file. Read this file to understand:
- Feature overview and requirements
- Expected behavior
- Edge cases to handle
- Success criteria

## Step 2: Analyze the Codebase

Use the Task tool with the Explore agent to understand:
- Current project architecture and structure
- Technologies and frameworks in use (async/sync, testing framework, type system)
- Existing code patterns and conventions
- How similar features are currently implemented
- Dependencies and build tools

Example exploration prompt:
```
Explore the codebase to understand:
1. The overall architecture (module structure, separation of concerns)
2. Whether the code is async/sync and what patterns are used
3. Testing framework and testing patterns
4. Type hints usage and documentation style
5. How errors are currently handled
6. Any similar features I can reference
```

## Step 3: Ask Interactive Design Questions

Based on the feature requirements and codebase analysis, ask the user design questions using the AskUserQuestion tool. Cover ALL of these areas:

### Architecture & Module Structure (4 questions)
- Should this be a separate module or integrated into existing code?
- Where should different responsibilities live (validation, business logic, I/O)?
- What should the public API surface look like (class-based or function-based)?
- How should configuration be passed through the application layers?

### Data Flow & Integration Points (3 questions)
- At what point in the application flow should this feature execute?
- How should data be passed between components?
- Should existing data structures be extended or new ones created?

### Implementation Details (4-6 questions depending on feature)
Examples based on feature type:
- **For file operations**: Async or sync I/O? Path handling? File naming conventions?
- **For API features**: Request/response format? Error handling? Retry logic?
- **For data processing**: Streaming or batch? Memory management? Performance considerations?
- **For UI features**: Component structure? State management? User feedback?

### Error Handling & Edge Cases (3 questions)
- How should failures be handled (cleanup, retry, fail-fast)?
- What validation should occur before starting?
- How should partial failures be managed?

### Testing Strategy (2 questions)
- What mix of unit tests, integration tests, and mocks?
- Where should test files be located?

### Output, Timestamps & Future Compatibility (3 questions)
- Format details (timestamps, versioning, metadata)
- Should design support future enhancements?
- Any extensibility patterns to use?

**IMPORTANT**: Ask questions in groups of 4 questions per AskUserQuestion call. This keeps the interface manageable. You should make 4-6 separate calls total.

**Question Format**: Each question should have:
- `header`: Short label (max 12 chars)
- `question`: Clear, specific question with context
- `options`: 2-4 distinct choices with descriptions explaining trade-offs
- `multiSelect`: false (unless multiple answers make sense)

## Step 4: Generate Comprehensive Design Document

Create a detailed implementation guide following this structure:

### Document Structure

```markdown
# Implementation Guide: [Feature Name]

## Overview
Brief description of the feature and what this guide provides.

## Design Decisions Summary

### Architecture
- [Decision category]: [Choice made] - [Rationale]
- [List all architectural decisions with brief rationale]

### Data Flow
- [Decision category]: [Choice made] - [Rationale]

### Implementation Details
- [Decision category]: [Choice made] - [Rationale]
- [Cover all specific implementation choices]

### Error Handling
- [Decision category]: [Choice made] - [Rationale]

### Testing
- [Decision category]: [Choice made] - [Rationale]

### [Other Categories]
- [All other decisions organized by category]

---

## Implementation Steps

### Step 1: [First Major Task]

**File**: `path/to/file`

[Clear instructions with context]

```[language]
[Complete, ready-to-use code example]
```

[Additional context or notes]

### Step 2: [Second Major Task]

**File**: `path/to/file` (new file) OR (continued)

[Instructions...]

```[language]
[Complete code example]
```

[Continue for all major implementation steps...]

### Step N: [Final Task]

---

## Testing Strategy

### Test Structure

**File**: `path/to/test_file.py` (or appropriate extension)

[Overview of testing approach]

```[language]
[Complete test file with multiple test cases covering:]
- Happy path scenarios
- Edge cases
- Error conditions
- Integration scenarios
```

---

## Implementation Checklist

Use this checklist to ensure all components are implemented:

### [Category 1]
- [ ] Item 1
- [ ] Item 2
- [ ] Item 3

### [Category 2]
- [ ] Item 1
- [ ] Item 2

[Continue for all major components...]

---

## Common Implementation Pitfalls

### Pitfall 1: [Common Mistake]
```[language]
# ❌ Wrong
[Example of incorrect code]

# ✅ Correct
[Example of correct code]
```
[Explanation of why this matters]

### Pitfall 2: [Another Mistake]
[Same structure...]

[Include 4-6 common pitfalls]

---

## Success Criteria

The implementation is complete when:

1. ✅ [Criterion 1]
2. ✅ [Criterion 2]
3. ✅ [Criterion 3]
[... continue for 10-12 criteria]

---

## Testing Commands

After implementation, run these commands to validate:

```bash
# [Test 1 description]
[command to run]

# [Test 2 description]
[command to run]

[Include 6-8 validation commands]
```

---

## Additional Notes

- [Important implementation note 1]
- [Important implementation note 2]
- [Design rationale or future considerations]
```

### Code Example Requirements

- Provide COMPLETE, production-ready code (not pseudocode or snippets)
- Include all imports, type hints, docstrings
- Follow the project's existing code style and patterns
- Show file paths clearly
- Indicate whether editing existing files or creating new ones
- Include error handling in examples
- Add comments explaining non-obvious logic

### Design Decisions Summary Requirements

- Document EVERY design decision from the interactive questions
- Include brief rationale for each choice
- Group by category (Architecture, Data Flow, etc.)
- Make it easy to scan and understand the overall approach

## Step 5: Save the Design Document

1. Extract the feature name from the input path:
   - Input: `.claude/feature_prompts/save_crawled_content_to_files.md`
   - Feature name: `save_crawled_content_to_files`

2. Create the output path:
   - `.claude/design_prompts/<feature_name>.md`

3. Create the `.claude/design_prompts/` directory if it doesn't exist

4. Write the design document to the file

5. Confirm to the user:
   ```
   ✅ Implementation design document created!
   📄 Saved to: .claude/design_prompts/<feature_name>.md

   This document is ready to be used by another developer or AI agent to implement the feature.
   ```

## Quality Standards

Your design document should be:
- **Comprehensive**: Cover every aspect of implementation
- **Actionable**: Another developer/AI could implement without additional questions
- **Specific**: Include actual code, not placeholders or TODOs
- **Well-organized**: Easy to navigate with clear sections
- **Complete**: Include tests, validation, checklists, and pitfalls

## Important Notes

- Take time to ask thorough design questions - these decisions shape the entire implementation
- Generate complete, working code examples - not pseudocode
- Consider edge cases and error scenarios in your examples
- Make the design document self-contained - all necessary information should be included
- Follow the project's existing patterns and conventions discovered during codebase analysis
