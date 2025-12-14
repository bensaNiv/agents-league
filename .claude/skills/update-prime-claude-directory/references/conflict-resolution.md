# Conflict Resolution Strategies Reference

A comprehensive guide to handling conflicts when copying Claude configuration components between projects, including detection methods, resolution strategies, and safe merge practices.

## Overview

When copying `.claude` components to the main claude_configuration directory, conflicts occur when the target already contains a file or directory with the same name. This reference provides systematic approaches to detect, analyze, and resolve these conflicts safely.

## Conflict Detection

### Detection Types

#### 1. No Conflict (`NONE`)
- Target file/directory doesn't exist
- Direct copy is safe
- **Action**: Proceed with standard copy operation

#### 2. Identical Content (`IDENTICAL`)
- Files have exactly the same content
- No functional difference
- **Action**: Skip copy to save time and avoid unnecessary operations

#### 3. Content Difference (`DIFF`)
- Files exist in both locations but have different content
- Most common conflict type requiring resolution
- **Action**: Present resolution options to user

#### 4. Type Mismatch (`TYPE_MISMATCH`)
- Source is file, target is directory (or vice versa)
- Structural conflict requiring careful handling
- **Action**: Backup target and replace with source type

### Detection Implementation

```bash
# Function to detect conflict type
detect_conflict() {
    local source_path="$1"
    local target_path="$2"

    # No conflict if target doesn't exist
    if [ ! -e "$target_path" ]; then
        echo "NONE"
        return
    fi

    # Type mismatch check
    if [ -f "$source_path" ] && [ -d "$target_path" ]; then
        echo "TYPE_MISMATCH_FILE_DIR"
        return
    fi

    if [ -d "$source_path" ] && [ -f "$target_path" ]; then
        echo "TYPE_MISMATCH_DIR_FILE"
        return
    fi

    # For files, check content similarity
    if [ -f "$source_path" ] && [ -f "$target_path" ]; then
        if cmp -s "$source_path" "$target_path"; then
            echo "IDENTICAL"
        else
            echo "CONTENT_DIFF"
        fi
        return
    fi

    # For directories, check structure and content
    if [ -d "$source_path" ] && [ -d "$target_path" ]; then
        local diff_output=$(diff -rq "$source_path" "$target_path" 2>/dev/null)
        if [ -z "$diff_output" ]; then
            echo "IDENTICAL"
        else
            echo "DIRECTORY_DIFF"
        fi
        return
    fi

    echo "UNKNOWN"
}
```

### Metadata Analysis

Extract useful information for conflict resolution decisions:

```bash
# Get file metadata for comparison
get_file_metadata() {
    local file_path="$1"

    if [ -f "$file_path" ]; then
        echo "Type: File"
        echo "Size: $(wc -c < "$file_path") bytes"
        echo "Lines: $(wc -l < "$file_path") lines"
        echo "Modified: $(stat -f "%Sm" -t "%Y-%m-%d %H:%M" "$file_path")"

        # Extract frontmatter if present
        if head -1 "$file_path" | grep -q "^---$"; then
            echo "Frontmatter:"
            sed -n '2,/^---$/p' "$file_path" | head -10
        fi
    elif [ -d "$file_path" ]; then
        echo "Type: Directory"
        echo "Files: $(find "$file_path" -type f | wc -l) files"
        echo "Subdirs: $(find "$file_path" -type d -mindepth 1 | wc -l) subdirectories"
        echo "Modified: $(stat -f "%Sm" -t "%Y-%m-%d %H:%M" "$file_path")"
    fi
}

# Compare two files/directories
compare_components() {
    local source="$1"
    local target="$2"

    echo "=== SOURCE ($source) ==="
    get_file_metadata "$source"
    echo ""
    echo "=== TARGET ($target) ==="
    get_file_metadata "$target"
    echo ""
    echo "=== DIFFERENCES ==="

    if [ -f "$source" ] && [ -f "$target" ]; then
        # Show line count differences for files
        local source_lines=$(wc -l < "$source")
        local target_lines=$(wc -l < "$target")
        echo "Line count difference: $((source_lines - target_lines)) lines"

        # Show size difference
        local source_size=$(wc -c < "$source")
        local target_size=$(wc -c < "$target")
        echo "Size difference: $((source_size - target_size)) bytes"
    fi
}
```

