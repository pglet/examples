import pglet
from pglet import Progress, Text

with pglet.page("basic-progress") as page:

    page.add(
        Text("Indeterminate Progress", size='xLarge'),
        Progress("Operation progress", description="Doing something indefinite...", width='50%')
    )
