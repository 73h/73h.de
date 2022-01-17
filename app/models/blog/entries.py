from models.blog.entry import Entry


class Entries:

    def __init__(self, entries: list):
        self.entries = list()
        for entry in entries:
            self.entries.append(Entry(**entry))
