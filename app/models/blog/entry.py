import datetime

import markdown2


class Entry:

    def __init__(self, _id: str, title: str, content: str, created: datetime, url: str):
        self._id = _id
        self.title = title
        self.content = content
        self.created = created
        self.url = url

    def get_markdown(self) -> str:
        return markdown2.markdown(self.content)

    def get_created(self) -> str:
        return self.created.strftime("%d.%m.%Y, %H:%M") + " Uhr"
