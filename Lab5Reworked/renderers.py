from abc import ABC, abstractmethod
from typing import Dict, Any


class Renderer(ABC):

    @abstractmethod
    def render_title(self, title: str) -> str:
        pass

    @abstractmethod
    def render_text(self, text: str) -> str:
        pass

    @abstractmethod
    def render_image(self, url: str) -> str:
        pass

    @abstractmethod
    def render_link(self, url: str, text: str) -> str:
        pass


class HTMLRenderer(Renderer):

    def render_title(self, title: str) -> str:
        return f"<h1>📝 {title}</h1>"

    def render_text(self, text: str) -> str:
        return f"<p>{text}</p>"

    def render_image(self, url: str) -> str:
        return f"<img src='{url}' alt='🖼️ Красивая картинка'/>"

    def render_link(self, url: str, text: str) -> str:
        return f"<a href='{url}'>🔗 {text}</a>"


class JsonRenderer(Renderer):
    """JSON-рендерер для любителей структурированных данных"""

    def render_title(self, title: str) -> str:
        return f'{{"type": "title", "content": "{title}"}}'

    def render_text(self, text: str) -> str:
        return f'{{"type": "text", "content": "{text}"}}'

    def render_image(self, url: str) -> str:
        return f'{{"type": "image", "url": "{url}"}}'

    def render_link(self, url: str, text: str) -> str:
        return f'{{"type": "link", "url": "{url}", "text": "{text}"}}'


class XMLRenderer(Renderer):

    def render_title(self, title: str) -> str:
        return f"<title>{title}</title>"

    def render_text(self, text: str) -> str:
        return f"<text>{text}</text>"

    def render_image(self, url: str) -> str:
        return f"<image src='{url}'/>"

    def render_link(self, url: str, text: str) -> str:
        return f"<link url='{url}'>{text}</link>"

