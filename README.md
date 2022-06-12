# Mezzo

A Python module to parse Markdown. Powered by `PyO3` and `pulldown-cmark`.

## Install

```bash
pip install mezzo
```

## Usage

Convert Markdown to HTML:

```python
import mezzo

mezzo.convert(your_markdown_text)
```

Convert Markdown file to HTML:

```python
import mezzo

mezzo.convert_file(your_markdown_file_path)
```
