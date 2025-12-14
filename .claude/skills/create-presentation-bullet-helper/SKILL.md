---
name: create-presentation-bullet-helper
description: Generate formal presentation bullet helper files with concise language for executive audiences
---

# Create Presentation Bullet Helper

Generate professional presentation bullet helper documents designed for executive and management audiences with limited time. These documents provide structured talking points, slide content, and Q&A preparation in a formal, concise format.

## When to Use This Skill

Use this skill when:
- Creating presentation scripts for executive or management audiences
- Preparing formal presentations with strict time constraints
- Generating Q&A preparation documents for technical presentations
- Building slide-by-slide speaking notes for business reviews
- User requests "create a presentation helper" or "prepare presentation bullets"
- Audience has limited time and requires high information density

## Core Principles

### Language Standards

1. **Formal Tone** - No theatrical, elaborate, or conversational language
2. **Concise Delivery** - Brief, factual statements without flowery prose
3. **Executive-Appropriate** - Assumes limited time, high information density
4. **Accuracy Over Style** - Factual precision beats engaging narratives
5. **Professional Brevity** - One sentence when possible, two when necessary

### Structural Requirements

1. **Sequential Slides** - Slides flow one after another without interruption
2. **Consolidated Q&A** - All questions moved to document bottom, organized by category
3. **No Table of Contents** - In the presentation file itself (TOC creates clutter)
4. **Clear Separators** - Use `---` between major sections
5. **Placeholder Flexibility** - Use `[bracketed placeholders]` for customizable content

## Prohibited Language Patterns

### Never Use These Phrases

❌ **Conversational openers:**
- "Great question"
- "Absolutely"
- "Let me walk you through"
- "This is exciting"
- "Here's the thing"

❌ **Theatrical language:**
- "The irony is..."
- Rhetorical questions ("So we asked ourselves...")
- "And this is the exciting part..."
- "Here's what's really interesting..."

❌ **Overly elaborate explanations:**
- "If you think about it..."
- "The way this works is..."
- "What we're really doing here is..."
- "Compare that to..." (when adding emphasis rather than facts)

❌ **Emotional appeals:**
- "We're passionate about..."
- "This is game-changing..."
- "Revolutionary approach..."
- Superlatives without data backing

### Preferred Language Style

✅ **Direct statements:**
- "The system does X" not "Let me show you how it does X"
- "We built Y" not "So we asked ourselves: why not build Y?"

✅ **Factual responses:**
- "API costs are $0.10-0.50 per radar" (period, end of sentence)
- Not: "Compare that to $50-100 in engineer time" (unless comparison requested)

✅ **Professional brevity:**
- One sentence when the point is clear
- Two sentences when context is needed
- Never three sentences when two will do

✅ **Concrete over abstract:**
- "60-70% reduction in triage time" not "significant time savings"
- "5-minute setup" not "quick and easy setup"

## Document Structure Standards

### Standard Template

```markdown
# [Project Name] - Presentation

## Slide 1: [Slide Title]

### [Section Name]

**[Stage marker]**

"[greetings starter sentence]

[Content with factual statements...]

**[Transition marker]**

[More content...]

**[Explain the system/process]**

The system operates in [N] stages:

1. **Stage Name** - Brief description
2. **Stage Name** - Brief description

[Summary statement]

**[Close with impact]**

[Closing statement]"

---

## Slide 2: [Slide Title]

### [Section Name]

[Content structure matching slide purpose]

**[Subsection]**
- Bullet point
- Bullet point

---

### [Subsection for Next Steps, if applicable]

• **Item Name** - Brief description

• **Item Name** - Brief description

---

## Key Talking Points to Remember

✓ **Label**: Brief statement
✓ **Label**: Brief statement
✓ **Label**: Brief statement

---

## Closing Statement

"One to two sentence professional closing that reinforces key message."

---

## Anticipated Questions & Responses

### Technical Questions

**Q: Question text?**
- "Brief, direct answer in 1-2 sentences."

**Q: Question text?**
- "Brief, direct answer in 1-2 sentences."

### Process Questions

**Q: Question text?**
- "Brief answer."

### Adoption & ROI Questions

**Q: Question text?**
- "Brief answer with data when available."

### Implementation Questions

**Q: Question text?**
- "Brief technical answer."

### Cost & Resources Questions

**Q: Question text?**
- "Brief answer with specific numbers."
```

