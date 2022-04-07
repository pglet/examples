import pglet
from pglet import Text, Image


def main(page):
    page.title = "Images example"
    page.gap = 20
    page.update()

    page.add(
        Image(
            src="https://via.placeholder.com/350x150",
            title="sample image",
            alt="Example with no image fit value and no height or width is specified.",
        ),
        Image(
            src="https://via.placeholder.com/350x150",
            width=600,
            title="sample image",
            alt="Example with no image fit value and only width is specified.",
        ),
        Image(
            src="https://via.placeholder.com/350x150",
            height=100,
            title="sample image",
            alt="Example with no image fit value and only height is specified.",
        ),
        Image(
            src="https://via.placeholder.com/350x150",
            width=100,
            height=100,
            title="sample image",
            alt="Example with no image fit value and height or width is specified.",
        ),
    )
    page.add(
        Image(src='https://via.placeholder.com/350x150', title='sample image', fit='cover')
    )
        


pglet.app("python-image", target=main)
