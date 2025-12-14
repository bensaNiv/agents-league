# Validation Rules Reference

A comprehensive guide to validation rules and integrity checks for Claude configuration components during copying, ensuring reliability and functionality of transferred configurations.

## Overview

When copying `.claude` components between projects, validation ensures that:
1. Components maintain their structural integrity
2. Internal references remain functional
3. Metadata and frontmatter are preserved correctly
4. Dependencies and links between components work properly
5. File permissions and execution capabilities are maintained

This reference provides systematic validation rules for each component type.

## Pre-Copy Validation

### Source Integrity Checks

Before copying any component, validate that the source is in good condition:

#### Frontmatter Validation

```bash
validate_frontmatter() {
    local file_path="$1"

    if [ ! -f "$file_path" ]; then
        echo "❌ File does not exist: $file_path"
        return 1
    fi

    # Check if file has frontmatter
    if ! head -1 "$file_path" | grep -q "^---$"; then
        echo "⚠️ No frontmatter detected in: $file_path"
        return 2
    fi

    # Extract frontmatter block
    local frontmatter=$(sed -n '2,/^---$/p' "$file_path" | head -n -1)

    # Check required fields based on component type
    local component_type=$(determine_component_type "$file_path")

    case "$component_type" in
        "skill")
            validate_skill_frontmatter "$file_path" "$frontmatter"
            ;;
        "agent")
            validate_agent_frontmatter "$file_path" "$frontmatter"
            ;;
        "command")
            validate_command_frontmatter "$file_path" "$frontmatter"
            ;;
        "output-style")
            validate_output_style_frontmatter "$file_path" "$frontmatter"
            ;;
    esac
}

validate_skill_frontmatter() {
    local file_path="$1"
    local frontmatter="$2"

    echo "🎯 Validating skill frontmatter: $(basename "$file_path")"

    # Required fields for skills
    if ! echo "$frontmatter" | grep -q "^name:"; then
        echo "❌ Missing required field: name"
        return 1
    fi

    if ! echo "$frontmatter" | grep -q "^description:"; then
        echo "❌ Missing required field: description"
        return 1
    fi

    # Extract and validate name format
    local skill_name=$(echo "$frontmatter" | grep "^name:" | cut -d: -f2- | xargs)
    if [[ ! "$skill_name" =~ ^[a-z0-9-]+$ ]]; then
        echo "⚠️ Skill name should use lowercase letters, numbers, and hyphens only: $skill_name"
    fi

    echo "✅ Skill frontmatter valid"
}

validate_agent_frontmatter() {
    local file_path="$1"
    local frontmatter="$2"

    echo "🤖 Validating agent frontmatter: $(basename "$file_path")"

    # Required fields for agents
    local required_fields=("name" "description" "tools")

    for field in "${required_fields[@]}"; do
        if ! echo "$frontmatter" | grep -q "^$field:"; then
            echo "❌ Missing required field: $field"
            return 1
        fi
    done

    # Validate tool list format
    local tools_line=$(echo "$frontmatter" | grep "^tools:")
    if echo "$tools_line" | grep -q "tools: \["; then
        # Array format: tools: [Tool1, Tool2, Tool3]
        echo "✅ Tools in array format"
    elif echo "$tools_line" | grep -q "tools: "; then
        # String format: tools: Tool1, Tool2, Tool3
        echo "✅ Tools in string format"
    else
        echo "❌ Invalid tools format"
        return 1
    fi

    echo "✅ Agent frontmatter valid"
}

validate_command_frontmatter() {
    local file_path="$1"
    local frontmatter="$2"

    echo "⚡ Validating command frontmatter: $(basename "$file_path")"

    # Commands must have allowed-tools and description
    if ! echo "$frontmatter" | grep -q "^allowed-tools:"; then
        echo "❌ Missing required field: allowed-tools"
        return 1
    fi

    if ! echo "$frontmatter" | grep -q "^description:"; then
        echo "❌ Missing required field: description"
        return 1
    fi

    echo "✅ Command frontmatter valid"
}
```

#### Directory Structure Validation

