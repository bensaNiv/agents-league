# INDEX.md Optimization Guide

## How Expert Agents Should Use INDEX.md Files

This guide provides best practices for expert agents to efficiently navigate Smart Librarian knowledge bases using INDEX.md files.

## Core Principle: INDEX-First Strategy

Expert agents should **always read the INDEX.md file first** before searching for specific information. This prevents inefficient context usage and ensures accurate information retrieval.

### Why INDEX-First?

1. **Consultation Rules**: INDEX.md contains "Consult when:" rules that map user intents to specific documents
2. **Context Efficiency**: Avoids loading irrelevant documents into context
3. **Accuracy**: Ensures the most relevant documents are consulted for each query
4. **Speed**: Direct navigation vs. broad searching

## Decision Tree for Information Retrieval

```
User Query Received
    ↓
1. Read INDEX.md (if not already in context)
    ↓
2. Analyze user intent and map to consultation rules
    ↓
3. Identify 1-3 most relevant documents from catalog
    ↓
4. Read only the identified relevant documents
    ↓
5. Provide answer based on specific documentation
```

## Consultation Rules Interpretation

### Understanding "Consult when:" Patterns

**Exact Match Patterns:**
- `"API configuration"` - User asks about API setup, authentication, configuration
- `"model selection"` - User asks about choosing models, comparing models
- `"error handling"` - User reports errors, asks about troubleshooting

**Contextual Match Patterns:**
- `"pricing"` - User asks about costs, billing, usage limits
- `"authentication"` - User has login issues, API key problems
- `"troubleshooting"` - User reports problems, needs debugging help

**Broad Category Patterns:**
- `"API documentation"` - Any API-related technical question
- `"getting started"` - User is new, needs basic guidance
- `"best practices"` - User wants recommendations, optimization advice

## Efficient Search Strategies

### 1. Keyword Mapping
Map user query keywords to INDEX.md consultation rules:

**User:** "How do I authenticate with Claude?"
**INDEX Strategy:** Look for consultation rules containing "authentication", "API", "setup"

**User:** "What's the pricing for different models?"
**INDEX Strategy:** Look for consultation rules containing "pricing", "models", "costs"

### 2. Intent Classification
Classify user intent and match to document purposes:

**Intent Types:**
- **Setup/Configuration** → Look for setup, configuration, getting started docs
- **Troubleshooting** → Look for error handling, troubleshooting, debugging docs
- **Feature Usage** → Look for feature-specific, how-to, implementation docs
- **Reference** → Look for API reference, specification, detailed technical docs

### 3. Progressive Disclosure
Start with most specific, then broaden if needed:

1. **Specific match**: Find exact consultation rule match
2. **Category match**: Find broader category if no specific match
3. **Fallback**: Use overview/index documents if no clear match

## Common Anti-Patterns to Avoid

### ❌ Don't Do This:
- Reading multiple documents without checking INDEX.md first
- Searching through all files to find information
- Ignoring consultation rules and guessing document relevance
- Loading entire knowledge base into context

### ✅ Do This Instead:
- Always read INDEX.md first to understand available documentation
- Use consultation rules to identify the 1-3 most relevant documents
- Read only the documents that match the user's specific intent
- Provide answers based on the specific documents you consulted

## Example Consultation Workflow

**User Query:** "How do I use streaming with the Claude API?"

**Step 1:** Read INDEX.md (if not in context)
```markdown
**File:** `streaming_messages_claude_docs.md`
**Consult when:** streaming, real-time responses, API streaming configuration
```

**Step 2:** Identify relevant document based on consultation rule
- Query contains "streaming" → matches consultation rule

**Step 3:** Read the specific document
- Read `streaming_messages_claude_docs.md`

**Step 4:** Provide specific answer from that document

## INDEX.md Structure Expectations

Expert agents should expect INDEX.md files to contain:

### Required Sections:
- **Usage Instructions** - How to use the index
- **Documentation Catalog** - List of all documents with consultation rules
- **Quick Reference** - Summary of key topics

### Document Entries Format:
```markdown
### Document Title
**File:** `filename.md`
**Source:** https://source.url
**Consult when:** keyword1, keyword2, specific use case
```

## Performance Optimization

### Context Management:
- Keep INDEX.md loaded in context for the session
- Only load additional documents as needed
- Remove documents from context after use if context space is limited

### Query Efficiency:
- Use consultation rules to pre-filter documents
- Match user intent to specific consultation patterns
- Avoid "shotgun" approach of reading many documents

### Response Quality:
- Always cite which specific document(s) you consulted
- Reference the exact section or information source
- Indicate confidence level based on documentation quality