## Resolution Strategies

### 1. Skip Strategy

**When to Use**:
- User wants to keep existing target version
- Source is older or less complete than target
- Low-impact components like output styles
- Experimental or work-in-progress sources

**Implementation**:
```bash
resolve_skip() {
    local source="$1"
    local target="$2"

    echo "⏭️ Skipping: $target (keeping existing version)"
    echo "   Source: $(basename "$source") will not be copied"
    echo "   Target: $(basename "$target") remains unchanged"

    # Log the skip decision
    echo "SKIPPED:$target:$(date)" >> .claude/.update-operation-log
}
```

**Advantages**:
- Zero risk of breaking existing functionality
- Fast execution
- Preserves local customizations

**Disadvantages**:
- Misses potential improvements in source
- May skip important updates

### 2. Overwrite Strategy

**When to Use**:
- Source is clearly newer/better than target
- Low-risk components (output styles, simple commands)
- User has high confidence in source quality
- Target is known to be outdated

**Implementation**:
```bash
resolve_overwrite() {
    local source="$1"
    local target="$2"

    echo "🔄 Overwriting: $target with $source"

    # Log the overwrite
    echo "OVERWRITE:$target:$(date)" >> .claude/.update-operation-log

    if [ -f "$source" ]; then
        cp "$source" "$target"
        echo "✅ File overwritten successfully"
    elif [ -d "$source" ]; then
        rm -rf "$target"
        cp -r "$source" "$target"
        echo "✅ Directory overwritten successfully"
    fi

    # Validate the copy
    validate_copied_component "$target"
}
```

**Advantages**:
- Gets latest improvements immediately
- Clean, simple resolution
- No backup clutter

**Disadvantages**:
- Risk of losing valuable local modifications
- No recovery option if source has issues

### 3. Backup + Replace Strategy

**When to Use**:
- High-value components (skills, agents, knowledge bases)
- Uncertain about which version is better
- Want safety net for rollback
- Source has significant changes from target

**Implementation**:
```bash
resolve_backup_replace() {
    local source="$1"
    local target="$2"
    local backup_timestamp="$3"

    echo "📦 Creating backup of existing target..."
    local backup_path="$target.bak.$backup_timestamp"

    if [ -f "$target" ]; then
        cp "$target" "$backup_path"
    elif [ -d "$target" ]; then
        cp -r "$target" "$backup_path"
    fi

    echo "✅ Backup created: $backup_path"

    # Log the backup
    echo "BACKUP:$target:$backup_path:$(date)" >> .claude/.update-operation-log

    # Now replace with source
    echo "🔄 Replacing with source..."
    if [ -f "$source" ]; then
        cp "$source" "$target"
    elif [ -d "$source" ]; then
        rm -rf "$target"
        cp -r "$source" "$target"
    fi

    echo "✅ Replacement completed successfully"
    echo "📁 Original preserved at: $backup_path"

    # Validate the copy
    validate_copied_component "$target"
}
```

**Advantages**:
- Complete safety - can always rollback
- Best of both worlds approach
- Detailed operation tracking

**Disadvantages**:
- Uses more disk space
- Creates backup file clutter
- Slightly slower operation

### 4. Review Diff Strategy

**When to Use**:
- Complex conflicts requiring analysis
- User wants to understand differences before deciding
- Critical components where wrong choice has high impact
- Educational purposes to learn from differences