```bash
validate_directory_structure() {
    local component_dir="$1"
    local component_type="$2"

    echo "📁 Validating directory structure: $(basename "$component_dir")"

    case "$component_type" in
        "skill")
            validate_skill_directory "$component_dir"
            ;;
        "knowledge")
            validate_knowledge_directory "$component_dir"
            ;;
        *)
            echo "ℹ️ No specific structure validation for type: $component_type"
            ;;
    esac
}

validate_skill_directory() {
    local skill_dir="$1"

    # Must have main skill file
    if [ -f "$skill_dir/SKILL.md" ]; then
        echo "✅ Main skill file found: SKILL.md"
    elif [ -f "$skill_dir/skill.md" ]; then
        echo "✅ Main skill file found: skill.md"
    else
        echo "❌ No main skill file found (SKILL.md or skill.md)"
        return 1
    fi

    # Check references directory if it exists
    if [ -d "$skill_dir/references" ]; then
        echo "📚 References directory found"
        local ref_files=$(find "$skill_dir/references" -name "*.md" | wc -l)
        echo "   Reference files: $ref_files"

        # Validate reference files have valid frontmatter (if any)
        find "$skill_dir/references" -name "*.md" | while read ref_file; do
            if head -1 "$ref_file" | grep -q "^---$"; then
                validate_frontmatter "$ref_file" || echo "⚠️ Reference file has invalid frontmatter: $ref_file"
            fi
        done
    fi

    # Check for internal references in main skill file
    local main_file="$skill_dir/SKILL.md"
    [ ! -f "$main_file" ] && main_file="$skill_dir/skill.md"

    if grep -q "references/" "$main_file"; then
        echo "🔗 Internal references detected - validating..."
        grep -o "references/[^)]*\.md" "$main_file" | while read ref_link; do
            if [ ! -f "$skill_dir/$ref_link" ]; then
                echo "❌ Broken reference link: $ref_link"
                return 1
            else
                echo "✅ Reference link valid: $ref_link"
            fi
        done
    fi
}

validate_knowledge_directory() {
    local knowledge_dir="$1"

    echo "🧠 Validating knowledge base: $(basename "$knowledge_dir")"

    # Check for index file
    if [ -f "$knowledge_dir/00_INDEX.md" ]; then
        echo "✅ Index file found: 00_INDEX.md"
    else
        echo "⚠️ No index file found (recommended: 00_INDEX.md)"
    fi

    # Check for numbered files (organized structure)
    local numbered_files=$(find "$knowledge_dir" -name "[0-9][0-9]_*.md" | wc -l)
    if [ "$numbered_files" -gt 0 ]; then
        echo "✅ Organized structure detected: $numbered_files numbered files"
    else
        echo "ℹ️ No numbered structure detected (files may be organized differently)"
    fi

    # Validate all markdown files
    find "$knowledge_dir" -name "*.md" | while read knowledge_file; do
        if [ ! -s "$knowledge_file" ]; then
            echo "⚠️ Empty knowledge file: $(basename "$knowledge_file")"
        fi
    done
}
```

#### Cross-Reference Validation

```bash
validate_cross_references() {
    local source_dir="$1"

    echo "🔗 Validating cross-references between components..."

    # Check agent → knowledge references
    if [ -d "$source_dir/agents" ] && [ -d "$source_dir/knowledge" ]; then
        find "$source_dir/agents" -name "*.md" | while read agent_file; do
            local knowledge_refs=$(grep -o "knowledge/[^)]*" "$agent_file" 2>/dev/null || true)
            if [ -n "$knowledge_refs" ]; then
                echo "Agent $(basename "$agent_file") references knowledge bases:"
                echo "$knowledge_refs" | while read knowledge_ref; do
                    if [ -d "$source_dir/$knowledge_ref" ]; then
                        echo "✅ Valid reference: $knowledge_ref"
                    else
                        echo "❌ Broken reference: $knowledge_ref"
                    fi
                done
            fi
        done
    fi

    # Check skill → references links
    if [ -d "$source_dir/skills" ]; then
        find "$source_dir/skills" -name "*.md" | while read skill_file; do
            local ref_links=$(grep -o "references/[^)]*\.md" "$skill_file" 2>/dev/null || true)
            if [ -n "$ref_links" ]; then
                local skill_dir=$(dirname "$skill_file")
                echo "Skill $(basename "$skill_file") has internal references:"
                echo "$ref_links" | while read ref_link; do
                    if [ -f "$skill_dir/$ref_link" ]; then
                        echo "✅ Valid reference: $ref_link"
                    else
                        echo "❌ Broken reference: $ref_link"
                    fi
                done
            fi
        done
    fi
}
```

### Executable Validation

