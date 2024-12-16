from models.time_recording.time_recording import TimeRecording


class TimeRecordings:

    def __init__(self, time_recordings: list):
        self.time_recordings = list()
        for time_recording in time_recordings:
            self.time_recordings.append(TimeRecording(**time_recording))
