import pglet
from pglet import Stack, Text

def main(page):
    
    page.add(
        Text('Sizes', size='large'),
        Stack(controls=[
            Text('tiny', size='tiny'),
            Text('xSmall', size='xSmall'),
            Text('small', size='small'),
            Text('smallPlus', size='smallPlus'),
            Text('medium', size='medium'),
            Text('mediumPlus', size='mediumPlus'),
            Text('large', size='large'),
            Text('xLarge', size='xLarge'),
            Text('xxLarge', size='xxLarge'),
            Text('superLarge', size='superLarge'),
            Text('mega', size='mega'),
        ]),
        Text('Styles', size='large'),
        Stack(controls=[
            Text('Bold', bold=True),
            Text('Italic', italic=True),
            Text('Preformatted text in monospace font', pre=True)
        ]),
        Text('Vertical and horizontal alignments', size='large'),
        Stack(horizontal=True, controls=[
            Text('left top', align='left', vertical_align='top', width=100, height=100, bgcolor='salmon', color='white', padding=5),
            Text('center top', align='center', vertical_align='top', width=100, height=100, bgcolor='salmon', color='white', padding=5, size='large', border='1px solid #555'),
            Text('right top', align='right', vertical_align='top', width=100, height=100, bgcolor='salmon', color='white', padding=5, border='2px solid #555')
        ]),
        Stack(horizontal=True, controls=[
            Text('left center', align='left', vertical_align='center', width=100, height=100, bgcolor='PaleGoldenrod', padding=5),
            Text('center center', align='center', vertical_align='center', width=100, height=100, bgcolor='PaleGoldenrod', padding=5, size='large', border='1px solid #555'),
            Text('right center', align='right', vertical_align='center', width=100, height=100, bgcolor='PaleGoldenrod', padding=5, border='2px solid #555')
        ]),
        Stack(horizontal=True, controls=[
            Text('left bottom', align='left', vertical_align='bottom', width=100, height=100, bgcolor='PaleGreen', padding=5),
            Text('center bottom', align='center', vertical_align='bottom', width=100, height=100, bgcolor='PaleGreen', padding=5, size='large', border='1px solid #555'),
            Text('right bottom', align='right', vertical_align='bottom', width=100, height=100, bgcolor='PaleGreen', padding=5, border='2px solid #555')
        ]),
        Text('Rounded corners', size='large'),
        Stack(horizontal=True, controls=[
            Text('Border radius 10% of width/height', align='center', vertical_align='center', width=100, height=100, border_radius=10, bgcolor='salmon'),
            Text('Border radius 25% of width/height', align='center', vertical_align='center', width=100, height=100, border_radius=25, bgcolor='PaleGoldenrod', border='1px solid #555'),
            Text('Border radius 50% of width/height', align='center', vertical_align='center', width=100, height=100, border_radius=50, bgcolor='PaleGreen', border='2px solid #555')
        ]),
        Text('Markdown', size='large'),
        Text('''
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

        ''', markdown=True)
    )

pglet.app("python-text", target=main)