```bash
validate_executable_components() {
    local source_dir="$1"

    echo "🐍 Validating executable components (hooks)..."

    if [ -d "$source_dir/hooks" ]; then
        find "$source_dir/hooks" -name "*.py" | while read hook_file; do
            echo "Validating hook: $(basename "$hook_file")"

            # Check Python syntax
            if python3 -m py_compile "$hook_file" 2>/dev/null; then
                echo "✅ Python syntax valid"
            else
                echo "❌ Python syntax error detected"
                return 1
            fi

            # Check for proper script header
            if head -3 "$hook_file" | grep -q "#!/usr/bin/env -S uv run --script"; then
                echo "✅ Proper script header found"
            else
                echo "⚠️ Missing or incorrect script header"
            fi

            # Check for dependencies declaration
            if grep -q "# dependencies =" "$hook_file"; then
                echo "✅ Dependencies declared"
            else
                echo "ℹ️ No dependencies declared (may be self-contained)"
            fi

            # Check file permissions
            if [ -x "$hook_file" ]; then
                echo "✅ Execute permission set"
            else
                echo "⚠️ Execute permission not set (will be fixed during copy)"
            fi
        done
    fi
}
```

## Post-Copy Validation

### Target Integrity Checks

After copying components, validate they were copied correctly:

#### File Integrity Validation

```bash
validate_copied_file() {
    local source_file="$1"
    local target_file="$2"

    echo "🔍 Validating copied file: $(basename "$target_file")"

    # Check file exists
    if [ ! -f "$target_file" ]; then
        echo "❌ Target file not created: $target_file"
        return 1
    fi

    # Compare file sizes
    local source_size=$(wc -c < "$source_file")
    local target_size=$(wc -c < "$target_file")

    if [ "$source_size" -ne "$target_size" ]; then
        echo "❌ File size mismatch: source=$source_size, target=$target_size"
        return 1
    fi

    # Compare content (basic check)
    if ! cmp -s "$source_file" "$target_file"; then
        echo "❌ File content differs from source"
        return 1
    fi

    # Validate frontmatter if applicable
    if [[ "$target_file" == *.md ]] && head -1 "$target_file" | grep -q "^---$"; then
        validate_frontmatter "$target_file" || return 1
    fi

    # Check file permissions
    local source_perms=$(stat -f "%Lp" "$source_file")
    local target_perms=$(stat -f "%Lp" "$target_file")

    if [ "$source_perms" != "$target_perms" ]; then
        echo "⚠️ Permission mismatch: source=$source_perms, target=$target_perms"
        # Fix permissions
        chmod "$source_perms" "$target_file"
        echo "✅ Permissions corrected"
    fi

    echo "✅ File integrity validated"
}

validate_copied_directory() {
    local source_dir="$1"
    local target_dir="$2"

    echo "📁 Validating copied directory: $(basename "$target_dir")"

    # Check directory exists
    if [ ! -d "$target_dir" ]; then
        echo "❌ Target directory not created: $target_dir"
        return 1
    fi

    # Compare directory structure
    local source_files=$(find "$source_dir" -type f | wc -l)
    local target_files=$(find "$target_dir" -type f | wc -l)

    if [ "$source_files" -ne "$target_files" ]; then
        echo "❌ File count mismatch: source=$source_files, target=$target_files"
        return 1
    fi

    local source_dirs=$(find "$source_dir" -type d | wc -l)
    local target_dirs=$(find "$target_dir" -type d | wc -l)

    if [ "$source_dirs" -ne "$target_dirs" ]; then
        echo "❌ Directory count mismatch: source=$source_dirs, target=$target_dirs"
        return 1
    fi

    # Validate each file in the directory
    find "$source_dir" -type f | while read source_file; do
        local relative_path="${source_file#$source_dir/}"
        local target_file="$target_dir/$relative_path"

        if [ -f "$target_file" ]; then
            validate_copied_file "$source_file" "$target_file" || return 1
        else
            echo "❌ Missing target file: $target_file"
            return 1
        fi
    done

    echo "✅ Directory integrity validated"
}
```

#### Functional Validation

