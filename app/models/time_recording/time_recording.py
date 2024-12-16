import datetime

class TimeRecording:

    def __init__(self, _id: str = None, user: str = None, date: datetime = datetime.datetime.now(), start: int = 0,
                 end: int = 0, pause: int = 0, absent: bool = False, notes: str = None):
        self._id = _id
        self.user = user
        self.date = date
        self.start = start
        self.end = end
        self.pause = pause
        self.absent = absent
        self.notes = notes

    @property
    def id(self):
        return self._id
    