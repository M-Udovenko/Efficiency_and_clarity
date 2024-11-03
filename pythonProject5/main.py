# Абстрактний клас для рендерера
class Renderer:
    def render_title(self, title: str) -> str:
        pass

    def render_text(self, text: str) -> str:
        pass

    def render_image(self, url: str) -> str:
        pass

    def render_product_details(self, id: str, name: str, description: str) -> str:
        pass


# Конкретні реалізації рендерерів
class HTMLRenderer(Renderer):
    def render_title(self, title: str) -> str:
        return f"<h1>{title}</h1>"

    def render_text(self, text: str) -> str:
        return f"<div>{text}</div>"

    def render_image(self, url: str) -> str:
        return f'<img src="{url}" />'

    def render_product_details(self, id: str, name: str, description: str) -> str:
        return f"""
            <div class="product" id="product-{id}">
                <h2>{name}</h2>
                <p>{description}</p>
            </div>
        """


class JsonRenderer(Renderer):
    def render_title(self, title: str) -> str:
        return f'{{"title": "{title}"}}'

    def render_text(self, text: str) -> str:
        return f'{{"content": "{text}"}}'

    def render_image(self, url: str) -> str:
        return f'{{"image": "{url}"}}'

    def render_product_details(self, id: str, name: str, description: str) -> str:
        return f"""{{
            "product": {{
                "id": "{id}",
                "name": "{name}",
                "description": "{description}"
            }}
        }}"""


class XMLRenderer(Renderer):
    def render_title(self, title: str) -> str:
        return f"<title>{title}</title>"

    def render_text(self, text: str) -> str:
        return f"<content>{text}</content>"

    def render_image(self, url: str) -> str:
        return f'<image src="{url}" />'

    def render_product_details(self, id: str, name: str, description: str) -> str:
        return f"""
            <product>
                <id>{id}</id>
                <name>{name}</name>
                <description>{description}</description>
            </product>
        """


# Клас продукту для зберігання інформації про товар
class Product:
    def __init__(self, id: str, name: str, description: str, image: str):
        self.id = id
        self.name = name
        self.description = description
        self.image = image


# Абстрактний клас сторінки
class Page:
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    def render(self) -> str:
        pass


# Конкретні реалізації сторінок
class SimplePage(Page):
    def __init__(self, renderer: Renderer, title: str, content: str):
        super().__init__(renderer)
        self.title = title
        self.content = content

    def render(self) -> str:
        return f"""
        {self.renderer.render_title(self.title)}
        {self.renderer.render_text(self.content)}
        """


class ProductPage(Page):
    def __init__(self, renderer: Renderer, product: Product):
        super().__init__(renderer)
        self.product = product

    def render(self) -> str:
        return f"""
        {self.renderer.render_product_details(
            self.product.id,
            self.product.name,
            self.product.description
        )}
        {self.renderer.render_image(self.product.image)}
        """


# Демонстрація роботи
def main():
    # Створюємо рендерери
    html_renderer = HTMLRenderer()
    json_renderer = JsonRenderer()
    xml_renderer = XMLRenderer()

    # Створюємо просту сторінку
    simple_page = SimplePage(
        html_renderer,
        "Ласкаво просимо!",
        "Це проста сторінка з базовим контентом."
    )

    # Створюємо продукт
    product = Product(
        "1",
        "Смартфон",
        "Новий потужний смартфон з відмінною камерою та екраном",
        "https://example.com/phone.jpg"
    )

    # Створюємо сторінку продукту
    product_page = ProductPage(json_renderer, product)

    # Виводимо результати рендерингу
    print("HTML-рендеринг простої сторінки:")
    print(simple_page.render())
    print("\nJSON-рендеринг сторінки продукту:")
    print(product_page.render())

    # Демонструємо можливість зміни рендерера
    product_page.renderer = xml_renderer
    print("\nXML-рендеринг тієї ж сторінки продукту:")
    print(product_page.render())


if __name__ == "__main__":
    main()