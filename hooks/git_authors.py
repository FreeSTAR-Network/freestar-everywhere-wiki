"""
MkDocs hook to add git author information to page metadata.
This hook extracts the last commit author for each page and adds it to the page meta.
"""

import subprocess
import logging

logger = logging.getLogger("mkdocs.plugins.git_authors")

# Define outside the hook function so it isn't re-allocated on every page build
LOOKUP_TABLE = {
    "M0VUB": "MØVUB",
    "ShaYmeZ": "MØVUB",
    "thelovebug": "M9TLB",
    "Dave Lee": "M9TLB",
    "copilot-swe-agent[bot]": "copilot",
}


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
    """
    # 1. Provide a safe default author in case page.file doesn't exist
    raw_author = "Unknown"

    # 2. Extract author from Git if source path is available
    if page.file and page.file.abs_src_path:
        raw_author = get_git_author(page.file.abs_src_path)

    author = get_git_author(page.file.abs_src_path)
    logger.info(
        f"Page: {page.file.abs_src_path} -> Raw Author: {raw_author} -> Author: {author}"
    )

    # 3. Apply substitution lookup
    callsign = LOOKUP_TABLE.get(raw_author, raw_author)

    # 4. Save to metadata dictionary
    page.meta["git_author"] = callsign

    return markdown
