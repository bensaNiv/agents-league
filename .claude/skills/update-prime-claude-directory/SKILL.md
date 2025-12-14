---
name: update-prime-claude-directory
description: Copy project-specific .claude configurations to main claude_configuration directory with interactive selection and conflict resolution
---

# Update Prime Claude Directory

A comprehensive skill for interactively copying project-specific `.claude` configurations to the main claude_configuration directory, facilitating sharing of developed skills, agents, commands, and configurations across projects.

## Overview

This skill enables selective copying of `.claude` components from local projects to your centralized claude_configuration directory. It provides:

- **Interactive Selection**: Choose exactly which components to copy
- **Conflict Resolution**: Smart detection with backup/overwrite/skip options
- **Safety First**: Comprehensive backup and validation strategies
- **Structure Preservation**: Maintains frontmatter, directory structures, and references

## When to Use This Skill

- After developing new skills, agents, or commands in a project
- When you want to share configurations across projects
- To maintain a centralized repository of reusable Claude components
- Before starting new projects to ensure latest configurations are available

## Core Workflow

### Phase 1: Discovery and Validation

First, scan and validate both source and target directories:

```bash
# Verify target directory exists and is writable
TARGET_DIR="/Users/omerbensalmon/Desktop/Apple/Work_related_stuff/code_repos/claude_configuration/.claude"

# Check if target directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "❌ Target directory does not exist: $TARGET_DIR"
    echo "Please ensure claude_configuration repository is cloned and accessible"
    exit 1
fi

# Check write permissions
if [ ! -w "$TARGET_DIR" ]; then
    echo "❌ Target directory is not writable: $TARGET_DIR"
    echo "Please check permissions"
    exit 1
fi

echo "✅ Target directory validated: $TARGET_DIR"

# Scan current project's .claude directory
echo "🔍 Scanning current project's .claude configuration..."
find .claude -type f -name "*.md" | head -20
find .claude -type d -mindepth 1 -maxdepth 2
```

### Phase 2: Component Classification

Analyze discovered components and classify them:

**Shareable Components (Default Include):**
- `skills/` - Universal development skills with subdirectories
- `agents/` - Reusable agent definitions with knowledge bases
- `commands/` - Generic command definitions
- `hooks/` - Workflow automation hooks
- `knowledge/` - Agent knowledge bases
- `output-styles/` - Display formatting templates

**Project-Specific (Default Exclude):**
- `logs/`, `data/` - Runtime data (always exclude)
- `settings.json`, `settings.local.json` - Configuration files
- `context/`, `*_prompts/`, `project_*` - Project-specific directories

### Phase 3: Interactive Category Selection

Present categories with status indicators using AskUserQuestion:

Use the AskUserQuestion tool to present available categories:

```
Available Categories for Copying:

Skills Directory (./claude/skills/):
- 4 items found (2 new, 1 conflict, 1 identical)
- Contains: run-tests, debug-unit-test-pass, code-quality-check, create-project-readme

Agents Directory (./claude/agents/):
- 6 items found (4 new, 2 conflicts)
- Contains: tester, code-reviewer, debugger, writer, meta-agent, work-completion-summary

Commands Directory (./claude/commands/):
- 18 items found (12 new, 6 conflicts)
- Contains: prime, question, create-feature-prompt, git_status, etc.

Hooks Directory (./claude/hooks/):
- 10 items found (8 new, 2 conflicts)
- Contains: pre_tool_use, post_tool_use, notification, stop, etc.

Knowledge Directory (./claude/knowledge/):
- 1 directory found (1 new)
- Contains: code-reviewer knowledge base

Output Styles Directory (./claude/output-styles/):
- 7 items found (3 new, 4 identical)
- Contains: ultra-concise, bullet-points, yaml-structured, etc.
```

### Phase 4: Item-Level Selection

For selected categories, show individual items for fine-grained control:

```
Selected Category: skills/

Individual Items:
[✓] debug-unit-test-pass/     [NEW] - Complete skill with references/ (275 lines)
[✓] run-tests/               [NEW] - Python test execution skill (700+ lines)
[ ] code-quality-check/       [CONFLICT] - Different version exists (target: Nov 28, source: Dec 7)
[✓] create-project-readme/   [CONFLICT] - Newer version available (target: 18KB, source: 21KB)
```

