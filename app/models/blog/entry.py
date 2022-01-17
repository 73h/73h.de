import datetime


class Entry:

    def __init__(self, _id: str, title: str, content: str, created: datetime):
        self._id = _id
        self.title = title
        self.content = content
        self.created = created

    def get_id(self) -> str:
        return str(self._id)

    def get_created(self) -> str:
        return self.created.strftime("%d.%m.%Y, %H:%M") + " Uhr"
