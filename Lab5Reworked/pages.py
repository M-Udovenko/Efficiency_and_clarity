from abc import ABC
from dataclasses import dataclass
from renderers import Renderer


class Page(ABC):

    def __init__(self, renderer: Renderer):
        self.renderer = renderer


@dataclass
class Product:
    id: str
    name: str
    description: str
    image_url: str


class SimplePage(Page):

    def __init__(self, renderer: Renderer, title: str, content: str):
        super().__init__(renderer)
        self.title = title
        self.content = content

    def render(self) -> str:
        return (
            f"{self.renderer.render_title(self.title)}\n"
            f"{self.renderer.render_text(self.content)}"
        )


class ProductPage(Page):

    def __init__(self, renderer: Renderer, product: Product):
        super().__init__(renderer)
        self.product = product

    def render(self) -> str:
        return (
            f"{self.renderer.render_title(self.product.name)}\n"
            f"{self.renderer.render_text(self.product.description)}\n"
            f"{self.renderer.render_image(self.product.image_url)}\n"
            f"{self.renderer.render_text(f'ID товара: {self.product.id}')}"
        )