```bash
validate_component_functionality() {
    local component_path="$1"
    local component_type="$2"

    echo "⚙️ Validating component functionality: $(basename "$component_path")"

    case "$component_type" in
        "skill")
            validate_skill_functionality "$component_path"
            ;;
        "agent")
            validate_agent_functionality "$component_path"
            ;;
        "command")
            validate_command_functionality "$component_path"
            ;;
        "hook")
            validate_hook_functionality "$component_path"
            ;;
        "knowledge")
            validate_knowledge_functionality "$component_path"
            ;;
    esac
}

validate_skill_functionality() {
    local skill_path="$1"

    # Check skill can be loaded (basic syntax)
    local main_file="$skill_path/SKILL.md"
    [ ! -f "$main_file" ] && main_file="$skill_path/skill.md"

    if [ -f "$main_file" ]; then
        # Validate markdown structure
        local headers=$(grep "^#" "$main_file" | wc -l)
        if [ "$headers" -gt 0 ]; then
            echo "✅ Skill has proper markdown structure ($headers headers)"
        else
            echo "⚠️ Skill has no markdown headers (may be malformed)"
        fi

        # Check for essential sections
        if grep -q "## Overview\|# Overview" "$main_file"; then
            echo "✅ Overview section found"
        else
            echo "⚠️ No Overview section found"
        fi

        # Validate references if they exist
        if [ -d "$skill_path/references" ]; then
            validate_skill_directory "$skill_path"
        fi
    fi
}

validate_agent_functionality() {
    local agent_path="$1"

    # Validate agent frontmatter structure
    validate_frontmatter "$agent_path"

    # Check for knowledge base references and validate them
    local knowledge_refs=$(grep -o "knowledge/[^)]*" "$agent_path" 2>/dev/null || true)
    if [ -n "$knowledge_refs" ]; then
        echo "$knowledge_refs" | while read knowledge_ref; do
            local knowledge_path=$(dirname "$(dirname "$agent_path")")/"$knowledge_ref"
            if [ -d "$knowledge_path" ]; then
                echo "✅ Referenced knowledge base exists: $knowledge_ref"
            else
                echo "❌ Referenced knowledge base missing: $knowledge_ref"
                return 1
            fi
        done
    fi
}

validate_hook_functionality() {
    local hook_path="$1"

    if [[ "$hook_path" == *.py ]]; then
        # Test Python syntax
        if python3 -m py_compile "$hook_path" 2>/dev/null; then
            echo "✅ Hook Python syntax valid"
        else
            echo "❌ Hook has Python syntax errors"
            return 1
        fi

        # Check dependencies can be resolved
        local deps=$(grep "^# dependencies =" "$hook_path" | cut -d'=' -f2- | tr -d '[]"' | tr ',' '\n')
        if [ -n "$deps" ]; then
            echo "$deps" | while read dep; do
                dep=$(echo "$dep" | xargs)  # trim whitespace
                if python3 -c "import $dep" 2>/dev/null; then
                    echo "✅ Dependency available: $dep"
                else
                    echo "⚠️ Dependency not available: $dep (may be installed on first use)"
                fi
            done
        fi
    fi
}
```

### Cross-Component Validation

```bash
validate_component_relationships() {
    local target_dir="$1"

    echo "🕸️ Validating component relationships in target directory..."

    # Validate agent → knowledge relationships
    if [ -d "$target_dir/agents" ] && [ -d "$target_dir/knowledge" ]; then
        find "$target_dir/agents" -name "*.md" | while read agent; do
            local knowledge_refs=$(grep -o "knowledge/[^)]*" "$agent" 2>/dev/null || true)
            if [ -n "$knowledge_refs" ]; then
                echo "Validating knowledge references for $(basename "$agent"):"
                echo "$knowledge_refs" | while read knowledge_ref; do
                    if [ -d "$target_dir/$knowledge_ref" ]; then
                        echo "✅ Knowledge base exists: $knowledge_ref"
                    else
                        echo "❌ Knowledge base missing: $knowledge_ref"
                        echo "   Agent: $agent"
                        echo "   This agent may not function correctly"
                    fi
                done
            fi
        done
    fi

    # Validate skill internal references
    if [ -d "$target_dir/skills" ]; then
        find "$target_dir/skills" -type d -mindepth 1 | while read skill_dir; do
            local main_file="$skill_dir/SKILL.md"
            [ ! -f "$main_file" ] && main_file="$skill_dir/skill.md"

            if [ -f "$main_file" ]; then
                local ref_links=$(grep -o "references/[^)]*\.md" "$main_file" 2>/dev/null || true)
                if [ -n "$ref_links" ]; then
                    echo "Validating references for skill $(basename "$skill_dir"):"
                    echo "$ref_links" | while read ref_link; do
                        if [ -f "$skill_dir/$ref_link" ]; then
                            echo "✅ Reference exists: $ref_link"
                        else
                            echo "❌ Reference missing: $ref_link"
                            echo "   Skill: $skill_dir"
                            echo "   This skill may have broken documentation links"
                        fi
                    done
                fi
            fi
        done
    fi
}
```

## Validation Rules by Component Type