**Implementation**:
```bash
resolve_review_diff() {
    local source="$1"
    local target="$2"

    echo "🔍 Reviewing differences between source and target..."
    echo ""

    compare_components "$source" "$target"
    echo ""

    if [ -f "$source" ] && [ -f "$target" ]; then
        echo "=== DETAILED FILE DIFF ==="
        # Use diff with context lines for better understanding
        diff -u "$target" "$source" | head -50
        echo ""

        # Show frontmatter differences specifically
        if head -1 "$source" | grep -q "^---$" && head -1 "$target" | grep -q "^---$"; then
            echo "=== FRONTMATTER COMPARISON ==="
            echo "Source frontmatter:"
            sed -n '2,/^---$/p' "$source" | head -10
            echo ""
            echo "Target frontmatter:"
            sed -n '2,/^---$/p' "$target" | head -10
        fi
    elif [ -d "$source" ] && [ -d "$target" ]; then
        echo "=== DIRECTORY STRUCTURE DIFF ==="
        diff -rq "$source" "$target" | head -20
    fi

    echo ""
    echo "After reviewing the differences above, please choose a resolution strategy:"
    echo "1. Skip (keep target)"
    echo "2. Overwrite (use source)"
    echo "3. Backup + Replace (safest option)"

    # This would integrate with AskUserQuestion in the main skill
}
```

**Advantages**:
- Informed decision making
- Educational value
- Can catch important differences

**Disadvantages**:
- Time-consuming for large diffs
- May overwhelm user with information
- Requires user expertise to interpret diffs

## Conflict Resolution by Component Type

### Skills (High Impact)

**Recommended Strategy**: Backup + Replace
**Reasoning**: Skills are complex with references/, high development investment

```bash
resolve_skill_conflict() {
    local source_skill="$1"
    local target_skill="$2"
    local backup_ts="$3"

    echo "🎯 Resolving SKILL conflict: $(basename "$source_skill")"

    # Check if skill has references directory
    if [ -d "$source_skill/references" ] || [ -d "$target_skill/references" ]; then
        echo "📚 References directory detected - using careful merge strategy"

        # Always backup when references are involved
        resolve_backup_replace "$source_skill" "$target_skill" "$backup_ts"

        # Validate references integrity
        validate_skill_references "$target_skill"
    else
        # Simple skill without references - safer to overwrite
        echo "📄 Simple skill structure detected"
        resolve_backup_replace "$source_skill" "$target_skill" "$backup_ts"
    fi
}

validate_skill_references() {
    local skill_dir="$1"

    if [ -d "$skill_dir/references" ]; then
        echo "🔍 Validating references integrity..."

        # Check for broken internal links
        find "$skill_dir" -name "*.md" -exec grep -l "references/" {} \; | while read main_file; do
            grep -o "references/[^)]*\.md" "$main_file" | while read ref_link; do
                if [ ! -f "$skill_dir/$ref_link" ]; then
                    echo "⚠️ Warning: Broken reference link: $ref_link in $main_file"
                fi
            done
        done
    fi
}
```

### Agents (Medium Impact)

**Recommended Strategy**: Review Diff → User Choice
**Reasoning**: Single files, but tool permissions and knowledge links important

```bash
resolve_agent_conflict() {
    local source_agent="$1"
    local target_agent="$2"

    echo "🤖 Resolving AGENT conflict: $(basename "$source_agent")"

    # Check for knowledge base references
    local knowledge_refs=$(grep -o "knowledge/[^)]*" "$source_agent" 2>/dev/null || true)
    if [ -n "$knowledge_refs" ]; then
        echo "🧠 Knowledge base references found:"
        echo "$knowledge_refs"
        echo "⚠️ Careful consideration required"
    fi

    # Show tool differences
    echo "🔧 Comparing tool permissions..."
    local source_tools=$(grep "^tools:" "$source_agent" 2>/dev/null || echo "tools: not specified")
    local target_tools=$(grep "^tools:" "$target_agent" 2>/dev/null || echo "tools: not specified")

    echo "Source: $source_tools"
    echo "Target: $target_tools"

    # Recommend review for agents with different tools
    if [ "$source_tools" != "$target_tools" ]; then
        echo "⚠️ Tool permissions differ - recommend reviewing differences"
        return 1  # Indicate review needed
    fi

    return 0  # OK to proceed with standard resolution
}
```

### Commands (Low-Medium Impact)