### Phase 5: Conflict Resolution

For each conflict, present resolution options:

```
Conflict Detected: code-quality-check/

Source:  Modified 2024-12-07, 15KB, includes new ruff configurations
Target:  Modified 2024-11-28, 12KB, older version

Resolution Options:
1. Skip - Keep existing target version unchanged
2. Overwrite - Replace target with source version
3. Backup + Replace - Move target to .bak, copy source
4. Review Diff - Show detailed differences first

Choose resolution strategy: [1-4]
```

### Phase 6: Execute Copy Operations

Process the copy operations with comprehensive feedback:

```bash
echo "🚀 Starting copy operations..."

# Create backup directory if needed
BACKUP_TIMESTAMP=$(date +%Y-%m-%d-%H-%M)
TARGET_BACKUP_DIR="$TARGET_DIR/.backups/$BACKUP_TIMESTAMP"

# Copy single files
copy_single_file() {
    local src_file="$1"
    local target_dir="$2"
    local conflict_strategy="$3"

    local target_file="$target_dir/$(basename "$src_file")"

    if [ -f "$target_file" ] && [ "$conflict_strategy" = "backup" ]; then
        echo "📦 Creating backup: $target_file.bak.$BACKUP_TIMESTAMP"
        cp "$target_file" "$target_file.bak.$BACKUP_TIMESTAMP"
    fi

    echo "📋 Copying: $src_file → $target_file"
    cp "$src_file" "$target_file"

    # Validate frontmatter integrity
    if head -5 "$target_file" | grep -q "^---$"; then
        echo "✅ Frontmatter validated"
    else
        echo "⚠️ Warning: No frontmatter detected in $target_file"
    fi
}

# Copy directory structures (skills with references/)
copy_directory_structure() {
    local src_dir="$1"
    local target_parent="$2"
    local conflict_strategy="$3"

    local target_dir="$target_parent/$(basename "$src_dir")"

    if [ -d "$target_dir" ] && [ "$conflict_strategy" = "backup" ]; then
        echo "📦 Creating directory backup: $target_dir.bak.$BACKUP_TIMESTAMP"
        cp -r "$target_dir" "$target_dir.bak.$BACKUP_TIMESTAMP"
    fi

    echo "📁 Copying directory: $src_dir → $target_dir"
    cp -r "$src_dir" "$target_parent/"

    # Validate directory structure
    if [ -f "$target_dir/SKILL.md" ] || [ -f "$target_dir/skill.md" ]; then
        echo "✅ Skill structure validated"
    fi

    if [ -d "$target_dir/references" ]; then
        echo "✅ References directory preserved"
    fi
}
```

### Phase 7: Post-Operation Validation and Reporting

Provide comprehensive summary of operations:

```bash
echo "📊 Operation Summary Report"
echo "=========================="
echo ""
echo "Categories Processed:"
echo "├── skills/         4 items → 3 copied, 1 skipped"
echo "├── agents/         6 items → 4 copied, 2 overwritten"
echo "├── hooks/          8 items → 8 copied (all new)"
echo "└── knowledge/      1 item  → 1 copied (directory)"
echo ""
echo "Conflict Resolutions Applied:"
echo "├── create-project-readme/SKILL.md → Backup + Replace"
echo "├── enhanced-agent.md → Overwrite"
echo "└── existing-hook.md → Skip (user choice)"
echo ""
echo "Files Modified in Target:"
echo "├── $TARGET_DIR/skills/new-skill/ [NEW DIRECTORY]"
echo "├── $TARGET_DIR/agents/enhanced-agent.md [OVERWRITTEN]"
echo "├── $TARGET_DIR/skills/create-project-readme.md.bak.$BACKUP_TIMESTAMP [BACKUP]"
echo "└── $TARGET_DIR/skills/create-project-readme.md [REPLACED]"
echo ""
echo "✅ Operation completed successfully"
echo "📁 Target location: $TARGET_DIR"
echo "📦 Backups created: $(find "$TARGET_DIR" -name "*.bak.$BACKUP_TIMESTAMP" | wc -l)"
```

