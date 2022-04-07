import datetime
from dataclasses import asdict
from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from typing import List
from typing import Union

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

from pglet import BarChart
from pglet import Checkbox
from pglet import Dialog
from pglet import Form
from pglet import SpinButton
from pglet import Stack
from pglet import Text
from pglet.barchart import Point
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

try:
    from replit import db
except ImportError:
    db = dict()


class Content:

    def introduction(self):
        """
        # Easy web development for Python developers

        Web technologies are available everywhere, and they seem like a good way to create a graphical user interface
        for your Python application, either on the desktop or on the web. Unfortunately, most Python coders like
        Python, and would like to avoid using a lot of other languages (HTML, Javascript and CSS) just to get a UI
        created.

        Pglet ("pagelet") is a web server that is written in Go and uses Fluent UI React components. Actual applications
        ("clients") provide the content and react to events using a proprietary protocol.

        None of the above is visible to a Python developer, since the server comes nicely bundled in the client install.
        All you need is:

        `pip install pglet`

        and you are off to creating a web-enabled UI in pure Python (3.7+).

        As a taste of what pglet-python code looks like, this is the code for the box on the right:

        [code]
        ```
        pglet.page().add(main_view)
        ```

        As another example, this site has also been created with pglet-python, with no HTML and no CSS in the code.

        For more details, supported controls and a tutorial, see the [pglet Python docs](https://pglet.io/docs/).

        # Easy forms

        One of the most-repeated type of UI is some kind of form for entering and updating information. While creating
        forms is easy in pglet, it is nevertheless a task that provides little programming joy. The next pages
        show how to create forms using a Form control that eats annotated Python classes, for example, Python's
        [dataclasses](https://docs.python.org/3/library/dataclasses.html).

        # Easy forms with validation

        Typically you also need to somehow validate user input before you can use it for anything: you need to check
        that necessary values have been provided, check that numbers are numbers, check dates etc.

        You can avoid this repetitive code by giving the Form control a [pydantic](https://pydantic-docs.helpmanual.io/)
        object. Validation defined on the object is performed before the data is returned to you. In some cases,
        you can use the exact same data definition with your APIs (e.g. FastAPI) or when writing to a document or SQL
        data store.
        """

        from pglet import Image, Stack, Text

        main_view = Stack(
            horizontal_align="center",
            padding=20, gap=20,
            controls=[
                Image(width="50%", src="https://www.python.org/static/img/python-logo@2x.png"),
                Image(width="30%", src="https://pglet.io/img/logo_dark.svg"),
                Text(value="pydantic", bold=True, size="xxLarge"),
            ],
        )

        return main_view

    def data_first_forms(self):
        """
        Using the Form control, form definition focuses on the data you need out of it, so we define a class with
        necessary information as attributes, information types as annotations, and default values as assignements.

        Python dataclasses are convenient for this, as we do not need to spend time creating the `__init__` and other
        boilerplate.

        To create the form, all we need to do is give the class definition to the Form control:

        [code]

        You can see the resulting form on the right. Change values, and click "OK" to see the data you would get.

        Form control understands the following data types explicitly, others will be by default be represented with a
        basic text box on the form:
        - str (see later for how you can decide between single line and multiline controls for text)
        - int
        - float
        - bool
        - datetime
        - date (current DatePicker timezone restrictions prevent using it here)
        - time
        - Decimal (current SpinButton restrictions prevent using it here)
        """

        @dataclass
        class DataclassDataModel:
            name: str = "Dataclass Person"
            birthdate: datetime.datetime = "2000-01-01"
            address: str = "Some Street 1, Some Town, Some Country"
            age: int = 33
            happy_today: bool = True
            email: str = "some@email.com"

        def show_data_on_submit(event):
            event.control.page.add(Dialog(
                open=True,
                title="Submitted data",
                blocking=True,
                controls=[
                    Text(value=str(event.control.value.__dict__))
                ]
            ))

        form = Form(
            value=DataclassDataModel,
            width=500,
            on_submit=show_data_on_submit
        )

        return form

    data_first_forms.display_name = "Data-first forms"

    def selecting_values(self):
        """
        Python enums are supported for selecting from a specific set of values.

        [code]
        """
        class ContactOption(str, Enum):
            EMAIL = 'email'
            PHONE = 'phone'

        @dataclass
        class DataclassDataModel:
            name: str = "Dataclass Person"
            ok_to_contact: bool = True
            contact_option: ContactOption = ContactOption.EMAIL

        return Form(value=DataclassDataModel, width=500, on_submit=show_submitted_data)

    def more_values(self):
        """
        If there are more than 3 values, we switch to a dropdown. The threshold is configurable with the
        `threshold_for_dropdown` Form attribute.
        """
        class ContactOption(str, Enum):
            EMAIL = 'email'
            PHONE = 'phone'
            MESSAGE = 'message'
            DOVE = 'dove'

        @dataclass
        class DataclassDataModel:
            name: str = "Dataclass Person"
            ok_to_contact: bool = True
            contact_option: ContactOption = ContactOption.EMAIL

        return Form(value=DataclassDataModel, width=500, on_submit=show_submitted_data)

    def selecting_multiple_values(self):
        """
        Annotating a field with a **list** of enums allows for multiple selection.

        [code]
        """

        class ContactOption(str, Enum):
            EMAIL = "email"
            PHONE = "phone"
            PIGEON = "pigeon"
            SMOKE_SIGNALS = "smoke signals"

        @dataclass
        class DataclassDataModel:
            contact_option: List[ContactOption] = field(
                default_factory=lambda: [ContactOption.EMAIL]
            )

        return Form(value=DataclassDataModel, width=500, on_submit=show_submitted_data)

    def lists_of_fields(self):
        """
        Field with a list annotation of other type than an enum is turned into a list control.
        """

        @dataclass
        class DataclassDataModel:
            alphabet: List[str] = field(
                default_factory=lambda: ["a", "b", "c"]
            )

        return Form(value=DataclassDataModel, width=500, on_submit=show_submitted_data)

    def nested_class_definitions(self):
        """
        Often we need to reuse parts of data structures. Form control supports nested class definitions, like `Movie`
        in the example below.

        [code]
        """
        @dataclass
        class Movie:
            title: str
            year: int

        @dataclass
        class DataclassDataModel:
            name: str = "Dataclass Person"
            email: str = "some@email.com"
            favorite_movie: Movie = Movie(
                title="My Little Pony: The Movie",
                year=2017,
            )

        return Form(value=DataclassDataModel, width=500, on_submit=show_submitted_data)

    def several_nested_objects(self):
        """
        Several nested objects are supported with a List annotation. Lists rely on a sensible `str()` implementation to
        display nicely, open up in a separate panel for editing, and support adding and deleting items.

        [code]

        Note that to support adding more movies, we need to provide default values for Movie attributes.
        """
        @dataclass
        class Movie:
            title: str = ""
            year: int = 2000

            def __str__(self):
                return f"{self.title} ({self.year})"

        movies = [
            Movie(title="The Name of the Rose", year=1986),
            Movie(title="My Little Pony: The Movie", year=2017),
        ]

        @dataclass
        class DataclassDataModel:
            name: str = "Dataclass Person"
            email: str = "some@email.com"
            favorite_movies: List[Movie] = field(default_factory=lambda: movies)

        return Form(value=DataclassDataModel, width=500, on_submit=show_submitted_data)

    def styling_and_dimensions(self):
        """
        Form is a Stack control, and inherits all the
        [attributes of Stacks](https://pglet.io/docs/controls/stack#properties).

        You can toggle the switch on the left to experiment with the light and dark themes.

        Example below shows using:
        - `title` to add a form title at the top,
        - `control_style` to define an alternative general style, with underlined text boxes,
        - `toggle_for_bool` to use a toggle instead of a checkbox for boolean values, and
        - a standard Stack attribute `gap` to add extra space between the lines.

        [code]
        """

        @dataclass
        class DataclassDataModel:
            name: str = "Dataclass Person"
            birthdate: datetime.date = "2000-01-01"
            address: str = "Some Street 1, Some Town, Some Country"
            age: int = 33
            happy_today: bool = True
            email: str = "some@email.com"

        form = Form(
            value=DataclassDataModel,
            title="Your information",
            control_style="line",
            toggle_for_bool=True,
            gap=24,
            width=500,
            on_submit=show_submitted_data,
        )

        return form

    def customizing_controls(self):
        """
        There are several ways to customize controls in a `Form`:

        1. Additional parameters for a specific field, as part of the data definition
        2. Additional parameters for a specific field, in an `__init__` parameter
        3. Map a data type to a specific control, for a single form
        4. Map a data type to a specific control, globally

        Example below covers the first 3:

        1. For dataclasses, the contents of the pglet metadata dictionary is passed as parameters for the control.
           Here we turn a single-line Textbox into a multiline one.
        2. If you do not want to mix your data model with UI specifics, you can pass a parameter to the Form,
           containing extra control initialization kwargs by field name.
        3. If you want to set all fields of a type to be mapped to a specific control, provide additional type to
           control mappings to Form. Here we want all `Amount`s have two decimals in the UI.

        [code]

        For option #4, you can set a type/control mapping globally by updating the mapping in the `Form` class directly,
        like this:

        ```
        Form.default_data_to_control_mapping["Amount"] = partial(
            SpinButton, step=.01,
        )
        ```

        ... or, of course, by subclassing the Form and setting values in the subclass `__init__`.
        """
        from dataclasses import field
        from functools import partial
        from typing import NewType


        Amount = NewType('Amount', float)

        @dataclass
        class DataclassDataModel:
            item: str = field(
                default="",
                metadata={"pglet": {
                    "multiline": True  # <<< 1
                }}
            )
            description: str = ""
            amount: Amount = Amount(0)


        form = Form(
            value=DataclassDataModel,
            control_kwargs={
                'description': {'multiline': True}  # <<< 2
            },
            control_mapping={
                "Amount": partial(  # <<< 3
                    SpinButton, step=.01,
                )
            },
            width=500,
            on_submit=show_submitted_data,
        )

        return form

    def introducing_pydantic(self):
        """
        Pydantic is not a dependency of pglet nor of the Form control, so you need to install it separately with:

        ```
        pip install pydantic
        ```

        If you need validation of email addresses, you should also install:

        ```
        pip install pydantic[email]
        ```

        Once you have pydantic, your data can inherit from `pydantic.BaseModel` instead of being decorated as a `dataclass`.

        [code]

        Next pages will cover the benefits of having pydantic in place.
        """
        from pydantic import BaseModel

        class PydanticDataModel(BaseModel):
            name: str = "Pydantic Person"
            email: str = "some@email.com"

        return Form(value=PydanticDataModel(), width=500, on_submit=show_submitted_data)

    def change_the_labels(self):
        """
        Normally, the labels on each line derived from the attribute names in your data. If you need something
        different, for example punctuation, use `Field.title`.

        [code]

        See pydantic docs for the full documentation on the
        [Field function](https://pydantic-docs.helpmanual.io/usage/schema/#field-customization).
        """
        from pydantic import Field

        class PydanticDataModel(BaseModel):
            name: str = "Pydantic Person"
            happy: bool = Field(True, title="Are you happy today?")

        return Form(value=PydanticDataModel(), width=500, on_submit=show_submitted_data)

    def placeholders(self):
        """
        If an input does not have text, a placeholder is shown, defined by `Field.description`.
        """
        class PydanticDataModel(BaseModel):
            name: str = "Pydantic Person"
            email: str = Field("", description="Enter a valid email address")

        return Form(value=PydanticDataModel(), width=500, on_submit=show_submitted_data)

    def customizing_pydantic_fields(self):
        """
        Pydantic equivalent of the `dataclasses.field.metadata["pglet"]` is `Field.pglet`.

        Here we use this option for the `notes` attribute to get a multiline `Textbox`.

        [code]
        """
        class PydanticDataModel(BaseModel):
            name: str = "Pydantic Person"
            notes: str = Field("", pglet={'multiline': True})

        return Form(value=PydanticDataModel(), width=500, on_submit=show_submitted_data)

    def validation(self):
        """
        Main benefit of adding pydantic is that get your data validated with the minimum of boilerplate code.

        Experiment with this view to see how the validation works.

        [code]

        Errors are pydantic validation errors, in English.

        Check pydantic documentation on the available
        [validating field types](https://pydantic-docs.helpmanual.io/usage/types/) and their usage.

        Form control currently maps the field types below to specific controls - everything else is a Textbox.

        - ConstrainedDecimal
        - ConstrainedFloat
        - ConstrainedInt
        - EmailStr
        - FutureDate
        - NegativeFloat
        - NegativeInt
        - PastDate
        - PositiveFloat
        - PositiveInt
        - StrictBool
        - StrictFloat
        - StrictInt
        """
        from pydantic import conint
        from pydantic import EmailStr


        class PydanticDataModel(BaseModel):
            name: str = "Pydantic Person"
            birthdate: datetime.date = "2000-01-01"
            age: conint(ge=0, lt=150) = 0
            email: EmailStr = Field("", description="Enter a valid email address")

        return Form(value=PydanticDataModel(), width=500, on_submit=show_submitted_data)

    def cross_field_validation(self):
        """
        Pydantic supports defining more complex relationships between fields.

        In this example, email must be filled (and a valid email) if newsletters have been requested.

        If validator returns an error, the capitalised str value of the error is shown to the user as the error
        message under the field. Pydantic standard validation errors are in English.

        [code]

        Again, pydantic docs contain a lot more information about
        [validators](https://pydantic-docs.helpmanual.io/usage/validators/).
        """
        from pydantic import validator

        class PydanticDataModel(BaseModel):
            name: str = "Pydantic Person"
            newsletter_ok: bool = Field(
                False, title="Send me the monthly newsletter"
            )
            email: Union[EmailStr, Literal[""]] = Field("", description="Valid email needed for newsletter")

            @validator('email', pre=True, allow_reuse=True)
            def email_filled_if_needed(cls, value, values):
                if values.get("newsletter_ok") and not value:
                    raise ValueError("Need email for newsletter")
                return value

        return Form(value=PydanticDataModel(), width=500, on_submit=show_submitted_data)

    cross_field_validation.display_name = "Cross-field validation"

    def status(self):
        """
        The status of the Form control is: **early Proof of Concept for discussion and feedback**

        *Some* todo items remain.

        [no code]
        """
        todo = '''
        Ordering of lists
        Slider option for number ranges
        Proper Documentation
        Responsive layout
        Align/integrate with Grid control
        Dates with DatePicker
        Manage decimal.Decimal values
        '''

        done = '''
        Lists for basic types
        Toggle as an alternative for Checkbox
        Support custom control parameters (e.g. multiline)
        Support customising controls for types
        Multiple selection from enums
        Some tests
        Documentation in the shape of this demo
        '''

        return Stack(
            padding=20,
            width=400,
            controls=[
                Checkbox(label=label.strip(), value=False, disabled=True)
                for label in todo.strip().splitlines()
            ] + [
                Checkbox(label=label.strip(), value=True, disabled=True)
                for label in done.strip().splitlines()
            ]
        )

    def grande_finale(self):
        """
        As one last thing, let's combine the Form control, replit database utility and the pglet graph control into a
        quick poll.

        Please select the options you are interested in and click "OK".

        [code]

        The `db` object here is a replit database that is essentially a dict with per-program persistent contents.
        """
        @dataclass
        class PollData:
            pglet: bool = False
            python: bool = False
            pglet_with_python: bool = False
            pglet_with_some_other_language: bool = False
            pglet_with_forms: bool = False
            pydantic: bool = False
            pydantic_form_validation: bool = False

        chart = BarChart(
            data_mode='fraction',
            padding=20,
            width=210,
            points=[]
        )

        def update_chart():
            chart.points.clear()
            values = list(reversed(sorted(
                [
                    (field, db.get(field, 0))
                    for field in PollData.__annotations__
                    if field != "answers"
                ],
                key=lambda value: value[1]
            )))
            max_value = values[0][1]
            for field, value in values:
                display_name = field.replace("_", " ").capitalize()
                chart.points.append(
                    Point(legend=display_name, x=value, y=max_value),
                )
        update_chart()

        poll = Form(
            value=PollData,
            title="I am interested in...",
            width=300,
            label_width="100%",
            control_width="fit-content",
        )

        def update_db_values(event):
            value = event.control.value
            for key, value in asdict(value).items():
                if value:
                    db[key] = db.get("key", 0) + 1
            db["answers"] = db.get("answers", 0) + 1

            update_chart()
            poll.submit_button.disabled = True
            event.control.page.update()

        poll.on_submit = update_db_values

        stack = Stack(controls=[poll, chart])

        return stack

    grande_finale.display_name = "Grande Finale"


def show_submitted_data(event):
    value = event.control.value
    event.control.page.add(Dialog(open=True, title="Submitted data", blocking=True, controls=[
        Text(value=str(value.__dict__))
    ]))


content = [value for attribute, value in Content.__dict__.items() if callable(value)]
