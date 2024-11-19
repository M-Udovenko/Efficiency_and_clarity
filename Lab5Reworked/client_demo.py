from renderers import HTMLRenderer, JsonRenderer, XMLRenderer
from pages import SimplePage, ProductPage, Product


def run_demo():

    print("✨ Демо №1: HTML-страничка")
    simple_html = SimplePage(
        HTMLRenderer(),
        "Привет, мир!",
        "Это простая HTML-страница с базовым форматированием"
    )
    print(simple_html.render())

    print("\n✨ Демо №2: Страница товара в JSON")
    cool_product = Product(
        id="221",
        name="Крутой гаджет",
        description="Незаменимая вещь в хозяйстве!",
        image_url="https://example.com/gadget.jpg"
    )
    product_json = ProductPage(JsonRenderer(), cool_product)
    print(product_json.render())

    print("\n✨ Демо №3: Тот же товар, но в XML")
    product_xml = ProductPage(XMLRenderer(), cool_product)
    print(product_xml.render())