**Recommended Strategy**: Overwrite (if generic) or Skip (if project-specific)
**Reasoning**: Usually single files, lower complexity

```bash
resolve_command_conflict() {
    local source_command="$1"
    local target_command="$2"

    echo "⚡ Resolving COMMAND conflict: $(basename "$source_command")"

    # Check if command appears project-specific
    local project_indicators=$(grep -E "(localhost|127\.0\.0\.1|/Users/|specific-project)" "$source_command" 2>/dev/null || true)

    if [ -n "$project_indicators" ]; then
        echo "🏠 Project-specific content detected:"
        echo "$project_indicators"
        echo "📋 Recommendation: SKIP (keep target)"
        return 1  # Recommend skip
    else
        echo "🌐 Generic command detected"
        echo "📋 Recommendation: OVERWRITE (use source)"
        return 0  # OK to overwrite
    fi
}
```

### Hooks (High Impact)

**Recommended Strategy**: Backup + Replace with careful validation
**Reasoning**: Affects system behavior, may have dependencies

```bash
resolve_hook_conflict() {
    local source_hook="$1"
    local target_hook="$2"
    local backup_ts="$3"

    echo "⚙️ Resolving HOOK conflict: $(basename "$source_hook")"

    # Check for project-specific paths
    local local_paths=$(grep -E "/Users/[^/]+/[^/]+/[^/]+/" "$source_hook" 2>/dev/null || true)
    if [ -n "$local_paths" ]; then
        echo "⚠️ Local paths detected in source hook:"
        echo "$local_paths"
        echo "This may cause issues in different environments"
    fi

    # Check dependencies
    local deps=$(grep "^# dependencies =" "$source_hook" 2>/dev/null || true)
    if [ -n "$deps" ]; then
        echo "📦 Dependencies found: $deps"
    fi

    # Always backup hooks due to high impact
    resolve_backup_replace "$source_hook" "$target_hook" "$backup_ts"

    # Validate syntax
    if [[ "$source_hook" == *.py ]]; then
        echo "🐍 Validating Python syntax..."
        python3 -m py_compile "$target_hook" 2>/dev/null && echo "✅ Syntax valid" || echo "❌ Syntax error detected"
    fi
}
```

### Knowledge Bases (High Impact)

**Recommended Strategy**: Backup + Replace (complete directory)
**Reasoning**: Complex structures, high value content, agent dependencies

```bash
resolve_knowledge_conflict() {
    local source_knowledge="$1"
    local target_knowledge="$2"
    local backup_ts="$3"

    echo "🧠 Resolving KNOWLEDGE BASE conflict: $(basename "$source_knowledge")"

    # Knowledge bases are directories - always backup
    resolve_backup_replace "$source_knowledge" "$target_knowledge" "$backup_ts"

    # Validate structure
    if [ -f "$target_knowledge/00_INDEX.md" ]; then
        echo "✅ Index file found - well-structured knowledge base"
    else
        echo "⚠️ No index file found - may be incomplete"
    fi

    # Check for referring agents
    echo "🔍 Checking for agents that reference this knowledge base..."
    find .claude/agents -name "*.md" -exec grep -l "knowledge/$(basename "$target_knowledge")" {} \; | while read agent; do
        echo "   Referenced by: $(basename "$agent")"
    done
}
```

## Interactive Resolution Workflow

### User Interface Flow

