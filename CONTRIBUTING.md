# Contributing to FreeSTAR Network Wiki

Thank you for your interest in contributing to the FreeSTAR Network documentation! This guide will help you get started.

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Wiki Structure](#wiki-structure)
- [Writing Documentation](#writing-documentation)
- [Style Guide](#style-guide)
- [Submitting Changes](#submitting-changes)

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork:**

   ```bash
   git clone https://github.com/YOUR-USERNAME/wiki.git
   cd wiki
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a branch:**

   ```bash
   git checkout -b feature/your-feature-name
   ```

## How to Contribute

### Adding or Updating Content

1. Navigate to the appropriate wiki directory:

   ```bash
   cd [wiki-name]/docs
   ```

2. Create or edit Markdown files

3. If adding a new page, update the navigation in `mkdocs.yml`:

   ```yaml
   nav:
     - Home: index.md
     - Your New Page: new-page.md
   ```

4. Test your changes locally:

   ```bash
   cd [wiki-name]
   mkdocs serve
   ```

5. View at [http://localhost:8000](http://localhost:8000)

### Adding Images

1. Place images in the wiki's `docs/img/` directory:

   ```bash
   cp image.png [wiki-name]/docs/img/
   ```

2. Reference in your Markdown:

   ```markdown
   ![Description](img/image.png)
   ```

### Adding External Links

Add external documentation links in the `mkdocs.yml` navigation:

```yaml
nav:
  - Home: index.md
  - External Resource: https://example.com/docs
```

## Wiki Structure

Each wiki follows this structure:

```text
[wiki-name]/
├── mkdocs.yml              # Configuration
├── docs/
│   ├── index.md           # Home page
│   ├── about.md           # About page
│   ├── getting-started.md # Getting started guide
│   ├── img/               # Images
│   └── stylesheets/
│       └── extra.css      # Custom styles
└── site/                  # Generated (ignored by git)
```

## Writing Documentation

### Markdown Basics

- Use `#` for headers (one `#` for h1, two `##` for h2, etc.)
- Use `**bold**` for **bold text**
- Use `*italic*` or `_italic_` for *italic text*
- Use `` `code` `` for inline code
- Use triple backticks for code blocks:

  ````markdown
  ```python
  def hello():
      print("Hello, FreeSTAR!")
  ```
  ````

### Using Admonitions

Create callout boxes for important information:

```markdown
!!! note "Note Title"
    This is a note with additional information.

!!! warning "Important Warning"
    This is a warning message.

!!! tip "Pro Tip"
    This is a helpful tip.

!!! danger "Danger"
    This indicates something dangerous or critical.
```

Types: `note`, `abstract`, `info`, `tip`, `success`, `question`, `warning`, `failure`, `danger`, `bug`, `example`, `quote`

### Creating Tabs

```markdown
=== "Tab 1"
    Content for the first tab

=== "Tab 2"
    Content for the second tab

=== "Tab 3"
    Content for the third tab
```

### Adding Task Lists

```markdown
- [x] Completed task
- [ ] Incomplete task
- [ ] Another task
```

### Creating Tables

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Value 1  | Value 2  | Value 3  |
| Value 4  | Value 5  | Value 6  |
```

## Style Guide

### General Guidelines

- **Be clear and concise** - Write in simple, straightforward language
- **Use active voice** - "Configure the system" rather than "The system should be configured"
- **Be consistent** - Follow existing patterns in the documentation
- **Use examples** - Show, don't just tell
- **Keep it updated** - Remove outdated information

### Voice and Tone

- **Professional but friendly** - We're writing for amateur radio operators
- **Technically accurate** - Verify technical details
- **Helpful** - Anticipate questions readers might have
- **Inclusive** - Use inclusive language

### Formatting Conventions

- **Code and commands** - Use inline code formatting: `` `command` ``
- **File paths** - Use code formatting: `` `/path/to/file` ``
- **UI elements** - Use **bold**: "Click the **Save** button"
- **Variables** - Use code with brackets: `` `<your-value>` ``
- **Links** - Use descriptive text: `[Installation Guide](install.md)` not `[click here](install.md)`

### Headers

- Use sentence case: "Getting started" not "Getting Started"
- Keep headers descriptive and scannable
- Use a logical hierarchy (don't skip levels)

### Code Examples

- Include comments for complex code
- Show the expected output when relevant
- Test all code examples before committing

## Submitting Changes

### Before Submitting

1. **Test locally:**

   ```bash
   cd [wiki-name]
   mkdocs serve
   ```

2. **Check for broken links** - Verify all links work

3. **Review spelling and grammar**

4. **Build all wikis to ensure no errors:**

   ```bash
   python build_all_wikis.py
   ```

### Creating a Pull Request

1. **Commit your changes:**

   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```

2. **Push to your fork:**

   ```bash
   git push origin feature/your-feature-name
   ```

3. **Open a Pull Request** on GitHub:
   - Provide a clear title
   - Describe what you changed and why
   - Reference any related issues

### Pull Request Guidelines

- **One topic per PR** - Keep PRs focused on a single topic or fix
- **Clear description** - Explain what and why, not just what
- **Test your changes** - Ensure everything builds correctly
- **Be responsive** - Address feedback from reviewers

## Creating a New Wiki

To add an entirely new wiki to the repository, see the [templates/README.md](templates/README.md) guide.

## Reporting Issues

Found a problem? Please [open an issue](https://github.com/FreeSTAR-Network/wiki/issues) with:

- Clear description of the problem
- Steps to reproduce (if applicable)
- Expected vs. actual behavior
- Which wiki is affected
- Screenshots if relevant

## Questions?

If you have questions about contributing:

- Check existing documentation in [README.md](README.md)
- Look at recent pull requests for examples
- Open an issue with your question

## License

By contributing, you agree that your contributions will be part of the FreeSTAR Network documentation for licensed amateur radio operators.

---

Thank you for helping make FreeSTAR documentation better! 🌟