## Safety and Error Handling

### Pre-Operation Validation

```bash
# Validate source components
validate_source_components() {
    echo "🔍 Validating source components..."

    # Check for malformed frontmatter
    find .claude -name "*.md" -exec grep -L "^---$" {} \; | while read file; do
        echo "⚠️ Warning: $file may have malformed frontmatter"
    done

    # Check for broken references in skills
    find .claude/skills -name "*.md" -exec grep -l "references/" {} \; | while read file; do
        local skill_dir=$(dirname "$file")
        if [ ! -d "$skill_dir/references" ]; then
            echo "⚠️ Warning: $file references missing directory $skill_dir/references"
        fi
    done
}

# Check disk space
check_disk_space() {
    local required_space=$(du -s .claude | cut -f1)
    local available_space=$(df "$TARGET_DIR" | tail -1 | awk '{print $4}')

    if [ "$required_space" -gt "$available_space" ]; then
        echo "❌ Insufficient disk space"
        echo "Required: ${required_space}KB, Available: ${available_space}KB"
        return 1
    fi
}
```

### Error Recovery and Rollback

```bash
# Transaction-style rollback capability
rollback_operation() {
    local backup_timestamp="$1"

    echo "🔄 Rolling back changes..."

    find "$TARGET_DIR" -name "*.bak.$backup_timestamp" | while read backup_file; do
        local original_file="${backup_file%.bak.$backup_timestamp}"
        echo "↩️ Restoring: $backup_file → $original_file"
        mv "$backup_file" "$original_file"
    done

    # Remove newly created files (tracked in operation log)
    if [ -f ".claude/.update-operation-log" ]; then
        grep "^CREATED:" ".claude/.update-operation-log" | cut -d: -f2 | while read created_file; do
            echo "🗑️ Removing: $created_file"
            rm -rf "$created_file"
        done
    fi

    echo "✅ Rollback completed"
}
```

## Quick Reference

### Essential Commands

```bash
# Validate target directory
ls -la /Users/omerbensalmon/Desktop/Apple/Work_related_stuff/code_repos/claude_configuration/.claude/

# Scan current project components
find .claude -type f -name "*.md" | grep -E "(skill|agent|command|hook)" | wc -l

# Check for conflicts
diff -rq .claude/skills claude_configuration/.claude/skills 2>/dev/null || true

# Create backup timestamp
BACKUP_TS=$(date +%Y-%m-%d-%H-%M)

# Clean up old backups (optional)
find "$TARGET_DIR" -name "*.bak.*" -mtime +30 -delete
```

### Interactive Workflow Commands

Use AskUserQuestion tool for each selection phase:

1. **Category Selection**: Present all available categories with status
2. **Item Selection**: For each selected category, show individual items
3. **Conflict Resolution**: For each conflict, show resolution options
4. **Final Confirmation**: Summary of planned operations before execution

### Success Validation

```bash
# Verify copied components have valid frontmatter
find "$TARGET_DIR" -name "*.md" -exec head -5 {} \; | grep -c "^---$"

# Check directory structure integrity
for skill_dir in "$TARGET_DIR"/skills/*/; do
    if [ -d "$skill_dir" ] && [ ! -f "$skill_dir/SKILL.md" ] && [ ! -f "$skill_dir/skill.md" ]; then
        echo "⚠️ Warning: $skill_dir missing main skill file"
    fi
done

# Validate knowledge base links
find "$TARGET_DIR/agents" -name "*.md" -exec grep -l "knowledge/" {} \; | while read agent; do
    local knowledge_ref=$(grep -o "knowledge/[^)]*" "$agent" | head -1)
    if [ -n "$knowledge_ref" ] && [ ! -d "$TARGET_DIR/$knowledge_ref" ]; then
        echo "⚠️ Warning: $agent references missing $knowledge_ref"
    fi
done
```

This skill provides a comprehensive, safe, and user-friendly system for managing Claude configuration sharing across projects while maintaining the integrity of both source and target configurations.