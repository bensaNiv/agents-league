#!/usr/bin/env python3
"""
Smart Librarian Knowledge Base Validator

Validates that a knowledge base follows the Smart Librarian format required
for creating expert agents.

Usage:
    python validate_smart_librarian.py <knowledge-base-path>
"""

import sys
from pathlib import Path


def validate_index_file(index_path: Path) -> tuple[bool, list[str]]:
    """Validate the INDEX.md file structure and content."""
    issues = []

    try:
        content = index_path.read_text(encoding='utf-8')
    except Exception as e:
        issues.append(f"Cannot read INDEX.md: {e}")
        return False, issues

    # Check for required sections
    required_sections = [
        "# Smart Librarian Index",
        "## Usage Instructions for AI Agents",
        "## Documentation Catalog"
    ]

    for section in required_sections:
        if section not in content:
            issues.append(f"Missing required section: {section}")

    # Check for consultation rules
    if "Consult when:" not in content:
        issues.append("No 'Consult when:' consultation rules found")

    # Check for document entries
    if "**File:**" not in content:
        issues.append("No document entries found (missing **File:** markers)")

    # Check for source URLs
    if "**Source:**" not in content:
        issues.append("No source URLs found (missing **Source:** markers)")

    return len(issues) == 0, issues


def validate_directory_structure(kb_path: Path) -> tuple[bool, list[str]]:
    """Validate the overall directory structure."""
    issues = []

    # Check if it's a directory
    if not kb_path.is_dir():
        issues.append("Knowledge base path is not a directory")
        return False, issues

    # Check for INDEX.md
    index_file = kb_path / "INDEX.md"
    if not index_file.exists():
        issues.append("INDEX.md file not found")
        return False, issues

    # Count markdown files
    md_files = list(kb_path.glob("*.md"))
    if len(md_files) < 2:  # INDEX.md + at least one other
        issues.append("Too few markdown files (need INDEX.md + documentation files)")

    # Check for non-INDEX markdown files
    doc_files = [f for f in md_files if f.name != "INDEX.md"]
    if not doc_files:
        issues.append("No documentation files found (only INDEX.md)")

    return len(issues) == 0, issues


def validate_document_references(kb_path: Path) -> tuple[bool, list[str]]:
    """Validate that files referenced in INDEX.md actually exist."""
    issues = []

    index_file = kb_path / "INDEX.md"
    try:
        content = index_file.read_text(encoding='utf-8')
    except Exception as e:
        issues.append(f"Cannot read INDEX.md for validation: {e}")
        return False, issues

    # Extract file references
    lines = content.split('\n')
    referenced_files = []

    for line in lines:
        if line.startswith("**File:**"):
            # Extract filename from **File:** `filename.md`
            parts = line.split('`')
            if len(parts) >= 2:
                filename = parts[1]
                referenced_files.append(filename)

    # Check if referenced files exist
    for filename in referenced_files:
        file_path = kb_path / filename
        if not file_path.exists():
            issues.append(f"Referenced file not found: {filename}")

    return len(issues) == 0, issues


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_smart_librarian.py <knowledge-base-path>")
        sys.exit(1)

    kb_path = Path(sys.argv[1]).resolve()

    print(f"Validating Smart Librarian knowledge base: {kb_path}")
    print("=" * 60)

    all_valid = True
    all_issues = []

    # 1. Directory structure validation
    print("1. Checking directory structure...")
    structure_valid, structure_issues = validate_directory_structure(kb_path)
    if structure_valid:
        print("   ✓ Directory structure is valid")
    else:
        print("   ✗ Directory structure issues:")
        for issue in structure_issues:
            print(f"     - {issue}")
        all_valid = False
        all_issues.extend(structure_issues)

    if not structure_valid:
        print("\nCannot continue validation due to structural issues.")
        sys.exit(1)

    # 2. INDEX.md validation
    print("\n2. Checking INDEX.md format...")
    index_file = kb_path / "INDEX.md"
    index_valid, index_issues = validate_index_file(index_file)
    if index_valid:
        print("   ✓ INDEX.md format is valid")
    else:
        print("   ✗ INDEX.md issues:")
        for issue in index_issues:
            print(f"     - {issue}")
        all_valid = False
        all_issues.extend(index_issues)

    # 3. Document reference validation
    print("\n3. Checking document references...")
    refs_valid, refs_issues = validate_document_references(kb_path)
    if refs_valid:
        print("   ✓ All referenced documents exist")
    else:
        print("   ✗ Document reference issues:")
        for issue in refs_issues:
            print(f"     - {issue}")
        all_valid = False
        all_issues.extend(refs_issues)

    # Summary
    print("\n" + "=" * 60)
    if all_valid:
        print("✓ Knowledge base is valid for expert agent creation!")
        print("\nThe knowledge base follows Smart Librarian format and can be used")
        print("to create an expert agent with efficient INDEX.md navigation.")
    else:
        print("✗ Knowledge base has validation issues:")
        print("\nIssues found:")
        for i, issue in enumerate(all_issues, 1):
            print(f"  {i}. {issue}")

        print("\nPlease fix these issues before creating an expert agent.")

    sys.exit(0 if all_valid else 1)


if __name__ == "__main__":
    main()