### File Structure Rules

1. **Title**: `# [Project Name] - Presentation`
2. **Slide Sections**: Start with `## Slide N: [Title]`
3. **Separators**: Use `---` between slides and major sections
4. **Subsections**: Use `###` for subsections within slides
5. **Stage Markers**: Use bold brackets like `**[Start with the problem]**` for speaking cues
6. **Lists**:
   - Numbered lists for sequential processes
   - Bullet lists (•) for features/next steps with `**Bold** - Description` format
   - Checkmark lists (✓) for talking points with `**Bold**: Statement` format

7. **No TOC**: Never include table of contents in the presentation document

## Formatting Patterns

### Slide Content Format

**Opening Script Pattern:**
```markdown
### Opening Script

**[Start with the problem]**

"[greetings starter sentence]

[Problem statement in 2-3 sentences]

**[Transition to solution]**

[Solution statement in 1 sentence]

**[Explain the system flow]**

The system operates in [N] stages:

1. **Stage** - Description
2. **Stage** - Description

[Summary of impact]

**[Close with impact]**

[Closing statement]"
```

**System Architecture Pattern:**
```markdown
### System Architecture

The system architecture consists of [N] stages:

**1. Stage Name**
- Component detail
- Component detail

**2. Stage Name**
- Component detail
- Component detail

All stages utilize [relevant technologies/tools].
```

**Next Steps Pattern:**
```markdown
### Next Steps

• **Feature Name** - Brief description of what this enables

• **Feature Name** - Brief description with context

• **Feature Name** - Brief description
```

### Q&A Format

**Standard Categories (in order):**
1. Technical Questions
2. Process Questions
3. Adoption & ROI Questions
4. Implementation Questions
5. Cost & Resources Questions

**Q&A Entry Format:**
```markdown
**Q: Clear, specific question?**
- "Direct answer. Additional detail if needed but keep to 1-2 sentences maximum."
```

### Key Talking Points Format

```markdown
## Key Talking Points to Remember

✓ **Label**: Brief factual statement
✓ **Label**: Brief factual statement with metric
✓ **Label**: Brief statement
```

### Closing Statement Format

```markdown
## Closing Statement

"Professional statement in 1-2 sentences that reinforces the value proposition and key constraint (e.g., human approval required)."
```

## Language Comparison Examples

### Opening Statements

❌ **Too Theatrical:**
"Good morning everyone! I want to talk about a challenge we've been facing - and the solution we've built to address it. The irony is that automatic radar creation was meant to help us, but it's created a new problem: radar overload. So we asked ourselves: if we can automatically create radars, why can't we automatically triage them?"

✅ **Formal and Concise:**
"[greetings starter sentence]

Since enabling automatic radar creation, engineers are spending significant time on manual triage - screening tickets, categorizing them, and assigning severity levels. This has become a bottleneck across testing, automation, and development teams.

We built an AI-powered Radar Triage Agent to automate this process."

### Q&A Responses

❌ **Too Conversational:**
"Great question! We're tracking metrics per agent: number of radars processed, PRs created, acceptance rate. Early data shows engineers spending 60-70% less time on initial triage. We'll have concrete ROI numbers in the next quarter."

✅ **Formal and Brief:**
"Early data shows 60-70% reduction in initial triage time. We track metrics per agent: radars processed, PRs created, and acceptance rate."

❌ **Too Elaborate:**
"The system is designed to be model-agnostic, so we can swap in different models as they improve. Right now we're using Claude Sonnet 4.5 which provides really strong code analysis capabilities."

✅ **Direct:**
"Claude Sonnet 4.5. The system is model-agnostic and can be upgraded as newer models become available."

### Feature Descriptions

❌ **Too Wordy:**
"When a radar comes in, the AI agent doesn't just read the description. It actually clones the relevant code repositories, analyzes the code, examines stack traces, and uses LLM capabilities to understand what's actually broken."

✅ **Concise:**
"When a radar matches criteria, the agent clones relevant repositories, analyzes code and stack traces, and identifies the root cause."

