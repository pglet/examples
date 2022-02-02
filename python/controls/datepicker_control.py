from datetime import datetime
import pglet
from pglet import DatePicker, Stack, Button


def main(page):
    def on_change(e):
        print(e.control.value)

    now = datetime.now()

    picker = DatePicker(label="Allow text input", allow_text_input=True)

    page.add(
        DatePicker("Start date", value=now, on_change=on_change),
        DatePicker(label="End date"),
        picker,
        Button("Check value", on_click=lambda e: print("Selected date:", picker.value)),
        DatePicker(
            label="Allow text input with placeholder",
            placeholder="Select date...",
            allow_text_input=True,
            width="50%",
        ),
        DatePicker(value=now, label="Required", required=True, allow_text_input=True),
    )


pglet.app("python-datepicker", target=main)
