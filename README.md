# FreeSTAR Network Wiki

Central documentation hub for all FreeSTAR Network projects, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## 🎯 Live Site

**Visit:** [https://freestar-network.github.io/wiki/](https://freestar-network.github.io/wiki/)

![FreeSTAR Wiki Hub](https://github.com/user-attachments/assets/1e128971-4072-4302-89eb-ef22eddf1ea1)

## 📚 Available Wikis

- **[FreeSTAR Everywhere](everywhere/)** - VoIP service for licensed amateur radio operators
- **[FreeSTAR Multi-Mode](multi-mode/)** - Versatile multi-mode communication platform
- **[FreeSTAR SystemX](systemx/)** - Network management system for amateur radio
- **[FreeSTAR ModuleX](modulex/)** - Modular component system for custom solutions
- **[SIP-DMR Portal](sip-dmr/)** - SIP to DMR bridge portal (exchange, bridge, PBX integration)

## 🚀 Quick Start

### Setup

```bash
# Clone the repository
git clone https://github.com/FreeSTAR-Network/wiki.git
cd wiki

# Install dependencies
pip install -r requirements.txt
```

### Build All Wikis

```bash
python build_all_wikis.py
```

This builds all wikis and creates a unified site accessible via `site/index.html`.

### Local Development

Serve a wiki locally with live reload:

```bash
cd everywhere
mkdocs serve
```

Then visit [http://localhost:8000](http://localhost:8000).

## ✏️ Editing Wiki Content

### Wiki Directory Structure

Each wiki follows this structure:

```
[wiki-name]/
├── mkdocs.yml          # Configuration
└── docs/
    ├── index.md        # Home page
    ├── about.md        # About page
    ├── img/            # Images
    └── stylesheets/    # Custom CSS
```

### Adding a New Page

1. **Create a Markdown file** in the wiki's `docs/` folder:
   ```bash
   cd everywhere/docs
   touch new-feature.md
   ```

2. **Add content** using Markdown:
   ```markdown
   # New Feature
   
   This is documentation for the new feature.
   
   ## Installation
   
   ```bash
   npm install new-feature
   ```
   
   ## Usage
   
   Use the feature like this...
   ```

3. **Update navigation** in `mkdocs.yml`:
   ```yaml
   nav:
     - Home: index.md
     - Getting Started: getting-started.md
     - New Feature: new-feature.md  # Add this line
     - About: about.md
   ```

4. **Preview your changes**:
   ```bash
   cd everywhere
   mkdocs serve
   ```

![Wiki Page Example](https://github.com/user-attachments/assets/9f7dcc80-e484-48f1-9998-acb1d7c820bd)

### Adding Images

1. **Place images** in the wiki's `docs/img/` folder:
   ```bash
   cp screenshot.png everywhere/docs/img/
   ```

2. **Reference in Markdown**:
   ```markdown
   ![Screenshot Description](img/screenshot.png)
   ```

### Markdown Features

MkDocs Material supports many advanced features:

**Code blocks with syntax highlighting:**
````markdown
```python
def hello_world():
    print("Hello, FreeSTAR!")
```
````

**Admonitions (callouts):**
```markdown
!!! note "Important Note"
    This is an important note.

!!! warning "Be Careful"
    This operation cannot be undone.
```

**Task lists:**
```markdown
- [x] Completed task
- [ ] Pending task
```

**Tabs:**
```markdown
=== "Linux"
    Install with: `apt install package`

=== "macOS"
    Install with: `brew install package`
```

## 🆕 Adding a New Wiki

1. **Create the directory structure**:
   ```bash
   mkdir -p new-wiki/docs/img
   mkdir -p new-wiki/docs/stylesheets
   ```

2. **Copy template files** (or copy from an existing wiki):
   ```bash
   cp templates/new-wiki/mkdocs.yml new-wiki/
   cp templates/new-wiki/docs/stylesheets/extra.css new-wiki/docs/stylesheets/
   ```

3. **Update `mkdocs.yml`** with your wiki details:
   ```yaml
   site_name: FreeSTAR New Wiki
   site_url: https://freestar-network.github.io/wiki/new-wiki/
   site_description: Your wiki description
   ```

4. **Create initial pages**:
   ```bash
   echo "# Welcome to New Wiki" > new-wiki/docs/index.md
   echo "# About" > new-wiki/docs/about.md
   ```

5. **Update the main `index.html`** to add a card for the new wiki

6. **Update `.github/workflows/deploy.yml`** to build the new wiki

7. **Add to `build_all_wikis.py`** in the `WIKIS` list

## 🎨 Theme Customization

Each wiki has unique colors. Edit `mkdocs.yml` to customize:

```yaml
theme:
  palette:
    - scheme: default
      primary: blue      # Change primary color
      accent: orange     # Change accent color
```

**Available colors:** red, pink, purple, indigo, blue, cyan, teal, green, lime, yellow, amber, orange

Custom CSS can be added to `docs/stylesheets/extra.css`.

## 🚀 Deployment

GitHub Actions automatically builds and deploys all wikis to GitHub Pages when changes are pushed to `main`.

**Manual deployment:**
```bash
python build_all_wikis.py
# Then commit and push the changes
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-docs`)
3. Make your changes
4. Test locally with `mkdocs serve`
5. Commit your changes (`git commit -m 'Add amazing documentation'`)
6. Push to the branch (`git push origin feature/amazing-docs`)
7. Open a Pull Request

## 📖 Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Markdown Guide](https://www.markdownguide.org/)

## 🔗 Links

- [FreeSTAR Network Website](https://freestar.network)
- [GitHub Organization](https://github.com/FreeSTAR-Network)

---

**Note**: All FreeSTAR services are designed exclusively for licensed amateur radio operators.
