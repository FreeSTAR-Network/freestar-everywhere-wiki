"""
MkDocs hook to add git author information to page metadata.
This hook extracts the last commit author for each page and adds it to the page meta.
"""

import subprocess
import logging

logger = logging.getLogger("mkdocs.plugins.git_authors")


def get_git_author(file_path):
    """
    Get the last author of a file from git history.

    Args:
        file_path: Path to the file

    Returns:
        str: Author name or "Unknown" if not found
    """
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--pretty=format:%an", str(file_path)],
            capture_output=True,
            text=True,
            check=False,
        )
        author = result.stdout.strip()
        return author if author else "Unknown"
    except Exception as e:
        logger.warning(f"Could not get git author for {file_path}: {e}")
        return "Unknown"


def on_page_markdown(markdown, page, config, files):
    """
    Hook that runs on each page's markdown content.
    Adds git author to page metadata.

    This is a MkDocs hook with a standardized signature. The 'files' parameter
    is required by the MkDocs hook interface even if not used in this implementation.

    Args:
        markdown: The markdown content
        page: The page object
        config: The global config
        files: All files (required by MkDocs hook interface)

    Returns:
        str: The markdown content (unchanged)
    """

    # Define the substitution table

    LOOKUP_TABLE = {
        "M0VUB": "MØVUB",
        "ShaYmeZ": "MØVUB",
        "thelovebug": "M9TLB",
        "copilot-swe-agent[bot]": "copilot",
    }

    # Get the source file path
    if page.file and page.file.abs_src_path:
        author = get_git_author(page.file.abs_src_path)
        # Store in page meta for use in templates

    try:
        callsign = LOOKUP_TABLE.get(author, author)
    except TypeError:
        callsign = author

    page.meta["git_author"] = callsign

    return markdown