```bash
interactive_conflict_resolution() {
    local source="$1"
    local target="$2"
    local component_type="$3"

    echo "⚡ CONFLICT DETECTED ⚡"
    echo "Component: $(basename "$source")"
    echo "Type: $component_type"
    echo ""

    # Show comparison
    compare_components "$source" "$target"
    echo ""

    # Component-specific analysis
    case "$component_type" in
        "skill")
            resolve_skill_conflict "$source" "$target" "$BACKUP_TIMESTAMP"
            ;;
        "agent")
            resolve_agent_conflict "$source" "$target" || show_diff_required=true
            ;;
        "command")
            resolve_command_conflict "$source" "$target" || recommend_skip=true
            ;;
        "hook")
            resolve_hook_conflict "$source" "$target" "$BACKUP_TIMESTAMP"
            ;;
        "knowledge")
            resolve_knowledge_conflict "$source" "$target" "$BACKUP_TIMESTAMP"
            ;;
    esac

    # Present options (would use AskUserQuestion in main skill)
    echo "Resolution Options:"
    echo "1. Skip - Keep existing target version"
    echo "2. Overwrite - Replace with source version"
    echo "3. Backup + Replace - Move target to .bak, copy source"
    echo "4. Review Diff - Show detailed differences first"

    if [ "$recommend_skip" = true ]; then
        echo ""
        echo "🎯 RECOMMENDED: Skip (Option 1) - Source appears project-specific"
    elif [ "$component_type" = "skill" ] || [ "$component_type" = "knowledge" ]; then
        echo ""
        echo "🎯 RECOMMENDED: Backup + Replace (Option 3) - High-value component"
    fi
}
```

## Rollback and Recovery

### Operation Logging

```bash
# Create detailed operation log for rollback capability
log_operation() {
    local operation="$1"
    local source="$2"
    local target="$3"
    local backup="$4"
    local timestamp=$(date '+%Y-%m-%d %H:%M:%S')

    echo "$timestamp|$operation|$source|$target|$backup" >> .claude/.update-operation-log
}

# Parse operation log for rollback
parse_operation_log() {
    local log_file=".claude/.update-operation-log"

    if [ ! -f "$log_file" ]; then
        echo "No operation log found"
        return 1
    fi

    echo "Recent operations:"
    tail -10 "$log_file" | while IFS='|' read timestamp operation source target backup; do
        echo "[$timestamp] $operation: $target"
        if [ -n "$backup" ]; then
            echo "  Backup: $backup"
        fi
    done
}
```

### Rollback Implementation

```bash
rollback_last_operation() {
    local log_file=".claude/.update-operation-log"

    if [ ! -f "$log_file" ]; then
        echo "❌ No operation log found - cannot rollback"
        return 1
    fi

    # Get last operation
    local last_op=$(tail -1 "$log_file")
    IFS='|' read timestamp operation source target backup <<< "$last_op"

    echo "🔄 Rolling back last operation:"
    echo "Operation: $operation"
    echo "Target: $target"
    echo "Backup: $backup"

    case "$operation" in
        "OVERWRITE"|"BACKUP_REPLACE")
            if [ -n "$backup" ] && [ -e "$backup" ]; then
                echo "↩️ Restoring from backup..."
                if [ -f "$backup" ]; then
                    cp "$backup" "$target"
                elif [ -d "$backup" ]; then
                    rm -rf "$target"
                    cp -r "$backup" "$target"
                fi
                echo "✅ Rollback completed"
            else
                echo "❌ Backup not found - cannot rollback"
                return 1
            fi
            ;;
        "SKIP")
            echo "ℹ️ Skip operation - nothing to rollback"
            ;;
        "CREATE")
            echo "🗑️ Removing created file/directory..."
            rm -rf "$target"
            echo "✅ Removal completed"
            ;;
    esac

    # Remove the last operation from log
    head -n -1 "$log_file" > "${log_file}.tmp" && mv "${log_file}.tmp" "$log_file"
}
```

## Best Practices

### Before Resolution
1. **Always backup high-impact components** (skills, agents, knowledge)
2. **Analyze component type** to choose appropriate strategy
3. **Check for cross-references** (agents → knowledge, skills → references)
4. **Validate source integrity** before using as replacement

### During Resolution
1. **Log all operations** for rollback capability
2. **Validate copies immediately** after resolution
3. **Preserve file permissions** and timestamps when possible
4. **Show clear progress indicators** to user

### After Resolution
1. **Verify functional integrity** of copied components
2. **Check for broken references** between components
3. **Clean up old backups** periodically
4. **Document any manual adjustments** needed

This comprehensive conflict resolution system ensures safe, informed decisions when managing Claude configuration components across projects.