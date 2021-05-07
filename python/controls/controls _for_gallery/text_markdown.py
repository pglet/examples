import pglet
from pglet import Stack, Text

page = pglet.page()

stack = Stack(controls=[
        Text('Markdown', size='large'),
        Text('''
# GitHub Flavored Markdown

## Autolink literals

www.example.com, https://example.com, and contact@example.com.

## Strikethrough

~one~ or ~~two~~ tildes.

### Code sample

```
import pglet
page = page.page()
```

## Table

| a | b  |  c |  d  |
| - | :- | -: | :-: |

        ''', markdown=True)
    ])

page.add(stack)