import datetime
import re

import markdown2


class Article:

    def __init__(self, title: str, content: str, _id: str = None, created: datetime = datetime.datetime.now(),
                 url: str = None, published: bool = False, modified: datetime = datetime.datetime.now()):
        self._id = _id
        self.title = title
        self.content = content
        self.created = created
        self.url = url
        self.published = published
        self.modified = modified

    def get_markdown(self) -> str:
        markdown_text = markdown2.markdown(self.content)
        markdown_text = re.sub(r'\<code\>\*([a-z]+)\*', r'<code class="language-\1">', markdown_text)
        markdown_text = re.sub(r'(\<code class=".+"\>)\n', r'\1', markdown_text)
        return markdown_text

    def get_created(self) -> str:
        return self.created.strftime("%Y-%m-%d, %H:%M")

    def get_published_state(self) -> str:
        return "checked" if self.published else ""

    @property
    def id(self):
        return self._id

    def get_save_object(self) -> dict:
        return {
            "title": self.title,
            "content": self.content,
            "created": self.created,
            "modified": datetime.datetime.now(),
            "url": self.url,
            "published": self.published,
        }
