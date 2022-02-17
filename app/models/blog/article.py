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
        # https://iconmonstr.com/smiley/
        smiley_2 = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="smiley"><path d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm5.507 13.941c-1.512 1.195-3.174 1.931-5.506 1.931-2.334 0-3.996-.736-5.508-1.931l-.493.493c1.127 1.72 3.2 3.566 6.001 3.566 2.8 0 4.872-1.846 5.999-3.566l-.493-.493zm-9.007-5.941c-.828 0-1.5.671-1.5 1.5s.672 1.5 1.5 1.5 1.5-.671 1.5-1.5-.672-1.5-1.5-1.5zm7 0c-.828 0-1.5.671-1.5 1.5s.672 1.5 1.5 1.5 1.5-.671 1.5-1.5-.672-1.5-1.5-1.5z"/></svg>'
        smiley_4 = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="smiley"><path d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm.001 14c-2.332 0-4.145 1.636-5.093 2.797l.471.58c1.286-.819 2.732-1.308 4.622-1.308s3.336.489 4.622 1.308l.471-.58c-.948-1.161-2.761-2.797-5.093-2.797zm-3.501-6c-.828 0-1.5.671-1.5 1.5s.672 1.5 1.5 1.5 1.5-.671 1.5-1.5-.672-1.5-1.5-1.5zm7 0c-.828 0-1.5.671-1.5 1.5s.672 1.5 1.5 1.5 1.5-.671 1.5-1.5-.672-1.5-1.5-1.5z"/></svg>'
        markdown_text = markdown_text.replace(":)", smiley_2)
        markdown_text = markdown_text.replace(":(", smiley_4)
        return markdown_text

    def get_created(self) -> str:
        return self.created.strftime("%d.%m.%Y, %H:%M")

    def get_published_state(self) -> str:
        return "checked" if self.published else ""

    @property
    def id(self):
        return self._id

    def update_url(self):
        url = self.title.lower()
        url = url.replace("ä", "ae")
        url = url.replace("ö", "oe")
        url = url.replace("ü", "ue")
        url = url.replace("ß", "ss")
        self.url = re.sub(r"[^a-z0-9-]+", "-", url)

    def get_save_object(self) -> dict:
        return {
            "title": self.title,
            "content": self.content,
            "created": self.created,
            "modified": datetime.datetime.now(),
            "url": self.url,
            "published": self.published,
        }
