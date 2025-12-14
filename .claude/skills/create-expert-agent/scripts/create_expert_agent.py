#!/usr/bin/env python3
"""
Expert Agent Creator

Creates specialized Claude Code sub-agents from Smart Librarian knowledge bases.

Usage:
    python create_expert_agent.py \
        --knowledge-base <path-to-knowledge-base> \
        --expert-name <expert-name> \
        --expert-description "<description>"

Examples:
    python create_expert_agent.py \
        --knowledge-base ./claude-docs \
        --expert-name claude-code \
        --expert-description "Claude Code and Agent SDK expert"
"""

import argparse
import shutil
import sys
from pathlib import Path


def validate_knowledge_base(kb_path: Path) -> bool:
    """Validate that the knowledge base follows Smart Librarian format."""
    if not kb_path.exists():
        print(f"Error: Knowledge base path does not exist: {kb_path}")
        return False

    if not kb_path.is_dir():
        print(f"Error: Knowledge base path is not a directory: {kb_path}")
        return False

    index_file = kb_path / "INDEX.md"
    if not index_file.exists():
        print(f"Error: INDEX.md not found in knowledge base: {kb_path}")
        print("This skill requires Smart Librarian format with INDEX.md file")
        return False

    # Check if INDEX.md contains consultation rules
    try:
        content = index_file.read_text(encoding='utf-8')
        if "Consult when:" not in content:
            print("Warning: INDEX.md doesn't contain 'Consult when:' rules")
            print("The expert agent may not work optimally without consultation rules")
    except Exception as e:
        print(f"Warning: Could not read INDEX.md: {e}")

    return True


def check_expert_exists(expert_name: str) -> tuple[bool, Path]:
    """Check if an expert agent with this name already exists."""
    # Assume we're in a Claude Code configuration
    current_dir = Path.cwd()

    # Look for .claude directory in current or parent directories
    claude_dir = None
    for parent in [current_dir] + list(current_dir.parents):
        potential_claude = parent / ".claude"
        if potential_claude.exists():
            claude_dir = potential_claude
            break

    if not claude_dir:
        print("Error: Could not find .claude directory")
        print("Please run this script from within a Claude Code configuration")
        sys.exit(1)

    # Expert agent files always end with "-expert.md"
    agent_file = claude_dir / "agents" / f"{expert_name}.md"
    return agent_file.exists(), agent_file


def copy_knowledge_base(kb_path: Path, expert_name: str) -> Path:
    """Copy knowledge base to .claude/docs/<expert-base-name>_knowledge/"""
    current_dir = Path.cwd()

    # Find .claude directory
    claude_dir = None
    for parent in [current_dir] + list(current_dir.parents):
        potential_claude = parent / ".claude"
        if potential_claude.exists():
            claude_dir = potential_claude
            break

    docs_dir = claude_dir / "docs"
    docs_dir.mkdir(exist_ok=True)

    # Use base name without "-expert" for knowledge base directory
    base_name = expert_name.replace('-expert', '')
    kb_dest = docs_dir / f"{base_name}_knowledge"

    # Remove existing knowledge base if it exists
    if kb_dest.exists():
        shutil.rmtree(kb_dest)

    # Copy knowledge base
    shutil.copytree(kb_path, kb_dest)
    print(f"Knowledge base copied to: {kb_dest}")

    return kb_dest


def create_agent_file(expert_name: str, expert_description: str, kb_path: Path) -> Path:
    """Create the expert agent file from template."""
    current_dir = Path.cwd()

    # Find .claude directory
    claude_dir = None
    for parent in [current_dir] + list(current_dir.parents):
        potential_claude = parent / ".claude"
        if potential_claude.exists():
            claude_dir = potential_claude
            break

    agents_dir = claude_dir / "agents"
    agents_dir.mkdir(exist_ok=True)

    # Expert agent files always end with "-expert.md"
    agent_file = agents_dir / f"{expert_name}.md"

    # Load template
    template_path = Path(__file__).parent.parent / "assets" / "expert_agent_template.md"
    if not template_path.exists():
        print(f"Error: Template file not found: {template_path}")
        sys.exit(1)

    template_content = template_path.read_text(encoding='utf-8')

    # Replace placeholders
    # Use base name without "-expert" for the placeholders in content
    base_name = expert_name.replace('-expert', '')
    agent_content = template_content.replace("{{EXPERT_NAME}}", base_name)
    agent_content = agent_content.replace("{{EXPERT_DESCRIPTION}}", expert_description)

    # Write agent file
    agent_file.write_text(agent_content, encoding='utf-8')
    print(f"Expert agent created: {agent_file}")

    return agent_file


def main():
    parser = argparse.ArgumentParser(description='Create expert Claude Code sub-agent')
    parser.add_argument('--knowledge-base', required=True,
                       help='Path to Smart Librarian knowledge base')
    parser.add_argument('--expert-name', required=True,
                       help='Name for the expert agent (e.g., claude-code, radar-api)')
    parser.add_argument('--expert-description', required=True,
                       help='Description of what the expert specializes in')

    args = parser.parse_args()

    kb_path = Path(args.knowledge_base).resolve()
    expert_name = args.expert_name.strip()
    expert_description = args.expert_description.strip()

    # Ensure expert name always ends with "-expert"
    if not expert_name.endswith('-expert'):
        expert_name = f"{expert_name}-expert"

    print(f"Creating expert agent: {expert_name}")
    print(f"Expertise: {expert_description}")
    print(f"Knowledge base: {kb_path}")
    print()

    # Validate knowledge base
    if not validate_knowledge_base(kb_path):
        sys.exit(1)

    # Check if expert already exists
    exists, agent_path = check_expert_exists(expert_name)
    if exists:
        print(f"Expert agent '{expert_name}' already exists at: {agent_path}")
        response = input("Do you want to overwrite it? (y/N): ").strip().lower()
        if response != 'y':
            print("Operation cancelled.")
            sys.exit(0)

    try:
        # Copy knowledge base
        kb_dest = copy_knowledge_base(kb_path, expert_name)

        # Create agent file
        agent_file = create_agent_file(expert_name, expert_description, kb_dest)

        print()
        print("✓ Expert agent created successfully!")
        print(f"  Agent: {agent_file}")
        print(f"  Knowledge: {kb_dest}")
        print()
        print("The expert agent is now available for consultation.")
        print(f"Try: 'Ask {expert_name.replace('-expert', '')} expert about...'")

    except Exception as e:
        print(f"Error creating expert agent: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()