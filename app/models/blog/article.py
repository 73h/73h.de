import datetime
import re

import markdown2


class Article:

    def __init__(self, _id: str, title: str, content: str, created: datetime, url: str):
        self._id = _id
        self.title = title
        self.content = content
        self.created = created
        self.url = url

    def get_markdown(self) -> str:
        markdown_text = markdown2.markdown(self.content)
        markdown_text = re.sub(r'\<code\>\*([a-z]+)\*', r'<code class=language-\1">', markdown_text)
        return markdown_text

    def get_created(self) -> str:
        return self.created.strftime("%d.%m.%Y, %H:%M") + " Uhr"
