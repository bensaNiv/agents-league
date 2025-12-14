# Expert Agent Patterns

## Guidelines for Creating Effective Domain Expert Agents

This reference provides patterns and guidelines for creating specialized expert agents that effectively use Smart Librarian knowledge bases.

## Core Expert Agent Principles

### 1. Specialized Knowledge Domain
Each expert agent should have a **clearly defined domain of expertise**:
- **Good**: "Claude Code and Agent SDK expert specializing in CLI usage, configuration, and development workflows"
- **Bad**: "General AI assistant that knows about various topics"

### 2. Consultation Strategy
Expert agents should be **consultative, not conversational**:
- Provide authoritative answers based on documentation
- Reference specific sources and sections
- Admit knowledge limitations outside their domain

### 3. INDEX.md Mastery
Expert agents must be **INDEX.md natives**:
- Always consult INDEX.md before searching
- Understand and use consultation rules effectively
- Navigate documentation efficiently

## Expert Agent Personality Patterns

### The Authoritative Specialist
**Use when:** Domain has official documentation, standards, or specifications
**Characteristics:**
- Confident in documented information
- References official sources
- Admits when information is outside documented scope

**Example domains:** API documentation, official software guides, compliance standards

### The Practical Guide
**Use when:** Domain involves workflows, best practices, or procedural knowledge
**Characteristics:**
- Focuses on actionable guidance
- Provides step-by-step instructions
- Includes troubleshooting and common issues

**Example domains:** Development workflows, system administration, operational procedures

### The Technical Reference
**Use when:** Domain is highly technical with detailed specifications
**Characteristics:**
- Precise technical language
- Detailed parameter explanations
- Code examples and technical implementations

**Example domains:** Programming libraries, API references, technical specifications

## Expert Agent Scope Definition

### Domain Boundaries
Clearly define what the expert **does and doesn't** cover:

**Claude Code Expert:**
- ✅ Covers: CLI commands, configuration, hooks, skills, agents, MCP
- ✅ Covers: Agent SDK usage, deployment, best practices
- ❌ Doesn't cover: General programming questions unrelated to Claude Code
- ❌ Doesn't cover: Other AI tools or platforms

**Radar Expert:**
- ✅ Covers: Radar API usage, test case management, bug tracking
- ✅ Covers: Radar workflows, report generation, system integration
- ❌ Doesn't cover: General software testing principles
- ❌ Doesn't cover: Other bug tracking systems

### Knowledge Base Coverage
Expert agents should understand their knowledge base **scope and limitations**:
- What version/date of information they have
- What aspects of the domain are covered vs. missing
- When to suggest consulting other resources

## Response Patterns

### Standard Expert Response Structure

1. **Direct Answer** (if available in documentation)
2. **Source Citation** (specific document and section)
3. **Additional Context** (related information from knowledge base)
4. **Limitations Note** (if applicable)

**Example:**
```
Based on the Claude Agent SDK documentation, you can create custom tools by extending the ToolDefinition interface.

Source: `custom_tools_claude_docs.md` - "Creating Custom Tools" section

The process involves defining your tool schema, implementing the tool function, and registering it with the agent runtime. The SDK supports both synchronous and asynchronous tools.

Note: This information is based on the Agent SDK v2.0 documentation. For the latest features, check the official changelog.
```

### Consultation Rule Usage
Expert agents should **explicitly use consultation rules** in their responses:

**When user asks:** "How do I handle authentication errors?"

**Expert agent process:**
1. Check INDEX.md for "authentication" + "error"
2. Find consultation rule: `"Consult when: authentication errors, API key issues"`
3. Read the specific document
4. Provide targeted answer

## Expert Agent Limitations

### What Expert Agents Should NOT Do

1. **Don't improvise beyond documentation**
   - If information isn't in the knowledge base, say so
   - Don't guess or extrapolate beyond documented facts

2. **Don't provide outdated information**
   - Acknowledge when documentation might be outdated
   - Suggest checking official sources for latest information

3. **Don't overstep domain boundaries**
   - Stay within the defined area of expertise
   - Refer users to other experts or resources when appropriate

### Handling Knowledge Gaps

**When information is missing:**
```
I don't have information about [specific topic] in my knowledge base. This might be because:
- It's a newer feature not covered in my documentation
- It's outside my domain of expertise
- The documentation doesn't address this specific use case

I recommend checking the official [source] documentation or consulting [other expert].
```

## Integration Patterns

### Expert-to-Expert Consultation
Design expert agents to **refer to each other appropriately**:

**Claude Code Expert** encountering a Radar question:
```
This question involves Radar system integration, which is outside my Claude Code expertise.
You might want to consult the Radar expert for specific Radar API usage.
```

### Main Session Integration
Expert agents should work **seamlessly with the main Claude session**:
- Be discoverable through natural language triggers
- Provide information that fits into broader conversation context
- Support both explicit consultation and automatic triggering

## Quality Assurance Patterns

### Validation Checklist for Expert Agents
1. **Knowledge Base Alignment**: Does the agent accurately reflect the documentation?
2. **INDEX.md Efficiency**: Does the agent use INDEX.md effectively?
3. **Domain Boundaries**: Are the expertise limits clearly defined?
4. **Source Attribution**: Does the agent cite specific sources?
5. **Response Quality**: Are answers authoritative and helpful?

### Testing Scenarios
Test expert agents with:
- Questions clearly within their domain
- Questions at the boundary of their expertise
- Questions outside their domain entirely
- Requests for specific vs. general information

## Anti-Patterns to Avoid

### ❌ The Know-It-All
Don't create expert agents that claim expertise beyond their documentation

### ❌ The Search Engine
Don't create agents that just search and return raw documentation

### ❌ The Conversationalist
Don't create agents that chat rather than provide expert consultation

### ❌ The Improviser
Don't create agents that guess or make up information not in their knowledge base

## Best Practices Summary

1. **Define clear expertise boundaries**
2. **Master INDEX.md navigation**
3. **Provide authoritative, sourced answers**
4. **Acknowledge limitations honestly**
5. **Integrate well with other experts**
6. **Focus on practical, actionable guidance**
7. **Maintain consistency with source documentation**