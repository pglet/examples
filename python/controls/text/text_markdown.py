import pglet
from pglet import Text
with pglet.page("text-markdown") as page:
  
  page.add(Text('''
# Heading1

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

        ''', markdown=True))
  
  
