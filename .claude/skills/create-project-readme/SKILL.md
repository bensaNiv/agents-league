---
name: create-project-readme
description: Generate well-structured README files following standardized formatting and organization principles.
---

# Create Project README

Generate well-structured README files following standardized formatting and organization principles.

## When to Use This Skill

Use this skill when:
- Creating a new project and need to generate a README file
- Refactoring an existing README to follow best practices
- User requests "create a README" or "improve the README structure"

## README Structure Standards

### Required Sections (in order)

1. **Main Header**
   - Project title (H1)
   - One-line description explaining what the project does
   - **Keep it simple** - avoid marketing language like "production-ready", "robust", etc.
   - Example: "A CLI tool for..." not "A production-ready CLI tool for..."

2. **Architecture** (NEW - before Table of Contents)
   - One line describing the architecture approach
   - 3-4 bullet points showing main capabilities
   - Format: `**Architecture:** Brief description.`
   - Example:
     ```markdown
     **Architecture:** Async browser automation with structured file export.
     - **Single Page Crawling** - Extract individual pages with metadata
     - **Deep Crawling** - Recursive BFS crawling with organized output
     - **File Export** - Markdown files with metadata and table of contents
     ```

3. **Horizontal Separator** (`---`)

4. **Table of Contents**
   - List only main sections (no sub-sections)
   - Use markdown anchor links
   - **Highlight Quick Start with rocket emoji**: `- [🚀 Quick Start](#-quick-start)`
   - Sections: 🚀 Quick Start, Overview, Features, Installation, Configuration, Development, Documentation

5. **Horizontal Separator** (`---`)

6. **🚀 Quick Start** (NEW TOP-LEVEL SECTION)
   - **Prerequisites** - Installation commands (brew install uv, clone, uv tool install ., playwright)
   - **Minimal Example** - Single command that works immediately
   - **What this does** - Checklist with checkmarks (✅) explaining each step
   - **Common Usage Patterns** - 3-5 practical examples
   - **Output** - Show what files/results are created
   - **Accessing Your Content** - How to use the results (for data/export tools)
   - **Commands use tool name directly** (assume global installation, no `uv run` prefix)

7. **Horizontal Separator** (`---`)

8. **Overview**
   - Detailed explanation of the main purpose
   - Key capabilities (bullet points)
   - Technology stack and approach
   - What problem it solves

9. **Features**
   - Key capabilities with descriptive explanations
   - Use bold for feature names followed by dash and description
   - Example: `**Feature Name** - Detailed explanation of what it does`

10. **Installation** (NEW MAIN SECTION - separate from Development)
    - Prerequisites (Python version, uv version)
    - **Option 1: Local Tool Installation**
      - Clone + `uv tool install .` + playwright install
      - "Use this when:" explanation (global command, modify code, no uv run prefix)
    - **Option 2: Development Mode**
      - Clone + `uv sync` + playwright install
      - "Use this when:" explanation (active development, instant changes, uv run prefix)
    - **Option 3: Remote Tool Installation**
      - `uv tool install git+ssh://...` + playwright install
      - "Use this when:" explanation (simplest, no code modification)

11. **Configuration**
    - All configuration options organized by category
    - Use markdown tables for configuration fields
    - Include: Field name, Description, Default value, Required status
    - Add code examples showing configuration format
    - Explain how configuration works

12. **Development**
    - Prerequisites (tools, versions)
    - Project Structure (directory tree)
    - Installation for Development (reference to Installation Option 2)
    - Running Tests
    - Adding Dependencies
    - Code Quality (check pyproject.toml for actual tools - see Tool Detection below)
    - **Commands use `uv run` prefix** (development mode)

13. **Documentation**
    - How It Works (detailed explanation)
    - Usage Examples (**use tool name directly**, no uv run - assume global install)
    - Output File Format (for data tools)
    - Path Handling (for file-based tools)
    - Requirements
    - Validation Commands (both global and dev mode versions)
    - Troubleshooting
    - Future Enhancements