## Workflow

### Step 1: Gather Context

Ask the user:
- What is the presentation about? (topic/project)
- Who is the audience? (executives, technical leads, peers)
- How much time is allocated? (5 min, 15 min, 30 min)
- What level of formality? (executive review, team meeting, conference)
- What are the main slides/topics to cover?

### Step 2: Determine Language Level

Based on answers:
- **Executive/Management + Limited Time** → Maximum formality, minimum elaboration
- **Technical Leads + Moderate Time** → Formal but can include more technical detail
- **Team/Peers + Flexible Time** → Professional but slightly more conversational

**Default assumption:** Executive audience with limited time (most formal, most concise)

### Step 3: Create Slide Content

For each slide:
1. Use stage markers in brackets `**[Stage name]**` for speaking cues
2. Write content in formal, direct language
3. Use numbered lists for processes, bullet lists for features
4. Keep descriptions brief (one sentence per bullet when possible)
5. Include placeholders like `[greetings starter sentence]` where customization is expected
6. Add summary statements after lists

### Step 4: Add Supporting Sections

After slides:
1. **Key Talking Points** - 5-7 checkmark bullets maximum
2. **Closing Statement** - 1-2 sentence professional closing

### Step 5: Consolidate Q&A

At document bottom:
1. Organize all questions into categories
2. Keep answers to 1-2 sentences
3. Remove conversational language
4. Use standard categories (Technical, Process, Adoption & ROI, Implementation, Cost & Resources)

### Step 6: Review and Refine

Check for:
- ❌ Theatrical phrases → Remove
- ❌ "Great question", "Absolutely" → Remove
- ❌ Rhetorical questions → Convert to statements
- ❌ Three+ sentence answers → Condense to two
- ❌ Flowery language → Make direct
- ✅ Factual tone maintained
- ✅ Professional brevity achieved

## Quick Reference

### Audience Type → Language Formality

| Audience | Formality | Elaboration | Sentence Limit |
|----------|-----------|-------------|----------------|
| C-level executives | Maximum | Minimum | 1-2 per point |
| Management | High | Low | 2 per point |
| Technical leads | Moderate | Moderate | 2-3 per point |
| Team/Peers | Professional | Moderate | 2-3 per point |

### Presentation Length → Detail Level

| Duration | Slides | Q&A Depth | Talking Points |
|----------|--------|-----------|----------------|
| 5-10 min | 2-3 | Brief (1 sentence) | 5-6 bullets |
| 15-20 min | 3-5 | Moderate (1-2 sentences) | 6-8 bullets |
| 30+ min | 5-8 | Detailed (2 sentences) | 8-10 bullets |

### Common Replacements

| Verbose/Theatrical | Concise/Formal |
|-------------------|----------------|
| "Great question. Every fix goes through..." | "All fixes require..." |
| "Let me walk you through how it works:" | "The system operates in [N] stages:" |
| "This is exciting - we're doing X, Y, and Z" | "The system does X, Y, and Z" |
| "So we asked ourselves: why not...?" | "We built..." |
| "Compare that to $50-100 in engineer time" | (Remove unless comparison is requested) |
| "We're passionate about..." | "The system provides..." |
| "What's really interesting here is..." | (Just state the fact) |

## Common Issues and Solutions

### Issue: Content too casual

**Symptoms:**
- Phrases like "Great question", "Let me show you"
- Rhetorical questions in script
- Conversational tone

**Solution:**
- Remove all conversational openers
- Convert rhetorical questions to direct statements
- Use imperative or declarative sentences only

### Issue: Answers too long

**Symptoms:**
- Q&A responses exceeding 2 sentences
- Unnecessary comparisons or justifications
- Repeated information

**Solution:**
- Cut to core answer only
- Remove comparative statements unless data-driven
- One fact per question, two facts maximum

### Issue: Missing placeholders

**Symptoms:**
- Script includes specific greetings or names
- Hard-coded values that should be customizable

**Solution:**
- Replace with `[placeholder description]`
- Use brackets for: greetings, names, specific metrics that vary
- Keep factual constants as-is (e.g., "Claude Sonnet 4.5")

