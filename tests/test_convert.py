from unittest import TestCase
import tempfile

from fugue import convert, convert_from_file


class ConvertTestCase(TestCase):
    def setUp(self) -> None:
        self.text = """# Title

## Second title

```python
print("Hello, world")
```
"""

        self.html = """<h1>Title</h1>
<h2>Second title</h2>
<pre><code class="language-python">print(&quot;Hello, world&quot;)
</code></pre>
"""

        return super().setUp()

    def test_convert(self) -> None:
        self.assertEqual(
            self.html,
            convert(self.text)
        )

    def test_convert_from_file(self) -> None:
        """
        test convert markdown file to html.
        write something into temp file, by `tempfile` standard library .
        """
        with tempfile.NamedTemporaryFile("w") as file:
            file.write(self.text)
            file.seek(0)
            self.assertEqual(
                self.html,
                convert_from_file(file.name)
            )