### Skills

**Required Structure**:
- Main file: `SKILL.md` or `skill.md` with valid frontmatter
- Optional: `references/` directory with supporting documentation
- Optional: `scripts/` directory with implementation helpers

**Frontmatter Requirements**:
- `name`: lowercase, hyphenated format
- `description`: clear, concise description
- Optional: `tags` for categorization

**Content Requirements**:
- Must have `## Overview` or `# Overview` section
- Should have clear usage instructions
- Internal references must point to existing files

### Agents

**Required Structure**:
- Single `.md` file with frontmatter

**Frontmatter Requirements**:
- `name`: agent name
- `description`: agent capabilities
- `tools`: list of allowed tools
- Optional: `model`, `color`

**Content Requirements**:
- Clear agent instructions in body
- Valid tool names in tools list
- Knowledge base references must exist

### Commands

**Required Structure**:
- Single `.md` file with frontmatter
- Or directory with `command.md` and supporting files

**Frontmatter Requirements**:
- `allowed-tools`: tools the command can use
- `description`: command purpose

**Content Requirements**:
- Command implementation in body
- Valid tool references

### Hooks

**Required Structure**:
- Python script (`.py`) with proper header
- Optional: supporting modules in subdirectories

**Header Requirements**:
```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.8"
# dependencies = ["package1", "package2"]
# ///
```

**Content Requirements**:
- Valid Python syntax
- Proper error handling for lifecycle events
- Dependencies should be commonly available

### Knowledge Bases

**Required Structure**:
- Directory with multiple `.md` files
- Recommended: `00_INDEX.md` for navigation
- Recommended: numbered files for organization

**Content Requirements**:
- Files should contain substantive knowledge content
- Index file should reference other files
- Consistent formatting across files

## Validation Error Handling

### Error Classification

```bash
classify_validation_error() {
    local error_type="$1"
    local severity="$2"

    case "$severity" in
        "critical")
            echo "❌ CRITICAL: $error_type - Copy operation should be aborted"
            return 1
            ;;
        "warning")
            echo "⚠️ WARNING: $error_type - Copy can proceed but may have issues"
            return 0
            ;;
        "info")
            echo "ℹ️ INFO: $error_type - Minor issue, copy will proceed"
            return 0
            ;;
    esac
}

# Example error classifications
validation_error_examples() {
    classify_validation_error "Missing frontmatter" "critical"
    classify_validation_error "Broken internal reference" "warning"
    classify_validation_error "No execute permission on hook" "warning"
    classify_validation_error "Missing index file in knowledge base" "info"
}
```

### Recovery Actions

```bash
attempt_error_recovery() {
    local error_type="$1"
    local component_path="$2"

    echo "🔧 Attempting recovery for: $error_type"

    case "$error_type" in
        "missing_execute_permission")
            chmod +x "$component_path"
            echo "✅ Execute permission added"
            ;;
        "malformed_frontmatter")
            echo "📝 Manual frontmatter repair needed for: $component_path"
            echo "   Please check the YAML format between --- markers"
            ;;
        "broken_reference")
            echo "🔗 Manual reference repair needed for: $component_path"
            echo "   Please check internal links to references/ directory"
            ;;
        *)
            echo "⚠️ No automatic recovery available for: $error_type"
            ;;
    esac
}
```

## Validation Report Generation

```bash
generate_validation_report() {
    local operation_timestamp="$1"
    local target_dir="$2"

    local report_file=".claude/.validation-report-$operation_timestamp.md"

    cat > "$report_file" << EOF
# Validation Report - $operation_timestamp

## Summary
- Target Directory: $target_dir
- Validation Date: $(date)
- Components Validated: $(find "$target_dir" -name "*.md" | wc -l) files

## Component Validation Results

### Skills
$(validate_all_skills "$target_dir" 2>&1)

### Agents
$(validate_all_agents "$target_dir" 2>&1)

### Commands
$(validate_all_commands "$target_dir" 2>&1)

### Hooks
$(validate_all_hooks "$target_dir" 2>&1)

### Knowledge Bases
$(validate_all_knowledge "$target_dir" 2>&1)

## Cross-Component Validation
$(validate_component_relationships "$target_dir" 2>&1)

## Recommendations
$(generate_recommendations "$target_dir" 2>&1)

---
Generated by update-prime-claude-directory skill
EOF

    echo "📋 Validation report generated: $report_file"
}
```

This comprehensive validation system ensures that copied Claude configuration components maintain their integrity, functionality, and relationships across different project environments.