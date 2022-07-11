# Micoda

A Python module to parse Markdown. Powered by `PyO3` and `pulldown-cmark`.

## Install

```bash
pip install micoda
```

## Usage

Convert Markdown to HTML:

```python
import micoda

micoda.convert(your_markdown_text)
```

Convert Markdown file to HTML:

```python
import micoda

micoda.convert_file(your_markdown_file_path)
```

Instances of the `micoda.Markdown` class:

```python
from micoda import Markdown, create_markdown

# Initialize class
markdown = Markdown()

# Or use `create_markdown`
markdown = create_markdown()

# call `__call__` method
markdown(your_markdown_text)

markdown.convert(your_markdown_text)
markdown.convert_file(your_markdown_file_path)
```

Extensions:

```python
from micoda import Markdown

# use an extension
markdown = Markdown(["tables"])

# use multiple extensions
# they are supported extensions
markdown = Markdown([
    "tables",
    "footnotes",
    "strikethrough",
    "tasklists",
    "smart_punctuation",
    "heading_attributes"
])

markdown.convert(your_markdown_text)

markdown.convert_file(your_markdown_file_path)
```