### Issue: Q&A scattered through document

**Symptoms:**
- Questions appear after each slide
- Inconsistent Q&A formatting

**Solution:**
- Move ALL questions to document bottom
- Organize into standard categories
- Maintain consistent formatting

## Instructions for Claude

When creating a presentation bullet helper using this skill:

1. **Always ask about context first:**
   - Audience type and seniority level
   - Time allocated for presentation
   - Formality requirements
   - Number of slides/topics to cover

2. **Default to maximum formality:**
   - Unless told otherwise, assume executive audience with limited time
   - Use the most concise, formal language patterns
   - Remove all theatrical elements

3. **Structure before content:**
   - Plan slide order first
   - Determine Q&A categories needed
   - Outline key talking points
   - Then write content

4. **Remove theatrical language during editing:**
   - Review every sentence for conversational patterns
   - Cut "Great question", "Absolutely", "Let me..."
   - Convert rhetorical questions to statements
   - Eliminate emotional appeals

5. **Keep Q&A responses to 1-2 sentences maximum:**
   - First sentence: Direct answer
   - Second sentence: Supporting detail (if needed)
   - Third sentence: Never needed - if you wrote three, combine into two

6. **Place all questions at document end:**
   - Never intersperse Q&A with slide content
   - Organize into standard categories
   - Maintain consistent format

7. **Use bracket placeholders for customization:**
   - `[greetings starter sentence]` for variable greetings
   - `[specific metric]` for data that may change
   - `[team name]` for audience-specific references

8. **Verify completeness:**
   - Each slide has clear content
   - Key talking points summarize main messages
   - Closing statement reinforces value
   - All likely questions covered in Q&A

9. **Final quality check:**
   - No conversational language remaining
   - All answers brief (1-2 sentences)
   - Structure matches template exactly
   - Professional tone throughout

## Example: Full Document Structure

```markdown
# [Project Name] - Presentation

## Slide 1: The Challenge & Our Solution

### Opening Script

**[Start with the problem]**

"[greetings starter sentence]

[Problem statement - 2-3 sentences describing current pain point]

**[Transition to solution]**

[Solution statement - 1 sentence]

**[Explain the system flow]**

The system operates in [N] stages:

1. **Stage** - Description
2. **Stage** - Description
3. **Stage** - Description

[Summary impact statement]

**[Close with impact]**

[Final statement about capabilities]"

---

## Slide 2: System Design & Next Steps

### System Architecture

The system architecture consists of [N] components:

**1. Component**
- Detail
- Detail

**2. Component**
- Detail
- Detail

All components utilize [relevant technologies].

---

### Next Steps

• **Initiative** - Description

• **Initiative** - Description

---

## Key Talking Points to Remember

✓ **Problem**: Brief statement
✓ **Solution**: Brief statement
✓ **Results**: Metric-based statement
✓ **Risk Management**: Brief statement
✓ **Adoption**: Brief statement
✓ **Scalability**: Brief statement

---

## Closing Statement

"Professional closing that reinforces value proposition. Key constraint or requirement."

---

## Anticipated Questions & Responses

### Technical Questions

**Q: Question?**
- "Brief answer."

### Process Questions

**Q: Question?**
- "Brief answer."

### Adoption & ROI Questions

**Q: Question?**
- "Brief answer with data."

### Implementation Questions

**Q: Question?**
- "Brief answer."

### Cost & Resources Questions

**Q: Question?**
- "Brief answer with numbers."
```

## Key Principles to Remember

1. **Formal beats conversational** - Always err on the side of too formal rather than too casual
2. **Brief beats comprehensive** - One clear sentence beats three explanatory sentences
3. **Facts beat narratives** - Data and specifics beat storytelling
4. **Structure beats flexibility** - Follow the template exactly for consistency
5. **Bottom-loaded Q&A beats distributed** - All questions go at the end, organized by category
6. **Placeholders beat hard-coding** - Use `[brackets]` for anything that might vary
7. **Direct beats elaborate** - "We built X" beats "So we asked ourselves: why not build X?"

---

This skill produces presentation helpers that respect the audience's time, maintain professional tone, and provide comprehensive preparation while avoiding theatrical or overly casual language.
