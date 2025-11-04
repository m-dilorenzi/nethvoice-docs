#!/usr/bin/env python3
"""
DocIndexer: Automatically update index.md files in Docusaurus documentation.

This script traverses a documentation tree and updates each index.md file
to contain a list of all Markdown files in the same directory.
"""

import os
import argparse
import re
from pathlib import Path
import frontmatter


def extract_title(filepath):
    """
    Extract the title from a Markdown file's front matter.
    
    Args:
        filepath (str): Path to the Markdown file.
        
    Returns:
        str: The title from front matter, or a formatted filename if not found.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            if 'title' in post.metadata:
                return post.metadata['title']
    except Exception as e:
        print(f"Warning: Could not parse {filepath}: {e}")
    
    # Fallback: convert filename to title
    filename = os.path.basename(filepath)
    name_without_ext = os.path.splitext(filename)[0]
    # Convert snake_case or kebab-case to Title Case
    title = name_without_ext.replace('_', ' ').replace('-', ' ').title()
    return title


def get_markdown_files(directory):
    """
    Get all Markdown files in a directory, excluding index.md and index.mdx.
    
    Args:
        directory (str): Path to the directory.
        
    Returns:
        list: Sorted list of (filename, title) tuples.
    """
    files = []
    
    try:
        for filename in os.listdir(directory):
            if filename.lower() in ('index.md', 'index.mdx'):
                continue
            if filename.endswith('.md') or filename.endswith('.mdx'):
                filepath = os.path.join(directory, filename)
                if os.path.isfile(filepath):
                    title = extract_title(filepath)
                    files.append((filename, title))
    except Exception as e:
        print(f"Warning: Could not read directory {directory}: {e}")
    
    # Sort alphabetically by filename
    files.sort(key=lambda x: x[0])
    return files


def generate_contents_section(markdown_files):
    """
    Generate a Markdown contents section with links to all files.
    
    Args:
        markdown_files (list): List of (filename, title) tuples.
        
    Returns:
        str: Markdown formatted contents section.
    """
    if not markdown_files:
        return "## Contents\n\nNo documents in this section.\n"
    
    lines = ["## Contents\n"]
    for filename, title in markdown_files:
        lines.append(f"- [{title}](./{filename})")
    
    return "\n".join(lines) + "\n"


def update_index_file(index_path, new_contents_section):
    """
    Update the index.md file with the new contents section.
    
    The function preserves any existing content before the ## Contents section
    and replaces everything from ## Contents onwards.
    
    Args:
        index_path (str): Path to the index.md file.
        new_contents_section (str): The new contents section to insert.
        
    Returns:
        tuple: (was_updated, new_content)
    """
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        print(f"Warning: Could not read {index_path}: {e}")
        return False, None
    
    # Find the ## Contents section
    pattern = r'^## Contents\n.*?(?=\n## |\Z)'
    match = re.search(pattern, original_content, re.MULTILINE | re.DOTALL)
    
    if match:
        # Replace existing ## Contents section
        new_content = original_content[:match.start()] + new_contents_section.rstrip() + "\n" + original_content[match.end():]
    else:
        # Append ## Contents section at the end
        new_content = original_content.rstrip() + "\n\n" + new_contents_section
    
    # Check if content has actually changed
    if new_content.strip() == original_content.strip():
        return False, new_content
    
    # Write the updated content
    try:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, new_content
    except Exception as e:
        print(f"Warning: Could not write to {index_path}: {e}")
        return False, new_content


def process_directory(directory):
    """
    Process a single directory and update its index.md if it exists.
    
    Args:
        directory (str): Path to the directory.
        
    Returns:
        tuple: (updated: bool, file_count: int, message: str)
    """
    index_path = os.path.join(directory, 'index.md')
    
    # Check if index.md exists
    if not os.path.isfile(index_path):
        return False, 0, None
    
    # Get all Markdown files in the directory
    markdown_files = get_markdown_files(directory)
    
    # Generate the contents section
    new_contents_section = generate_contents_section(markdown_files)
    
    # Update the index file
    was_updated, _ = update_index_file(index_path, new_contents_section)
    
    return was_updated, len(markdown_files), index_path


def process_tree(source_dir):
    """
    Traverse the documentation tree and update all index.md files.
    
    Args:
        source_dir (str): Root path of the documentation tree.
    """
    if not os.path.isdir(source_dir):
        print(f"Error: {source_dir} is not a valid directory.")
        return
    
    print(f"Processing documentation tree: {source_dir}\n")
    
    updated_count = 0
    unchanged_count = 0
    
    # Use os.walk to traverse all subdirectories
    for root, dirs, files in os.walk(source_dir):
        # Skip hidden directories and node_modules
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        
        was_updated, file_count, index_path = process_directory(root)
        
        if index_path is not None:
            relative_path = os.path.relpath(index_path, source_dir)
            if was_updated:
                print(f"✓ Updated: {relative_path} ({file_count} files listed)")
                updated_count += 1
            else:
                print(f"  No changes: {relative_path}")
                unchanged_count += 1
    
    print(f"\nSummary:")
    print(f"  Updated: {updated_count}")
    print(f"  Unchanged: {unchanged_count}")


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Automatically update index.md files in a Docusaurus documentation tree."
    )
    parser.add_argument(
        'source_dir',
        help='Path to the root of the documentation tree (e.g., ../docs)'
    )
    
    args = parser.parse_args()
    
    # Convert to absolute path
    source_dir = os.path.abspath(args.source_dir)
    
    process_tree(source_dir)


if __name__ == '__main__':
    main()