## Formatting Guidelines

### Table of Contents
- Keep it simple - only main section links
- No nested sub-sections in TOC
- Use anchor links (#section-name)

**Example:**
```markdown
## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Configuration](#configuration)
- [Development](#development)
- [Documentation](#documentation)
```

### Configuration Tables

Use markdown tables for all configuration fields:

```markdown
| Field | Description | Default | Required |
|-------|-------------|---------|----------|
| `field_name` | What this field controls | `default_value` | Yes/No |
```

### Code Examples

Include code blocks for:
- Configuration examples
- Installation commands
- Usage examples
- Output examples

### Section Headers

- Use H2 (##) for main sections
- Use H3 (###) for subsections
- Use descriptive header names

## Tool Detection

Before creating the README, detect the project type to determine the correct command patterns:

### Detecting CLI Tools

Check `pyproject.toml` for these indicators:

```toml
[project.scripts]
tool-name = "module.cli:app"
```

**If found**: This is a CLI tool
- Quick Start should show: `brew install uv`, `uv tool install .`, then `tool-name` commands
- Quick Start/Usage Examples use: `tool-name crawl ...` (no `uv run` prefix)
- Development section uses: `uv run tool-name ...`
- Installation section shows all 3 options (local tool, development, remote)

### Detecting Libraries

If no `[project.scripts]` section exists, this is a library.

**For libraries**:
- Quick Start shows: `brew install uv`, `uv add package-name`
- Examples show: Python import statements and usage
- No tool installation options
- Focus on API documentation

### Checking Dev Dependencies

Always check `pyproject.toml` for actual dev tools before documenting them:

```toml
[tool.uv]
dev-dependencies = [
    "pytest>=8.0.0",
    "pytest-asyncio>=0.23.0",
]
```

**Code Quality section rules**:
- If `pytest` exists → show pytest commands
- If `ruff` exists → show ruff format and check commands
- If `mypy` exists → show mypy commands
- If `black` exists → show black commands
- **Never assume tools exist** - only document what's actually in dev-dependencies

Example:
```markdown
### Code Quality

\`\`\`bash
# Run tests
uv run pytest tests/ -v

# Run tests with coverage
uv run pytest tests/ --cov=package_name --cov-report=html
\`\`\`
```

## Command Patterns

### For CLI Tools

**Quick Start Section** (assumes global tool installation):
```bash
# Install the tool
brew install uv
git clone <repo>
cd <repo>
uv tool install .

# Use it
tool-name command --option value
```

**Usage Examples Section** (assumes global tool installation):
```bash
# Example 1
tool-name crawl https://example.com --depth 2

# Example 2
tool-name export --format json
```

**Development Section** (development mode with uv run):
```bash
# Run tests
uv run pytest tests/ -v

# Run the tool in development
uv run tool-name command --option value
```

**Validation Commands Section** (show both):
```bash
# For tool installation (Option 1 or 3):
tool-name --help
tool-name command --option value

# For development mode (Option 2):
uv run tool-name --help
uv run tool-name command --option value
```

### For Libraries

Always use import/API patterns, never command-line patterns.

## Example README Structure

```markdown
# Project Name

A CLI tool for web crawling and content extraction.

**Architecture:** Async browser automation with structured file export.
- **Single Page Crawling** - Extract individual pages with metadata
- **Deep Crawling** - Recursive BFS crawling with organized output
- **File Export** - Markdown files with metadata and table of contents

---

## Table of Contents

- [🚀 Quick Start](#-quick-start)
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Development](#development)
- [Documentation](#documentation)

---

## 🚀 Quick Start

### Prerequisites

\`\`\`bash
# Install uv package manager (if not already installed)
brew install uv

# Clone and install the tool
git clone <repo-url>
cd <repo-name>
uv tool install .

# Install Playwright browsers (required)
uvx playwright install
\`\`\`

### Minimal Example

**Crawl a page and save to file:**
\`\`\`bash
tool-name crawl https://example.com --save-to ./output.md
\`\`\`

**What this does:**
1. ✅ **Crawls** the URL using a headless browser
2. ✅ **Extracts** clean markdown content (filters out navigation, ads, etc.)
3. ✅ **Saves** to `output.md` with metadata header (timestamp, URL, stats)
4. ✅ **Follows links** up to depth 1 (default), max 10 pages

### Common Usage Patterns

**Single page with export:**
\`\`\`bash
tool-name crawl https://example.com --depth 0 --save-to ./page.md
\`\`\`

**Deep crawl documentation site:**
\`\`\`bash
tool-name crawl https://docs.example.com --depth 2 --max-pages 15 --save-to ./docs/crawl.md
\`\`\`

**Crawl without saving (display only):**
\`\`\`bash
tool-name crawl https://example.com --depth 0
\`\`\`

### Output

**Single page crawl creates:**
\`\`\`
output.md       # Markdown file with metadata + content
\`\`\`

**Deep crawl creates:**
\`\`\`
docs/
  crawl.md              # Index file with table of contents
  crawl_pages/          # Directory with individual pages
    page_001.md
    page_002.md
    ...
\`\`\`

### Accessing Your Content

Once saved, files contain:
- **Metadata header** - Timestamp, URLs, crawl options, statistics
- **Clean markdown** - Content extracted from the page(s)
- **Table of contents** (deep crawls) - Links to all crawled pages

Example metadata:
\`\`\`markdown
---
# Crawl Metadata (v1.0)
- Timestamp: 2024-12-04T10:30:00-08:00
- Source URL: https://example.com
- Statistics:
  - Status: Success
  - Content Length: 1,234 characters
---

[Page content here...]
\`\`\`

---

## Overview

Detailed explanation of the project's main purpose...

**Key capabilities:**
- Single-page and multi-page crawling with configurable depth
- Browser-based rendering for JavaScript-heavy sites
- Intelligent content extraction and markdown conversion

**Technology stack:**
- **crawl4ai** - Async web crawler with Playwright-based browser automation
- **typer** - Modern CLI framework with excellent type hints
- **aiofiles** - Async file I/O for efficient export operations

**What problem it solves:**

Explanation of what problem this tool solves...

## Features

- **File Export with Metadata** - Save crawled content to markdown files with structured metadata headers
- **Organized Output Structure** - Deep crawls create an index file with table of contents plus individual page files
- **Smart Content Filtering** - Removes navigation, headers, footers, and other noise to focus on main content
- **Browser Automation** - Uses Playwright for JavaScript rendering and dynamic content loading

## Installation

### Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) package manager (>=0.4.0)

### Option 1: Local Tool Installation

Clone the repository and install as a global tool (lets you modify code while having global access):

\`\`\`bash
# Clone the repository
git clone <repo-url>
cd <repo-name>

# Install as a UV tool from local path
uv tool install .

# Install Playwright browsers (required)
uvx playwright install
\`\`\`

After installation, the `tool-name` command will be available globally. When you modify code in the cloned directory, reinstall with `uv tool install . --force` to update.

**Use this when:**
- You want to use `tool-name` as a global command
- You want to modify the code occasionally
- You want easy access without `uv run` prefix

### Option 2: Development Mode (Recommended for Active Development)

Clone the repository and work in development mode:

\`\`\`bash
# Clone the repository
git clone <repo-url>
cd <repo-name>

# Install dependencies
uv sync

# Install Playwright browsers (required)
uv run playwright install
\`\`\`

Run commands with `uv run tool-name` prefix. Code changes take effect immediately without reinstallation.

**Use this when:**
- You're actively developing new features
- You want instant code changes without reinstalling
- You're writing tests or debugging

### Option 3: Remote Tool Installation

Install directly from the repository without cloning:

\`\`\`bash
# Install from remote repository
uv tool install git+ssh://git@<repo-url>

# Install Playwright browsers (required)
uvx playwright install
\`\`\`

**Use this when:**
- You just want to use the tool without modifying code
- You want the simplest installation

## Configuration

### Command-Line Options

\`\`\`bash
tool-name command <URL> [OPTIONS]
\`\`\`

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--option1` | `-o` | What this option does | `value` |
| `--option2` | `-v` | Another option | `false` |

### Environment Variables

Configuration can be managed through environment variables using a `.env` file.

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `VAR_NAME` | What this variable controls | `default` | No |

**Note:** Command-line arguments will override environment variables.

## Development

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (>=0.4.0)
- Playwright browsers

### Project Structure

\`\`\`
project/
├── src/
│   └── package_name/
│       ├── __init__.py
│       ├── cli.py
│       └── module.py
├── tests/
│   ├── __init__.py
│   └── test_module.py
├── pyproject.toml
└── README.md
\`\`\`

### Installation for Development

Follow **Option 2: Development Mode** from the [Installation](#installation) section above.

### Running Tests

\`\`\`bash
# Run all tests
uv run pytest tests/ -v

# Run specific test file
uv run pytest tests/test_module.py -v

# Run with coverage
uv run pytest tests/ --cov=package_name --cov-report=html
\`\`\`

### Adding Dependencies

\`\`\`bash
# Add a new dependency
uv add package-name

# Add a dev dependency
uv add --dev package-name

# Update dependencies
uv sync
\`\`\`

### Code Quality

\`\`\`bash
# Run tests
uv run pytest tests/ -v

# Run tests with coverage
uv run pytest tests/ --cov=package_name --cov-report=html
\`\`\`

## Documentation

### How It Works

The tool follows a 5-step pipeline:

1. **Step 1** - Description
2. **Step 2** - Description
3. **Step 3** - Description
4. **Step 4** - Description
5. **Step 5** - Description

### Usage Examples

**Example 1: Basic usage**
\`\`\`bash
tool-name command https://example.com --option value
\`\`\`

**Output:**
\`\`\`
Sample output showing what the user will see...
\`\`\`

**Example 2: Advanced usage**
\`\`\`bash
tool-name command https://example.com --depth 2 --max-pages 15
\`\`\`

### Output File Format

When using the `--save-to` option, content is saved to markdown files with structured metadata.

**Example output:**
\`\`\`markdown
---
# Metadata (v1.0)
- Timestamp: 2024-12-04T10:30:00-08:00
- Source: https://example.com
---

[Content here...]
\`\`\`

### Requirements

- Python 3.12 or higher (for modern async/await features)
- Network connectivity for fetching web pages
- Memory: Minimum 2GB RAM, recommended 4GB+ for large operations

### Validation Commands

Test your installation with these commands:

**For tool installation (Option 1 or 3):**

\`\`\`bash
# Tool is installed and accessible
tool-name --help

# Basic command
tool-name command https://example.com

# Verify output
ls -lh ./output/
\`\`\`

**For development mode (Option 2):**

\`\`\`bash
# Dependencies installed correctly
uv run python -c "import package_name; print('✅ All imports OK')"

# Tests pass
uv run pytest tests/ -v

# CLI available
uv run tool-name --help
\`\`\`

### Troubleshooting

**Problem: "Package not found"**
\`\`\`bash
# Solution: Reinstall dependencies
uv sync
\`\`\`

**Problem: Network errors or timeouts**
\`\`\`bash
# Solution: Try with verbose mode to see detailed logs
tool-name command <url> --verbose  # Tool installation
uv run tool-name command <url> --verbose  # Development mode
\`\`\`

### Future Enhancements

- **Enhancement 1** - Description of planned feature
- **Enhancement 2** - Description of planned feature
- **Enhancement 3** - Description of planned feature

## License

See LICENSE file for details.

## Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Check existing documentation
- Review related docs: https://example.com/
```

## Key Principles

1. **Clarity First** - Make it easy for users to understand what the project does
2. **Organization** - Follow the standard section order consistently
3. **Quick Start Emphasis** - Put Quick Start BEFORE Installation with rocket emoji (🚀) in TOC
4. **Architecture Up Front** - Show high-level architecture before TOC
5. **Tool vs Development Mode** - Use tool-name commands in Quick Start/Examples, uv run in Development
6. **Horizontal Separators** - Use `---` around Quick Start section for visual emphasis
7. **Check pyproject.toml** - Always verify dev-dependencies before documenting code quality tools
8. **Homebrew for uv** - Show `brew install uv` not curl script
9. **Simple Language** - Avoid marketing terms like "production-ready", "robust", excessive superlatives
10. **Detail Where It Matters** - Configuration and usage should be comprehensive
11. **Clean TOC** - Keep table of contents simple with only main sections
12. **Examples Everywhere** - Show configuration, usage, and output examples
13. **Tables for Config** - Use markdown tables for structured configuration documentation
14. **Installation Options** - Always show 3 options for CLI tools (local tool, development, remote)

## Instructions for Claude

When creating a README using this skill:

1. **Detect project type first** - Check pyproject.toml for [project.scripts] to determine if CLI tool or library
2. **Read dev-dependencies** - Check pyproject.toml [tool.uv] dev-dependencies before documenting code quality tools
3. **Use correct command patterns**:
   - CLI tools: Use `tool-name` in Quick Start and Usage Examples (global installation)
   - CLI tools: Use `uv run tool-name` in Development section
   - Libraries: Use import statements, never command-line patterns
4. **Structure order**: Architecture → --- → TOC → --- → Quick Start → --- → Overview → Features → Installation → Configuration → Development → Documentation
5. **Quick Start section must include**:
   - Prerequisites with `brew install uv`
   - Tool installation with `uv tool install .`
   - Minimal working example
   - "What this does" checklist with ✅
   - Common usage patterns (3-5 examples)
   - Output examples
6. **Installation section for CLI tools**:
   - Show all 3 options (local tool, development, remote)
   - Each with "Use this when:" explanation
   - Option 1 and 3: Use `uvx playwright install`
   - Option 2: Use `uv run playwright install`
7. **Table of Contents**:
   - Highlight Quick Start with 🚀 emoji
   - Only main sections, no sub-sections
8. **Language guidelines**:
   - Avoid "production-ready", "robust", marketing fluff
   - Keep descriptions factual and simple
   - Example: "A CLI tool for..." not "A production-ready CLI tool for..."
9. **Code Quality section**:
   - Only document tools that exist in dev-dependencies
   - If only pytest exists, only show pytest commands
   - Don't assume ruff, mypy, or black exist
10. **Horizontal separators**:
    - Use `---` before and after Quick Start section
    - Use `---` before and after Table of Contents
11. **Architecture section**:
    - One line with bold "Architecture:" label
    - 3-4 bullet points of main capabilities
12. **Validation Commands section**:
    - Show both tool installation and development mode versions
    - Clearly label which is which

## Common Patterns

### For CLI Tools
- Show command-line usage with arguments
- Include output examples
- Document environment variables

### For Libraries
- Show installation via package manager
- Include import/usage examples
- Document API methods

### For Services
- Document startup commands
- Show configuration files
- Include deployment instructions

### For Web Crawlers/Indexers
- Explain the crawling pipeline
- Show progress output
- Document storage/output location
- Include first-run notes

## Notes

- Always create comprehensive README files that users can understand without asking questions
- Balance between completeness and readability
- Use the Index MCP README as a reference example of this structure
- Adapt the structure to the specific project type while maintaining the core organization
